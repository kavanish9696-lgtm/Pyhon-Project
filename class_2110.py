#                                         PROJECT - 1

balance=10000
correct_pin=1234
attempt=1
history = []
while 0<attempt <= 3:
    user_pin = int(input("Enter Your ATM Pin : ",))
    attempt+=1
    if user_pin == correct_pin :
        while True :
            print("1.Check Balance")
            print("2.Deposite Money")
            print("3.Withdraw Cash")
            print("4.Exit")
            bal=1
            deposite=2
            withdraw=3
            exit=4
            option= int(input("Choose Option Number (1-4) : ",))
            if option == bal :
                print("Available Balance : ",balance)
                history.append(f"Balance : {int(balance)}")
            elif option == deposite :
                depo= int(input("Enter Deposite Amount : ",))
                balance+=depo
                print("Deposite : ",depo)
                print("New Balance : ", balance)
                history.append(f"Deposite Amount : {int(depo)}")
                history.append(f"Balance After Deposite : {int(balance)}")
            elif option == withdraw :            
                withd = int(input("Enter Your Withdrawl Amount : ",))
                balance-=withd 
                if withd>0 :
                    if withd<=balance :
                        print("Withdraw Amount : ",withd)
                        print("Remaining Balance :",balance)
                        history.append(f"Withdrawl Amount : {int(withd)}")
                        history.append(f"Remaining Balance : {int(balance)}")
                    else:
                        print("Insufficiant Balance")
            elif option == exit :
                if history :
                    for i in history :
                        print(i)
                print("Thank You!")
                
                break
        break       
    elif attempt<=3:
            
        print("wrong Pin. Left Attempt :",3-(attempt-1))
    
else :
    print("Card Blocked")


#                                              PROJECT -2
        
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

def calculate_average(marks):
    return sum(marks) / len(marks)

while True:
    print("\n1. Add student\n2. View all\n3. Show topper\n4. Exit")
    choice = input("Enter option(1-4): ",)

    if choice == "1":
        name = input("Enter student name: ").strip()
        if name in students:
            print("Student already exists.")
            continue
        
        marks = []
        for i in range(1, 4):
            while True:
                try:
                    mark = float(input(f"Enter mark {i}: ",))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Invalid mark, try again.")
                except ValueError:
                    print("Invalid mark, try again.")
        
        students[name] = marks

    elif choice == "2":
        
        for name, marks in students.items():
            avg = round(calculate_average(marks), 2)
            grade = get_grade(avg)
            print(f"{name} {avg:.2f} {grade}")

    elif choice == "3":
        
        topper_name = None
        highest_avg = -1.0

        for name, marks in students.items():
            avg = calculate_average(marks)
            if avg > highest_avg:
                highest_avg = avg
                topper_name = name

        if topper_name:
            print(f"Topper: {topper_name}")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")