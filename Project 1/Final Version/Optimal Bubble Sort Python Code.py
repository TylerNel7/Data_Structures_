#Optimal Bubble Sort Python Code
#Tyler Nelson

#Optimal Bubble Sort Function 
def bubbleSortAlgorithm(array):
    n = len(array)
    numberComp = 0

    for i in range(n - 1):
        tmparr = array[:]
        for x in range(n - 1):
            numberComp += 1
            if array[x] > array[x + 1]:
                temporaryHolder = array[x]
                array[x] = array[x + 1]
                array[x + 1] = temporaryHolder
            
        if tmparr == array:
            return array, numberComp

    return array, numberComp

numberArray = [8, 3, 4, 5, 7, 2, 1, 9, 20, 18, 12, 13, 6, 19, 11, 15, 10, 17, 14, 16]

result = bubbleSortAlgorithm(numberArray)
print(result)
