#@author: kgsharathkumar from PathTech
''' Write and Execute a python program to
	a) Read a value from User via Cmd Line.
	b) Check that enterd value is Number or String?
	c) If given value is in Number, Convert into Single digit.
	d) If given number is in sting, give error message
'''
def add_digits(num):
         if num > 0:
            return (num - 1) % 9 + 1
         else:
             return 0

print(add_digits(int(input("Enter number which we need to conver into Single digit: "))))

