import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

md_file = sys.argv[1]
html_file = sys.argv[2]

if not os.path.exists(md_file):
    print(f"Missing {md_file}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)

