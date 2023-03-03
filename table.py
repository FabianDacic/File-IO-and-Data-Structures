# A binary search based dictionary imlementation
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child


# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None, None, None, None]


# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root, key, value):
    if root[0] is None or root[0] == key:
        root[0] = key
        root[1] = value

    else:
        if key > root[0]:
            if root[3] is None:
                root[3] = [key, value, None, None]
            else:
                add(root[3], key, value)

        if key < root[0]:
            if root[2] is None:
                root[2] = [key, value, None, None]
            else:
                add(root[2], key, value)
    return root


# Returns a string representation of the table content.
# That is, all key-value pairs
def to_string(node):
    s = ""

    if node[2] is not None:
        s += to_string(node[2]).strip("{}" + " ")

    s += f" ({node[0]},{node[1]}) "

    if node[3] is not None:
        s += to_string(node[3]).strip("{}" + " ")

    return f"{{ {s} }}"


# Returns the value for the given key. Returns None if key doesn't exists.
def get(node, key):
    if node[0] is None:
        return None

    if node[0] == key:
        return node[1]

    else:
        if node[0] > key:
            if node[2] is not None:
                return get(node[2], key)

        if node[0] < key:
            if node[3] is not None:
                return get(node[3], key)


# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):
    if node is None:
        return 0   # return 0 for none nodes

    left_depth = max_depth(node[2])    # find the max_depth on the left side
    right_depth = max_depth(node[3])   # find the max_depth on the right side

    return max(left_depth, right_depth) + 1  # return 1 for not none nodes


# Returns the number og key-value pairs currently stored in the table
def count(node):
    counter = 0

    if node[2] is not None:
        counter += count(node[2])

    counter += 1

    if node[3] is not None:
        counter += count(node[3])

    return counter


# Returns a list of all key-value pairs as tuples
# sorted as left-to-right, in-order
def get_all_pairs(root):
    pairs = []

    if root[2] is not None:
        pairs += get_all_pairs(root[2])

    pairs += [(root[0], root[1])]

    if root[3] is not None:
        pairs += get_all_pairs(root[3])

    return pairs
