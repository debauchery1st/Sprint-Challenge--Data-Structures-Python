import time
from os import path
from ls_bst import BinarySearchTree


src_dir = path.split(path.abspath(__file__))[0]  # absolute path to folder
names1 = path.join(src_dir, 'names_1.txt')  # absolute path to names_1.txt
names2 = path.join(src_dir, 'names_2.txt')  # absolute path to names_2.txt

f = open(names1, 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(names2, 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


def print_duplicates(lst):
    print(f"{len(lst)} duplicates:\n\n{', '.join(lst)}\n\n")


def print_runtime(descr, s, e):
    print(f"[{descr}] runtime: {e - s} seconds")


start_time = time.time()

duplicates = []  # Return the list of duplicates in this data structure

description = "originally 2 nested for_loops"
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
end_time = time.time()
print_duplicates(duplicates)
print_runtime(description, start_time, end_time)

description = "solution 1: one for-loop"
start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure

for name in names_1:
    if name in names_2:
        duplicates.append(name)

end_time = time.time()
print_duplicates(duplicates)
print_runtime(description, start_time, end_time)

description = "solution 2: list comprehension"
start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure
[duplicates.append(name) for name in names_1 if name in names_2]
end_time = time.time()
print_duplicates(duplicates)
print_runtime(description, start_time, end_time)


description = "solution 3: BST start with _ "
start_time = time.time()
duplicates = []
bst = BinarySearchTree("_")
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
end_time = time.time()
print_duplicates(duplicates)
print_runtime(description, start_time, end_time)

description = "solution 4: BST start with name A"
start_name = names_1.index("Abagail Dillon")
start_time = time.time()
duplicates = []
print(names_1[start_name])
bst = BinarySearchTree(names_1.pop(start_name))
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
end_time = time.time()
print_duplicates(duplicates)
print_runtime(description, start_time, end_time)

description = "solution 4: BST start with Z "
start_name = names_1.index("Zackery Meadows")
start_time = time.time()
duplicates = []
# print(names_1[start_name])
bst = BinarySearchTree(names_1.pop(start_name))
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
end_time = time.time()
print_duplicates(duplicates)
print_runtime(description, start_time, end_time)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
