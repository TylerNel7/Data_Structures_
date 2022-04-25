#Counting Sort Python Code
#Tyler Nelson

#Counting Sort Function 

def countingSortAlgorithm(array, max_no):
    m = max_no + 1
    count = [0] * m                
    for a in array:
        count[a] += 1         
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array[i] = a
            i += 1
    return array

numberArray = [8, 3, 4, 5, 7, 2, 1, 9, 20, 18, 12, 13, 6, 19, 11, 15, 10, 17, 14, 16]

result = countingSortAlgorithm(numberArray, 20)
print(result)
