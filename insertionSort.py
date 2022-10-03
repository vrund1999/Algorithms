def insertionSort(list):
    for i in range(1, len(list)):
        j = i - 1

        num = list[i]

        while(j >= 0 and list[j] > num):
            list[j + 1] = list[j]
            j = j - 1
        
        list[j + 1] = num
    
    return list

if __name__ == '__main__':
    sampleList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]
    sortedList = insertionSort(sampleList)
    print(sortedList)
        