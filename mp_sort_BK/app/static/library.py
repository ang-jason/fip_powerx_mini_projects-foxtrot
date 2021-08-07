from org.transcrypt.stubs.browser import *
import random

## document foxtrot
array = []

def gen_random_int(number, seed):
	## code begins
	random.seed(seed)
	result = list(range(number))
	random.shuffle(result)
	return result
	## code ends


def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number, seed)


	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = ",".join(str(element) for element in array)+"."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def bubble_sort(array):
	changed = True
	n = len(array)
	while changed:
		changed = False
		next_n = 0
		for i in range(1,n):
			if array[i-1] > array[i]:
				array[i-1], array[i] = array[i], array[i-1]
				changed = True
				next_n = i
		n = next_n



def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

	sort_array = array[:]  ## make a copy
	bubble_sort(sort_array)

	array_str = ",".join(str(element) for element in sort_array)+"."
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	words = value.split(",") 
	try:
		nums = [float(elem) for elem in words]
	except:
		window.alert("Your textbox contains invalid numerics")
		return
	# store the final string to the variable array_str
	bubble_sort(nums)


	array_str = ",".join(str(element) for element in nums)+"."

	document.getElementById("sorted").innerHTML = array_str


