

# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         # Flag to optimize if no swaps occur
#         swapped = False
        
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # Traverse the array from 0 to n-i-1
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
        
#         # If no swapping occurred in this pass, array is sorted
#         if not swapped:
#             break
    
#     return arr

# my_list = [9,4,7,12,97,3,32]




# # Breakout Room:
# # Instructions:
# # Implement the Bubble Sort algorithm as shown
# # Trace the algorithm's execution for the array [64, 34, 25, 12, 22, 11, 90]
# # Count the number of comparisons and swaps required
# # Discuss any observations or insights about the algorithm
# # Expected Output:
# # A working Bubble Sort implementation
# # A step-by-step trace of the algorithm's execution
# # Counts of comparisons and swaps
# # Insights about the algorithm's behavior

# my_sorted_list = length(list)

# for numbers in range of my_sorted_list:








# *******************selection and insertion sort********************

def selection_sort(arr):

    value_list = len(arr)
    
    for value in range(value_list):

        minimum_index = value 

        for number in range(value+1, value_list):
            if arr[minimum_index] < arr[minimum_index]:
                minimum_index = number

        arr[value], arr[minimum_index] = arr[minimum_index], arr[value]

    return arr

my_list = [5, 3, 8, 4, 2]
sort_list = selection_sort(my_list)
print(sort_list)




def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                
