import random
import os
import webbrowser

def welcome():
    """Приветствует пользователя и сообщает ему название Project_2017."""
    print(
          "="*32, "COMPASSPLUSS","="*32+"\n"+
          "="*34,"presents","="*34,"\n"+
          "="*32,"Project_2017","="*32,"\n"+
          "="*22," Sidelnikov:Pavel:Alexandrovich ","="*22,"\n"
          )
    print("Hello World!\nПрограмма создана для генерации имен пользователей из входного файла \nПо умолчанию входным файлом является users.txt. ")
def generate_password():
    """
    Генерирует случайный пароль
    длиной PWD_LEN и возвращает его.
    """
    PWD_LEN = 8
    password=""
    symbols = [
               'a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V', 'W','X','Y','Z',
               '1','2','3','4','5','6','7','8','9','0','~','!','@',
               '#','$','%','^','&','*','(',')','-','='
              ]
    passwords=[]
    pass_list = []
    for i in range(PWD_LEN):
        pass_list.append(random.choice(symbols))
    password = "".join(pass_list)
    passwords.append(password)
    return password

def open_file():
    File_name="users"
    print(
        '''
    1 - Да
        '''
         )
    yes_1=(input("Уверены?  >>> "))
    try:
        if (yes_1 == str(1)):
            File_name=(input("File:"))
            file=open("files.txt/"+File_name+".txt","r")

        else:
            file=open("files.txt/"+File_name+".txt","r")
            print("Исходный файл не изменен")
    except FileNotFoundError:
        input("Извините,но данный файл не найден")
    return File_name

def open_1(File_name='users'):
    '''
    Открывает нужный файл
    в зависимости от выбора
    пользователя.
    '''
    file=open("files.txt/"+File_name+".txt" ,'r')
    return file
    
def ex():
    okay()
    file=open("files.txt\Задание.txt","r")
    for line in file.readlines():
        print(line)
    input("Нажмите Enter для возвращения на преведущий экран ")
    file.close()    
def qwerty(File_name='users'):
    """ (str, dict of (lastname, firstname, id):User ) -> None
    Сохраняет фамилию, имя, первую букву отчества (если есть),
    имя пользователя и пароль в выходной файл с именем out_file_name
    Формат одной сроки данных в выходном файле:
    Lukashenko, Sergey :N:7505:snlukashen1:!@upPdL&
    """
    try:
        file=open("files.txt/"+File_name+".txt","r")
    
        save=open('files.out/'+File_name+".out",'w')
        #print('Фамилия:Имя:Отчество:ID:Логин:Пароль\n')
        
        n=0
        l=0
        kl=1
        usernames=[]
        passwords=[]
        lines=[]
        for line in file.readlines():
            
                    index = ""
                    name = ""
                    gr_name = ""
                    otch = ""
                    password=""
                    username=""
                    
    #------------------ ID ------------------                  
                    for t in line:
                        if t != ":":
                            index+=t
                        else:
                             break

                    line=line[len(index)+1:len(line):]
    #---------------- Имена -----------------
                    for t in line:
                        if t != ":":
                            name+=t
                        else:
                            a=name[0]       # 1я буква логина
                            break

                    line=line[len(name)+1:len(line):]
    #---------------- Отчество ----------------                  
                    for t in line:
                        if t != ":":
                            otch+=t
                        else:
                            break

                    line=line[len(otch)+1:len(line):]
    #---------------- Фамилия ----------------    
                    for t in line:
                        if t != ":":
                            gr_name+=t
                        else:      
                            b=gr_name[0:9]  # оставшаяся часть логина
                            break
                    
                    line=line[len(gr_name)+1:len(line):]
                    '''
                    роверяет наличие Отчества.
                    Считывается количество символов, и если оно не меньше 3, то записывается,иначе пропускается
                    '''
                    if (int(len(otch)) <= int(len(otch[0:4]))):
                        otch_pr=str("")
                    else:
                        otch_pr=str(":"+otch)
                    # Проверяет наличие одинаковых паролей
                    l+=1
                    password=str(generate_password())
                    passwords.append(password)
                    for i in range(l+1):
                        kl=0
                        for j in range(i+1,l):
                            while passwords[i] == passwords[j]:
                                passwords[j]=str(generate_password())
                                password=passwords[j]
                    # Проверяет наличие одинаковых логинов и номерует их
                    n=0
                    username=str(a+b)
                    un_len = len(username)
                    ex_len= len(usernames)
                    while username in usernames:
                        username = username[0:un_len]+str(n+1)
                        #usernames.append(username + str(n+1))
                        n+=1
                    else:
                        usernames.append(username)
                    #print(username)
                    """for i in range(n+1):
                        kl=0
                        for j in range(i+1,n):
                            tyu=usernames[j]
                            kl+=1
                            
                            while usernames[i] == usernames[j]:
                                usernames[j]=username+str(kl)
                                if len(usernames[j])>len(username):
                                    usernames[j]==username[0:9]
                                    print(usernames[j])
                                
                                
                                username=usernames[j]
                    """
                    c=str(gr_name+':'+name+otch_pr+":"+index+':'+username+':'+password)
                    lines.append(c)
                    lines.sort()
                    
        save.write("\n".join(lines))
        file.close()
        save.close()
    except FileNotFoundError:
        print("Извините,но данный файл не найден")
        return 0
    #print("Данные из входного файла запсины в выходной файл того же имени.\nДанный файл находится в корневой папке")
def okay():
    os.system('cls')
    welcome()

def main():
    open_1()
    
    EXIT, GENERATION, FOLDER, WORK, EXP = map(str, range(5))

    welcome()
    passwords=[]
    numbr=0
    choice = None
    ds=None
    p=None
    while choice != EXIT:
        if ds!=None:
            name=ds
        else:
            name="users"
        print("\nИспользуемый файл\nFile:"+name+".txt" )
        if p!=None:
            print(p)
        print(
        """
    0 - Выйти
    1 - Сгенерировать имена пользователей
    2 - Открыть папку с генерированными именами пользователей
    3 - Изменить входной файл
    4 - Текст задания
    
        """
        )
        
        choice = input("Ваш выбор: ").strip()
#-------Bыход
        if choice == EXIT:
            print("До свидания.")
            input("Для завершения работы нажмите Enter для выхода...")
            break
#-------Генерация имен
        elif choice == GENERATION:
            if (ds!=None):
                okay()
                qwerty(ds)
                
                p=("\nДанные из входного файла записаны в выходной файл того же имени.\nДанный файл находится в корневой папке или же его не сущетвует, \nкак и самого входного файла")
            else:
                qwerty()
                okay()
                p=("\nДанные из входного файла записаны в выходной файл того же имени.\nДанный файл находится в корневой папке")

#-------Открывает папку с выходными данными
        elif choice == FOLDER:
            webbrowser.open("files.out")
            okay()
            p=("\nОперация выполнена")
            
#-------Возможность заменить входной файл
        elif choice == WORK:
            ds=open_file()
            okay()
            if (ds !="users"):
                p=("\nВходной файл  изменен или файла не существует")
            else:
                p=("\nВходной файл не изменен или файл не существует")
#-------Текст самого задания
        elif choice == EXP:
            ex()
            okay()
            p=("\nЧтение текста задания завершено")
        else: # Иначе производится чистка
            numbr+=1
            if (numbr>0):
                os.system('cls')
                welcome()
                numbr=0
                p=("\nИзвините, попробуйте снова")
                
          

main()
exit()
