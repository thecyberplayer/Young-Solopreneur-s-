from webbrowser import get

# A Short dictionary , it can be edited ......
mydict = {
    705 : "Tycon Wire 0.75 mm ",
    830 : "Tycon Wire 1.00 mm ",
    1230 : "Tycon Wire 1.5 mm",
    2010 : "Tycon Wire 2.5 mm ",
    2980 : "Tycon Wire 4.0 mm",
    1000 : "Tycon Cable 4.0 mm ",
    1370 : "Tycon Cable 6.00 mm ",
    2170 : "Tycon Cable 10.00 mm",
}


 
# A logic which calculate the price and gives the item .....
sum = 0
while(True):
    
    userInput = int(input("Enter The item Price or press to 987 quit: \n"))# i have close  this function because giving input again again 
    u = int(input("Enter the piece:  \n")  ) 
    print(mydict.get(userInput))
    if(userInput!=987):
        sum = int (userInput)*(int(u)) + sum 
        print(f"Order total so far: {sum}")

    else:
        print(f"Your Bill total is {sum}. Thanks for shoping with us")
        break
 

'''
Thank you 
Regards Utkarsh Trivedi
'''