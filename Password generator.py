import string 
import random  
print(string.ascii_letters)
print(string.ascii_lowercase)

print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)  # ' \t\n\r\x0b\x0c'
print(string.punctuation)
#String constants 




if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 =  string.punctuation
    # print(s4)
    plen = int(input("Enter passward length\n")) # handle extra gebrish 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    print("Your password is")
    # print("" . join(s[0:plen]))\
    # print(random.sample(s,plen))

    print('' .join(s[0:plen])) 