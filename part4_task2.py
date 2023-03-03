import os
import word_set as ws
from random import sample
import matplotlib.pyplot as plt
import time


# file read
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


max_size = 1000    # words to be added
max_buckets = []
set_sizes = []
add_times = []

samp = sample(lst_eng, max_size)    # list with random sample words
word_set = ws.new_empty_set()
for words in samp:               # add sample words into the set
    before = time.time()
    ws.add(word_set, words)     # count add time per set size
    after = time.time()
    add_times.append(after-before)
    max_buckets.append(ws.max_bucket_size(word_set))   # get max bucket size
    set_sizes.append(ws.count(word_set))              # get set size


# raph plot
fig = plt.figure(1)
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(set_sizes, add_times, 'b.')
ax1.set_ylabel('Add time')
ax1.set_title('Set size vs Add time')

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(set_sizes, max_buckets, 'b.')
ax2.set_xlabel('Set size')
ax2.set_ylabel('Max bucket size')
ax2.set_title('Set size vs Max bucket size')
plt.show()
