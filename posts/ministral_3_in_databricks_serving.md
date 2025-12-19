---
title: ministral 3 in databricks serving
date: 2025-12-19
description: Hoe krijg je MVP ministral draaiend in Databricks serving endpoint
---

# Ministral 3 in Databricks serving endpoint

De Nederlandse overheid vanuit AI visie Rijksoverheid en de diverse visie documenten vanuit de ministeries zoveel mogelijk gebruik te maken van Europese modellen. 
Het is daarom interessant dat er begin december weer een nieuw klein model vanuit Mistral is uitgebracht; Ministral 3 in diverse formaten. 

Zie o.a. [Ministral 3 - 3b](https://legal.mistral.ai/ai-governance/models/ministral-3-3b) en [collectie op huggingface](https://huggingface.co/collections/mistralai/ministral-3). 
Met vLLM op Kubernetes heb je deze in een aantal commandlines aan de praat. Zie ook de docs van Huggingface. 
Dit los in Databricks als serving endpoint basic aan de praat krijgen is iets meer gehannes. 

## Model direct in notebook testen

Laad het model in GPU.

```python
import torch
from transformers import Mistral3ForConditionalGeneration, AutoTokenizer

# Check GPU first
assert torch.cuda.is_available(), "CUDA not available! Check cluster type and runtime."

model_id = "mistralai/Ministral-3-3B-Instruct-2512-BF16"

tokenizer = AutoTokenizer.from_pretrained(model_id, tokenizer_type="mistral")

model = Mistral3ForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)
```

Stel een vraag.

```python
prompt = "What is Databricks?"

inputs = tokenizer(
    prompt,
    return_tensors="pt"
).to(device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=1024,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Registreer een model

Je kan een eigen PythonModel class maken om met het Mistral model te gebruiken. 
Deze registreer je vervolgens met onderstaande code. 

```python
ministral_model = Ministral3bModel()

example_input = {
    "prompt": "What is Databricks?",
    "max_new_tokens": 64,
    "temperature": 0.7,
    "top_p": 0.9,
}
example_output = ministral_model.predict(example_input)
signature = infer_signature(example_input, example_output)

model_name = "ministral_3b_instruct"
mlflow.set_registry_uri("databricks-uc")
mlflow.set_experiment("/Shared/ministral-3-3b-instruct-experiment")

with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        name="model",
        python_model=ministral_model,
        registered_model_name=f"{catalog_name}.{schema_name}.ministral_3_3b_instruct",
        signature=signature,
        input_example=example_input,
        pip_requirements=[
            "mlflow==3.0.1",
            "huggingface_hub==1.2.3",
            "sentencepiece==0.2.1",
            "tokenizers==0.22.2rc0",
            "cloudpickle==3.1.2",
            "torch==2.7.0",
            "transformers==5.0.0rc0",
            "mistral-common==1.8.6",
            "tiktoken==0.9.0",  # Explicitly add for tekken support
            "accelerate==1.12.0"
        ]
    )
```

## Test je UC model

Voor je een serving endpoint aanmaakt is het raadzaam om je model in een notebook sessie te laden en op die manier te testen. 
Dit omdat de serving endpoint container aanmaakactie en serving endpoint aanmaakactie beiden erg traag en ietwat moeilijk te debuggen zijn. 

Installeer de benodigde libs.

```python
%pip install uv
```

```python
import mlflow

model_uri = 'models:/m-xxx'

env_file = mlflow.pyfunc.get_model_dependencies(model_uri)
dbutils.widgets.text("env_file", env_file)
%pip install -r $env_file
%restart_python
```

Test call met eenmalig model laden zodat je hem wat vaker kunt gebruiken met verschillende testcalls zonder telkens opnieuw laadtijd. 

```python
import mlflow

model_uri = 'models:/m-xxx'
model = mlflow.pyfunc.load_model(model_uri)

INPUT_EXAMPLE = {
    "prompt": "Waarom is een banaan krom?",
    "max_new_tokens": 1000,
    "temperature": 0.7,
    "top_p": 0.9
}

