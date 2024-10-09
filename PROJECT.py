#import module needed
from tkinter import *
import tkinter as tk
import csv
import os
import schedule
import mysql.connector as sc
import csv
def main_1():
    t="rekha"
    LIST1=[]
    NUMBEROFPERIODS=[]
    LIST3=[]
    LIST4=[]
    LIST5=[]
    LIST6=[]
    NUMBER_OF_LINES=0
    FD="24-03-21"
    
    def unique(list1): 
      
        # intilize a null list 
        unique_list = []                      
          
        # traverse for all elements 
        for x in list1: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x)
        return(unique_list)

    
    a=sc.connect(host="localhost",user="root",passwd="Chintoo@7",database="PROJECT")
    cursor=a.cursor()
    TD="26-03-21"
    
    p=open("C:/Users/yashv/OneDrive/Desktop/substitution number.txt","r")
    d=p.readlines()
    for i in d:
        LIST1.append(i.split(",")[0])
        LIST3.append(i.split(","))
    TD=str(int(TD[0:2])+1)+TD[2:]
    FD=str(int(FD[0:2])-1)+FD[2:]


    
        



    def absent_teacher_periods(t):
        aperiods=[]
        TEMP1=[]
        for a in LIST6:
            TEMP2=[]
            TEMP1.append(a)
            for b in unique(LIST5):
                TEMP2.append(b)
                TEMP3=[]
                q="Select "+"*"+" from "+a
                #periods of t on b day in a class
                cursor.execute(q)
                XY=cursor.fetchall()
                for m in XY:
                    if m[0] == b:
                        for d in range(0,len(m)):
                            if m[d]==t:
                                TEMP3.append(d)
                TEMP2.append(TEMP3)
            TEMP1.append(TEMP2)
            aperiods.append(TEMP1)
        return(unique(aperiods))





    def teachers_free():
        teachersfree=[]
        for a in range(0,len(aperiods)):
            TEMP1=[]
            if a%2==0:
                teachersfree.append(aperiods[a])
            else:
                for b in range(0,len(aperiods[a])):
                    if b%2==0 and aperiods[a][b]!=[]:
                        TEMP2=[]
                        teachersfree.append(aperiods[a][b])
                    else:
                        TEMP2=[]
                        if aperiods[a][b]==[]:
                            TEMP2.append(0)
                        else:
                            for c in aperiods[a][b]:
                                TNOFREE=[]
                                TFREE=[]
                                #teacher free on aperiod[a][b-1] at c period
                                f=open("C:/Users/yashv/OneDrive/Desktop/comp1.csv","r")
                                DAT=f.readlines()
                                for k in range(0,len(DAT)):
                                    if k%9==0:
                                        tname=DAT[k][6:9]
                                        q="Select "+"*"+" from "+tname
                                        LIST6.append(tname)
                                        cursor.execute(q)
                                        XY=cursor.fetchall()
                                        for m in XY:
                                            if (TD>m[9]>FD) == True:
                                                if m[0]==aperiods[a][b-1]:
                                                    if m[c]!="NULL":
                                                        TNOFREE.append(m[c])
                                for f in LIST1:
                                    if f not in TNOFREE:
                                        TEMP2.append([f,c])
                    if TEMP2!=[]:
                        teachersfree.append(TEMP2)
        return(teachersfree)
                                
                                  
                                
                
            
            
            
                
    def NUMBEROFPERIODS():
        f=open("C:/Users/yashv/OneDrive/Desktop/comp1.csv","r")
        DAT=f.readlines()
        for k in range(0,len(DAT)):
            if k%9==0:
                tname=DAT[k][6:9]
                q="Select "+"*"+" from "+tname
                LIST6.append(tname)
                cursor.execute(q)
                XY=cursor.fetchall()
                for m in XY:
                    if (TD>m[9]>FD) == True:
                        LIST5.append(m[0])
        for h in LIST1:
            for g in LIST5:
                COUNT=0
                for k in range(0,len(DAT)):
                    if k%9==0:
                        tname=DAT[k][6:9]
                        q="Select "+"*"+" from "+tname
                        cursor.execute(q)
                        XY=cursor.fetchall()
                        for m in XY:
                            if m[0]==g:
                                COUNT=m.count(h)+COUNT
                FI=[h,g,COUNT]
                LIST4.append(FI)
        return(unique(LIST4))
                
                    
    NUMBEROFPERIODS=NUMBEROFPERIODS()
    
    aperiods=(absent_teacher_periods(t)[0])
    teachersfree=teachers_free()



    def least_no_periods():
        leastperiods=[]
        for a in range(0,len(teachersfree)):
            lperiod=10
            if type(teachersfree[a])==list:
                if len(teachersfree[a])>1:
                    for b in teachersfree[a]:
                        for c in NUMBEROFPERIODS:
                            if b[0]==c[0]:
                                if c[1]==teachersfree[a-1]:
                                    if c[2]<lperiod:
                                        lperiod=c[2]
                    for d in teachersfree[a]:
                        for e in NUMBEROFPERIODS:
                            if e[0]==d[0] and e[1]==teachersfree[a-1] and e[2]==lperiod:
                                leastperiods.append(e[1])
                                leastperiods.append(d)
            elif len(teachersfree[a])<4:
                leastperiods.append(teachersfree[a])
        return(leastperiods)                        
                                        
    leastperiods=least_no_periods()

    def substitution():
        TEMP4=[]
        TEMP5=[]
        for a in range(0,len(leastperiods)):
            if type(leastperiods[a])==str:
                TEMP1=[]
                if leastperiods[a]!=[]:
                    TEMP1.append(leastperiods[a])
                TEMP2=[]
                for t in range(a+1,len(leastperiods)):
                    if type(leastperiods[t])==list:
                        if leastperiods[a]!=[]:
                            TEMP2.append(leastperiods[t])
                    else:
                        break
                if TEMP2!=[]:
                    TEMP1.append(TEMP2)
                TEMP4.append(TEMP1)
        for z in range(0,len(TEMP4)):
            if len(TEMP4[z])==1:
                TEMP5.append(TEMP4[z])
                TEMP6=[]
                TEMP7=[]
            else:
                if TEMP4[z][0] not in TEMP6:
                    TEMP5.append(TEMP4[z])
                    TEMP6.append(TEMP4[z][0])
                    for k in range(0,len(LIST3)):
                        if LIST3[k][0]==TEMP4[z][1][0][0]:
                            LIST3[k][1]=str(int(LIST3[k][1])+1)
                if TEMP4[z][0]==TEMP4[z-1][0] and TEMP4[z][1][0][1]!=TEMP4[z-1][1][0][1]:
                    TEMP5.append(TEMP4[z])
                    for k in range(0,len(LIST3)):
                        if LIST3[k][0]==TEMP4[z][1][0][0]:
                            LIST3[k][1]=str(int(LIST3[k][1])+1)
        return(TEMP5)
    TEMP5=substitution()
    #TEMP5=[['12A'], ['Wednesday', [['hema', 7]]], ['Thursday', [['lekha', 3]]], ['Thursday', [['lekha', 4]]], ['Friday', [['jaya', 3]]], ['Friday', [['jaya', 4]]], ['12B'], ['Tuesday', [['lekha', 4]]], ['Wednesday', [['hema', 2]]], ['11A'], ['Wednesday', [['hema', 8]]], ['Thursday', [['lekha', 4]]], ['Friday', [['jaya', 4]]], ['11B'], ['Tuesday', [['lekha', 3]]], ['Wednesday', [['hema', 1]]]]
    def addsubs():
        word=""        
        TEMP5=substitution()
        for i in LIST3:
            if LIST3.index(i)==0:
                word=word+i[0]+","+i[1]
            elif LIST3.index(i)==(len(LIST3)-1):
                word=word+i[0]+","+i[1]
            else:
                word=word+i[0]+","+i[1]+"\n"
        q=open("C:/Users/yashv/OneDrive/Desktop/substitution number.txt","w")
        q.write(word)
        q.close()


    def fsubstitution():
        s=open("C:/Users/yashv/OneDrive/Desktop/comp1.csv","r")
        t=open("C:/Users/yashv/OneDrive/Desktop/comp1-Copy.csv","w")
        d=s.readlines()
        Count=0
        s.seek(0)
        for i in TEMP5:
            for j in range(0,len(d)):
                k=s.readline()
                if len(i)==1 and i[0]==k[6:9]:
                    Count=Count+1
                if Count==1:
                    t.write(k)
                else:
                    t.write("\n"+k)
                n=s.readline()
                TEMP9=[]
                t.write(n)
                for m in range(6):
                            n=s.readline()
                            p=n.split(",")
                            for o in range((TEMP5.index(i))+1,len(TEMP5)):
                                if len(TEMP5[o])!=1:
                                    if p[0]==TEMP5[o][0]:
                                        p[int(TEMP5[o][1][0][1])]=TEMP5[o][1][0][0]
                                else:
                                    break
                            q=""
                            for r in p:
                                if p.index(r)!=(len(p)-1):
                                    q=q+r+","
                                else:
                                    q=q+r
                            t.write(q)
        s.seek(0)                
        t.close()      
    fsubstitution()
 
# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
     
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
     
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
     
    global username_verify
    global password_verify
     
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
     
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
def register_user():
 
    username_info = username.get()
    password_info = password.get()
     
    file = open("username_info.txt", "a")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    f1 = open("substitutions.txt","a")
    f1.write(username_info+" "+"0")
     
    username_entry.delete(0, END)
    password_entry.delete(0, END)
     
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
     
    # Implementing event on login button
     
def login_verify():
    global abcd
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    abcd=username1
    list_of_files = os.listdir()
     
    file1 = open("username_info.txt", "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        if username1 in verify:
            if password1=="admin" and username1=="admin":
     
                login_success()
            else:
                login_success1()
     
    else:
        password_not_recognised()
 
 
# Designing popup for login success

def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=function_screen).pack()
 
def login_success1():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=function_screen1).pack()
     
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
     
# Deleting popups
def delete_login_succesful():
    login_success_screen.destroy()
     
 
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 

# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 

def function_screen():#function
    delete_login_succesful()
    function_screen = Tk()
    function_screen.geometry("500x500")
    function_screen.title("ASPS")
    Label(function_screen,text="").pack()
     
     
    Button(function_screen,text="ADMIN POWERS", height="2", width="30", command = ADMIN_POWERS).pack()
    Label(function_screen,text="").pack()
     
    Button(function_screen, text="APPLYING FOR HOLIDAY", height="2", width="30", command = APPLYING_HOLIDAY).pack()
    Label(function_screen,text="").pack()
     
     
    Button(function_screen, text="VIEWING INFORMATION", height="2", width="30", command = VIEWING_INFO).pack()
     
