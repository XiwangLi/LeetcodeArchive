 #QuickSort
def sort(A):
 	if not A or len(A) == 0:
 		return
 	quicksort(A, 0, len(A) - 1)
	print A

def quicksort(A, start, end):
 	if start >= end:
 		return
 	left, right = start, end
 	pivot = A[(start + end) / 2]
 	while left <= right:
 		while left <= right and A[left] < pivot:
 			left += 1
 		while right >= left and A[right] > pivot:
 			right -= 1
 		if left <= right:
 			A[left], A[right] = A[right], A[left]
 			left += 1
 			right -= 1
 	quicksort(A, start, right)
 	quicksort(A, left, end)


