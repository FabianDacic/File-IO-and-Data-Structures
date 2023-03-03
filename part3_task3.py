import os
import table as tbl
import operator  # Tools for generalized attribute and item lookups


# Read the words from the words.txt and words2.txt files
def read_file(file_path):
    try:
        with open(file_path, encoding='latin-1') as file:
            word_lst = file.read().split()
        return word_lst
    except FileNotFoundError as e:
        print(e)
        print("No such file or directory:", file_path)


# Return a list of words with more than 4 letters
def freq(word_lst):
    freq_letters = []
    for word in word_lst:
        if len(word) > 4:
            freq_letters.append(word)
    return freq_letters


# Function to sort out the most frequent word, descending order
def sort_pairs(ls4):
    # <https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value>
    ls4.sort(key=operator.itemgetter(1))
    ls4.reverse()
    return ls4


# Addition of the words from the list to the table (root,key,value) == (root,word,count)
def table(lst):
    root = tbl.new_empty_root()
    for word in lst:
        counter = tbl.get(root, word)
        if counter is None:
            tbl.add(root, word,  1)
        else:
            tbl.add(root, word, counter + 1)
    return root


# Program starts (1)
path = os.getcwd()
file_path_holy = path + "/holy_grail_words.txt"
file_path_eng = path + "/eng_news_words.txt"
lst_holy = read_file(file_path_holy)
lst_eng = read_file(file_path_eng)


# Program starts (2) :sample:
lst_h = read_file(file_path_holy)
lst2_h = freq(lst_h)
ls3_h = table(lst2_h)
ls4_h = tbl.get_all_pairs(ls3_h)
lst_e = read_file(file_path_eng)
lst2_e = freq(lst_e)
ls3_e = table(lst2_e)
ls4_e = tbl.get_all_pairs(ls3_e)


# Program starts (3)
top_10_h = sort_pairs(ls4_h)
top_10_e = sort_pairs(ls4_e)
# print out the first ten elements
print("Top 10 words in Monty Python are:", top_10_h[:10])
print()
print("Top 10 words in News are: ", top_10_e[:10])
