
file = open("1.txt", "r")       
buffer = file.read().split()    
if not buffer:                 
    print("Файл 1.txt пустой")
print("Числа в буфере:",buffer) 

dict = {0: "Ноль", 1: "Один", 2: "Два", 3: "Три"}

for x in buffer:
    print( "Число:", x )
    if (x[-1] == str(1) or x[-1] == str(3))  and int(x) < 100000:  
                                                                   

        if x[-2] == str(1):    
            y = x[::-1]
            if x == y:         
                z = [int(i) for i in str(x)] 
            
                for j in z:                  
                    print(dict[j], end = " ")
            else:
                print("Число записанное в обратном порядке:",y)
        else:
            print("Вторая цифра справа не равна 1")



    else:
        print("Число четное или больше 1024")











