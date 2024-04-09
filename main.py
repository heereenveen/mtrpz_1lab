import argparse
import sys
import re

def convert_paragraphs_to_html(markdown_text):
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<em>\1</em>', markdown_text)
    markdown_text = re.sub(r'(?<!`)(?!```)`([^`]+)`(?!```)', r'<code>\1</code>', markdown_text)
    return markdown_text

def check_nested_markup(markdown_text):
    clean_text = re.sub(r'```(.*?)```', '', markdown_text, flags=re.DOTALL)
    if re.search(r'\*\*_|_\*\*|`\*`|`\*`|`\*_|_`\*|`\*\*|`\*\*', clean_text):
        return False
    return True

def check_correct_nested(markdown_text):
    start_patterns = [
        r'(?<!\w)_(?=\w)',
        r'(?<!\w)\*\*',
        r'(?<!\w)`(?=\w)',
        r'(?<!\w)```(?=\w)'
    ]
    end_patterns = [
        r'\w_(?!\w)',
        r'(?<=\w)\*\*',
        r'(?<=\w)`',
        r'(?<=\w)```',
    ]
    for start_pattern, end_pattern in zip(start_patterns, end_patterns):
        start_matches = re.findall(start_pattern, markdown_text)
        end_matches = re.findall(end_pattern, markdown_text)
        if len(start_matches) != len(end_matches):
            return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='input_file', type=str)
    parser.add_argument('--out', dest='output_file', metavar='output_file', type=str)
    args = parser.parse_args()