def function_screen1():#function
    delete_login_succesful()
    function_screen = Tk()
    function_screen.geometry("500x500")
    function_screen.title("ASPS")
    Label(function_screen,text="").pack()
     
    Button(function_screen, text="APPLYING FOR HOLIDAY", height="2", width="30", command = APPLYING_HOLIDAY).pack()
    Label(function_screen,text="").pack()
     
     
    Button(function_screen, text="VIEWING INFORMATION", height="2", width="30", command = VIEWING_INFO).pack()
     
#BUTTONS

def ADMIN_POWERS():
    ADMIN_POWERS=Tk()
    f=open("substitution number.txt","r")
    x=f.read()
    print(x)

    Label(ADMIN_POWERS,text=x).pack()




def APPLYING_HOLIDAY():
    APPLYING_HOLIDAY = Tk()
    APPLYING_HOLIDAY.geometry("400x400")
    APPLYING_HOLIDAY.title("APPLYING HOLIDAY")
    global D
    global F
    F = StringVar()
    D = StringVar()
    Label(APPLYING_HOLIDAY,text="ENTER START DATE (dd-mm-yy)").pack()
    sdate = Entry(APPLYING_HOLIDAY, textvariable=F)
    sdate.pack()
    Label(APPLYING_HOLIDAY,text="ENTER END DATE (dd-mm-yy)").pack()
    edate = Entry(APPLYING_HOLIDAY, textvariable=D)
    edate.pack()
    Button(APPLYING_HOLIDAY, text="SUBMIT", height="2", width="30", command = lambda: APPLICATION_SUCCESSFUL(F,D)).pack()


