import json
from collections import Counter

def count_words_in_file(filename):
    word_count = Counter()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.lower()
            words = text.split()
            word_count.update(words)
    except FileNotFoundError:
        print("file does not exist")
        return None
    
    return word_count

if __name__ == "__main__":
    filename_in = "text.txt" 

    word_count = count_words_in_file(filename_in)
    if word_count is not None:
        result = json.dumps(word_count, ensure_ascii=False, indent=4)
        print(result)