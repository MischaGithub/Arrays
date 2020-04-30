from array import *

#Creating a array
my_array = array("i",[20, 61, 35, 84, 77, 81, 91, 12, 31, 10])

#Creating a loop for the array
for i in my_array:
    print(i)

#Getting the total and the average of the marks
total = sum(my_array)
average = total//10
print(total)
print(average)