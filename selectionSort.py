# Time complexity: 
#   Best:   Big Omega(n^2)
#   Avg:    Big Theta(n^2)
#   Worst:  O(n^2)

# Space Complexity
#   Worst: O(1)

def selectionSort(list):
    i = 0
    j = 0
    temp = 0
    min = 0
    for i in range(0, len(list)):
        min = i
        for j in range(i+1, len(list)):
            if(list[j] < list[min]):
                min = j
                
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    
    return list

if __name__ == '__main__':
    sampleList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]
    sortedList = selectionSort(sampleList)
    print(sortedList)
