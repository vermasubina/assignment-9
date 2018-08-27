#the code below shows ZeroDivisionError
#Q.1
a=3
if a<4:
    try:
        a=a/(a-3)
    except ZeroDivisionError:
        print("you can't divide by zero")
print(a)

#the code below shows IndexError
#Q.2
l=[1,2,3]
try:
    print(l[3]) 
except:
    print("index out of range.")

#Q.3
#An exception
#error

#Q.4
#-5.0
#a/b result in 0


#Q.5
#1.IMPORT ERROR
try:
    import subinaa
except ImportError as message:
    print('Exception:', message)
#2.VALUE ERROR
try:
    n=int(input("enter a number"))
except ValueError as message:
    print('Exception:', message)
#3.INDEX ERROR
lst=[1,2,3]
try:
    print(lst[3]) 
except:
    print("index out of range.")
