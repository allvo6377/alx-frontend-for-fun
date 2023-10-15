import sys

def markdown2html(markdown_file, output_file):
  """Converts a Markdown file to HTML.

  Args:
    markdown_file: The path to the Markdown file.
    output_file: The path to the output HTML file.
  """

  with open(markdown_file, "r") as f:
    markdown_content = f.read()

  html_content = markdown2html(markdown_content)

  with open(output_file, "w") as f:
    f.write(html_content)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

  markdown_file = sys.argv[1]
  output_file = sys.argv[2]

  if not os.path.exists(markdown_file):
    print("Missing {}".format(markdown_file), file=sys.stderr)
    sys.exit(1)

  markdown2html(markdown_file, output_file)

  sys.exit(0)
