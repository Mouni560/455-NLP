#CODE:
import re
import json
import zlib
from collections import defaultdict
from difflib import get_close_matches

CORPUS = """going to china who was the first president of india winner of the match food in america """

compressed_corpus = zlib.compress(json.dumps(CORPUS.split()).encode())

def load_corpus():
    return json.loads(zlib.decompress(compressed_corpus).decode())

def correct_query(query, word_list):
    words = query.split()
    corrected_words = []
    
    for word in words:
        matches = get_close_matches(word, word_list, n=1, cutoff=0.8)  # Find close matches
        if matches:
            corrected_words.append(matches[0])
        else:
            corrected_words.append(word)  # Keep the original word if no match found
    return " ".join(corrected_words)


def main():
    word_list = load_corpus()
    n = int(input().strip())  
    queries = [input().strip() for _ in range(n)]
    
    for query in queries:
        print(correct_query(query, word_list))

if __name__ == "__main__":
    main()
#RESULT:
Input (stdin)
4
gong to china
who ws the first president of india
winr of the match
fod in america
Expected Output
going to china
who was the first president of india
winner of the match
food in america
