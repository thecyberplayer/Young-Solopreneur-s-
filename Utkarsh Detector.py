import os 

def isutkarsh (filename):
    with open(filename , "r") as f :
        fileContent = f.read()
    #detect all forms of binod like bInOD
    if "Utkarsh" in fileContent.lower():
        if "Utkarsh" in fileContent.lower():
            return True
    else :
        return False            

if __name__ == "__main__":
    #listing the content of this folder... 
    dir_contents = os.listdir
    nUtkarsh = 0 
    print(dir_contents)
    # for each text file , run isutkarsh in them
    for item in dir_contents  :
        if item.endswitch('txt'):
            print(f"Detecting Utkarsh in {item }")
            flag =isutkarsh(item)
            if (flag):
                print(f"Utkarsh found in this item ")
                nUtkarsh +=1

            else:
                print("Binod not found")

print("***************Utkarsh Decetor summary******************************************************" )
print(f'{nUtkarsh} files found Utkarsh hidden into them ')   #have tro make it properly in 
# night and have to upload on  blogspot 