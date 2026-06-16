#Python-To_Do_List

tasks_list=[]

while True:
    print("")
    print("~~~TO-DO LIST~~~")
    print("")
    print(">>>Select Your Choice<<<")
    print("01. Add Task")
    print("02. View Tasks")
    print("03. Remove Task")
    print("04. Exit")

    choice=str(input("Enter Your Choice: "))
    
    if(choice=='01' or choice=='1'):
        task=str(input("Enter Your Task: "))
        tasks_list.append(task)
        print("Task Add!")

    elif(choice=='02' or choice=='2'):
        if(len(tasks_list)==0):
            print("No Task Available!")
        else:
            print("~~~Your Tasks~~~")
            for x, task in enumerate(tasks_list, start=1):
                print(x,".",task)

    elif(choice=='03' or choice=='3'):
        if(len(tasks_list)==0):
            print("No Tasks To Remove!")
        else:
            print("~~~Your Tasks~~~")
            for x, task in enumerate(tasks_list, start=1):
                print(x,".",task)

            while True:
                number=str(input("Enter Your Remove Task Number: "))
                try:
                    number=int(number)
                    break
                except:
                    print("Invalid number. Please try again.")

            if(1<=number<=len(tasks_list)):
                tasks_list.pop(number-1)
                print("Removed Task!")
            else:
                print("Invalid Number!")

    elif(choice=='04' or choice=='4'):
        print("Good Bye!")
        break

    else:
        print("Invalid Number!")                            
                         


