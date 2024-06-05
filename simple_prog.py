#print("hello")

#a="Hello World"
#print(a[1])

#print(a[2:5])


#print(a.upper())

#print(a.lower())

#print(a.split())

'''def first():
    print("string is "+a)

first()'''

#program for the even and odd number

'''print("to check even or odd number:")
a=int(input("Enter a number:"))
if a/2:
    print(a,"is even")
else:
    print(a, "is odd")'''

#program for the prime number

'''n=int(input("enter a number:"))
if n > 1:
    for i in range(2, (n//2)+1):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
        else:
         print(n, "is a prime number")
else:
    print(n, "is not a prime number")'''

#program for the largest of 2 number

a=int(input("Enter 1st number:"))
b=int(input("Enter 2ed number:"))
if a > b :
    print(a,"is larger")
else:
    print(b, "is larger")