import os
import table as tbl
from random import sample
from random import choice
import matplotlib.pyplot as plt
import time


# word reading
def read_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            word_lst = file.read().split()
        return word_lst
    except FileNotFoundError as e:
        print(e)
        print("No such file or directory:", file_path)


path = os.getcwd()
eng_path = path + "/eng_news_words.txt"
lst_eng = read_file(eng_path)


lst_size = [100, 1000, 2000, 5000, 7000,
            10000, 15000, 20000, 30000, 40000, 50000]   # sample sizes

repeat = 20000   # amount of look-ups
avg_times = []
max_d = []

for size in lst_size:
    samp = sample(lst_eng, size)    # list with ranndom sample words
    root = tbl.new_empty_root()
    for words in samp:
        tbl.add(root, words, 0)
    local_times = []
    for lookup in range(repeat):
        # choosing one random word from our sample list
        rand_word = choice(samp)
        before = time.time()
        tbl.get(root, rand_word)    # counting time to look up for the word
        after = time.time()
        local_times.append(after - before)
    max_d.append(tbl.max_depth(root))             # get max depth
    avg_times.append(sum(local_times)/repeat)    # get average look-up time


# graph plot
fig = plt.figure(1)
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(lst_size, avg_times, 'b.')
ax1.set_ylabel('Look - up time')
ax1.set_title('Look - up time vs Tree size')

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(lst_size, max_d, 'b.')
ax2.set_xlabel('Tree size')
ax2.set_ylabel('Max depth')
ax2.set_title('Max depth vs Tree size')
plt.show()
