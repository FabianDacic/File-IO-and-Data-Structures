import word_set as ws

# By using the set you should be able to count
# how many unique words that are used in the two given texts files
# words from "eng_news_100K-sentences.txt" are stored in eng_news_words.txt
# words from "holy_grail.txt" are stored in holy_grail_words.txt


try:
    with open("holy_grail_words.txt") as file:
        word_list2 = file.read().split("\n")
except IOError as e:
    print(e)
    print("Cannot find the file: holy_grail_words.txt")

word_set2 = ws.new_empty_set()
for word in word_list2:
    ws.add(word_set2, word)

print("File: holy_grail_words.txt")
print("The number of unique words:", ws.count(word_set2))

# takes times but the word count should be correct
try:
    with open("eng_news_words.txt", encoding="utf-8") as file:
        word_list1 = file.read().split("\n")
except IOError as e:
    print(e)
    print("Cannot find the file: eng_news_words.txt")

word_set1 = ws.new_empty_set()
for word in word_list1:
    ws.add(word_set1, word)

print("File: eng_news_words.txt")
print("The number of unique words:", ws.count(word_set1))
