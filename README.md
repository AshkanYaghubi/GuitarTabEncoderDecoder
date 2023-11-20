# Guitar Tab Encoder and Decoder

This Python script encodes and decodes guitar tabs. It can be used as a foundation for creating a machine-learning app that generates tabs for any song uploaded. The script currently supports basic encoding and decoding of guitar tabs, including frets and techniques.

## Features
- **Encoding:** Convert a human-readable guitar tab into a machine-readable format.
- **Decoding:** Convert an encoded guitar tab back to a human-readable format.
- **Techniques:** Supports common techniques like slides, bends, and more.

## Usage

### Encoding
```python
# Example
# A part of the Seven Nation Army Tab :)
tab = """
E|--------------------------
B|--------------------------
G|--------------------------
D|--------------------------
A|-7--7--/10--7--5--3--2----
E|--------------------------
"""

encoded_tab = encode_tab(tab)
print(encoded_tab)
```
#### Output
```python
[17, 17, 20, 110, 17, 15, 13, 12]
```

### Decoding
```python
# Example
encoded_tab = [17, 17, 20, 110, 17, 15, 13, 12]  
decoded_tab = decode_tab(encoded_tab)
print(decoded_tab)
```
#### Output
```python
E|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
B|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
G|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
D|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
A|7|7|-|/10|7|5|3|2|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
E|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
```

## Future Work
- Extend encoding and decoding capabilities
- Integrate wich machine learning for automatic tab generation

Feel free to contribute and enhance the functionality!

## Contributors
- Ashkan Yaghubi

## Licence
This project is licensed under the MIT License.
