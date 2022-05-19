import json


userInput = input('Enter a .JSON file to read: ')
with open(userInput, "r") as read_file:
    print("Converting .JSON file to be able to read in Python")
    developer = json.load(read_file)
    print("Reading the .JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading .JSON file")


#This section will just check to see if it is solvable or not
def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0,9):
        for j in range (0,9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle):
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)

puzzle = [7,2,4],[5,0,6],[8,3,1]
if(isSolvable):
    print("solvable")
else:
    print("Not solvable")