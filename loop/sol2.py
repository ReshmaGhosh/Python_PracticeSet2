# Sum of even number

n = int(input("Enter the upper limit: ") ) 
sum_even = 0

for i in range(1, n+1):
    if i % 2 ==0 : 
        sum_even =sum_even + i

print("Sum of even numbers is: ", sum_even)