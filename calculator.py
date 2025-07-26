import math 
import turtle
print("Welcome to calculator(+,-,*,%,/)")
user=float(input("Enter the first value: "))
operator=input("Enter the value operator(+,-,*,%,/): ")
user2=float(input("Enter the second value: "))
result=None
if operator=='+':
    result= user+user2
elif operator=='-':
    result=user-user2

elif operator=='*':
    result=user*user2    

elif operator=="%":
    result=user%user2
    
elif operator=="/":
    if (user2!=0):
        result=user/user2
    else:
        print("Cannot be divisible")

def complex_function():
    num=float(input("Enter the value for log:"))
    result=math.log10(num)
    print(f" Log value of{num}:", result)
    angle_degrees=float(input("Enter any trignometric values in degree:"))
    angle_radians=math.radians(angle_degrees) ##converted to radians
    sin_val=math.sin(angle_radians)
    cos_val=math.cos(angle_radians)
    try:
        tan_val=math.tan(angle_radians)  ##to handle the value 90 and 270 degree
    except:
        tan_val="undefiend" 

    print(f"sin value({angle_degrees})",round(sin_val,4))
    print(f"cos value({angle_degrees})",round(cos_val,4))
    print(f"tan value({angle_degrees})",round(tan_val,4))

print(f"Result: {result}")
more=int(input("Could you want to find the LOG and TRIGNOMETRIC values Enter 1 for Yes , 0 for No "))
if more==1:
    complex_function()
else:
    print("Thankyou for your response")



