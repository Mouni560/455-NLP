#CODE:
import re

def load_words(file_path="words.txt"):
    """Load the dictionary of words from a file."""
    with open(file_path, "r") as file:
        return set(word.strip().lower() for word in file.readlines())

def preprocess_input(input_line):
    """
    Preprocess the input:
    - Remove "www." and domain extensions for domain names.
    - Remove "#" for hashtags.
    """
    input_line = input_line.lower()
    if input_line.startswith("www."):
        # Remove "www." and domain extensions
        input_line = re.sub(r'^www\.|(\.[a-z]{2,3}(\.[a-z]{2})?)$', '', input_line)
    elif input_line.startswith("#"):
        # Remove the hashtag symbol
        input_line = input_line[1:]
    elif re.match(r"^[a-z]+\.[a-z]{2,3}(\.[a-z]{2})?$", input_line):
        # For standalone domain names, remove extensions
        input_line = re.sub(r'\.[a-z]{2,3}(\.[a-z]{2})?$', '', input_line)
    return input_line

def segment_string(s, word_set):
    """
    Segment a string into valid words or numbers using a greedy algorithm.
    - Tries to match the longest possible prefix in the dictionary or as a number.
    """
    if not s:
        return []

    for i in range(len(s), 0, -1):
        prefix = s[:i]
        
        if prefix in word_set or re.fullmatch(r'\d+(\.\d+)?', prefix):
            rest = segment_string(s[i:], word_set)
            if rest is not None:  # Successful segmentation
                return [prefix] + rest
    return None  # No valid segmentation

def main():
    
    word_set = load_words("words.txt")
    
    
    n = int(input())
    inputs = [input().strip() for _ in range(n)]
    
    
    results = []
    for line in inputs:
        processed_input = preprocess_input(line)
        segmented = segment_string(processed_input, word_set)
        if segmented:
            results.append(" ".join(segmented))
        else:
            
            results.append(processed_input)
    
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
#RESULT
Compiler Message
Success
Input (stdin)
30
weather.com
businessweek.com
#businessweek89
#businessweek29.5
noaa.gov
whitehouse.gov
#56media
bluehost.com
privacy.gov.au
mediafire.com
opensource.org
people.com.cn
last.fm
bandcamp.com
dropbox.com
independent.co.uk
who.int
discovery.com
house.gov{-truncated-}
Expected Output
weather
business week
business week 89
business week 29.5
no a a
white house
56 media
blue host
privacy
media fire
open source
people
last
band camp
drop box
independent
who
discovery
house
blink web{-truncated-}
