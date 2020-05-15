import time
from os import path
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

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
