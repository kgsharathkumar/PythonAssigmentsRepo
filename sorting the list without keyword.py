#@author: kgsharathkumar from PathTech
''' Write and Execute a python program to sort given list, without using keyword?
	'''
a=[1,4,6,3,2,5,8,7,9,0]
print("unsorted list:",a)

for i in range(0,9):
    for j in range (0,9):
        if(a[j]<a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

        
print("sorted list:",a)        
