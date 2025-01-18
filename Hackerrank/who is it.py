import re

def resolve_pronouns(text, entities):
    # Find all highlighted pronouns in the text
    pronouns = re.findall(r'\*\*(.*?)\*\*', text)
    
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Mapping of pronouns to entities
    pronoun_to_entity = []
    
    for pronoun in pronouns:
        resolved_entity = None
        closest_distance = float('inf')
        
        # Iterate through each sentence to find the pronoun and its closest entity
        for sentence in sentences:
            if f"**{pronoun}**" in sentence:
                # Get the position of the pronoun in the sentence
                pronoun_index = sentence.find(f"**{pronoun}**")
                
                # Check for the closest entity before the pronoun
                for entity in entities:
                    entity_index = sentence.find(entity)
                    if 0 <= entity_index < pronoun_index:
                        distance = pronoun_index - entity_index
                        if distance < closest_distance:
                            closest_distance = distance
                            resolved_entity = entity

        if not resolved_entity:
            # Fallback to search the entire text for the nearest entity if no match in the same sentence
            text_index = text.find(f"**{pronoun}**")
            for entity in entities:
                entity_index = text.find(entity)
                if 0 <= entity_index < text_index:
                    distance = text_index - entity_index
                    if distance < closest_distance:
                        closest_distance = distance
                        resolved_entity = entity
        
        pronoun_to_entity.append(resolved_entity)

    return pronoun_to_entity

def main():
    # Input reading
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])  # Number of lines in the text
    text = " ".join(data[1:N + 1])  # Combine text lines
    entities = data[N + 1].split(";")  # List of entities
    
    # Resolve pronouns
    results = resolve_pronouns(text, entities)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
#Result:
Compiler Message
Success
Input (stdin)
3
Alice was not a bit hurt, and **she** jumped up on to her feet in a moment: she looked up, but it was all dark overhead; before **her** was another long passage, and the White Rabbit was still in sight, hurrying down it. There was not a moment to be lost: away went Alice like the wind, and was just in time to hear it say, as **it** turned a corner, 'Oh my ears and whiskers, how late it's getting!' She was close behind **it** when she turned the corner, but the Rabbit was no longer to be seen: she found herself in a long, low hall, which was lit up by a row of lamps hanging from the roof. There were doors all round the hall, but they were all locked; and when Alice had been all the way down one side and up the other, trying every door, she walked sadly down the middle, wondering how she was ever to get out again. Suddenly she came upon a little three-legged table, all made of solid glass; there was nothing on **it** except a tiny golden key, and Alice's first thought was that **it** might belong to one of th{-truncated-}
Your Output (stdout)
Alice
Alice
door
door
door
door
door
Expected Output
Alice
Alice
White Rabbit
White Rabbit
three-legged table
tiny golden key
door
