#Scott Cagnard
#Assignment 2

#2.1 practice

str = "hello, i am a string"              #Create any certain string

x = str.find("am")      #Set x to find the position of "am" in str

print(x)              #Print the location of "am"

print(str.replace("i", "me"))   #Replace "i" with "me" in the string and print the new string

print("\n\n")  # print a couple of blank lines
input("Press and key to continute")
print("\n\n")  # print a couple of blank lines

#2.2 practice

s = "a string with words"    

n = len(s)          #This tells us the length of the string

print(s[0], s[1], s[2], s[n - 1])    #Print the characters of the string under a certain location

a = s[4:8]
b = s[:5]        #Locate the chain of characters under the specific location
c = s[5:]

print("t --> |" + a + "|")  
print("t --> |" + b + "|")          #Print the characters that were extracted
print("v --> |" + c + "|")

print("\n\n")  # print a couple of blank lines
input("Press and key to continute")
print("\n\n")  # print a couple of blank lines

#2.3


expr = "12+27"              #define the expression as a string

op_pos = expr.find("+")      #locate the plus sign in the expression

num1 = int(expr[:op_pos])       #extract the first number of the expression
num2 = int(expr[op_pos+1:])   #extract the second number of the expression



print("12 + 37 = ", num1 + num2)                  #calculate and print the sum of num1 and num2



x = input("Please enter an expression in the form num1 + num2") #Acquire an expression of addition
y = x.find("+")   #Locate the plus sign

if x.find("+") == -1:
    pass              #Do nothing if no plus sign found

n1= int(x[:y])              #Extract number before plus sign
n2 = int(x[y + 1:])           #Extract number after plus sign
 
print(n1, "+", n2, "=", n1 + n2)      #Calculate sum of two numbers and print finished expression with solution

print("\n\n")  # print a couple of blank lines
input("Press and key to continute")
print("\n\n")  # print a couple of blank lines


#2.4

b = input("Please enter an expression calculating two numbers")   #Acquire a numeric expression from user

while b != "end":    #Create a while loop with the condition that b is not equal to "end"
                #This while loop will keep asking for expressions to calculate until the user enters "end", which will end the calculator

    if b.find("+") == -1:      #If no plus sign found, do nothing
        pass
    else:
        y = b.find("+")    #If plus sign found, extract number before and after plus sign
        n1= int(b[:y])
        n2 = int(b[y + 1:])
        print(n1, "+", n2, "=", n1 + n2)   #Calculate and print full expression
        b = input("Please enter an expression calculating two numbers")   #Ask for new expression

    if b.find("-") == -1:
        pass              #If no minus sign found, do nothing
    else:
        y = b.find("-")   #If minus sign found, extract number before and after minus sign
        n1= int(b[:y])
        n2 = int(b[y + 1:])
        print(n1, "-", n2, "=", n1 - n2)    #Calculate and print full expression
        b = input("Please enter an expression calculating two numbers") #Ask for new expression to calculate

    if b.find("/") == -1:   #If no division sign found, do nothing
        pass
    else:
        y = b.find("/")
        n1= int(b[:y])       #If division sign found, extract the number before and after division sign
        n2 = int(b[y + 1:])
        print(n1, "/", n2, "=", n1 / n2)  #Calculate and print full expression
        b = input("Please enter an expression calculating two numbers")   #Ask for a new expression to calculate

    if b.find("*") == -1:
        pass        #If multiplication sign not found, do nothing
    else:
        y = b.find("*")
        n1= int(b[:y])        #If multiplication sign found, extract the number before and after the multiplication sign
        n2 = int(b[y + 1:])
        print(n1, "*", n2, "=", n1 * n2)  #Calculate and print full expression
        b = input("Please enter an expression calculating two numbers")  #Ask for new expression to calculate

    if b.find("+") == -1 and b.find("-") == -1 and b.find("/") == -1 and b.find("*") == -1:
        print("invalid expresssion")   #If no arithmetic sign found, print "invalid expression"
        b = input("Please enter an expression calculating two numbers")  #Ask for new expression to calculate

