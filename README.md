# Mini-project report 
Members: Fabian Dacic, Marios Gkikopouli, and Qingqing Dai  

Program: Software Technology  

Course: 1DV501 

Date of submission: 2020-10-30


## Introduction  

This project consists of four parts which involve text file handling, implementation and application of two data structures, and time measurement experiments.

## Part 1: Divide the text into words
The definition of a word depends on person to person. It is a consensus that it is a unit of a language, but in programming, it is quite difficult to define words. For the sake of the project, it has been decided that in order for it to be counted as a word it needs to be in English (Latin alphabet) and that special characters or punctuation placed in between the letters of a word would not be deemed as such. Complex words such as compound ones are also taken into account. The way this definition was implemented into our code is this: 

```python
lst = []
    text = file.read()
    lines = text.lower()
    lst += re.findall(r"[a-z'-]+", lines)
        return lst
```
Different methods and functions were experimented on in order to get the code to function properly and meet our demands. Finally, a decision was made to use the regular expression (re) module. 
The usage of the ``re`` module in this part was done with the help of a source that is credible and trusted by many and deemed as a genuine good source of learning for any beginner in Python named Guru99. [Reference to it](https://www.guru99.com/python-regular-expressions-complete-tutorial.html)
The words are read from the file and all of them are then lowered to make extraction easier. Then the re module is utilized through the ``findall()`` to get a list of the matching pattern that is every lowercase letter that is from a to z. Then the list is returned. The word count for ``holygrail.txt`` is 11277 and for ``eng_news_100k-sentences.txt`` is 1975479.





## Part 2: Implementing data structures
- Hash-based word set
	* The add() function in word_set has two help functions - my_hash() and rehashing():

	```python
	def add(word_set, word):
		hash_value = my_hash(word)
		bucket_number = hash_value%len(word_set)
		if len(word_set) > count(word_set):
			if word not in word_set[bucket_number]:
				word_set[bucket_number] += [word]
		else:
			rehashing(word_set, word)

	def my_hash(word):
		hash_value = 0
		for char in word:
			ascii_code = ord(char)
			hash_value += ascii_code
		return hash_value

	def rehashing(word_set, word):
		clone = word_set.copy()
		word_set.clear()
		for i in range(len(clone)*2):
			word_set.append([])
		for b in clone:
			for w in b:
				add(word_set, w)
		add(word_set, word)
	```

	``my_hash()`` calculates the hash value of a word by adding all the ASCII code of each character.\
	``rehashing()`` makes a copy of the word_set, empties the word_set, double its size, adds the elements from copy back to word_set and adds the word which is required to add.

	* differences
		The output of ``to_string()`` function is different from what the demo program shows as well as the max bucket size because of a different hashing method was used.
		
		
	* max_bucket_size
		The max bucket size of eng_news_words.txt: 308\
		The max bucket size of holy_grail.txt: 17

- The BST based table
	* The ``add()`` and ``max_depth()`` functions in table:
	```python
	def add(root,key,value):
		if root[0] == key:
			root[1] = value
		if root[0] == None:
			root[0] = key
			root[1] = value
		if root[0] > key:  # left
			if root[2] == None:
				root[2] = [key, value, None, None]
			else:
				add(root[2], key, value)
		if root[0] < key:  # right
			if root[3] == None:
				root[3] = [key, value, None, None]
			else:
				add(root[3], key, value)

	def max_depth(node):
    if node is None:
        return 0   # return 0 for none nodes

    left_depth = max_depth(node[2])   # find the max_depth on the left side
    right_depth = max_depth(node[3])   # find the max_depth on the right side

    return max(left_depth, right_depth) + 1  # return 1 for not none nodes
	```
	``add()`` function adds a key-value pair to the root. If the key is the same as the first element in the root, update the value. If it is an empty node, update it with the key-value pair. Otherwise, if the key is smaller than the first element of the node, check if its left-child is None. If so, update the left-child with the key-value pair. If not, call ``add()`` function. If the key is greater than the first element, check if the node's right-child is None. If so, update the right-child. If not, call ``add()`` function.

	``max_depth()`` function first checks if the node is None. If so, return 0. If not, call ``max_depth()`` while passing the left-child as a parameter, and assign the value to the variable left. Do the same to the variable right. In the end, return the bigger number of left and right plus 1. 1 is the root. In this way, the function can find the max_depth on the left side and the max_depth on the right side, and finally, return the max_depth of the tree.

	* The results are exactly the same as the example shows when running "table_main.py"
	* max_depth
		* max_depth for eng news: 43
		* max_depth for holy grail: 24




## Part 3: Word related exercises
- **First task:** by using set count the number of unique words in both files. The path this task followed to the solution started with reading the words generated by part 1. After the words are read they are then put into a list where in a collection based loop (other words, a ``for`` loop), the words are added to the set through the ``add()`` function. The function gets the hash value of a word and divides it with the length of the set and receives the remainder. Said remainder is the index position of the word. If the word is not in the set and the length of the set is larger than the count of elements in the buckets the word is then added with its corresponding index position. If the word is already in the bucket, it will not be added hence all words in the set are unique. Otherwise, rehashing undergoes. ``count()`` is then used to return the number of the unique words. Using this implementation, there are 1828 unique words in the ``holygrail.txt`` file and 86599 unique words in the ``eng_news_100k-sentences.txt`` one. 


- **Second task:** by using the table on should be able to count how many words of a given length each text has and to present a histogram (length vs count, plotted using matplotlib). First, the texts containing the unique words are read and the said words are then added to a list. Next step is a function being defined that for every word in the list the ``tbl.get()`` is used as a mean to check if the key (being len(word)) has a corresponding value (its occurrences). If not, then the key is added to the table and its values is set to one. Else if the key already has a value, then the said value is increased by one. 

```python
 def table(lst):
    root = tbl.new_empty_root()
    for word in lst:
        counter = tbl.get(root, len(word))    # look-up for key
        if counter is None:
            tbl.add(root, len(word),  1)    # if not found set value to one
        else:
            tbl.add(root, len(word), counter + 1)    # if found increase by one
    return root
```
Afterwards, with the help of the ``tbl.get_all_pairs()`` all key-value pairs are retrieved as tuples which are then turned into individual lists and used on the axis on our subplots to create the histogram. Looking at the histogram, it can be seen that words with 3 letters are the most occurring ones in ``eng_news_100k-sentences.txt`` whereas words with 4 letters are the most occurring ones in ``holygrail.txt``.


   <img src="https://i.imgur.com/mYUwgfL.png" width="500"/> 
	                                                           
    
- **Third task:** by using the table one should be able to present a list of the top 10 most frequently used words having a length larger than 4 letters.
After some trial and error, finally, a solution was found. First, the ``read_file()`` function is used in order to read the words extracted from part 1. Those very same words are then put in another function to return a list with words that have more than 4 letters. That list is then put in the ``table()`` function where for each key (in this case, keys = words) a corresponding value (value = words' occurrences) is attached to it. After that process is done, the pairs are retrieved and then ``sort_pairs()`` is utilized to sort out the pairs based on the occurrences. That is when ``item.getter()`` comes in. The implementation of it was done through the help of another user in StackOverflow which essentially is a question and answer site for programmers. [Reference to it](https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value). It groups the key-value pairs by the value. Finally, the result is then printed out.


**Monty Python text file:** 

|  Word         |   Occurrences   |
|:--------------|----------------:|
| arthur        | 261             |
| launcelot     | 101             |
| knight        |  84             |
| galahad       |  81             |
| father        |  74             |
| bedevere      |  68             |
| knights       |  65             |
| robin         |  58             |
| guard         |  58             |
| right         |  57             |

**English News text file:**

|  Word         |   Occurrences   |
|:--------------|----------------:|
| their         | 6145            |
| about         | 4612            |
| there         | 4298            |
| would         | 3884            |
| people        | 3883            |
| which         | 3578            |
| after         | 3016            |
| first         | 2888            |
| years         | 2815            |
| other         | 2757            |





## Part 4: Measuring time
- **First task:** Measure the time to look-up a fixed number of keys in trees of different sizes in your table implementation, Measure also the max tree depth at the same sizes. And present two plots (using matplotlib) showing look-up time vs tree size, and max depth vs tree size. Like the previous tasks we started by reading our text files and appended the contained words to a list, also, we created another list containing different sample sizes for our table.
Then for every size, we used the ``random.sample()`` function to create a new list with random words from the list that was storing our words and added them to the table. Next, we used ``random.choice()`` function to get a random word from our new list and measured the average time needed to look-up a word (key) ( for 20000 look-ups as ) well as the max depth. 

```python
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
        rand_word = choice(samp)    # choosing one random word from our sample list
        before = time.time()
        tbl.get(root, rand_word)    # counting time to look up for the word
        after = time.time()
        local_times.append(after - before)
    max_d.append(tbl.max_depth(root))             # get max depth
    avg_times.append(sum(local_times)/repeat)    # get average look-up time 
```
**Credits and sources:** The idea of implementing sample() and choice() functions was recommended by other students and how to implement and use them was looked up at [docs.python.org](https://docs.python.org/3/library/random.html)

Finally, we used our sample sizes, the average time measurements and the max depths as the axis of our subplots and we created the graphs.


<img src="https://i.imgur.com/6eAvrOi.png" width="600"/>

For the first graph **Look-up time vs Tree size**, The output is really close to what was expected, closely resembling a logarithmic function when comparing look-up time to tree size since the time complexity for a binary search tree when searching for an element is **O(logn)** but unfortunately, this wasn’t the case for every run maybe because our samples weren’t well randomized or enough.

For the second graph **Max depth vs Tree size**, the output seems to be as expected as well with the function increasing at a log rate when comparing max depth to tree size.

- **Second task:** Design an experiment measuring the time it takes to add new elements to your hash set and how it correlates to the rehashing. Measure also the max bucket size at various set sizes and present two plots (using matplotlib) showing add time vs set size, and max bucket size vs set size.
We start one more time by reading our files and storing the words to a list. 
Next using the ``random.sample()`` like the previous task we create a new list with a size of our choosing containing random words from our list storing the words then we start adding them to the set and we measure the time it takes to be added as well as the max bucket size using the ``ws.max_bucket_size()`` function and the set size using ``ws.count()`` function ( we measured the add time for 1000 words ).

```python
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
```
Finally, we used the set sizes, the add times that we measured as well as the max bucket sizes as the axis of our subplots and we create the graphs.

<img src="https://i.imgur.com/GmMIW6N.png" width="500"/>

The first **graph Set size vs Add time** seems to be as expected, the add time remains rather constant with a time complexity **O(1)** only increasing when the rehashing occurs and the rehashing time increases as the set size increases. 

The second graph Set **size vs Max bucket size** seems to be as expected as well, with the max bucket size increasing as the set size increases. 



### Technical issues 
- **What were the major technical challenges as you see it? What parts were the hardest and most time-consuming?**
	* Every part was demanding on its own way but in **part 2** of the project, the construction of the hash table and binary search tree required the most research and time of them all. 
	* Getting familiar using git lab was also another challenge we had to overcome.
- **What lessons have you learned?**
	* We learned the basics about constructing and implementing data structures(hash table and binary search tree), and about their time complexities. 
	* We also had the chance to get a better understanding of recursive functions since they were used consistently in **part 2** of the project.

- **How could the results be improved if you were given a bit more time to complete the tasks, what should you have done differently if you now were facing a similar project?**
    * Further improving the code in **part 1** so that it wouldn’t return words of huge lengths and we wouldn’t have to define single letters as words
	* create a better hashing function.
	* Try and figure how to make the time needed to count the number of unique words significantly shorter in **Part 3 Task 1**.
	* Had there been more time, we would also have used the opportunity to look further into different modules and functions so that our codes would be simpler, easier to read and more efficient. 
	* As well as working more on **part 4** tasks in order to produce more accurate results. 


### Project issues
- **Describe how your team organized the work. How did you communicate? How often did you communicate?**
	* First we examined the tasks and then divided the work. The main form of communication was (mostly) Slack, and commits in GitLab. We communicated on average almost every other day.
- **For each individual team member:** 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify the main contributors and co-contributors.
 	* Estimate hours spend each week (on average)
	    * **Part 1:**  Main contributor: Fabian , Co-contributors: Qingqing(``is_word()``)
		* **part 2:**  Co-contributors: Marios(Table) , Qingqing(Word set , table)
		* **part 3:**  Co-contributors: Fabian(task 2 , 3) , Marios( ``table()``) , Qingqing(task 1)
		* **part 4:**  Main contributors: Marios

		* Fabian: Estimated hours spend: 12-14 hr/w
		* Marios: Estimated hours spend: 30 hr/w
		* Qingqing: Estimated hours spend: 14 hr/w

 - **What lessons have you learned? What should you have done differently if you now were facing a similar project?**
	* We learned how to divide a project into small parts or tasks and share the responsibilities.
	* We also realized that doing proper research on the subjects you are asked to work on and having good communication with your team-mates is key for this kind of projects in order to avoid progress stall.
    * one thing we would have done differently is to use a task management tool like Trello to assign tasks to each member in our team and regularly check if things have been done in order to organize better. would also have had more meetings to discuss how we would approach certain problems.
