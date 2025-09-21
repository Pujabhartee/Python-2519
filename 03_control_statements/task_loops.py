# Random OTP Simulation

import random

otp = random.randint(1000,9999)
print(otp)

# attempt =1
for attempt in range(3):
    user_otp = int(input("Enter the 4-digit OTP: "))
    if user_otp == otp:
        print("Transaction Succcess")
        break
    else:
        print(f"OTP is incorrect.")
        # #attempt += 1
        # if attempt + 1 >= 3:
        #     print("Maximum Attempt Reached, Try after 24 Hours.")
        # else:
        #     print(f"Try Again. Attempt: {attempt + 1}")
if attempt + 1 = 3:
    print("Maximum Attempt Reached, Try after 24 Hours.")
