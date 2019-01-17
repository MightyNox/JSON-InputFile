import sys
import json
from pathlib import Path

# Check number of arguments
args = len(sys.argv)
if args == 1:
    print("No arguments were given!")
    exit(1)
elif args > 2:
    print("Too many arguments!")
    exit(1)

# Check input file path
path = sys.argv[1]
path_length = len(path)

if not path.endswith('.json'):
    print("Wrong extension!")
    exit(1)

print("Given path: ", path)

# Checking if file exists
if Path(path).is_file() == 0:
    print("File doesn't exist!")
    exit(1)

# Loading input
array = []
with open(path, "r") as json_file:
    data = json.load(json_file)
    for i in data["input_list"]:
        array.append(i)
        print(i, end=" ")
print("")

# Bubble Sort
sorted = False
while not sorted:
    sorted = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            sorted = False
            tmp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = tmp

# Print Sorted Array
for i in array:
    print(i, end=" ")
print("")
