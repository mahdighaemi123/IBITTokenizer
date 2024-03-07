from tokenizers import Tokenizer
import os
from pathlib import Path


class IBITTokenizer():

    def __init__(
        self: "IBITTokenizer",
        *args, **kwargs
    ) -> None:

        self.dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.tokenizer_path = str(
            self.dir_path / 'resource' / 'IBIT_TOKENIZER.json')

        self.tokenizer = Tokenizer.from_file(self.tokenizer_path)

    def encode(self, data):
        encoded = self.tokenizer.encode(data)
        return encoded

    def decode(self, data):
        decoded = self.tokenizer.decode(data)
        return decoded

    def tokenize(self, data):
        tokenized = self.tokenizer.encode(data)
        return tokenized.tokens

    def huggingface_tokenizer(self):
        return self.tokenizer


if __name__ == "__main__":
    ibit_tokenizer = IBITTokenizer()
    tokenizer = ibit_tokenizer.huggingface_tokenizer()

    text = "سلام خوبی"

    encoded = ibit_tokenizer.encode(text)
    decoded = ibit_tokenizer.decode(encoded.ids)
    tokenized = ibit_tokenizer.tokenize(text)

    print(encoded)
    print(decoded)
    print(tokenized)
