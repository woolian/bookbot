frankenstein = "books/frankenstein.txt"

def main():
    report()
    

def get_text(path):
    with open(path) as f:
        text = f.read()
    return text

def count_words(text):
    return len(text.split())

def count_chars(text):
    lowered_text = text.lower()
    characters = {}
    for char in lowered_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def report():
    contents = get_text(frankenstein)
    words = count_words(contents)
    characters = count_chars(contents)
    print(f"--- Begin report of {frankenstein} ---")
    print(f"{words} words found in the document \n")
    sorted = []
    for char in characters:
        if char.isalpha() == True:
            sorted.append({"char":char, "count": characters[char]})    
    sorted.sort(reverse=True, key=sort_on)      
    for i in range(len(sorted)):
        print(f"The '{sorted[i]["char"]}' character was found {sorted[i]["count"]} times") 
    print("--- End report ---")

main()