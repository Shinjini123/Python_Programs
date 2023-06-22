a=input("enter a number ")
print(f"Multiplication table of {a} is:")
try:
    for i in range (5):
        print(f"{int(a)*i}")
except Exception as e:
    print(e)

    print("some important lines of code")
    print("end of program")
