# Convert between units: km to miles, Celsius to Fahrenheit, etc.
# Terminal Based
# Math, conditions, formatting

def km_to_m(a):
    return a*1000

def m_to_km(a):
    return a/1000

def cel_to_far(a):
    return a*(9/5) +32

def far_to_cel(a):
    return a*(5/9) - 32

num = int(input("Enter the number: "))

while True:
    conv = int(input("What conversion do you want to perform? 1-(km to m), 2-(m to km), 3-(celcius to fahrenheit), 4-(f to c): "))

    if conv == 1:
        print(km_to_m(num))
    
    elif conv == 2:
        print(m_to_km(num)) 
    elif conv == 3:
        print(cel_to_far(num))
    elif conv == 4:
        print(far_to_cel(num))
    else:
        print("invalid option")
        break
    