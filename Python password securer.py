Secure = (('a' , '@') , ('s','*') , ('arrow' , '->') , ('and' , '&') , ('h' , '#'))
def securepassword(password):
    for a,b in Secure :
        password = password.replace(a,b)
    return password 


if __name__ == "__main__":
    password = str(input("Enter the password : "))
    password = securepassword(password)
    print(f' Your new password is :- {password}  ' )

print(100*100)