def APPLICATION_SUCCESSFUL(F,D):
    s=F.get()
    e=D.get()
    main_1()
    AS=Tk()
    Label(AS, text="LEAVE APPLIED SUCCESSFULLY").pack()
    Button(AS, text="DoNE", command = AS.destroy).pack()
    print(s,e)


    
def VIEWING_INFO():
    VIEW_INFO=Tk()
    f=open("substitution number.txt","r")
    f1=open("username_info.txt","r")
    
    x=f1.readlines()
    y=x[0]
    a=f.readlines()
    l=x[0].split()
    for i in a:
        k=i.split(",")
        if k[0]==l[0]:
            Label(VIEW_INFO,text=(y+"has "+k[1]+" number of substitutions till date")).pack()
        

 
 
 
 

#MAIN FUNCTIONALITY

#OUTPUT





main_account_screen()





#CHANGE IN DATES
import time
def change_date():
    import datetime
    import csv
    x = datetime.datetime.now()
    f=open("C:/Users/yashv/OneDrive/Desktop/comp1.csv","r")
    #x = datetime.datetime.now() is used to obtain current time,date,month year,millisec,etc.
    def feb():
        for i in range(0,len(data)):
            if (data[i])[0]=="M" or (data[i])[0]=="W" or (data[i])[0]=="T" or (data[i])[0]=="F" or (data[i])[0]=="S":
                word=data[i].split(',')
                if int(((word)[9])[0:2])>21:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7-28
                    c=int(((word)[9])[4])+1
            # reading the CSV file
                    text=open(f, "r")
                     
                    #join() method combines all contents of
                    # csvfile.csv and formed as a string
                    text=''.join([j for j in text])
                                                            # search and replace the contents
                    text=text.replace(a,str(b))
                    text=text.replace(((word)[9])[4],str(c))
                    # output.csv is the output file opened in write mode
                    f_=open(f,"w")
                     
                    # all the replaced text is written in the output.csv file
                    f_.writelines(text)
                    f_.close()
                else:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7
                # reading the CSV file
                text=open(f, "r")
                 
                #join() method combines all contents of
                # csvfile.csv and formed as a string
                text=''.join([j for j in text])
                 
                # search and replace the contents
                text=text.replace(a,str(b))
                # output.csv is the output file opened in write mode
                f_=open(f,"w")
                 
                # all the replaced text is written in the output.csv file
                f_.writelines(text)
                f_.close()
            else:
                pass
     
    def thirtyone():
        for i in range(0,len(data)):
            if (data[i])[0]=="M" or (data[i])[0]=="W" or (data[i])[0]=="T" or (data[i])[0]=="F" or (data[i])[0]=="S":
                word=data[i].split(',')
                if int(((word)[9])[0:2])>24:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7-31
                    c=int(((word)[9])[4])+1
                    # reading the CSV file
                    text=open(f, "r")
                     
                    #join() method combines all contents of
                    # csvfile.csv and formed as a string
                    text=''.join([j for j in text])
                      # search and replace the contents
                    text=text.replace(a,str(b))
                    text=text.replace(((word)[9])[4],str(c))
                    # output.csv is the output file opened in write mode
                    f_=open(f,"w")
                     
                    # all the replaced text is written in the output.csv file
                    f_.writelines(text)
                    f_.close()
                else:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7
        # reading the CSV file
                text=open(f, "r")
         
        #join() method combines all contents of
        # csvfile.csv and formed as a string
                text=''.join([j for j in text])
         
        # search and replace the contents
                text=text.replace(a,str(b))
        # output.csv is the output file opened in write mode
                f_=open(f,"w")
         
        # all the replaced text is written in the output.csv file
                f_.writelines(text)
                f_.close()
            else:
                pass
     
     
    def thirty():
        for i in range(0,len(data)):
            if (data[i])[0]=="M" or (data[i])[0]=="W" or (data[i])[0]=="T" or (data[i])[0]=="F" or (data[i])[0]=="S":
                word=data[i].split(',')
                if int(((word)[9])[0:2])>23:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7-30
                    c=int(((word)[9])[4])+1
    # reading the CSV file
                    text=open(f, "r")
     
    #join() method combines all contents of
    # csvfile.csv and formed as a string
                    text=''.join([j for j in text])
      # search and replace the contents
                    text=text.replace(a,str(b))
                    text=text.replace(((word)[9])[4],str(c))
    # output.csv is the output file opened in write mode
                    f_=open(f,"w")
     
    # all the replaced text is written in the output.csv file
                    f_.writelines(text)
                    f_.close()
                else:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7
    # reading the CSV file
                    text=open(f, "r")
     
    #join() method combines all contents of
    # csvfile.csv and formed as a string
                    text=''.join([j for j in text])
                     
                    # search and replace the contents
                    text=text.replace(a,str(b))
                    # output.csv is the output file opened in write mode
                    f_=open(f,"w")
                     
                    # all the replaced text is written in the output.csv file
                    f_.writelines(text)
                    f_.close()
            else:
                pass
     
    def dec():
        for i in range(0,len(data)):
            if (data[i])[0]=="M" or (data[i])[0]=="W" or (data[i])[0]=="T" or (data[i])[0]=="F" or (data[i])[0]=="S":
                word=data[i].split(',')
                if int(((word)[9])[0:2])>24:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7-31
                    c=int(x.strftime("%Y"))+1             ###x.strftime("%Y") gives current year.
                # reading the CSV file
                    text=open(f, "r")
                #join() method combines all contents of
                # csvfile.csv and formed as a string
                    text=''.join([j for j in text])
                    text=text.replace(a,str(b))
                    text=text.replace(((word[9])[3:5],"01"))                      #6:10
                    text=text.replace(((word)[9])[6:10],str(c))
                 
                # search and replace the contents
                # output.csv is the output file opened in write mode
                    f_=open(f,"w")
                 
                # all the replaced text is written in the output.csv file
                    f_.writelines(text)
                    f_.close()
                else:
                    a=""
                    a=a+((word)[9])[0:2]
                    b=int(((word)[9])[0:2])+7
                # reading the CSV file
                text=open(f,"r")
                 
                #join() method combines all contents of
                #file and formed as a string
                text=''.join([j for j in text])
                 
                # search and replace the contents
                text=text.replace(a,str(b))
                # same file is thr output fil and is opened in write mode.
                f_=open(f,"w")
                 
                # all the replaced text is written in the output.csv file
                f_.writelines(text)
                f_.close()
            else:
                pass
    f="C:/Users/yashv/OneDrive/Desktop/comp1.csv"#address
    f1=open(f,"r")
    data=f1.readlines()
    # csv.reader helps
    #to read the file and returns the data in the form of a list
    if x.strftime("%A")=="Sunday":
    #on sunday date gets updated automatically
        if x.strftime("%b")=="Feb":                        #x.strftime("%b") gives the current month
            feb()
        elif x.strftime("%b")=="Jan" or x.strftime("%b")=="Mar" or x.strftime("%b")=="july" or x.strftime("%b")=="May" or x.strftime("%b")=="Aug" or x.strftime("%b")=="Oct":
            thirtyone()
        elif x.strftime("%b")=="Dec":
            dec()
        else:
            thirty()
schedule.every().sunday.do(change_date)
"""import mysql.connector as sc
a=sc.connect(host="localhost",user="root",passwd="****",database="PROJECT")
f=open("C:/Users/yashv/OneDrive/Desktop/comp1.csv","r")
d=f.readlines()
y=" (day char(10),period1 char(10),period2 char(10),period3 char(10),period4 char(10),period5 char(10),period6 char(10),period7 char(10),period8 char(10),date char(10));"
cursor=a.cursor()
for i in range(0,len(d)):
    data=d[i].replace("\n","")
    if i%9==0:
        tname=d[i][6:9]
        q="create table "+tname+y
        cursor.execute(q)
        r="insert into "+tname+" values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k in range(2,8):
            val=(d[i+k]).split(",")
            cursor.execute(r,val)
a.commit()
f.close()"""
