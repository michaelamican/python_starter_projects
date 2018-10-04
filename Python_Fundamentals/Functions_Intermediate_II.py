#1. Figure out all of this below

def update_x(a,b,c):
	for x[a][b] in x:
		x[a][b] = c
	print(x[a][b])
	print(x[a])

update_x(1,0,15)

def update_name(a,b):
    for students[a]['last_name'] in students:
        students[a]['last_name'] = b
    print(students[a]['last_name'])
    print(students[a])

update_name(0,'Bryant')

def update_sports(a,b):
    for sports_directory['soccer'][a] in sports_directory:
        sports_directory['soccer'][a] = b
    print(sports_directory['soccer'][a])
    print(sports_directory['soccer'])

def update_z(a,b):
	for z[1][a] in z:
		z[1][a] = b
	print(z[1][a])
	print(z[1])


#2. 
def iterate_dictionary(students):
	for students in students:
		print(students)

#3.
def iterate_dictionary_2(students):
	for students in students:
		print(students['first_name'])

#4.
def print_dojo_info(dojo):
	for locations in dojo:
		count = 0
		count += 1
		print(count+" LOCATIONS")
		print(dojo['locations'])
	for instructors in dojo:
		count = 0
		count += 1
		print(count+" INSTRUCTORS")
		print(dojo['instructors'])

