import time

#16:12:33

while True:
    current_time = time.localtime()
    formatted_time = time.strftime("%I : %M : %S %p %A %d %B %Y", current_time)
    print(formatted_time)
    # time.sleep(1)


