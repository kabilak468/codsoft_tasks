contact_list=[]

def add_contacts():
    
    #Code block for adding contacts
    
    print("<<< Adding Contacts >>>")
    while True:
        print("Enter name: ",end="")
        name=input()
        if name=="" or name.isdigit():
            print("Invalid input")
        else:
            break
    while True:
        print("Enter mobile number: ",end="")
        phone=input()
        if phone == "" or not phone.isdigit() or len(phone) != 10:
            print("Invalid input")
        else:
            break

    while True:
        print("Enter email id: ",end="")
        email=input()
        if email=="":
            print("Invalid input")
        else:
            break     
            
    while True:
        print("Enter address: ",end="")
        address=input()
        if address=="":
            print("Invalid input")
        else:
            break

    contact = {"name": name.capitalize(),"phone": phone,"email": email,"address": address}
    contact_list.append(contact)
    print("\n<<<Contact added successfully>>>")
    print("\n")      
    
def view_contacts():

    #Code block for viewing contacts

    print("\n<<< Viewing contact details >>>")
    
    if len(contact_list)==0:
        print("No contacts found")
        return 
        
    print("\n")
    for items in contact_list:
        print(f"Name: {items['name']}\nContact number: {items['phone']}\nEmail id: {items['email']}\nAddress: {items['address']}")
        print("\n")


def search_contacts():

    #Code block for searching contacts
    
    print("<<< Searching Contacts >>>")
    if len(contact_list)==0:
        print("No contacts found")
        return
    while True:
        print("Enter name: ",end="")
        name=input()
        if name=="" or name.isdigit():
            print("Invalid input")
        else:
            break
    while True:
        print("Enter mobile number: ",end="")
        phone=input()
        if phone=="" or len(phone)!=10 or not phone.isdigit():
            print("Invalid input")
        else:
            break
        
    for items in contact_list:
        if items['name'].lower()==name.lower() or items['phone']==phone:
            print("\n") 
            print(f"Name: {items['name']}\nContact number: {items['phone']}\nEmail id: {items['email']}\nAddress: {items['address']}")
            print("\n")
            break
    else:
        print("Contact not found..!!")

def update_contacts():

    #Code block for updating contacts

    print("<<< Updating Contacts >>>")
    if len(contact_list)==0:
        print("No contacts found")
        return
    while True:
        print("Enter name: ",end="")
        up_name=input()
        if up_name=="" or up_name.isdigit():
            print("Invalid input")
        else:
            break    
    for items in contact_list:
        if items['name'].lower()==up_name.lower():
            print("\nCONTACT FOUND !")
            print("\n")
            print("What do you want to update?\n")
            print("Enter (1) to update name")
            print("Enter (2) to update mobile number")
            print("Enter (3) to update email id")
            print("Enter (4) to update address")
            print("\n")
            while True:
                print("Enter your choice: ",end="")
                Update=input()
                if Update=="" or not Update.isdigit() or int(Update)<=0 or int(Update)>6:
                    print("Invalid input")
                else:
                    update=int(Update)
                    break

            if update==1:
                while True:
                    print("Enter name to update: ",end="")
                    updated_name=input()
                    if updated_name=="" or updated_name.isdigit():
                        print("Invalid input")
                    else:
                        items['name']=updated_name
                        print("\nName updated successfully !!\n")
                        return

            if update==2:
                while True:
                    print("Enter mobile number: ",end="")
                    updated_phone=input()
                    if updated_phone == "" or not updated_phone.isdigit() or len(updated_phone) != 10:
                        print("Invalid input")
                    else:
                        items['phone']=updated_phone
                        print("\nMobile number updated successfully !!\n")
                        return


            if update==3:
                while True:
                    print("Enter email id: ",end="")
                    updated_email=input()
                    if updated_email=="":
                        print("Invalid input")
                    else:
                        items['email'] = updated_email
                        print("\nMail id updated successfully !!\n")
                        return
                    
            if update==4:
                while True:
                    print("Enter address: ",end="")
                    updated_address=input()
                    if updated_address=="":
                        print("Invalid input")
                    else:
                        items['address'] = updated_address
                        print("\nAddress updated successfully !!\n")
                        return
                
    else:
        print("Not found!")
         

def delete_contacts():

    #Code block for deleting contacts
    
    print("<<< Deleting Contacts >>>")
    if len(contact_list)==0:
        print("No contacts found")
        return
    while True:
        print("Enter name: ",end="")
        del_name=input()
        if del_name=="" or del_name.isdigit():
            print("Invalid input")
        else:
            break
        
    for i in range(len(contact_list)):
        if contact_list[i]['name'].lower()==del_name.lower():
            print("\nContact Found!\nDeleting founded contact..!!")
            print("\n")
            contact_list.pop(i)
            return
    print("Contact not found")    
                 
        

print("-------------------------------------\n")
print("Enter (1) to add contact details")
print("Enter (2) to view contact details")
print("Enter (3) to search contact details")
print("Enter (4) to update contact details")
print("Enter (5) to delete contact details")
print("Enter (6) to exit...")
print("\n--------------------------------------")

while True:

    while True:
        print("Enter your choice: ",end="")
        option=input()
        if option=="" or not option.isdigit() or int(option)<=0 or int(option)>6:
            print("Invalid input")
        else:
            choice=int(option)
            break
    
    if choice==1:
        add_contacts()
    if choice==2:
        view_contacts()
    if choice==3:
        search_contacts()
    if choice==4:
        update_contacts()
    if choice==5:
        delete_contacts()
    if choice==6:
        print("<<< EXITING >>>")
        exit()
