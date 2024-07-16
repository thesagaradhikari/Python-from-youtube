# type caste
a = "1"
b = "3"
print(a + b)
# prints 13 cause it just concadinates the two strings

#implicit type casting
c = 3
d = 4
print(c+d)
#prints 7 adding the value of c and d 

#explicit type casting
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)