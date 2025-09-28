#!/usr/bin/env python3
"""
PDF Generator for Carbon-Aware Route Optimizer Presentation Prompt
"""

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

def markdown_to_pdf(markdown_file, output_file):
    """Convert Markdown file to PDF"""
    
    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(
        markdown_content,
        extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.toc',
            'markdown.extensions.codehilite'
        ]
    )
    
    # Create full HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Carbon-Aware Route Optimizer - Presentation Prompt</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                margin: 40px;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #ecf0f1;
                padding-bottom: 5px;
                margin-top: 30px;
            }}
            h3 {{
                color: #7f8c8d;
                margin-top: 25px;
            }}
            h4 {{
                color: #95a5a6;
                margin-top: 20px;
            }}
            code {{
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #3498db;
                overflow-x: auto;
            }}
            pre code {{
                background: none;
                padding: 0;
            }}
            ul, ol {{
                margin-left: 20px;
            }}
            li {{
                margin-bottom: 5px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            .page-break {{
                page-break-before: always;
            }}
            @media print {{
                body {{
                    margin: 20px;
                }}
            }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    try:
        font_config = FontConfiguration()
        HTML(string=full_html).write_pdf(
            output_file,
            font_config=font_config,
            stylesheets=[CSS(string='''
                @page {
                    size: A4;
                    margin: 2cm;
                }
                body {
                    font-size: 11pt;
                }
                h1 {
                    font-size: 18pt;
                }
                h2 {
                    font-size: 14pt;
                }
                h3 {
                    font-size: 12pt;
                }
                h4 {
                    font-size: 11pt;
                }
            ''')]
        )
        print(f"✅ PDF generated successfully: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False

if __name__ == "__main__":
    # File paths
    markdown_file = "Carbon_Aware_Route_Optimizer_Presentation_Prompt.md"
    output_file = "Carbon_Aware_Route_Optimizer_Presentation_Prompt.pdf"
    
    # Check if markdown file exists
    if not os.path.exists(markdown_file):
        print(f"❌ Markdown file not found: {markdown_file}")
        exit(1)
    
    # Generate PDF
    success = markdown_to_pdf(markdown_file, output_file)
    
    if success:
        print(f"\n🎉 PDF created successfully!")
        print(f"📁 Location: {os.path.abspath(output_file)}")
        print(f"📄 File size: {os.path.getsize(output_file)} bytes")
    else:
        print("\n❌ Failed to create PDF")
        exit(1)
