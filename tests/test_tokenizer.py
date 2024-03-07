import unittest
from IBITTokenizer.tokenizer import IBITTokenizer


class TestTokenizer(unittest.TestCase):

    def test_tokenizer_text(self):
        ibit_tokenizer = IBITTokenizer()

        text = "سلام خوبی"

        encoded = ibit_tokenizer.encode(text)
        decoded = ibit_tokenizer.decode(encoded.ids)
        tokenized = ibit_tokenizer.tokenize(text)

        print(encoded)
        print(decoded)
        print(tokenized)

        self.assertEqual(text, decoded)


if __name__ == '__main__':
    unittest.main()
