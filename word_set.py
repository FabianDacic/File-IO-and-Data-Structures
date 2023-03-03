# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.

size = 0     # global variable, current number of elements


# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets


# Adds word to word set if not already added
def add(word_set, word):
    hash_value = my_hash(word)
    bucket_number = hash_value % len(word_set)
    if len(word_set) > count(word_set):
        if word not in word_set[bucket_number]:
            word_set[bucket_number] += [word]
    else:
        rehashing(word_set, word)


# Calculates the hash value of a word
def my_hash(word):
    hash_value = 0
    for char in word:
        ascii_code = ord(char)
        hash_value += ascii_code
    return hash_value


# make a copy of word_set, clear it, double its size
# add the original elements back to it
# add the word
def rehashing(word_set, word):
    clone = word_set.copy()
    word_set.clear()
    for i in range(len(clone)*2):
        word_set.append([])
    for b in clone:
        for w in b:
            add(word_set, w)
    add(word_set, word)


# Returns current number of elements in set
def count(word_set):
    c = 0
    for bucket in word_set:
        c += len(bucket)
    return c



# Returns current size of bucket list
def bucket_list_size(word_set):
    return len(word_set)



# Returns a string representation of the set content
def to_string(word_set):
    s = ''
    for bucket in word_set:
        for word in bucket:
            s += (word+' ')
    s = '{ ' + s + '}'
    return s



# Returns True if word in set, otherwise False
def contains(word_set, word):
    # check bucket number
    for bucket in word_set:
        if word in bucket:
            return True
    return False



# Removes word from set if there, does nothing
# if word not in set
def remove(word_set, word):
    # check bucket number
    for bucket in word_set:
        if word in bucket:
            bucket.remove(word)



# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    max_size = 0
    for bucket in word_set:
        if len(bucket) > max_size:
            max_size = len(bucket)
    return max_size
