temperature=float(input("enter the temperature:"))
method=int(input("enter 1 for centi to fahren and enter 2 to convert feren to centi:"))
if(method==1):
    result=(temperature * 9/5)+32
    print(result)
elif(method==2):
    result = [(temperature-32)*5]/9
    print(result)
else:
    print("invalid entry")