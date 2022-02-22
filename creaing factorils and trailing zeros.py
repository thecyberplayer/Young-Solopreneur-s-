def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)

def FactorialTrailingZeros(number):
     
    # fac = factorial(number)
    # while(fac%10==0):
    #     count = fac + 1
    #     number = fac/10
    # return count
    count = 0
    i = 5
    while(number//i !=0):
        count += int(number/i)
        i = i*5
        return count



if __name__ == '__main__':
    number = int (input(" Enter The Number \n"))
    fac = factorial(number)
    print(f"The factorial is {fac}")
    # z = int(input("Enter The number \n"))
    print(  FactorialTrailingZeros( number))
