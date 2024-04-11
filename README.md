# Markdown to HTML Converter

## Description
This Python application converts Markdown files to HTML format. It supports the conversion of basic Markdown syntax, including bold, italic, and inline code, to their HTML counterparts. The application also includes validation for nested and correct usage of Markdown syntax to ensure the output HTML is as expected.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
Clone the repository to your local machine:
   ```sh
   git clone https://github.com/heereenveen/mtrpz_1lab
   ```

### Running the Application
To convert a Markdown file to HTML, run the `main.py` script with the input file name as an argument. Optionally, you can specify an output file name to save the converted HTML:

```sh
python main.py input_file.md --out output_file.html
```

If no output file is specified, the program will print the converted HTML to standard output.

## User Guide

### Supported Markdown Features
- **Bold**: Wrap your text with `**` to make it bold. For example, `**bold text**` converts to `<strong>bold text</strong>`.
- *Italic*: Use `_` to italicize your text. For instance, `_italic text_` becomes `<em>italic text</em>`.
- `Inline Code`: To format text as inline code, enclose it with backticks (`` ` ``). For example, `` `code` `` turns into `<code>code</code>`.

### Validation
The application checks for incorrect nesting and unmatched symbols to ensure the Markdown is correctly formed before conversion.

### Error Handling
If there are any issues with the Markdown syntax or if the input file cannot be found, the application will provide an error message and terminate the execution to prevent incorrect HTML conversion.

## Revert-commit
The [following link](https://github.com/heereenveen/mtrpz_1lab/commit/789b3fd20cd69e7ea2a349c2456b45ca08eedab1) contains our reverse commit.

## Failure commit for CI tests:
The [following link](https://github.com/heereenveen/mtrpz_1lab/commit/cba4a3fd18f35dd38cd2773df12bd53352e08e23) contains our failure commit.

## Brief conclusions about Unit Tests:
I think unit tests are very useful and easy to use. I used the unittests library to create my tests, and it didn't take much time to write them, read the documentation - write the code. Testing is very helpful when your code is very "heavy" and structural, when one small change can destroy everything and you can't know why it happened, unit tests help with this. You can never have too many unit tests :3