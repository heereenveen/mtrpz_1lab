import argparse
import sys
import re

def convert_paragraphs_to_html(markdown_text):
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<em>\1</em>', markdown_text)
    markdown_text = re.sub(r'(?<!`)(?!```)`([^`]+)`(?!```)', r'<code>\1</code>', markdown_text)
    return markdown_text

def convert_md_to_ansi(markdown_text):
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'\033[1m\1\033[0m', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'\033[3m\1\033[0m', markdown_text)
    markdown_text = re.sub(r'(?<!`)(?!```)`([^`]+)`(?!```)', r'\033[4m\1\033[0m', markdown_text)
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

def convert_markdown_to_format(input_file, output_file=None, output_format=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        if not check_nested_markup(markdown_text) or not check_correct_nested(markdown_text):
            sys.stderr.write("ПОМИЛКА: Розмітка не є коректною.")
            sys.exit(1)
        code_blocks = re.findall(r'```(.*?)```', markdown_text, flags=re.DOTALL)
        clean_text = markdown_text
        if output_format == 'ansi' or (output_format is None and output_file is None):
            clean_text = convert_md_to_ansi(clean_text)
            for block in code_blocks:
                default_block = block
                block = convert_md_to_ansi(default_block)
                clean_text = clean_text.replace(f'```{block}```', f'\033[7m{default_block}\033[0m')
        else:
            clean_text = convert_paragraphs_to_html(clean_text)
            for block in code_blocks:
                default_block = block
                block = convert_paragraphs_to_html(block)
                clean_text = clean_text.replace(f'```{block}```', f'<pre>{default_block}</pre>')
            paragraphs = clean_text.split('\n\n')
            html_paragraphs = [f'<p>{text}</p>' for text in paragraphs]
            clean_text = ''.join(html_paragraphs)
        if output_file:
            if output_file is None:
                sys.stdout.write(clean_text)
            else:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(clean_text)
        else:
            sys.stdout.write(clean_text)
    except FileNotFoundError:
        sys.stderr.write("Помилка: Файл не знайдено\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Помилка: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='input_file', type=str)
    parser.add_argument('--out', dest='output_file', metavar='output_file', type=str)
    args = parser.parse_args()
    convert_markdown_to_format(args.input_file, args.output_file, args.output_format)