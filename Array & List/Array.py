from array import *
ar1 = array('i', [1,3,4,5,])
ar2 = array('d', [2.5,12.3])

print(ar1 , " and array 2 is : ", ar2)
#take input from list
li = [1,2,3,4]
ar1.fromlist(li)
print(ar1) #its auto extended with the list input
print(ar1.index(2)) #find the index of value 2

print(ar1.count(1))

li1 = [1,3,5,7,11]
del li1[1:3]
li1.pop(1)
print(li1)