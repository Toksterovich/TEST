def enter_pin ():
    print("Enter PIN:")
    code = 1234
    pin = int(input())
    if pin == code:
        print("Hello")
    else:
        enter_pin()

enter_pin()

bankomat = {
    100: 100,
    50: 100,
    20: 100,
    10: 100,
    5: 100,
    2: 100,
    1: 100
}

print ("Введите сумму: ")
num = int(input())

def output_money (num):
    for key in bankomat.keys():
        a = int(num // key)
        num -= a*key
        bankomat[key] -= a
        if a != 0:
            print ("Получите номинал", key, "в количестве", a)

output_money(num)

print(bankomat)