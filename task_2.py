print("-----------------------------------------\n")
print("Enter (1) to add tasks")
print("Enter (2) to view tasks")
print("Enter (3) to update tasks")
print("Enter (4) to delete tasks")
print("Enter (5) to exit")
print("\n-----------------------------------------")
lst=[]
while True:

    #Code block for selecting choice for the user to <<< ADD VIEW UPDATE DELETE EXIT >>> tasks
    
    while True:
        print("Enter your choice: ",end="")
        num=input()
        if not num.isdigit():
            print("Invalid input..!!")
        elif int(num)<=0 or int(num)>5:
            print("Invalid..!!")
        else:
            n=int(num)
            break

    #Code block for adding task
   
    if n==1:
        print("Enter tasks")
        task=input()
        input("\nPress Enter to continue...\n")
        if task=="":
            print("Invalid..!!Task is empty")
            print("Please add some tasks")
        lst.append(task)

    #Code block for viewing task
    
    if n==2:
        if len(lst)==0:
            print("Tasks are empty..!!\nAdd some tasks")
            continue
        for i in range(len(lst)):
            print(f"{i+1}. {(lst[i]).capitalize()}")

    #Code for updating completed task
    
    if n==3:
        while True:
            print("Enter completed task: Task ",end="")
            Task=input()
            if not Task.isdigit():
                print("Invalid input..!!")
            elif int(Task)<=0 or int(Task)>len(lst):
                print("Invalid input..!!")
            else:
                task=int(Task)
                break

        updated=[]    
        for i in range(len(lst)):
            if i==task-1:
                up=lst[i]+"(Completed)"
                updated.append(up)
            else:
                updated.append(lst[i])
        lst=updated       

    #Code block for deleting task
                
    if n==4:
        while True:
            print("Enter the task that is to be deleted: Task ",end="")
            Delete_task=input()
            if not Delete_task.isdigit():
                print("Invalid input..!!")
            elif int(Delete_task)<=0 or int(Delete_task)>len(lst):
                print("Invalid input..!!")
            else:
                task=int(Delete_task)
                break
        lst.pop(task-1)

    #Code block for exiting
        
    if n==5:
        print("<<<EXITING>>>\nThank you for using our TO-DO")
        exit()  
        
