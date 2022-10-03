# Time complexity: 
#   Best:   Big Omega(n)
#   Avg:    Big Theta(n^2)
#   Worst:  O(n^2)

# Space Complexity
#   Worst: O(1)

def bubbleSort(list):
    i = 0
    j = 0
    swapped = False

    for i in range(0, len(list)):
        swapped = False
        for j in range(0, len(list) - 1 - i):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                swapped = True
        if(not swapped):
            break

    return list

if __name__ == '__main__':
    sampleList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]
    sortedList = bubbleSort(sampleList)
    print(sortedList)
