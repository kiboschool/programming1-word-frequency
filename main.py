# word frequency analyzer
# counts the frequency of each word in some text
import re

def word_frequency(text):
    frequencies = {}
    words = text.replace('.', '').split()
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def report_frequency(text):
    frequencies = word_frequency(text)
    for key in frequencies:
        print(key, frequencies[key])

# Bonus: Normalization
def normalized_word_frequency(text):
    frequencies = {}
    # Example: split on a regex word boundary to strip punctuation
    # word_boundary = r'\W'
    # words = re.split(word_boundary, text)
    words = text.split()
    for word in words:
        word = word.lower()
        word = re.sub('\W', '', word)
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

# Run the report_frequency function when running the file
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        file = sys.argv[1]
        with open(file) as f:
            report_frequency(f.read())
    else:
        print("Usage: python main.py [file]")

