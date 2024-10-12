#dosyayı açan ve okuyan kod
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
file_path = 'eylulhaziran.txt'
text = read_file(file_path)
print(text)

import string
from collections import Counter
#metni kelimelere ayıran ve noktalama işaretlerini ayıklayan kod
def clean_and_split_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()  
    words = text.split()  
    return words
#kelime sıklığını sayan kod
def count_words(words):
    return Counter(words)
words = clean_and_split_text(text)
word_counts = count_words(words)
print(word_counts.most_common(5))

#en sık kullanılmış ilk 5 kelimeyi sayan kod
def display_top_words(word_counts, n=5):
    most_common = word_counts.most_common(5)
    print(f"Top {5} words:")
    for word, count in most_common:
        print(f"{word}: {count}")

#yukarıdaki kodu display eden kod
display_top_words(word_counts, 5)


    