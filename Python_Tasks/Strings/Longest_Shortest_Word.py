### Напишете програма, която търси най-дългата
# и най-късата дума в едно изречение
# и изведете бройката на всички думи в изречението

def analyze_sentence(sentence):
    raw_words = sentence.split()
    words = [word.strip(".,!?;:") for word in raw_words]
    if not words:
        return None
    longest_word = max(words, key = len)
    shortest_word = min(words, key = len)
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Total words: {len(words)}")

text = input("Enter a sentence: ")
analyze_sentence(text)
