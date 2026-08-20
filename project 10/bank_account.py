# Bank Account Management System
# Basic Python Project

from datetime import datetime, timedelta

# -------------------------------
# Account Limits
# -------------------------------

MAX_BALANCE = 50000000          # ₹5 Crore
MAX_TRANSACTIONS = 200          # 200 transactions per day
MAX_VIOLATIONS = 5              # More than 5 violations
BLOCK_DAYS = 30                 # 1 month = 30 days

# -------------------------------
# Account Information
# -------------------------------

balance = 0
transaction_count = 0
violation_count = 0
transaction_number = 0

blocked = False
block_until = None

# Stores transaction history
transaction_history = []

# Stores the date on which the current
# daily transaction count is being maintained
current_date = datetime.now().date()

# Prevents multiple violations on the same day
daily_violation_recorded = False


# -------------------------------
# Check New Day
# -------------------------------

def check_new_day():

    global transaction_count
    global current_date
    global daily_violation_recorded

    today = datetime.now().date()

    if today != current_date:
        transaction_count = 0
        daily_violation_recorded = False
        current_date = today


# -------------------------------
# Check Block Status
# -------------------------------

def check_block_status():

    global blocked
    global block_until

    if blocked:

        if datetime.now() >= block_until:

            blocked = False
            block_until = None

            print("\nAccount block period completed.")
            print("Your account is ACTIVE again.")


# -------------------------------
# Record Violation
# -------------------------------

def record_violation():

    global violation_count
    global daily_violation_recorded
    global blocked
    global block_until

    if not daily_violation_recorded:

        violation_count = violation_count + 1
        daily_violation_recorded = True

        print("\nDaily transaction limit violation recorded.")
        print("Violations this year:", violation_count)

        # Block after more than 5 violations
        if violation_count > MAX_VIOLATIONS:

            blocked = True
            block_until = datetime.now() + timedelta(days=BLOCK_DAYS)

            print("\n==========================================")
            print("            ACCOUNT BLOCKED")
            print("==========================================")
            print("More than 5 violations occurred this year.")
            print("Account is blocked for 30 days.")
            print("Block until:", block_until.strftime("%d-%m-%Y"))
            print("==========================================")


# -------------------------------
# Deposit
# -------------------------------

def deposit():

    global balance
    global transaction_count
    global transaction_number

    check_new_day()
    check_block_status()

    if blocked:

        print("\nAccount is currently BLOCKED.")
        print("Deposit is not allowed.")
        return

    if transaction_count >= MAX_TRANSACTIONS:

        print("\nDaily transaction limit reached.")
        print("Deposit is not allowed.")

        record_violation()
        return

    try:

        amount = float(input("Enter deposit amount: ₹"))

    except ValueError:

        print("Please enter a valid amount.")
        return

    if amount <= 0:

        print("Amount must be greater than zero.")
        return

    if balance + amount > MAX_BALANCE:

        print("\nTransaction not allowed.")
        print("Maximum account balance is ₹5 crore.")
        return

    # Update account
    balance = balance + amount
    transaction_count = transaction_count + 1
    transaction_number = transaction_number + 1

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    # Store transaction
    transaction_history.append(
        (
            transaction_number,
            "Deposit",
            amount,
            date,
            time,
            balance
        )
    )

    print("\nDeposit successful.")
    print("Transaction No:", transaction_number)
    print("Amount: ₹", amount)
    print("Date:", date)
    print("Time:", time)
    print("Current Balance: ₹", balance)


# -------------------------------
# Withdrawal
# -------------------------------

def withdraw():

    global balance
    global transaction_count
    global transaction_number

    check_new_day()
    check_block_status()

    if blocked:

        print("\nAccount is currently BLOCKED.")
        print("Withdrawal is not allowed.")
        return

    if transaction_count >= MAX_TRANSACTIONS:

        print("\nDaily transaction limit reached.")
        print("Withdrawal is not allowed.")

        record_violation()
        return

    try:

        amount = float(input("Enter withdrawal amount: ₹"))

    except ValueError:

        print("Please enter a valid amount.")
        return

    if amount <= 0:

        print("Amount must be greater than zero.")
        return

    if amount > balance:

        print("\nInsufficient balance.")
        return

    # Update account
    balance = balance - amount
    transaction_count = transaction_count + 1
    transaction_number = transaction_number + 1

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")

    # Store transaction
    transaction_history.append(
        (
            transaction_number,
            "Withdrawal",
            amount,
            date,
            time,
            balance
        )
    )

    print("\nWithdrawal successful.")
    print("Transaction No:", transaction_number)
    print("Amount: ₹", amount)
    print("Date:", date)
    print("Time:", time)
    print("Current Balance: ₹", balance)


# -------------------------------
# Check Balance
# -------------------------------

def check_balance():

    check_new_day()
    check_block_status()

    print("\n==========================================")
    print("             ACCOUNT BALANCE")
    print("==========================================")
    print("Current Balance: ₹", balance)
    print("==========================================")


# -------------------------------
# Show Transaction History
# -------------------------------

def show_history():

    check_new_day()
    check_block_status()

    print("\n==============================================================")
    print("                  TRANSACTION HISTORY")
    print("==============================================================")

    if len(transaction_history) == 0:

        print("No transactions available.")

    else:

        print(
            "No. | Type       | Amount       | Date       | Time       | Balance"
        )

        print("--------------------------------------------------------------")

        for transaction in transaction_history:

            number = transaction[0]
            transaction_type = transaction[1]
            amount = transaction[2]
            date = transaction[3]
            time = transaction[4]
            remaining_balance = transaction[5]

            print(
                number,
                "|",
                transaction_type,
                "| ₹",
                amount,
                "|",
                date,
                "|",
                time,
                "| ₹",
                remaining_balance
            )

    print("==============================================================")


# -------------------------------
# Account Status
# -------------------------------

def account_status():

    check_new_day()
    check_block_status()

    print("\n==========================================")
    print("             ACCOUNT STATUS")
    print("==========================================")

    print("Balance: ₹", balance)

    print(
        "Transactions Today:",
        transaction_count,
        "/",
        MAX_TRANSACTIONS
    )

    print(
        "Violations This Year:",
        violation_count
    )

    if blocked:

        print("Status: BLOCKED")
        print(
            "Blocked Until:",
            block_until.strftime("%d-%m-%Y")
        )

    else:

        print("Status: ACTIVE")

    print("==========================================")


# -------------------------------
# Main Program
# -------------------------------

print("==========================================")
print("       BANK ACCOUNT MANAGEMENT SYSTEM")
print("==========================================")
print("Maximum Balance: ₹5 Crore")
print("Daily Transaction Limit: 200")
print("==========================================")

while True:

    check_new_day()
    check_block_status()

    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Account Status")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        deposit()

    elif choice == "2":

        withdraw()

    elif choice == "3":

        check_balance()

    elif choice == "4":

        show_history()

    elif choice == "5":

        account_status()

    elif choice == "6":

        print("\nThank you for using the")
        print("Bank Account Management System.")
        break

    else:

        print("Invalid choice. Please try again.")