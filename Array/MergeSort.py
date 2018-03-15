#.................................................
def sortII(A):
        # Write your code here
        temp = [0] * len(A)
        merge_sort(A, 0, len(A) - 1, temp)
        print A
        
def merge_sort(A, start, end, temp):
    if start >= end:
        return
    
    mid = (start + end) / 2
    merge_sort(A, start, mid, temp)
    merge_sort(A, mid + 1, end, temp)
    merge(A, start, mid, end, temp)
        
def merge(A, start, mid, end, temp):
    left, right = start, mid + 1
    index = start
    while left <= mid and right <= end:
        if A[left] < A[right]:
            temp[index] = A[left]
            left += 1
        else:
            temp[index] = A[right];
            right += 1           
        index += 1
        
    while left <= mid:
        temp[index] = A[left]
        left += 1
        index += 1
        
    while right <= end:
        temp[index] = A[right]
        right += 1
        index += 1
        
    for index in range(start, end + 1):
        A[index] = temp[index]	


sortII([3,2,1,4,5])



