import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title_single_line(self):
        text = "# This is the header"
        result = extract_title(text)
        correct = "This is the header"
        self.assertEqual(result,correct)
    
    def test_extract_title_multi_line(self):
        text = """# This is the h1 header

## This is the h2 header

### This is the h3 header

This is text with **bold** and *italic* words.
"""
        result = extract_title(text)
        correct = "This is the h1 header"
        self.assertEqual(result, correct)