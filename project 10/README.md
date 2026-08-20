# Bank Account Management System using Python

## Description

The Bank Account Management System is a basic Python project that simulates common banking operations such as depositing money, withdrawing money, checking the account balance, and viewing transaction history.

The project also implements account security rules. The maximum account balance is ₹5 crore and a maximum of 200 transactions are allowed per day.

Every successful deposit or withdrawal is automatically recorded with a transaction number, transaction type, amount, date, time, and balance after the transaction.

If more than five daily transaction-limit violations occur in one year, the account is blocked for 30 days.

## Technologies Used

* Python
* `datetime` module
* Variables
* Lists
* Tuples
* `while` loop
* `for` loop
* `if-else` statements
* Functions
* Basic arithmetic
* Comparison operators

No database, API, or external data is required.

## Main Features

* Deposit money
* Withdraw money
* Check balance
* Transaction history
* Transaction number
* Transaction date
* Transaction time
* Balance after each transaction
* Daily transaction counter
* Yearly violation counter
* ₹5 crore maximum balance
* 200 transaction daily limit
* 30-day account block after more than five violations

## Account Rules

### 1. Maximum Account Balance

The maximum amount that can be stored is:

```text
₹50,000,000
₹5 Crore
```

The program does not allow a deposit if the resulting balance would exceed ₹5 crore.

### 2. Daily Transaction Limit

The account can perform a maximum of:

```text
200 successful transactions per day
```

Both deposits and withdrawals count as transactions.

For example:

```text
150 Deposits
+
50 Withdrawals
=
200 Transactions
```

The next transaction is rejected.

### 3. Transaction-Limit Violation

When a user attempts another transaction after reaching 200 transactions, the transaction is rejected and a violation is recorded.

Only one violation is recorded for a particular day, even if the user keeps trying more transactions.

### 4. Yearly Violation Rule

The account can have five violations in one year.

If the account receives a sixth violation:

```text
Account → BLOCKED
Block period → 30 days
```

The account cannot perform deposits or withdrawals during the block period.

## Transaction Date and Time

The project uses Python's built-in `datetime` module to record the exact date and time of every successful transaction.

The following code gets the current date and time:

```python
from datetime import datetime

now = datetime.now()
```

The date is stored using:

```python
date = now.strftime("%d-%m-%Y")
```

The time is stored using:

```python
time = now.strftime("%I:%M:%S %p")
```

For example:

```text
Date: 09-08-2026
Time: 01:30:15 PM
```

This means the project does not require the user to manually enter the transaction date or time. It uses the computer's current date and time.

## Transaction History

Every successful transaction is stored in the `transaction_history` list.

Each transaction contains:

```text
Transaction Number
Transaction Type
Amount
Date
Time
Balance After Transaction
```

Example:

```text
1 | Deposit | ₹50000 | 09-08-2026 | 01:30:15 PM | ₹50000
2 | Withdrawal | ₹10000 | 09-08-2026 | 01:45:22 PM | ₹40000
```

## Important Note About Storage

This is a beginner-level project and does not use a database or permanent file storage.

The transaction history is stored in memory using a Python list while the program is running.

Therefore, if the program is closed, the transaction history is cleared.

Permanent storage can be added as a future improvement using file handling or a database.

## Menu

```text
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Transaction History
5. Account Status
6. Exit
```

## Working

### Deposit

1. The user selects Deposit.
2. The program checks whether the account is blocked.
3. It checks the daily transaction limit.
4. The user enters the deposit amount.
5. The program checks the ₹5 crore maximum balance.
6. If valid, the amount is added to the balance.
7. A transaction number is generated.
8. Current date and time are recorded.
9. The transaction is added to the transaction history.

### Withdrawal

1. The user selects Withdrawal.
2. The program checks the account status.
3. The daily transaction limit is checked.
4. The user enters the withdrawal amount.
5. The program checks whether sufficient balance is available.
6. If valid, the amount is deducted.
7. The date and time are recorded.
8. The transaction is added to the transaction history.

## Example Transaction

```text
Deposit successful.

Transaction No: 1
Amount: ₹50000
Date: 09-08-2026
Time: 01:30:15 PM
Current Balance: ₹50000
```

## Transaction History Example

```text
==============================================================
                  TRANSACTION HISTORY
==============================================================
No. | Type       | Amount       | Date       | Time       | Balance
--------------------------------------------------------------
1 | Deposit | ₹50000 | 09-08-2026 | 01:30:15 PM | ₹50000
2 | Withdrawal | ₹10000 | 09-08-2026 | 01:45:22 PM | ₹40000
==============================================================
```

## Project Structure

```text
Bank-Account-Management-System/
│
├── bank_account.py
├── testbench.py
├── output.txt
└── README.md
```

## How to Run

### Run the main program

Open Command Prompt or Terminal in the project folder:

```text
python bank_account.py
```

### Run the testbench

```text
python testbench.py
```

No additional Python packages need to be installed because `datetime` is included with Python.

## Testbench

The testbench checks:

1. Maximum balance of ₹5 crore
2. Balance limit protection
3. 200 transaction limit
4. Rejection of the 201st transaction
5. Detection of the sixth violation
6. Account blocking
7. Transaction date recording
8. Transaction time recording
9. Transaction history

Expected result:

```text
Test 1: ₹5 Crore Maximum Balance - PASS
Test 2: Balance Limit Protection - PASS
Test 3: 200 Transactions Allowed - PASS
Test 4: 201st Transaction Rejected - PASS
Test 5: Sixth Violation Detected - PASS
Test 6: Account Block - PASS
Test 7: Transaction Date Recording - PASS
Test 8: Transaction Time Recording - PASS
Test 9: Transaction History - PASS
```

## Advantages

* Simple and beginner-friendly
* Uses basic Python concepts
* Records transaction date and time automatically
* Maintains transaction history
* No database required
* No external data required
* Implements a maximum account balance
* Implements a daily transaction limit
* Tracks yearly violations
* Provides temporary account blocking

## Future Scope

The project can be improved by adding:

* Permanent transaction storage using files
* SQLite database
* Multiple bank accounts
* Customer registration
* PIN authentication
* Account number generation
* Monthly statements
* Interest calculation
* Fund transfer between accounts
* ATM simulation
* Graphical user interface
* PDF transaction statements

## Conclusion

The Bank Account Management System demonstrates how basic Python programming can be used to simulate a banking system. It supports deposits, withdrawals, balance checking, transaction history, transaction date and time recording, daily transaction limits, yearly violation tracking, and temporary account blocking.

The project is suitable for a beginner-level BTech project and can later be extended into a more advanced banking application.
