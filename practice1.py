temperature=float(input("enter the temperature:"))
method=int(input("enter 1 for centi to feren and enter 2 to convert feren to centi:"))
if(method==1):
    F=(temperature * 9/5)+32
    print(F)
elif(method==2):
    C = [(temperature-32)*5]/9
    print(C)
else:
    print("invalid entry")