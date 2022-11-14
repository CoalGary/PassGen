import random
import os

g = ...
#start cycle
while g:
    #get data
    LwrAndUppr_lettandDigits = ("abcdefghijklmnopqrstuvwxyz"
                                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
                                "1234567890987654321")
    #Upr_lett = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #Digits = ("1234567890987654321")
    #Chrs = ("!@#$%&*?<>_/`~")

    #create folder
    Folder = "C:/Users/Public/Desktop/Passed"
    #ErorBecouseFolderAlreadyCreated
    try:
        os.mkdir(Folder)
    except FileExistsError:
        try:
            leng = float(input("\nВведите длинну пароля: "))
            placewhereneedpass = input("Введите место использования пароля\nИли любвые удобные вам пометки: ")
            if leng >= 1 and leng <= 1000:
                #Сycle in cycle
                for cycl in range(int(leng)):
                    cycl = random.choice(LwrAndUppr_lettandDigits)# + Upr_lett + str(Digits)) #+ Chrs)

                    #savePasswrd*
                    file = open("C:/Users/Public/Desktop/Passed/passTest.txt", "a+")
                    print(cycl, end="")
                    file.write(cycl)
                    file.flush()
                    file.close()
                    #*
                    """
                    Если следующие строки закинуть в цикл в цикле(while) 
                    то будет сохраняться только последняя буква пароля
                    """
                print("\nПароль находится в:  ", end=Folder + "/passTest.txt")
                file = open("C:/Users/Public/Desktop/Passed/passTest.txt", "a+")
                file.write("  -  " + placewhereneedpass)
                file.write("\n*-----------------------------------------------------------*\n")
                file.flush()
                file.close()
                #file = open("C:/Users/Public/Desktop/Passed/passTest.txt", "r")
                #g = file.read()
                #print(g)
                #file.close()
            elif print("Не больше --- 1000 символов: "):
                pass
        except ValueError:
           print("Только цифры"); pass
        #else:
            #return leng