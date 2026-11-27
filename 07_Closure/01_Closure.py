# Python mein Closure ek aisa concept hai jisme inner function, apne outer function ke variables ko yaad rakhta hai, even after outer function execute hokar finish ho chuka hota hai.
def outer():
    message = "Hello Deepak"

    def inner():
        print(message)

    return inner   # ye line ka mtlb h ki jb outer fn call hua to inner fn return hua ,na ki call hua


my_func = outer()

my_func()



# Maan lo ek bank account hai jisme balance ko maintain karna hai.

def bank_account(balance):

    def deposit(amount):

        nonlocal balance

        balance += amount

        print("Deposited:", amount)
        print("Total Balance:", balance)

    return deposit


account = bank_account(1000)

account(500)
account(200)
account(1000)