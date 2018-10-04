#Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggie_size(arr):
    for i in arr:
    	if i > 0:
    		arr[i] = "big"
    return arr



#Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(arr):
	pos = 0
	for i in arr:
        if i > 0:
        	pos += 1
    arr[len(arr)-1] = pos
    return arr


#SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sum_total(arr):
   sum = 0
   for i in arr:
        sum += i
    return sum


#Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def average(arr):
	sum = 0
	counter = 0
    for i in arr:
    	counter += 1
    	sum += i
    return(sum/counter)


#Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def find_length(arr):
	count = 0
	for i in arr:
		count += 1
	return count


#Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def find_min(arr):
	min = arr[0]
	for i in arr:
		if len(arr) == 0:
			return False
		elif min > i:
		    min = i
		else:
			i += 1
	return min


#Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.


def find_max(arr):
	max = arr[0]
	for i in arr:
		if len(arr) == 0:
			return False
		elif max < i:
		    max = i
		else:
			i += 1
	return max

#UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultimate_analyze(arr):
	sum = 0
	avg = 0
	min = arr[0]
	max = arr[0]
	count = 0
	for i in arr:
		if max < i:
			max = i
		if min > i:
			min = i
		sum += i
		count += 1
	return({'sumTotal':sum,'average':(sum/count),'minimum':min,'maximum':max,'length':count})

#ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse_list(arr):
	temp = 0
	for i in (len(arr))/2:
		temp = arr[i]
		arr[i] = arr[len(arr)-1-i]
		arr[len(arr)-1-i] = temp