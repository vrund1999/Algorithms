# Time complexity: 
#   Best:   Big Omega(n log(n))
#   Avg:    Big Theta(n log(n))
#   Worst:  O(n log(n))

# Space Complexity
#   Worst: O(n)

def mergeSort(list):
    if(len(list) > 1):
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        mergeSort(left)

        mergeSort(right)

        l = 0
        r = 0
        i = 0

        #Compare and add to sorted list
        while(l < len(left) and r < len(right)):
            if (left[l] <= right[r]):
                list[i] = left[l]
                l += 1
            else:
                list[i] = right[r]
                r += 1
            i += 1
        
        #Add anything left over from the left and right lists
        while(l < len(left)):
            list[i] = left[l]
            l += 1
            i += 1
        
        while(r < len(right)):
            list[i] = right[r]
            r += 1
            i += 1

    return list

if __name__ == '__main__':
    sampleList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5]
    sortedList = mergeSort(sampleList)
    print(sortedList)
