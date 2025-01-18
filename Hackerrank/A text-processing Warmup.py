#code:
import re

def count_articles_and_dates(text):
    # Patterns to detect articles
    a_pattern = r'\\ba\\b'
    an_pattern = r'\\ban\\b'
    the_pattern = r'\\bthe\\b'

    # Patterns to detect dates
    date_patterns = [
        # Dates like 15/11/2012 or 15/11/12
        r'\\b\\d{1,2}/\\d{1,2}/\\d{2,4}\\b',
        # Dates like 15th March 1999 or 15th March 99
        r'\\b\\d{1,2}(st|nd|rd|th)?\\s+(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\\s+\\d{2,4}\\b',
        # Dates like 20th of March, 1999
        r'\\b\\d{1,2}(st|nd|rd|th)?\\s+of\\s+(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec),?\\s+\\d{2,4}\\b'
    ]

    # Count articles
    a_count = len(re.findall(a_pattern, text, re.IGNORECASE))
    an_count = len(re.findall(an_pattern, text, re.IGNORECASE))
    the_count = len(re.findall(the_pattern, text, re.IGNORECASE))

    # Count dates
    date_count = sum(len(re.findall(pattern, text, re.IGNORECASE)) for pattern in date_patterns)

    return a_count, an_count, the_count, date_count

def main():
    import sys
    input = sys.stdin.read().strip().splitlines()  # Properly split input into lines

    T = int(input[0])  # First line is the number of test cases
    results = []

    index = 1
    for _ in range(T):
        # Read text fragment
        text = input[index].strip()
        index += 2  # Skip the blank line after each fragment

        # Get counts
        a_count, an_count, the_count, date_count = count_articles_and_dates(text)

        # Store results
        results.extend([a_count, an_count, the_count, date_count])

    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
  #Result:
  Compiler Message
Success
Input (stdin)
5
Delhi, is a metropolitan and the capital region of India which includes the national capital city, New Delhi. It is the second most populous metropolis in India after Mumbai and the largest city in terms of area.
Mumbai, also known as Bombay, is the capital city of the Indian state of Maharashtra. It is the most populous city in India, and the fourth most populous city in the world, with a total metropolitan area population of approximately 20.5 million.
New York is a state in the Northeastern region of the United States. New York is the 27th-most extensive, the 3rd-most populous, and the 7th-most densely populated of the 50 United States.
The Indian Rebellion of 1857 began as a mutiny of sepoys of the East India Company's army on 10 May 1857, in the town of Meerut, and soon escalated into other mutinies and civilian rebellions largely in the upper Gangetic plain and central India, with the major hostilities confined to present-day Uttar Pradesh, Bihar, northern Madhya Pradesh, and the Delhi region.
The{-truncated-}
Your Output (stdout)
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Expected Output
1
0
4
0
1
0
5
0
1
0
6
0
1
0
6
1
4
1
13
1
