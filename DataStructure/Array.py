#write a python function to create Array and implement its function
import  array  as arr #importing array module
#creating array of integers
a=arr.array('i',[1,2,3,4,5,6])

print(a.typecode) #print data type of array

print(a.itemsize) #print lenght of bits of array

print(a.count(1)) #count the frequency of given argument

print(len(a))

#Run a loop to print the elements of the array'a'
print('the new created array is',end=' ')
for i in range (0,len(a)):
    print(a[i],end=' ')
print('\r') #moves pointer to the starts

#implementing some function over array
#insert, append,pop,extend

b=arr.array('i',[1,2,3,4,5,6])

a.append(0) #appending 0 to array a

a.extend(b) #adding all the array b into a

# again make a loop for printing new array
print('The new modified array is',end=' ')
for i in range(0,len(a)):
    print(a[i],end=' ')
print('\r')

print(a.pop()) #enter the index of number you want to remove
print(a.remove(5))
print(a)









