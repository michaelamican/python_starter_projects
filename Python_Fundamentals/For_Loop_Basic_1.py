#1 Basic - Print all the numbers from 0/150

def basic():
    x = 0
    while x<=150:
        print(x)
        x += 1

basic()

#2 Multiples of Five: Print all the multiples of 5 from 5 to 1,000,000
def multiples():
	x = 5
	while x <= 1000000:
	    print(x)
        x += 5

multiples()

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print "Dojo."
def countingDojo():
	x = 0
	while x <= 100:
		x += 1
		if x % 10 == 0:
            print("Dojo")
        elif x % 5 == 0:
            print("Coding")
        else:
            print(x)

countingDojo()

#4 Whoa, that sucker's huge. Add odd integers from 0 to 500,000, and print the final sum.

def suckersHuge():
	x = 0
	sum = 0
	while x <= 500000:
	    x += 1
	    sum += x
	print(sum)

suckersHuge()

#5. Countdown by Fours: Print positive numbers starting at 2018, counting down by fours (exclude 0)

def finalCountDown():
	x = 2018
	while x > 0:
		print(x)
		x -= 4

finalCountDown()

#6 Flexible Countdown. Based on earlier Countdown by Fours, given lowNum, highNum, mult, print multiples of mult from lowNum to highNum using a FOR loop. For(2, 9, 3) print 3 6 9 (on successive lines).

def flexibleCountDown(lowNum, highNum, mult):
	x = lowNum
	while x <= highNum:
		if x % mult != 0:
			x += 1
		else:
		    print(x)
		    x += mult

flexibleCountDown(2,9,3)



list = [3,5,1,2]
for i in list:
	print(i)

#returns 3,5,1,2

list = [3,5,1,2]
for i in range(list):
	print(i)

#returns undefined: list is not an integer;

list = [3,5,1,2]
for i in range(len(list)):
	print(i)

#returns 0,1,2,3