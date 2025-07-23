# Terminal Based
# Let user input time in seconds and count down to zero with a message or sound.
# time.sleep(), loops

import time

a = int(input("Enter time in seconds: "))
count = a

for i in range(a):
    time.sleep(1)
    print(i+1)
    if (i + 1) == a:
        print("Time up!")
