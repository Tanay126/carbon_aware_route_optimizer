#!/usr/bin/env python3
"""
HTML Generator for Carbon-Aware Route Optimizer Presentation Prompt
Creates a well-formatted HTML file that can be easily converted to PDF
"""

import markdown
import os

def markdown_to_html(markdown_file, output_file):
    """Convert Markdown file to HTML with professional styling"""
    
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
    
    # Create full HTML document with professional styling
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Carbon-Aware Route Optimizer - Presentation Prompt</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                color: #333;
                background: #fff;
            }}
            
            .container {{
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            
            h1 {{
                color: #2c3e50;
                border-bottom: 4px solid #3498db;
                padding-bottom: 15px;
                margin-bottom: 30px;
                font-size: 2.2em;
                text-align: center;
            }}
            
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #ecf0f1;
                padding-bottom: 8px;
                margin-top: 35px;
                margin-bottom: 20px;
                font-size: 1.5em;
            }}
            
            h3 {{
                color: #7f8c8d;
                margin-top: 25px;
                margin-bottom: 15px;
                font-size: 1.2em;
            }}
            
            h4 {{
                color: #95a5a6;
                margin-top: 20px;
                margin-bottom: 10px;
                font-size: 1.1em;
            }}
            
            p {{
                margin-bottom: 15px;
                text-align: justify;
            }}
            
            code {{
                background-color: #f8f9fa;
                padding: 3px 6px;
                border-radius: 4px;
                font-family: 'Courier New', 'Monaco', monospace;
                font-size: 0.9em;
                color: #e74c3c;
                border: 1px solid #e9ecef;
            }}
            
            pre {{
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                border-left: 5px solid #3498db;
                overflow-x: auto;
                margin: 20px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            
            pre code {{
                background: none;
                padding: 0;
                border: none;
                color: #2c3e50;
                font-size: 0.9em;
            }}
            
            ul, ol {{
                margin-left: 25px;
                margin-bottom: 15px;
            }}
            
            li {{
                margin-bottom: 8px;
            }}
            
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                border-radius: 8px;
                overflow: hidden;
            }}
            
            th, td {{
                border: 1px solid #ddd;
                padding: 15px;
                text-align: left;
            }}
            
            th {{
                background: linear-gradient(135deg, #3498db, #2980b9);
                color: white;
                font-weight: bold;
                text-transform: uppercase;
                font-size: 0.9em;
                letter-spacing: 0.5px;
            }}
            
            tr:nth-child(even) {{
                background-color: #f8f9fa;
            }}
            
            tr:hover {{
                background-color: #e8f4f8;
            }}
            
            .highlight {{
                background-color: #fff3cd;
                padding: 15px;
                border-left: 4px solid #ffc107;
                margin: 20px 0;
                border-radius: 4px;
            }}
            
            .info-box {{
                background-color: #d1ecf1;
                padding: 15px;
                border-left: 4px solid #17a2b8;
                margin: 20px 0;
                border-radius: 4px;
            }}
            
            .success-box {{
                background-color: #d4edda;
                padding: 15px;
                border-left: 4px solid #28a745;
                margin: 20px 0;
                border-radius: 4px;
            }}
            
            .page-break {{
                page-break-before: always;
            }}
            
            .toc {{
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
            }}
            
            .toc h2 {{
                margin-top: 0;
                color: #2c3e50;
            }}
            
            .toc ul {{
                list-style-type: none;
                padding-left: 0;
            }}
            
            .toc li {{
                margin: 5px 0;
            }}
            
            .toc a {{
                text-decoration: none;
                color: #3498db;
            }}
            
            .toc a:hover {{
                text-decoration: underline;
            }}
            
            @media print {{
                body {{
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    box-shadow: none;
                    padding: 0;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {html}
            
            <div class="page-break"></div>
            
            <div class="info-box">
                <h3>📋 Document Information</h3>
                <p><strong>Project:</strong> Carbon-Aware Route Optimizer</p>
                <p><strong>Version:</strong> 1.0</p>
                <p><strong>Last Updated:</strong> September 28, 2024</p>
                <p><strong>Status:</strong> Fully Functional with Advanced AI Features</p>
                <p><strong>Generated:</strong> {os.popen('date').read().strip()}</p>
            </div>
            
            <div class="success-box">
                <h3>🎯 Ready for Presentation</h3>
                <p>This document contains all the technical specifications, machine learning models, and business requirements needed to create a comprehensive PowerPoint presentation for the Carbon-Aware Route Optimizer project.</p>
                <p><strong>Next Steps:</strong> Use this document as input for AI presentation tools like Gamma AI to generate professional slides.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✅ HTML file generated successfully: {output_file}")
    print(f"📄 File size: {os.path.getsize(output_file)} bytes")
    return True

if __name__ == "__main__":
    # File paths
    markdown_file = "Carbon_Aware_Route_Optimizer_Presentation_Prompt.md"
    output_file = "Carbon_Aware_Route_Optimizer_Presentation_Prompt.html"
    
    # Check if markdown file exists
    if not os.path.exists(markdown_file):
        print(f"❌ Markdown file not found: {markdown_file}")
        exit(1)
    
    # Generate HTML
    success = markdown_to_html(markdown_file, output_file)
    
    if success:
        print(f"\n🎉 HTML file created successfully!")
        print(f"📁 Location: {os.path.abspath(output_file)}")
        print(f"\n💡 To convert to PDF:")
        print(f"   1. Open {output_file} in your web browser")
        print(f"   2. Press Ctrl+P (or Cmd+P on Mac)")
        print(f"   3. Select 'Save as PDF'")
        print(f"   4. Choose 'More settings' and set margins to 'Minimum'")
        print(f"   5. Click 'Save'")
    else:
        print("\n❌ Failed to create HTML file")
        exit(1)
