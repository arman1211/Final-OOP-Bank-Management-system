class Bank:
    def __init__(self) -> None:
        self.users = {}
        self.admin = {}
        self.loan_allow = True
        self.is_bankrupt = False
        self.total_balance = 0
        self.total_loan = 0
    def create_account(self,user):
        account_no = len(self.users)+1
        self.users[account_no] = user
        print(f"successfully created. Acount Id no is {account_no}")
    def create_admin(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        account_no = len(self.admin)+1
        user_acount = self
        self.admin[account_no] = user_acount
        print(f"Admin added succesfully. Id is {account_no}")


class Admin(Bank):
    def __init__(self,bank) -> None:
        self.bank = bank
        super().__init__()
    
    def login_admin(self,id,password):
         if id in self.bank.admin:
             for key,val in self.bank.admin.items():
                 print(key, self.bank.admin[key].password)
             if self.bank.admin[id].password == password:
                 print("Login successfull")
                 return True
             else:
                 print("Incorrect Password")
                 return False
         else:
             print("admin doesnot exists")
             return False

    def delete_account(self,account_no):
        if account_no in self.bank.users:
            del self.bank.users[account_no]
            print(f" account no {account_no} deleted")
        else:
            print(f"Sorry, account no {account_no} does not exists")

    def account_list(self):
        if len(self.bank.users)>0:
            print(f'id \tname \temail  \taddress \ttype')
            for acc_no,user in self.bank.users.items():
                print(f'{acc_no}\t{user.name}\t{user.email}\t{user.address}\t{user.account_type}')
        else:
            print('Sorry, no user exists')

    def total_bank_balance(self):
        total = 0
        for user in self.bank.users.values():
            total += user.balance
        self.bank.total_balance = total
        print(f"Total bank balance is {total}")

    def total_loan_amount(self):
        total = 0
        for user in self.bank.users.values():
            total += user.loan
        self.bank.total_loan = total
        print(f"Total loan amount is {total}")

    def change_loan_feature(self):
        if self.bank.loan_allow:
            self.bank.loan_allow = False
            print("Loan feature is now turned off")
        else:
            self.bank.loan_allow = True
            print("loan feature is now turned on")

    def change_bankrupt(self):
        if self.bank.is_bankrupt:
            self.bank.is_bankrupt = False
            print("Bank is ok")
        else:
            self.bank.is_bankrupt = True
            print("Bank is bankrupt")


class User:
    def __init__(self,name,email,address,account_type,bank) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = 0
        self.loan_cnt = 0
        self.transaction_history = {}
        self.bank = bank
        super().__init__()

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            transaction_id = len(self.transaction_history)+101
            self.transaction_history[transaction_id] = ["deposit",amount]
            print(f"Succesfully deposited {amount} tk")
        else:
            print("Sorry, the amount can't be negative")

    def withdraw(self,amount):
        if self.bank.is_bankrupt:
            print("Sorry, Your bank is bankrupt")
        else:
            if 0< amount< self.balance:
                self.balance -= amount
                transaction_id = len(self.transaction_history)+101
                self.transaction_history[transaction_id] = ["withdraw",amount]
                print(f"Succesfully withdrawed {amount} tk")
            else:
                print("Withdrawl amount exceded")

    def check_balance(self):
        print(f"Your available balance is {self.balance + self.loan}")

    def check_transaction_history(self):
        if len(self.transaction_history)>0:
            print('--------------------------------------------------')
            print("Id\tType\t\tAmount")
            print('--------------------------------------------------')
            for t_id,history in self.transaction_history.items():
                print(f'{t_id}\t\t{history[0]}\t\t{history[1]}')
        else:
            print("No transaction history available")
    def take_loan(self,amount):
        if self.loan_cnt <2 and self.bank.loan_allow:
            self.loan += amount
            self.loan_cnt += 1
            transaction_id = len(self.transaction_history)+101
            self.transaction_history[transaction_id] = ["loan",amount]
            print(f'Succesfully taken loan amount {amount}')
        elif self.loan>=2:
            print("Maximul loan limit exceeded")
        elif self.bank.loan_allow == False:
            print("Sorry, You  do not have permission to take loan")
        else:
            print("Something went wrong")
    def transfer_money(self,account_no,amount):
        if account_no in self.bank.users:
            if amount < self.balance:
                self.bank.users[account_no].balance += amount
                self.balance -= amount
                transaction_id = len(self.transaction_history)+101
                self.transaction_history[transaction_id] = ["transfer",amount]

                transaction_id = len(self.bank.users[account_no].transaction_history)+101
                self.bank.users[account_no].transaction_history[transaction_id] = ["recieved",amount]
                print("Money transfer succesful.")
            else:
                print("Insufficient balance")
        else:
            print("Sorry,account does not exists")

my_bank = Bank()

my_bank.create_admin('admin','admin@gmail.com',"1234")
admin = Admin(my_bank)



while True:
    print('-----------------------------')
    print("Welcome to our Bank")
    print("Option 1: login as Admin")
    print("Option 2: Register as User")
    print("Option 3: exit")
    print('-----------------------------')
    opt = int(input("Choose an option: "))
    if opt == 1:
        print("Initial admin id is 1 and password is 1234")
        id = int(input("Enter Your id: "))
        password = input("Enter yout password: ")
        is_success = admin.login_admin(id,password)
        if(is_success):
            while True:
                print('-------------------------------------------')
                print("Welcome admin")
                print("Option 1: Create an user Acount")
                print("Option 2: Delete an user Acount")
                print("Option 3: See user acount list")
                print("Option 4: Check available balance in Bank")
                print("Option 5: Check total loan in Bank")
                print("Option 6: Change loan allowed status")
                print("Option 7: Change bankrupt status")
                print("Option 8: Add another admin")
                print("Option 9: Exit as admin")
                print('-------------------------------------------')
                op = int(input("Enter an option: "))
                if op == 1:
                    name = input("Enter User Name: ")
                    email = input("Enter User email: ")
                    address = input("Enter User address: ")
                    account_type = input("Enter acount type: ")
                    user = User(name,email,address,account_type,my_bank)
                    my_bank.create_account(user)
                elif op ==2:
                    account_no = int(input("Enter acount no to delete: "))
                    admin.delete_account(account_no)
                elif op ==3:
                    admin.account_list()
                elif op ==4:
                    admin.total_bank_balance()
                elif op ==5:
                    admin.total_loan_amount()
                elif op ==6:
                    admin.change_loan_feature()
                elif op ==7:
                    admin.change_bankrupt()
                elif op ==8:
                    name = input("Enter admin Name: ")
                    email = input("Enter admin email: ")
                    password = input("Enter a password: ")
                    my_bank.create_admin(name,email,password)
                elif op ==9:
                    break
                else:
                    print("Invalid option")
        else:
            print("Sorry,login failed")
    elif opt == 2:
        name = input("Enter Your Name: ")
        email = input("Enter Your email: ")
        address = input("Enter yout address: ")
        account_type = input("Enter acount type: ")
        user = User(name,email,address,account_type,my_bank)
        my_bank.create_account(user)
        while True:
            print('--------------------------------------------')
            print("Welcome ")
            print("Option 1: Deposit Money")
            print("Option 2: Withdraw money")
            print("Option 3: Check Balance")
            print("Option 4: Check Transaction History")
            print("Option 5: Take Loan")
            print("Option 6: Transfer money")
            print("Option 7: Exit as user")
            print('--------------------------------------------')

            op = int(input("Chose an option: "))
            if op == 1:
                amount = int(input("Enter amount: "))
                user.deposit(amount)
            elif op ==2:
                amount = int(input("Enter amount: "))
                user.withdraw(amount)
            elif op ==3:
                user.check_balance()
            elif op ==4:
                user.check_transaction_history()
            elif op ==5:
                amount = int(input("Enter amount to take loan: "))
                user.take_loan(amount)
            elif op ==6:
                account_no = int(input("Enter reciever acount no: "))
                amount = int(input("Enter amount: "))
                user.transfer_money(account_no,amount)
            elif op ==7:
                break
            

    elif opt == 3:
        break
    else:
        print("Invalid option")

        