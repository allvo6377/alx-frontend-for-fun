#!/usr/bin/python3
import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Convert a Markdown file to HTML.

    Args:
        input_file (str): The name of the Markdown file.
        output_file (str): The name of the output HTML file.

    Raises:
        FileNotFoundError: If the input Markdown file does not exist.

    Returns:
        None
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Missing {input_file}")

    with open(input_file, 'r') as f:
        markdown_content = f.read()
        html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    """
    Convert a Markdown file to HTML from the command line.

    Usage: python markdown2html.py <input_file> <output_file>
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_markdown_to_html(input_file, output_file)
        sys.exit(0)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
