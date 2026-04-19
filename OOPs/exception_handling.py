# try:
#     with open("Demo.txt", "r") as j:
#         data = j.read()
#         print(data)

# except FileNotFoundError:
#     print("FIle you are trying to open is not available or deleted please try another")
# try:
#     rs = 10 / 0
# except ZeroDivisionError:
#     print("Can not divide by 0")
# class AgeError(Exception):
#     pass
# try:
    
#     age = int(input("Enter Your age : "))
#     if age < 0:  
#         raise AgeError("Age can not be in Negative")
#     if age >= 18:
#         print("You can drive ")
   
    
# except AgeError:
#     print("Bad Age")
try:
    rs = 10 / 4
except ZeroDivisionError:
    print("Can't divide by 0")
else:
    print("Succes resut is",rs)
finally:
    print("Done")