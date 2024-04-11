import unittest
from main import (
    convert_paragraphs_to_html, convert_md_to_ansi,
    check_nested_markup, check_correct_nested
)

class TestMarkdownConverter(unittest.TestCase):
    def test_convert_paragraphs_to_html(self):
        test_cases = [
            ('**bold**', '<strong>bold</strong>'),
            ('_italic_', '<em>italic</em>'),
            ('`code`', '<code>code</code>'),
        ]

        for input_text, expected_output in test_cases:
            with self.subTest(i=input_text):
                self.assertEqual(convert_paragraphs_to_html(input_text), expected_output)

    def test_convert_md_to_ansi(self):
        test_cases = [
            ('**bold**', '\033[1mbold\033[0m'),
            ('_italic_', '\033[3mitalic\033[0m'),
            ('`code`', '\033[4mcode\033[0m'),
        ]

        for input_text, expected_output in test_cases:
            with self.subTest(i=input_text):
                self.assertEqual(convert_md_to_ansi(input_text), expected_output)

    def test_check_nested_markup(self):
        test_cases = [
            ('This is **bold and _nested_ bold** text', True),
            ('This is **bold and _not nested**_ text', False),
        ]

        for input_text, expected_output in test_cases:
            with self.subTest(i=input_text):
                self.assertEqual(check_nested_markup(input_text), expected_output)

    def test_check_correct_nested(self):
        test_cases = [
            ('**bold** _italic_ `code`', True),
            ('**bold _italic_ `code`', False),
        ]

        for input_text, expected_output in test_cases:
            with self.subTest(i=input_text):
                self.assertEqual(check_correct_nested(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
