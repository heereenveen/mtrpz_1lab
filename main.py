import argparse
import sys
import re

def convert_paragraphs_to_html(markdown_text):
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<em>\1</em>', markdown_text)
    markdown_text = re.sub(r'(?<!`)(?!```)`([^`]+)`(?!```)', r'<code>\1</code>', markdown_text)
    return markdown_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='input_file', type=str)
    parser.add_argument('--out', dest='output_file', metavar='output_file', type=str)
    args = parser.parse_args()