input_data = INPUT_EXAMPLE
predictions = model.predict(input_data)
display(predictions)
```

## Serving endpoint aanmaken

Dit op basis van de laatste versie die je in unity catalog hebt geladen.
Indien al beschikbaar gaat de call erroren en daarom separaat een lelijke update in de catch. 

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import (
    EndpointCoreConfigInput, 
    EndpointTag,
    ServedEntityInput,
    ServingModelWorkloadType
)

w = WorkspaceClient()

endpoint_tags = [
    EndpointTag(key="x", value="y"),
    EndpointTag(key="y", value="x")
]

budget_policy_id = "xxx"
endpoint_name = "ministral-3-3b-instruct"
model_name_uc = f"{catalog_name}.{schema_name}.{model_name}"

# List all versions of the model in Unity Catalog
model_versions = w.model_versions.list(
    full_name=model_name_uc
)

# Get the latest version (assuming version numbers are integers)
latest_version = max(
    model_versions,
    key=lambda mv: int(mv.version)
)
print(f"Latest model version: {latest_version.version}")

# Create or update the endpoint
try:
    print(f"Creating endpoint: {endpoint_name} with budget policy: {budget_policy_id}")
    w.serving_endpoints.create(
        name=endpoint_name,
        config=EndpointCoreConfigInput(
            name=endpoint_name,
            served_entities=[
                ServedEntityInput(
                    entity_name=model_name_uc,
                    entity_version=latest_version.version,
                    workload_size="Small",
                    scale_to_zero_enabled=True,
                    workload_type=ServingModelWorkloadType.GPU_SMALL
                )
            ]
        ),
        budget_policy_id=budget_policy_id,
        route_optimized=True,
        tags=endpoint_tags,
        description="Ministral 3 3B instruct"
    )
    print(f"Created endpoint: {endpoint_name} with budget policy: {budget_policy_id}")
except Exception as e:
    
    print(f"Error with create endpoint: {e}")

    if "already exists" in str(e):
        print(f"Endpoint already exists thus updating")

        w.serving_endpoints.update_config(
            name=endpoint_name,
            served_entities=[
                ServedEntityInput(
                    entity_name=model_name_uc,
                    entity_version=latest_version.version,
                    workload_size="Small",
                    scale_to_zero_enabled=True,
                    workload_type=ServingModelWorkloadType.GPU_SMALL
                )
            ]
        )
        print(f"Updated endpoint: {endpoint_name}")

        print(f"Updating tags for endpoint: {endpoint_name}")
        w.serving_endpoints.patch(
            name=endpoint_name,
            add_tags=endpoint_tags
        )
        print(f"Updated tags for endpoint: {endpoint_name}")
```

## Query endpoint

En dan wil je met de vernieuwe serving Databricks endpoints automatisch OAUTH tokens aanmaken om het model aan te roepen. 
Voor het ophalen van Keyvault secrets dien je zelf een functie te schrijven maar dat is niet heel spannend. 
Dat ligt ook deels aan of je Keyvault met RBAC gebruikt of met Access Policies. Databricks lijkt nog steeds de RBAC variant niet te ondersteunen. 

```python
from databricks.sdk import WorkspaceClient
import databricks.sdk.core as client
from python_module.utils import (
    get_env, 
    get_secret_from_keyvault,
)

host = spark.conf.get("spark.databricks.workspaceUrl")
env = get_env()

clientid = get_secret_from_keyvault(secret_name="sp-servingendpoints-clientid", env=env)
secret = get_secret_from_keyvault(secret_name="sp-servingendpoints-secret", env=env)

endpoint_name = "ministral-3-3b-instruct"

# Initialize Databricks SDK
c = client.Config(
    host=host,
    client_id=clientid, 
    client_secret=secret   
)
w = WorkspaceClient(
    config = c
)

response = w.serving_endpoints_data_plane.query(
    endpoint_name,
    inputs={
        "prompt": "Explain Databricks in 3 words.",
        "max_new_tokens": 60,
        "temperature": 0.7,
        "top_p": 0.9
    }
)

answer = response.predictions['answer']
print("antwoord: ",answer)
```

Dit kan je voor alle groottes van de Ministral modellen toepassen al dan niet in een loop mits je je geheugen net leegmaakt na runs zodat je geen OOM errors krijgt. 

## Nut kleine modellen

De grotere fullsize modellen die ergens tussen de 1.2TB en 3TB aan GPU memory zweven zijn interessant en leuk om mee te werken. 
Echter voor veel situaties is dit totaal overkill qua energiegebruik en uitdagingen rondom het mogelijk maken van het seperaat draaien van modellen voor specifieke usecases. 
Iedere ronde GenAI modellen laat weer een vooruitgang zien waarbij de kleinere modellen de oude grote modellen van een paar jaar terug op sommige vlakken weten te evenaren. 
Kleinere modellen zorgen ervoor dat meer business cases van GenAI toepassingen haalbaar zijn en zijn daarom interessant om in de gaten te houden. 

Of misschien toch voor 40k aan Mac studios aanschaffen.. 

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/x4_RsUxRjKU?si=W7R-gT9sVl5fRKID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
