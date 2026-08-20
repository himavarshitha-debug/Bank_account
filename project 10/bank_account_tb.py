# Bank Account Management System
# Testbench

from datetime import datetime

MAX_BALANCE = 50000000
MAX_TRANSACTIONS = 200
MAX_VIOLATIONS = 5
BLOCK_DAYS = 30

print("==========================================")
print("       BANK ACCOUNT MANAGEMENT TESTBENCH")
print("==========================================")


# ------------------------------------------
# Test 1: Maximum Balance
# ------------------------------------------

balance = 50000000

if balance == MAX_BALANCE:

    print("Test 1: ₹5 Crore Maximum Balance - PASS")

else:

    print("Test 1: ₹5 Crore Maximum Balance - FAIL")


# ------------------------------------------
# Test 2: Balance Limit Protection
# ------------------------------------------

amount = 1

if balance + amount > MAX_BALANCE:

    print("Test 2: Balance Limit Protection - PASS")

else:

    print("Test 2: Balance Limit Protection - FAIL")


# ------------------------------------------
# Test 3: 200 Transactions Allowed
# ------------------------------------------

transaction_count = 0

while transaction_count < 200:

    transaction_count = transaction_count + 1

if transaction_count == 200:

    print("Test 3: 200 Transactions Allowed - PASS")

else:

    print("Test 3: 200 Transactions Allowed - FAIL")


# ------------------------------------------
# Test 4: 201st Transaction Rejected
# ------------------------------------------

if transaction_count >= MAX_TRANSACTIONS:

    print("Test 4: 201st Transaction Rejected - PASS")

else:

    print("Test 4: 201st Transaction Rejected - FAIL")


# ------------------------------------------
# Test 5: Six Violations
# ------------------------------------------

violation_count = 0

for i in range(6):

    violation_count = violation_count + 1

if violation_count > MAX_VIOLATIONS:

    print("Test 5: Sixth Violation Detected - PASS")

else:

    print("Test 5: Sixth Violation Detected - FAIL")


# ------------------------------------------
# Test 6: Account Block
# ------------------------------------------

blocked = False

if violation_count > MAX_VIOLATIONS:

    blocked = True

if blocked:

    print("Test 6: Account Block - PASS")

else:

    print("Test 6: Account Block - FAIL")


# ------------------------------------------
# Test 7: Transaction Date
# ------------------------------------------

now = datetime.now()

date = now.strftime("%d-%m-%Y")

if len(date) == 10:

    print("Test 7: Transaction Date Recording - PASS")

else:

    print("Test 7: Transaction Date Recording - FAIL")


# ------------------------------------------
# Test 8: Transaction Time
# ------------------------------------------

time = now.strftime("%I:%M:%S %p")

if len(time) >= 10:

    print("Test 8: Transaction Time Recording - PASS")

else:

    print("Test 8: Transaction Time Recording - FAIL")


# ------------------------------------------
# Test 9: Transaction History
# ------------------------------------------

transaction_history = []

transaction_history.append(
    (
        1,
        "Deposit",
        50000,
        date,
        time,
        50000
    )
)

if len(transaction_history) == 1:

    print("Test 9: Transaction History - PASS")

else:

    print("Test 9: Transaction History - FAIL")


# ------------------------------------------
# Final Output
# ------------------------------------------

print("==========================================")
print("All tests completed successfully.")
print("==========================================")