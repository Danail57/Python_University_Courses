### Напиши програма текстов анализатор и цензура

def extract_domain(email):
    if "@" in email:
        return email.split("@")[-1]
    return "Invalid email"

def censor_word(text, word):
    if len(word) > 3:
        return text.replace(word, "*" * len(word))
    return text

def reverse_long_words(text):
    words = text.split()
    new_words = []
    for word in words:
        if len(word) > 5:
            new_words.append(word[::-1])
        else:
            new_words.append(word)
    return " ".join(new_words)

text = input("Enter some text: ")
word_to_censor = input("Enter word to censor: ")
email_to_check = input("Enter email to extract domain: ")
print("Domain:", extract_domain(email_to_check))
print("Censored text:", censor_word(text, word_to_censor))
print("Reversed long words:", reverse_long_words(text))
