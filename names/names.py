import time
from os import path
from ls_bst import BinarySearchTree

src_dir = path.split(path.abspath(__file__))[0]  # absolute path to source file
names1 = path.join(src_dir, 'names_1.txt')  # absoloute path to names_1.txt
names2 = path.join(src_dir, 'names_2.txt')  # absolute path to names_2.txt
start_time = time.time()

f = open(names1, 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(names2, 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# original nested for_loop => runtime: 5.117471933364868 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# solution 1: one for-loop =>  runtime: 1.2671453952789307 seconds
for x in names_1:
    if x in names_2:
        duplicates.append(x)


# solution 2: list comprehension => runtime: 1.7966792583465576 seconds
[duplicates.append(i) for i in names_1 if i in names_2]


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
