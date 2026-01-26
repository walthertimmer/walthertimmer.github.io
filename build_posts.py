"""Convert markdown files to html and add them to index.html"""
import os
import re
import html
from datetime import datetime

def parse_markdown_to_html(markdown_text):
    """
    Simple Markdown to HTML converter without external dependencies.
    Supports: headers, paragraphs, bold, italic, code blocks, inline code, links, images, lists
    """
    html_content = markdown_text

    # Convert headers (# ## ###)
    html_content = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^# (.*$)', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)

    # Convert code blocks (```)
    html_content = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', html_content, flags=re.DOTALL)

    # Convert inline code (`)
    html_content = re.sub(r'`([^`]+)`', r'<code>\1</code>', html_content)

    # Convert images ![alt](url) - BEFORE links to avoid conflicts
    html_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" class="post-image">', html_content)

    # Convert bold (**text**)
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)

    # Convert italic (*text*)
    html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)

    # Convert links [text](url)
    html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)

    # Convert unordered lists
    lines = html_content.split('\n')
    processed_lines = []
    in_list = False

    for line in lines:
        if re.match(r'^[-*+] ', line):
            if not in_list:
                processed_lines.append('<ul>')
                in_list = True
            item_text = re.sub(r'^[-*+] ', '', line)
            processed_lines.append(f'<li>{item_text}</li>')
        else:
            if in_list:
                processed_lines.append('</ul>')
                in_list = False
            processed_lines.append(line)

    if in_list:
        processed_lines.append('</ul>')

    html_content = '\n'.join(processed_lines)

    # Convert paragraphs (empty line separated text)
    paragraphs = html_content.split('\n\n')
    formatted_paragraphs = []

    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            # Only wrap in <p> if it's not already an HTML tag
            formatted_paragraphs.append(f'<p>{para}</p>')
        elif para:
            formatted_paragraphs.append(para)

    return '\n\n'.join(formatted_paragraphs)

def wrap_youtube_iframes(html_content):
    """
    Wrap YouTube iframes with video-container div if not already wrapped
    """
    import re
    
    # Pattern to match iframe tags containing YouTube URLs
    iframe_pattern = r'<iframe([^>]*(?:youtube\.com|youtu\.be)[^>]*)></iframe>'
    
    def replace_iframe(match):
        iframe_tag = match.group(0)
        # Check if already wrapped by looking for video-container div before and after
        # This is a simple check: if the iframe is not inside a div with class="video-container"
        # We'll use a broader check
        if '<div class="video-container">' in iframe_tag or '</div>' in iframe_tag:
            return iframe_tag  # Already wrapped or part of wrapped content
        else:
            return f'<div class="video-container">{iframe_tag}</div>'
    
    # Replace all YouTube iframes
    html_content = re.sub(iframe_pattern, replace_iframe, html_content, flags=re.IGNORECASE | re.DOTALL)
    
    return html_content

def extract_metadata(markdown_content):
    """
    Extract metadata from markdown front matter or first line
    """
    lines = markdown_content.strip().split('\n')

    # Check for front matter (--- at start)
    if lines[0] == '---':
        metadata = {}
        i = 1
        while i < len(lines) and lines[i] != '---':
            if ':' in lines[i]:
                key, value = lines[i].split(':', 1)
                metadata[key.strip()] = value.strip()
            i += 1
        content = '\n'.join(lines[i+1:])
        return metadata, content

    # If no front matter, use first line as title
    title = lines[0].replace('# ', '') if lines[0].startswith('# ') else 'Untitled'
    return {'title': title}, markdown_content

def create_html_post(title, content, date_str=None, description=None):
    """
    Create complete HTML post using external CSS file
    """
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Create full title with site name
    full_title = f"{html.escape(title)} | Walther Timmer's meterkast"

    # Default description if none provided
    if not description:
        description = f"Een post van Walther Timmer over {title.lower()}. Data engineering, cloud computing, en technische inzichten."

    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <title>{full_title}</title>
    <meta name="description" content="{html.escape(description)}">
    <meta name="author" content="Walther Timmer">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://walthertimmer.nl/posts/{title.lower().replace(' ', '_')}.html">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{html.escape(title)}">
    <meta name="twitter:description" content="{html.escape(description)}">
    <link rel="stylesheet" href="../styles/styles.css">
</head>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KXHQQJVBNV"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-KXHQQJVBNV');
</script>

<body>
    <div class="banner"></div>
    <div class="container">
        {content}

        <a href="../index.html" class="back-link">Terug naar thuis</a>
    </div>
</body>
</html>"""

def process_markdown_files():
    """
    Process all markdown files in the posts directory
    """
    posts_dir = 'posts'

    # Create posts directory if it doesn't exist
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    # Find all .md files in posts directory
    markdown_files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]

    if not markdown_files:
        print("No markdown files found in posts directory")
        return []

    generated_posts = []

    for md_file in markdown_files:
        print(f"Processing {md_file}...")

        # Read markdown file
        with open(os.path.join(posts_dir, md_file), 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Extract metadata and content
        metadata, content = extract_metadata(markdown_content)

        # Convert markdown to HTML
        html_content = parse_markdown_to_html(content)

        # Wrap YouTube iframes with video-container
        html_content = wrap_youtube_iframes(html_content)

        # Create complete HTML page
        title = metadata.get('title', md_file.replace('.md', ''))
        date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
        description = metadata.get('description', None)

        html_page = create_html_post(title, html_content, date, description)

        # Write HTML file
        html_filename = md_file.replace('.md', '.html')
        html_path = os.path.join(posts_dir, html_filename)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_page)

        generated_posts.append({
            'title': title,
            'date': date,
            'filename': html_filename
        })

        print(f"Generated {html_filename}")

    return generated_posts

def update_index_html(posts):
    """
    Update index.html with the list of posts
    """
    # Read current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate posts HTML
    posts_html = []
    for post in sorted(posts, key=lambda x: x['date'], reverse=True):
        post_html = f'''            <a href="posts/{post['filename']}" class="post">
                <span class="post-date">{post['date']}</span> -
                <span class="post-title">{html.escape(post['title'])}</span>
            </a>'''
        posts_html.append(post_html)

    # Replace the posts section
    posts_section = '\n'.join(posts_html)

    # Find and replace the posts section
    pattern = r'(<div id="post-list-container">.*?<h2>blogs</h2>.*?)(.*?)(</div>)'
    replacement = f'\\1\n{posts_section}\n        \\3'

    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write updated index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("Updated index.html with new posts")

if __name__ == "__main__":
    # Process all markdown files
    posts = process_markdown_files()

    if posts:
        # Update index.html
        update_index_html(posts)
        print(f"\nSuccessfully processed {len(posts)} posts:")
        for post in posts:
            print(f"  - {post['title']} ({post['date']})")
    else:
        print("No posts to process")
