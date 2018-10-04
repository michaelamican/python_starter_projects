def selection_sort(arr):
	temp = ""
	min = arr[0]
	for j in arr:
		for i in arr:
			if min > arr[i]:
			    min = arr[i]
		if arr[j] != min:
		    arr[j], min = arr[i], arr[j]
	print(arr)

arr=[50, 3, 2, 91, 7]