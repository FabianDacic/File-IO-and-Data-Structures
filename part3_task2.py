import os
import table as tbl
import matplotlib.pyplot as plt


# file read
def read_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            word_lst = file.read().split("\n")
        return word_lst
    except FileNotFoundError as e:
        print(e)
        print("No such file or directory:", file_path)


# lenghts of words count
def table(lst):
    root = tbl.new_empty_root()
    for word in lst:
        counter = tbl.get(root, len(word))  # look-up for key
        if counter is None:
            tbl.add(root, len(word),  1)  # if not found set value to one
        else:
            tbl.add(root, len(word), counter + 1)  # if found increase by one
    return root


path = os.getcwd()
file_path_holy = path + "/holy_grail_words.txt"
file_path_eng = path + "/eng_news_words.txt"

lst_holy = read_file(file_path_holy)
lst_eng = read_file(file_path_eng)


pairs_eng = tbl.get_all_pairs(table(lst_eng))
pairs_holy = tbl.get_all_pairs(table(lst_holy))

x1 = [l for l, c in pairs_eng]
y1 = [c for l, c in pairs_eng]

x2 = [l for l, c in pairs_holy]
y2 = [c for l, c in pairs_holy]

fig = plt.figure(1)
ax1 = fig.add_subplot(2, 1, 1)
ax1.bar(x1, y1)
ax1.set_ylabel('Word count')
ax1.set_title('English news')

fig = plt.figure(1)
ax2 = fig.add_subplot(2, 1, 2)
labels = [str(n) for n in x2]
ax2.bar(x2, y2)
plt.xticks(x2, labels)
ax2.set_xlabel('Word length')
ax2.set_ylabel('Word count')
ax2.set_title('Holy grail')
plt.show()
