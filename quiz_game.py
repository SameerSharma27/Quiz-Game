import sqlite3
import welcome
import random
import os
import time 
con=sqlite3.connect("question_bank.db")

# tables for c questions
con.execute("CREATE TABLE IF NOT EXISTS c_bank_level_1(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS c_bank_level_2(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS c_bank_level_3(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS c_bank_level_4(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS c_bank_level_5(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
# tables for java questions
con.execute("CREATE TABLE IF NOT EXISTS java_bank_level_1(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS java_bank_level_2(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS java_bank_level_3(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS java_bank_level_4(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS java_bank_level_5(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
#tables for python questions
con.execute("CREATE TABLE IF NOT EXISTS python_bank_level_1(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS python_bank_level_2(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS python_bank_level_3(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS python_bank_level_4(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
con.execute("CREATE TABLE IF NOT EXISTS python_bank_level_5(S_NO NUMBER ,question varchar(300) PRIMARY KEY NOT NULL,choice1 varchar(50),choice2 varchar(50),choice3 varchar(50),choice4 varchar(50),answer varchar(1))")
os.system("CLS")
welcome.welcome()
# here we can make the user login and maintain a database of each users activity and performance
def main_menu():
    print("""\n 
    \t 1.TEST YOUR C SKILLS
    \t 2.TEST YOUR JAVA SKILLS(This option is under precess,Sorry)
    \t 3.TEST YOUR PYTHON SKILLS(This option is under precess,Sorry)
    \t 4.README\n\n""")
    try:
        choice=int(input("Please Enter your Choice  "))
    except ValueError:
        os.system("CLS")
        print("\t\tPlease Enter a valid Choice only\n\n")
        os.system("pause")
        os.system("CLS")
        welcome.welcome()
        main_menu()
    if choice==1:
        level_1(1,[],1)
    elif choice==2:
        level_1(1,[],2)
    elif choice==3:
        level_1(1,[],3)
    elif choice==4:
        read_me()


def level_1(counter,q_list,skill):
    #skill here denotes the choice the user has picked to play like c or java or python
    os.system('CLS')
    while True:
        #picks a random number and checks if the number is already inside the list or not ,if not then the number is unique and picks the question with same serial number
        # q_list contains the serial number of those question which are already picked in the current session
        q_choice=random.randint(1,5)
        if q_choice not in q_list:
            break
    q_list.append(q_choice)
    if skill==1:
        row=con.execute("SELECT * FROM c_bank_level_1 WHERE c_bank_level_1.S_NO= ?",(q_choice,))
    elif skill==2:
        row=con.execute("SELECT * FROM java_bank_level_1 WHERE java_bank_level_2.S_NO= ?",(q_choice,))
    elif skill==3:
        row=con.execute("SELECT * FROM python_bank_level_1 WHERE python_bank_level_2.S_NO= ?",(q_choice,))
    for i in row:
        pass
    while(True):
        print(str(counter),i[1],"?",end="\n\n",sep=" ")
        print("A.",i[2],"\t\t\t\t","B.",i[3],end="\n\n")
        print("C.",i[4],"\t\t\t\t","D.",i[5])
        answer=input("\n\nWhich Option do you thing can be the correct one  ")
        if answer in ["a","b","c","d","A","B","C","D"]:
            break
        else :
            os.system("CLS")
            print("\n\n\t\t\tPlease enter your choice from the options given\n\n")
            os.system("pause")
            os.system("CLS")
            continue
        
    if answer.upper()==str(i[6]):
        print("\n\n\n\t\t\t Congratulations!!! you have given the correct Answer\n\n")
        os.system('pause')
    else:
        print("\n\n\n\t\t So Unlucky,This answer is not correct\n\n")
        os.system("pause")
        result(counter,1)#this functions will print the final result
        
    counter+=1
    if(counter==4):
        os.system("CLS")
        print("\n\n\n\t\t HURRAH!! you have completed level 1 ,it's time to move on to level 2\n\n")
        os.system("pause")
        level_2(1,[],skill)
    else:
        level_1(counter,q_list,skill)

def level_2(counter,q_list,skill):
    os.system('CLS')
    while True:
        q_choice=random.randint(1,5)
        if q_choice not in q_list:
            break
    q_list.append(q_choice)
    if skill==1:
        row=con.execute("SELECT * FROM c_bank_level_2 WHERE c_bank_level_2.S_NO= ?",(q_choice,))
    elif skill==2:
        row=con.execute("SELECT * FROM java_bank_level_2 WHERE java_bank_level_2.S_NO= ?",(q_choice,))
    elif skill==3:
        row=con.execute("SELECT * FROM python_bank_level_2 WHERE python_bank_level_2.S_NO= ?",(q_choice,))
    
    for i in row:
        pass
    while(True):
        print(str(counter+3),i[1],"?",end="\n\n",sep=" ")
        print("A.",i[2],"\t\t\t\t","B.",i[3],end="\n\n")
        print("C.",i[4],"\t\t\t\t","D.",i[5])
        answer=input("\n\nWhich Option do you thing can be the correct one  ")
        if answer in ["a","b","c","d","A","B","C","D"]:
            break
        else :
            os.system("CLS")
            print("\n\n\t\t\tPlease enter your choice from the options given\n\n")
            os.system("pause")
            os.system("CLS")
            continue

    
    if answer.upper()==i[6]:
        print("\n\n\n\t\t Congratulations!!! you have given the correct Answer\n\n")
    else:
        print("\n\n\n\t\t So Unlucky,This answer is not correct\n\n")
        os.system("pause")
        result(counter,2)#this functions will print the final result
    os.system('pause')    
    counter+=1
    if(counter==4):
        os.system("CLS")
        print("\n\n\n\t\t HURRAH!! you have completed level 2 ,it's time to move on to level 3\n\n")
        os.system("pause")
        level_3(1,[],skill)
    else:
        level_2(counter,q_list,skill)

def level_3(counter,q_list,skill):
    os.system('CLS')
    while True:
        q_choice=random.randint(1,5)
        if q_choice not in q_list:
            break
    q_list.append(q_choice)
    if skill==1:
        row=con.execute("SELECT * FROM c_bank_level_3 WHERE S_NO= ?",(q_choice,))
    elif skill==2:
        row=con.execute("SELECT * FROM java_bank_level_3 WHERE S_NO= ?",(q_choice,))
    elif skill==3:
        row=con.execute("SELECT * FROM python_bank_level_3 WHERE S_NO= ?",(q_choice,))
    
    for i in row:
        pass
    while(True):
        
        print(str(counter+6),i[1],"?",end="\n\n",sep=" ")
        print("A.",i[2],"\t\t\t\t","B.",i[3],end="\n\n")
        print("C.",i[4],"\t\t\t\t","D.",i[5])
        answer=input("\n\nWhich Option do you thing can be the correct one  ")
        if answer in ["a","b","c","d","A","B","C","D"]:
            break
        else :
            os.system("CLS")
            print("\n\n\t\t\tPlease enter your choice from the options given\n\n")
            os.system("pause")
            os.system("CLS")
            continue
    if answer.upper()==i[6]:
        print("\n\n\n\t\t Congratulations!!! you have given the correct Answer\n\n")
        os.system('pause')
    else:
        print("\n\n\n\t\tSo Unlucky,This answer is not correct\n\n")
        os.system("pause")
        result(counter,3)#this functions will print the final result
        
    counter+=1
    if(counter==4):
        os.system("CLS")
        print("\n\n\n\t\tHURRAH!! you have completed level 3 ,it's time to move on to level 4\n\n")
        os.system("pause")
        level_4(1,[],skill)
    else:
        level_3(counter,q_list,skill)
    

def level_4(counter,q_list,skill):
    os.system('CLS')
    while True:
        q_choice=random.randint(1,5)
        if q_choice not in q_list:
            break
    q_list.append(q_choice)
    if skill==1:
        row=con.execute("SELECT * FROM c_bank_level_4 WHERE S_NO= ?",(q_choice,))
    elif skill==2:
        row=con.execute("SELECT * FROM java_bank_level_4 WHERE S_NO= ?",(q_choice,))
    elif skill==3:
        row=con.execute("SELECT * FROM python_bank_level_4 WHERE S_NO= ?",(q_choice,))
    
    for i in row:
        pass
    while(True):
        print(str(counter+9),i[1],"?",end="\n\n",sep=" ")
        print("A.",i[2],"\t\t\t\t","B.",i[3],end="\n\n")
        print("C.",i[4],"\t\t\t\t","D.",i[5])
        answer=input("\n\nWhich Option do you thing can be the correct one  ")
        if answer in ["a","b","c","d","A","B","C","D"]:
            break
        else :
            os.system("CLS")
            print("\n\n\t\t\tPlease enter your choice from the options given\n\n")
            os.system("pause")
            os.system("CLS")
            continue
    if answer.upper()==i[6]:
        print("\n\n\n\t\tCongratulations!!! you have given the correct Answer\n\n")
        os.system('pause')
    else:
        print("\n\n\n\t\tSo Unlucky,This answer is not correct\n\n")
        os.system("pause")
        result(counter,4)#this functions will print the final result
        
    counter+=1
    if(counter==4):
        os.system("CLS")
        print("\n\n\n\t\tHURRAH!! you have completed level 4 ,it's time to move on to level 5\n\n")
        os.system("pause")
        level_5(1,[],skill)
    else:
        level_4(counter,q_list,skill)



def level_5(counter,q_list,skill):
    os.system('CLS')
    while True:
        q_choice=random.randint(1,5)
        if q_choice not in q_list:
            break
    q_list.append(q_choice)
    if skill==1:
        row=con.execute("SELECT * FROM c_bank_level_5 WHERE S_NO= ?",(q_choice,))
    elif skill==2:
        row=con.execute("SELECT * FROM java_bank_level_5 WHERE S_NO= ?",(q_choice,))
    elif skill==3:
        row=con.execute("SELECT * FROM python_bank_level_5 WHERE S_NO= ?",(q_choice,))
    
    for i in row:
        pass
    while(True): 
        print(str(counter+12),i[1],"?",end="\n\n",sep=" ")
        print("A.",i[2],"\t\t\t\t","B.",i[3],end="\n\n")
        print("C.",i[4],"\t\t\t\t","D.",i[5])
        answer=input("\n\nWhich Option do you thing can be the correct one  ")
        if answer in ["a","b","c","d","A","B","C","D"]:
            break
        else :
            os.system("CLS")
            print("\n\n\t\t\tPlease enter your choice from the options given\n\n")
            os.system("pause")
            os.system("CLS")
            continue
    if answer.upper()==i[6]:
        print("\n\n\n\t\tCongratulations!!! you have given the correct Answer\n\n")
        os.system('pause')
    else:
        print("\n\n\n\t\tSo Unlucky,This answer is not correct\n\n")
        os.system("pause")
        result(counter,5)#this functions will print the final result
    counter+=1 
    if(counter==4):
        os.system("CLS")
        print("\n\n\t\t\tHURRAH!! you have completed the game\n\n")
        os.system("pause")
        result(counter,5)
    else:
        level_5(counter,q_list,skill)

def read_me():
    os.system('CLS')
    print("""
    This is a knowledge testing game .
    The game is divided into 5 Levels.
    Each level contains three questions each.
    Answering three successive questions you can clear one level.

""")
    a=input("\t\tEnter any key to continue")
    os.system("CLS")
    main_menu()


def result(counter,level):
    os.system('CLS')
    print("\n\n")
    if level ==5:
        print("\t\tEXCELLENT")
    elif level==4:
        print("\t\tGREAT,YOU ARE ON THE VERGE OF MASTERING C")
    elif level==3:
        print("\t\tGOOD ,A LITTLE PUSH WILL LEAD YOU TO SUCCESS")
    elif level==2:
        print("\t\tYOU ARE GOOD BUT LITTLE HARD WORK REQUIRED")
    else:
        print("\t\tSUCCESS REQUIRES HARD WORK")
    print("\n\n")
    os.system('pause')
    exit()


main_menu()




