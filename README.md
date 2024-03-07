# IBITTokenizer
Simple persian text-tokenizer base on tokenizers lib

## install
```
pip install IBITTokenizer --upgrade
```

## import

```
from IBITTokenizer.tokenizer import IBITTokenizer
```

## usage
```
ibit_tokenizer = IBITTokenizer()
tokenizer = ibit_tokenizer.huggingface_tokenizer()

text = "سلام خوبی"

encoded = ibit_tokenizer.encode(text)
decoded = ibit_tokenizer.decode(encoded.ids)
tokenized = ibit_tokenizer.tokenize(text)

print(encoded)
print(decoded)
print(tokenized)
```
