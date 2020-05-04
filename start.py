from time import sleep
value1 = input('Enter a number: ')
value2 = input('Enter a second number: ')
sleep(2)
menu = int(input('[01] Sum\n[02] Subtraction\n[03] Multiplication\n[04] Division\n What do you want to do?: '))
if menu == 1:
    su = value1 + value2
    print("The sum of {} + {} is equal to {}".format(value1, value2, su))
elif menu == 2:
    sub = value1 - value2
    print("The substraction of {} - {} is equal to {}".format(value1, value2, sub))
elif menu == 3:
    mu = value1 * value2
    print("The multiplication of {} * {} is equal to {}".format(value1, value2, mu))
elif menu == 4:
    di = value1 / value2
    print("The division of {} / {} is equal to {}".format(value1, value2, di))
else:
    print("We dont have this option")
    sleep(3)
    exit()
