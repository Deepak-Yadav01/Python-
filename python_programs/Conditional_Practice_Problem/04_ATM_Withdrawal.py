Balance = int(input("Enter the BankBalance: "))
Withdrawal_Amount = int(input("Enter the withDrawal Amount: "))

if Withdrawal_Amount<= Balance:
    print("Withdrawal Successful")
elif Withdrawal_Amount > Balance:
    print("Insufficiant Balance")
else:
    print("Something Went Wrong")    