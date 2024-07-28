# Numeronym-ish

Numeronym-ish is a Python program that automatically converts words to their corresponding numbers based on their phonetic similarity. It leverages the International Phonetic Alphabet (IPA) to identify similar sounding parts of words and replaces them with numbers. This can lead to fun and creative transformations of text while maintaining readability.

## How Numeronym-ish Works

1. **IPA JSON Data**: Numeronym-ish uses an IPA JSON file (`IPA.json`) containing mappings of words to their IPA representations. If the JSON file doesn't exist, it's automatically downloaded.

2. **IPA Representation of Numbers**: The program generates IPA representations for numbers from 0 to 10 using the IPA JSON data. These representations are used as a reference for identifying similar sounding parts of words.

3. **Input Sentence**: Users are prompted to enter a sentence.

4. **Conversion to IPA**: The sentence is converted to IPA representations using the IPA JSON data. Words not found in the JSON data remain unchanged.

5. **Transformation**: Numeronym-ish identifies IPA words that contain similar sounding parts of numbers and replaces them with corresponding numbers. For example, "ate" might be transformed to "8".

6. **Conversion Back to Words**: The transformed IPA sentence is converted back to a sentence of words. Words that haven't been transformed remain unchanged.

7. **Display Results**: The transformed sentence is displayed, showcasing the creative and phonetically driven Numeronym-ish transformations.

## Example

Suppose you have the sentence: `Hate in the nation`

Numeronym-ish might transform it to: `H8 in the nation`


## Getting Started

1. Clone this repository to your local machine.
2. (optional) Make a virtualenv 
3. Get requirements by `pip install -r requirements.txt`
4. Run `main.py` using Python 3: `python main.py`.

## Dependencies

Numeronym-ish relies on the following components:

- `util.py`: Utility functions for reading and writing files, handling JSON data, and more.
- `ipa.py`: Functions for generating IPA representations of numbers, transforming IPA sentences, and converting between IPA and words.
- `downloadJSON.py`: Downloads the IPA JSON data if it doesn't already exist.

## Contribute

Contributions are welcome! If you'd like to add new features, improve existing ones, or fix issues, feel free to create a pull request.

## Acknowledgments

Numeronym-ish was inspired by the creative ways text can be transformed while retaining phonetic similarities.

## License

This project is licensed under the [MIT License](LICENSE).
