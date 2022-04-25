#Algorithm Testing App
#Tyler Nelson

#Required Imports 
import math 
import random
import time
from time import perf_counter

###Assist Functions###
def ArrayGenerator(num):
    array = []
    for i in range(num):
        array.append(random.randint(0, 1000))
    return array

def Swap(var1, var2, var3):
    temporaryHolder = var1[var2]
    var1[var2] = var1[var3]
    var1[var3] = temporaryHolder

def QuickSortSetUp(array):
    tic = perf_counter()
    low = 0
    high = len(array) - 1
    output = QuickSortAlgorithm(array, low, high)
    toc = perf_counter()
    time = toc - tic
    return output, time

def heapify(array, n, i, numberComp):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      numberComp += 2
      if l < n and array[largest] < array[l]:
          largest = l
      numberComp += 2
      if r < n and array[largest] < array[r]:
          largest = r
      numberComp += 1
      if largest != i:
          array[i], array[largest] = array[largest], array[i]
          nunbmerComp = heapify(array, n, largest, numberComp)
      return numberComp

###Algorithm Functions###
def SelectionSortAlgorithm(array):
    tic = perf_counter()
    numberComp = 0
    for i in range(len(array)):
        least = i
        for k in range(i + 1, len(array)):
            numberComp += 1
            if array[k] < array[least]:
                least = k
                Swap(array, least, i)
    toc = perf_counter()
    time = toc - tic
    return numberComp, time

def InsertionSortAlgorithm(array):
    tic = perf_counter()
    numberComp = 0
    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            numberComp += 2
            array[j + 1] = array[j]
            j = j - 1
        numberComp += 2
        array[j + 1] = k
    toc = perf_counter()
    time = toc - tic
    return numberComp, time
    
def MergeSortAlgorithm(array):
    tic = perf_counter()
    numberComp = 0
    numberComp += 1
    if len(array) > 1:
        r = len(array)//2
        fh = array[:r]
        lh = array[r:]
        MergeSortAlgorithm(fh)
        MergeSortAlgorithm(lh)
        i = j = k = 0
        while i < len(fh) and j < len(lh):
            numberComp += 2
            numberComp += 1
            if fh[i] < lh[j]:
                array[k] = fh[i]
                i += 1
            else:
                array[k] = lh[j]
                j += 1
            k += 1
        numberComp += 2
        while i < len(fh):
            numberComp += 1
            array[k] = fh[i]
            i += 1
            k += 1
        numberComp += 1
        while j < len(lh):
            numberComp += 1
            array[k] = lh[j]
            j += 1
            k += 1
        numberComp += 1
    toc = perf_counter()
    time = toc - tic
    return numberComp, time

def QuickSortAlgorithm(array, low, high):
    numberComp = 0
    numberComp += 1
    if low < high:
        p = low 
        i = low
        j = high
        while i < j:
            numberComp += 1
            while array[j] <= array[p] and i < high:
                numberComp += 2
                i += 1
            numberComp += 2
            while array[j] > array[p]:
                numberComp += 1
                j -= 1
            numberComp += 1
            numberComp += 1    
            if i < j:
                array[i], array[j] = array[j], array[i]
        numberComp += 1
        array[p], array[j] = array[j], array[p]
        QuickSortAlgorithm(array, low, j - 1)
        QuickSortAlgorithm(array, j + 1, high)
        return numberComp
    return numberComp

def HeapSortAlgorithm(array):
    tic = perf_counter()
    numberComp = 0
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        numberComp = heapify(array, n, i, numberComp)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        numberComp = heapify(array, i, 0, numberComp)
    toc = perf_counter()
    time = toc - tic
    return numberComp, time
    
def BubbleSortAlgorithm(array):
    tic = perf_counter()
    n = len(array)
    numberComp = 0
    for i in range(n - 1):
        for x in range(n - 1):
            numberComp += 1
            if array[x] > array[x + 1]:
                temporaryHolder = array[x]
                array[x] = array[x + 1]
                array[x + 1] = temporaryHolder
    toc = perf_counter()
    time = toc - tic 
    return numberComp, time

def OptimalBubbleSortAlgorithm(array):
    tic = perf_counter()
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
            toc = perf_counter()
            time = toc - tic
            return numberComp, time
    toc = perf_counter()
    time = toc - tic
    return numberComp, time

def CountingSortAlgorithm(array):
    max_no = None 
    for y in array:
        if (max_no is None or y > max_no):
            max_no = y
    
    tic = perf_counter()
    m = max_no + 1
    count = [0] * m 
    numberComp = 0               
    for a in array:
        count[a] += 1             
    i = 0
    for a in range(m):  
        numberComp += 1         
        for c in range(count[a]):  
            array[i] = a
            i += 1
            numberComp += 1
    toc = perf_counter()
    time = toc - tic
    return numberComp, time

