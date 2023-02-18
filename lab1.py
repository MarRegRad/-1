import time
xx = {'1':'один', '2' : 'два', '3' : 'три', '4' : 'четыре', '5' : 'пять', '6': 'шесть', '7' : 'семь', '8' : 'восемь', '9': 'девять', '0' : 'ноль'}
fail = open("sss.txt", "r")
cifra = "0123456789"
w = ""
q = []
last_len = 0
cifra_4x = '0123'
while 1:
    status = True
    x = fail.read(1)
    #print(x)
    if x in cifra:
        w += x
    else:
        #print(w)
        if w != "":
            for i in w: 
                if i in cifra_4x:
                    status = True
                else:
                    status = False
                    break
            if (w[-1] != '0' and w[-1] != '2') and (w[-2] == '1') and int(w) <= 100000 and status:     #проверка условий
                ww = ""
                for r in range(len(w) -1, -1, -1):
                    ww += w[r]  #разворачиваю число
                if w == ww:
                    for kk in range(len(w) -1, -1, -1):
                        print(xx.get(w[kk]), end = " ")
                    print("\n")
                else:                               # если число не полиндром, то вывод цифр в обратном порядке
                    for hhh in range(len(w) - 1, -1, -1):
                        print(w[hhh], end="")
                    print("\n")
        w = ""
