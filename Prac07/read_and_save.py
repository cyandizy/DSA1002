import sys
from hash_table import *

if len(sys.argv) != 2:
    raise IndexError("Input file not specified in the argument.")

key_list = []
value_list = []

try:
    inputfile = open(sys.argv[1], "r")
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)

for line in inputfile:
    try:
        key, value = line.strip().split(",")
    except ValueError:
        print("Error: invalid format. Skipping this line.")
        continue
    
    key_list.append(key)
    value_list.append(value)

inputfile.close()

hash_table = DSAHashTable(11)
for key, value in zip(key_list, value_list):
    hash_table.put(key, value)

try:
    outputfile = open("saved_table.csv", "w")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

for key in sorted(set(key_list), key=key_list.index):
    outputfile.write(f"{key},{hash_table.get(key)}\n")

print(f"Successfully saved to a file.")

outputfile.close()