while True:
    print('Welcome to the Algorthm Testing App!\nHere we will be testing various sorting algorithms with an array of randomly generated variables\nFirstly, would you like to test a single all of them?')
    print('------------------------------------------')
    print('Options (Input respected number)\n(1) Test an individual sorting algorithm\n(2) Test multiple sorting algorithms\n(q) To quite application')
    choice1 = str(input('Please enter you choice here: '))

    if choice1 == '1':
        print(' ')
        print('You have selected a single algorithm test\nWhich out of the following algorithms would you like to test?')
        print('------------------------------------------')
        print('Options (Input respected number)\n(1) Select Sort Algorithm\n(2) Insertion Sort Algorithm\n(3) Merge Sort Algorithm\n(4) Quick Sort Algorithm\n(5) Heap Sort Algorithm\n(6) Bubble Sort Algorithm\n(7) Optimal-Bubble Sort Algorithm\n(8) Counting Sort Algorithm')
        choice2 = str(input('Please enter your choice here: '))

        if choice2 == '1':
            print('\nYou have selected "Select Sort"')
            arraysize1 = int(input('Please enter your array size here: '))
            array1 = ArrayGenerator(arraysize1)
            print('Your array is: ' + str(array1))
            output1 = SelectionSortAlgorithm(array1)
            comp1, time1 = output1[0], str(output1[1] * 1000)
            print('The Select Sort of array length ' + str(arraysize1) + ' made ' + str(comp1) + ' comparisons and took ' + time1[:6] + ' ms\n')

        elif choice2 == '2':
            print('\nYou have selected "Insertion Sort"')
            arraysize2 = int(input('Please enter your array size here: '))
            array2 = ArrayGenerator(arraysize2)
            print('Your array is: ' + str(array2))
            output2 = InsertionSortAlgorithm(array2)
            comp2, time2 = output2[0], str(output2[1] * 1000)
            print('The Insert Sort of array length ' + str(arraysize2) + ' made ' + str(comp2) + ' comparisons and took ' + time2[:6] + ' ms\n')

        elif choice2 == '3':
            print('\nYou have selected "Merge Sort"')
            arraysize3 = int(input('Please enter your array size here: '))
            array3 = ArrayGenerator(arraysize3)
            print('Your array is: ' + str(array3))
            output3 = MergeSortAlgorithm(array3)
            comp3, time3 = output3[0], str(output3[1] * 1000)
            print('The Merge Sort of array length ' + str(arraysize3) + ' made ' + str(comp3) + ' comparisons and took ' + time3[:6] + ' ms\n')

        elif choice2 == '4':
            print('\nYou have selected "Quick Sort"')
            arraysize4 = int(input('Please enter your array size here: '))
            array4 = ArrayGenerator(arraysize4)
            print('Your array is: ' + str(array4))
            output4 = QuickSortSetUp(array4)
            comp4, time4 = output4[0], str(output4[1] * 1000)
            print('The Quick Sort of array length ' + str(arraysize4) + ' made ' + str(comp4) + ' comparisons and took ' + time4[:6] + ' ms\n')

        elif choice2 == '5':
            print('\nYou have selected "Heap Sort"')
            arraysize5 = int(input('Please enter your array size here: '))
            array5 = ArrayGenerator(arraysize5)
            print('Your array is: ' + str(array5))
            output5 = HeapSortAlgorithm(array5)
            comp5, time5 = output5[0], str(output5[1] * 1000)
            print('The Heap Sort of array length ' + str(arraysize5) + ' made ' + str(comp5) + ' comparisons and took ' + time5[:6] + ' ms\n')

        elif choice2 == '6':
            print('\nYou have selected "Bubble Sort"')
            arraysize6 = int(input('Please enter your array size here: '))
            array6 = ArrayGenerator(arraysize6)
            print('Your array is: ' + str(array6))
            output6 = BubbleSortAlgorithm(array6)
            comp6, time6 = output6[0], str(output6[1] * 1000)
            print('The Bubble Sort of array length ' + str(arraysize6) + ' made ' + str(comp6) + ' comparisons and took ' + time6[:6] + ' ms\n')

        elif choice2 == '7':
            print('\nYou have selected "Optimal-Bubble Sort"')
            arraysize7 = int(input('Please enter your array size here: '))
            array7 = ArrayGenerator(arraysize7)
            print('Your array is: ' + str(array7))
            output7 = OptimalBubbleSortAlgorithm(array7)
            comp7, time7 = output7[0], str(output7[1] * 1000)
            print('The Optimal-Bubble Sort of array length ' + str(arraysize7) + ' made ' + str(comp7) + ' comparisons and took ' + time7[:6] + ' ms\n')

        elif choice2 == '8':
            print('\nYou have selected "Counting Sort"')
            arraysize8 = int(input('Please enter your array size here: '))
            array8 = ArrayGenerator(arraysize8)
            print('Your array is: ' + str(array8))
            output8 = CountingSortAlgorithm(array8)
            comp8, time8 = output8[0], str(output8[1] * 1000)
            print('The Counting Sort of array length ' + str(arraysize8) + ' made ' + str(comp8) + ' comparisons and took ' + time8[:6] + ' ms\n')
        
        else:
            print(' ')
            print('Invalid choice\n')
            continue

    elif choice1 == '2':
        print(' ')
        print('You have selected to testing all algorithms\nResults will be displayed in a table such as:\n')
        print('---------------------------------------------------\n' +
              '| Sorting        | Array | Num. of     | Run time |\n' +
              '| Algorithm name | Size  | Comparisons | (in ms)  |\n' +
              '---------------------------------------------------\n')
        
        arrayallno = int(input('Please enter your array size here: '))
        arrayall = ArrayGenerator(arrayallno)
        print('Your array size is: ' + str(arrayallno) + '\n')
        print(arrayall)
        print('Running Algorithms...')
        time.sleep(1)

        print('---------------------------------------------------\n' +
              '| Sorting        | Array | Num. of     | Run time |\n' +
              '| Algorithm name | Size  | Comparisons | (in ms)  |\n' +
              '---------------------------------------------------\n')

        arrayall1 = arrayall.copy()
        arrayall2 = arrayall.copy()
        arrayall3 = arrayall.copy()
        arrayall4 = arrayall.copy()
        arrayall5 = arrayall.copy()
        arrayall6 = arrayall.copy()
        arrayall7 = arrayall.copy()
        arrayall8 = arrayall.copy()

        selectsort = SelectionSortAlgorithm(arrayall1)
        selectsortcomp, selectsorttime = selectsort[0], str(selectsort[1] * 1000)
        print('| Select Sort    | ' + str(arrayallno) + ' | ' + str(selectsortcomp) + ' | ' + selectsorttime[:6] + ' |\n' +
              '---------------------------------------------------\n')
        
        insertsort = InsertionSortAlgorithm(arrayall2)
        insertsortcomp, insertsorttime = insertsort[0], str(insertsort[1] * 1000)
        print('| Insert Sort    | ' + str(arrayallno) + ' | ' + str(insertsortcomp) + ' | ' + insertsorttime[:6] + ' |\n' +
              '---------------------------------------------------\n')
        
        mergesort = MergeSortAlgorithm(arrayall3)
        mergesortcomp, mergesorttime = mergesort[0], str(mergesort[1] * 1000)
        print('| Merge Sort     | ' + str(arrayallno) + ' | ' + str(mergesortcomp) + ' | ' + mergesorttime[:6] + ' |\n' +
              '---------------------------------------------------\n')

        quicksort = QuickSortSetUp(arrayall4)
        quicksortcomp, quicksorttime = quicksort[0], str(quicksort[1] * 1000)
        print('| Quick Sort     | ' + str(arrayallno) + ' | ' + str(quicksortcomp) + ' | ' + quicksorttime[:6] + ' |\n' +
              '---------------------------------------------------\n')

        heapsort = HeapSortAlgorithm(arrayall5)
        heapsortcomp, heapsorttime = heapsort[0], str(heapsort[1] * 1000)
        print('| Heap Sort      | ' + str(arrayallno) + ' | ' + str(heapsortcomp) + ' | ' + str(heapsorttime[:6]) + ' |\n' +
              '---------------------------------------------------\n')

        bubblesort = BubbleSortAlgorithm(arrayall6)
        bubblesortcomp, bubblesorttime = bubblesort[0], str(bubblesort[1] * 1000)
        print('| Bubble Sort    | ' + str(arrayallno) + ' | ' + str(bubblesortcomp) + ' | ' + str(bubblesorttime[:6]) + ' |\n' +
              '---------------------------------------------------\n')

        optimalbubblesort = OptimalBubbleSortAlgorithm(arrayall7)
        optimalbubblesortcomp, optimalbubblesorttime = optimalbubblesort[0], str(optimalbubblesort[1] * 1000)
        print('| Optimal Bubble Sort | ' + str(arrayallno) + ' | ' + str(optimalbubblesortcomp) + ' | ' + str(optimalbubblesorttime[:6]) + ' |\n' +
              '---------------------------------------------------\n')

        countingsort = CountingSortAlgorithm(arrayall8)
        countingsortcomp, countingsorttime = countingsort[0], str(countingsort[1] * 1000)
        print('| Counting Sort | ' + str(arrayallno) + ' | ' + str(countingsortcomp) + ' | ' + str(countingsorttime[:6]) + ' |\n' +
              '---------------------------------------------------\n')

    elif choice1 == 'q':
        print(' ')
        print('Shutting down...')
        print('Goodbye!')
        time.sleep(2)
        break 

    else:
        print(' ')
        print('Invlide choice\n')
        time.sleep(2)
        pass