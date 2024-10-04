import random
import csv
import os

class Main_Options:
    def create_account(self):
        amount = 0
        acnt_no = random.randint(10000,30000)
        user_name = input("Enter your name: ")

        try:
            file_exists = os.path.isfile('user_details.csv')
            print(f"File exists: {file_exists}. Writing to CSV...")
            with open('user_details.csv','a',newline='') as file:
                content = csv.writer(file)
                if not file_exists:
                    content.writerow(["Account Number","User Name"])
                content.writerow([acnt_no,user_name,amount])
            print(f"Account created successfully, Your Account Number: {acnt_no}")
        except (IOError, csv.Error) as e:  # Catch specific exceptions related to file operations and CSV writing
            print(f"Error writing to CSV file: {e}")

    def login(self):
        
        user_ac_no  = int(input("enter your account number: "))
        try:
            with open('user_details.csv','r',newline='') as file:
                csvreader = csv.reader(file)
                for i in csvreader:
                    if i[0] == str(user_ac_no):
                        name = i[1]
                        print(f"Welcome {name.upper()}")
                        break
            menu_second = BankingSystem()
            menu_second.display_menu_second(user_ac_no)
        except Exception as e:
            print(e)
    
    def deposit(self,acnt_no,amount):
        try:
            with open('user_details.csv','r',newline='') as file:
                csvreader = list(csv.reader(file))
                for i in csvreader:
                    if i[0] == str(acnt_no):
                        i[2] = str(int(i[2])+amount)
                        print("your balance is",i[2])
            with open('user_details.csv','w',newline='') as file:
                content = csv.writer(file)
                content.writerows(csvreader)
        except Exception as e:
            print(e)
        
    def withdraw(self,acnt_no,amount):
        try:
            with open('user_details.csv','r',newline='') as file:
                csvreader = list(csv.reader(file))
                for i in csvreader:
                    if i[0] == str(acnt_no):
                        if int(i[2]) >= amount:
                            i[2] = str(int(i[2])-amount)
                            print("Withdrawal successful")
                            print("your balance is",i[2])
                        elif int(i[2]) < amount:
                            print("insufficient balance")
            with open('user_details.csv','w',newline='') as file:
                content = csv.writer(file)  
                content.writerows(csvreader)
        except Exception as e:
            print(e)


class BankingSystem:
    def display_menu(self):
        print("1. Create Account")
        print("2. login")
        print("3. Exit")
        main_option = int(input("Enter your choice"))
        self.check_main_option(main_option)

    def check_main_option(self,option):
        try:
            main_option = Main_Options()
            if option ==1:
                main_option.create_account()
            elif option == 2:
                main_option.login()
            elif option ==3:
                exit()
        except Exception as e:
            print(e)
            self.display_menu()

    def display_menu_second(self,user_ac_no):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        second_option = int(input("Enter your choice"))
        self.check_second_option(user_ac_no,second_option)

    def check_second_option(self,acnt_no,second_option):
        try:
            main_option = Main_Options()
            if second_option ==1:
                amount = int(input("enter your amount: "))
                main_option.deposit(acnt_no,amount)
            elif second_option == 2:
                amount = int(input("enter your amount: "))
                main_option.withdraw(acnt_no,amount)
            elif second_option ==3:
                exit()
        except Exception as e:
            print(e)
            self.display_menu()

    def main(self):
        print("Welcome to Banking System")
        self.display_menu()

if __name__ =="__main__":
    mainobj = BankingSystem()
    mainobj.main()