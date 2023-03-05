# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
             count_even+=1
        else:
             count_odd+=1
print("Count of even numbers :",count_even)
print("Count of odd numbers :",count_odd)

#New question of declering tuple

numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,52,432,86,59,31,32,324,39,56) # Declaring the tuple
odd = 0
even = 0
for x in numbers:
        if not x % 2:
             even+=1
        else:
             odd+=1
print("Count of even numbers :",even)
print("Count of odd numbers :",odd)