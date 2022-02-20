phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:  
        search = str(input())

        if search in phonebook.keys():
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print (output.__getitem__)
        else:
            print ("Not found")
        
    except EOFError: 
        break
