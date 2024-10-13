# word frequency analyzer
# counts the frequency of each word in some text

def word_frequency(text):
    pass
    
def report_frequency(text):
    pass

# Run the report_frequency function when running the file
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        file = sys.argv[1]
        with open(file) as f:
            report_frequency(f.read())
    else:
        print("Usage: python main.py [file]")

