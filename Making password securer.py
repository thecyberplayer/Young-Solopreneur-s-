SECURE = (('s' , '$') , ("and" , '&' ) , ('a' , '@') , ('1' , '!') , ('hash' , '#' ) , ('arrow' '->') , ('o' ,  "0"))
def securepassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password



if __name__ == "__main__":
    password  = input ("Enter you password: \n ")
    password = securepassword(password)
    print(f'Your secure password id {password}')


