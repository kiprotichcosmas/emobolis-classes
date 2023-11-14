# while, for, and foreach loops
from time import sleep

start = input("Enter the Starting Number: ")
stop = input("Enter the Stopping Number: ")

if start.isnumeric() and stop.isnumeric():
    start = int(start)
    stop = int(stop)
    counter = start
    while counter <= stop:
        if counter == stop:
            print(f"Count No. {counter}, This is the Last Point")
            sleep(3)
        elif counter == start:
            print(f"Count No. {counter}, This is the Starting  Point")
            sleep(3)
        else:
            print(f"Count No. {counter}")
            sleep(3)
        counter = counter + 1
else:
    print("Invalid Values, Kindly enter Numbers only")
