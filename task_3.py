import random
import string

while True:

    #Code block for requesting password length
    
    while True:
        print("Enter password length: ",end="")
        num=input()
        if not num.isdigit():
            print("Invalid number..!!")
        elif int(num)<=0:
            print("Invalid number..!!")
        else:
            n=int(num)
            break

    #Code block for requesting complexity
        
    while True:
        print("Enter complexity of the password [Easy,Medium,Hard]: ",end="")
        complexity=input()
        complexity_lst=["easy","medium","hard"]
        if complexity.lower() not in complexity_lst:
            print("Invalid complexity..!!\nChoose (Easy or Medium or Hard)")
        elif not complexity.isalpha():
            print("Invalid complexity..!!\nChoose (Easy or Medium or Hard)")
        else:
            break

    #Code block for generating easy level passwords
        
    if complexity.lower()=="easy":
        lst=[]
        for i in range(n):
            lst.append(random.choice(string.ascii_uppercase))
            lst.append(random.choice(string.ascii_lowercase))    
        print("\"Your password:\"","".join(lst[:n]))


    #Code block for generating medium level passwords

    if complexity.lower()=="medium":
        lst=[]
        for i in range(n):
            lst.append(random.choice(string.ascii_uppercase))
            lst.append(random.choice(string.ascii_lowercase))
            lst.append(random.choice(string.digits))
        random.shuffle(lst)    
        print("\"Your password:\"","".join(lst[:n]))


    #Code block for generating hard level passwords
        
    if complexity.lower()=="hard":
        lst=[]
        for i in range(n):
            lst.append(random.choice(string.ascii_uppercase))
            lst.append(random.choice(string.ascii_lowercase))
            lst.append(random.choice(string.digits))
            special="!@#$%&*?<>"
            lst.append(random.choice(special))
        random.shuffle(lst)    
        print("\"Your password:\"","".join(lst[:n]))

    #Code block to decide whether to continue the process or not
    
    while True:
        print("Do you want to continue[Yes/No]: ",end="")
        choice=input()
        if choice.lower()!="yes" and choice.lower()!="no":
            print("Invalid choice")
        elif choice.lower()=="yes":
            break
        elif choice.lower()=="no":
            print("<<<EXITING>>>")
            exit()
        
