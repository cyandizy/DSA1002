# From Practical 07
import sys
from dsa_heap import *
from heap_entry_sort import heap_sort


if len(sys.argv) != 2:
    raise IndexError("Input file not specified in the argument.")

heap_entry_list = []

try:
    inputfile = open(sys.argv[1], "r")
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)

for line in inputfile:
    try:
        priority, value = line.strip().split(",")
    except ValueError:
        print("Error: invalid format. Skipping this line.")
        continue
    
    heap_entry = DSAHeapEntry(priority, value)
    heap_entry_list.append(heap_entry)

inputfile.close()

heap_sort(heap_entry_list)
print("The data have been sorted.")

try:
    outputfile = open(f"{sys.argv[1]}_sorted", "w")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

for entry in heap_entry_list:
    outputfile.write(f"{entry.get_priority()},{entry.get_value()}\n")

print(f"Successfully saved to a file.")

outputfile.close()