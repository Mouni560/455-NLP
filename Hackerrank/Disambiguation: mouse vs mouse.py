#code:
def classify_mouse(sentence):
    
    computer_keywords = {"input", "device", "cursor", "usb", "click", "computer", "wireless", "screen"}
    animal_keywords = {"tail", "genome", "rodent", "postnatal", "environment", "development", "animal", "mouse"}

    
    words = set(sentence.lower().split())
    
    
    if computer_keywords & words:
        return "computer-mouse"
    elif animal_keywords & words:
        return "animal"
    else:
        return "animal"  

def main():
    
    N = int(input())
    
    
    for _ in range(N):
        sentence = input().strip()
        print(classify_mouse(sentence))

if __name__ == "__main__":
    main()
#RESULT:
Compiler Message
Success
Input (stdin)
3
The complete mouse reference genome was sequenced in 2002.
A mouse is an input device.
Tail length varies according to the environmental temperature of the mouse during postnatal development.
Expected Output
animal
computer-mouse
animal
