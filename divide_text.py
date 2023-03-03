import os
import re

# some more restriction to define the words
def is_word(s):
    for char in s:
        if not char.isalpha() and char != "'" and char != "-":
            return False
    if s.count("-") > 1:
        return False
    if s.count("'") > 1:
        return False
    if s.count("-") == 1:
        index_hyphen = s.index("-")
        # if hyphen(-) is at the beginning or in the end of string s
        if index_hyphen == 0 or index_hyphen == len(s)-1:
            return False
    if s.count("'") == 1:
        index_quote = s.index("'")
        # if single quote(') is at the beginning or in the end of string s
        if index_quote == 0 or index_quote == len(s)-1:
            return False
    return True


def read_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            lst = []
            text = file.read()
            lines = text.lower()
            lst += re.findall(r"[a-z'-]+", lines)
        return lst
    except FileNotFoundError as e:
        print(e)
        print("No such file or directory:", file_path)


# write all words to the file "words.txt", one word per line
def write_file(lst, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for string in lst:
                if is_word(string) is True:
                    file.write(string + "\n")
    except FileNotFoundError as e:
        print(e)
        print("No such file or directory:", file_path)


path = os.getcwd()

eng_path = path + "/eng_news_100K-sentences.txt"
eng_words_path = path + "/eng_news_words.txt"

lst_eng = read_file(eng_path)
write_file(lst_eng, eng_words_path)

holy_path = path + "/holy_grail.txt"
holy_words_path = path + "/holy_grail_words.txt"

lst_holy = read_file(holy_path)
write_file(lst_holy, holy_words_path)
