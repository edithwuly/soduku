import random
import threading
import time
from Tkinter import*
from tkMessageBox import * 

z=[-1,-1]
k=0
new_record=''
origin1=[[8,3,7,4,6,1,5,2,9],[5,4,1,9,2,8,7,3,6],[2,6,9,5,3,7,4,1,8],[9,5,4,6,8,3,2,7,1],[7,2,8,1,9,5,3,6,4],[3,1,6,7,4,2,8,9,5],[4,7,5,3,1,9,6,8,2],[1,8,3,2,5,6,9,4,7],[6,9,2,8,7,4,1,5,3]]
image='default'
red='default'
r=[]
num=0

def sudu():
    global origin1
    a=random.randint(1,9)
    b=random.randint(1,9)
    while a==b:
        b=random.randint(1,9)
    for i in range(9):
        index1=origin1[i].index(a)
        index2=origin1[i].index(b)
        origin1[i][index1]=b
        origin1[i][index2]=a
    return



def GUI():
    global origin1,z,r
    for i in range(9):
        sudu()
    root0=Tk()
    root0.title('PLAY ME')
    root0.iconbitmap("sudoku.ico")
    root0.resizable(False, False)
    v=IntVar()
    v.set(0)
    Radiobutton(root0,text='EASY',variable=v,value=0).grid(row=0,column=0)
    Radiobutton(root0,text='MEDIUM',variable=v,value=1).grid(row=0,column=1)
    Radiobutton(root0,text='HARD',variable=v,value=2).grid(row=0,column=2)
    Radiobutton(root0,text='HELL',variable=v,value=3).grid(row=0,column=3)
    def f():
            global z,r,num
            num=0
            z=[-1,-1]
            r=[]
            try:
                pre=open('previous','r')
            except IOError:
                pre=open('previous','a')
                pre.write('EASY59:59:59\nMEDIUM59:59:59\nHARD59:59:59\nHELL59:59:59')
                pre.close()
                pre=open('previous','r')
            previous=pre.read()
            if v.get()==0:
                record=previous[4:12]
            if v.get()==1:
                record=previous[19:27]
            if v.get()==2:
                record=previous[32:40]
            if v.get()==3:
                record=previous[45:53]
            pre.close()
            def n():
                global k,new_record
                second=0
                minute=0
                hour=0
                t1=time.time()
                try:
                    while True:
                        t2=time.time()
                        t=t2-t1
                        if k==1:
                            t1=t2
                        if k==0:
                            if t>=1:
                                second=second+1
                                if second==60:
                                    minute=minute+1
                                    second=0
                                if minute==60:
                                    hour=hour+1
                                    minute=0
                                if hour>=10 and minute>=10 and second>=10:
                                    label2.config(text=str(hour)+':'+str(minute)+':'+str(second))
                                    new_record=str(hour)+':'+str(minute)+':'+str(second)
                                if hour<10 and minute<10 and second<10:
                                    label2.config(text='0'+str(hour)+':'+'0'+str(minute)+':'+'0'+str(second))
                                    new_record='0'+str(hour)+':'+'0'+str(minute)+':'+'0'+str(second)
                                if hour>=10 and minute<10 and second<10:
                                    label2.config(text=str(hour)+':'+'0'+str(minute)+':'+'0'+str(second))
                                    new_record=str(hour)+':'+'0'+str(minute)+':'+'0'+str(second)
                                if hour>=10 and minute>=10 and second<10:
                                    label2.config(text=str(hour)+':'+str(minute)+':'+'0'+str(second))
                                    new_record=str(hour)+':'+str(minute)+':'+'0'+str(second)
                                if hour<10 and minute>=10 and second>=10:
                                    label2.config(text=str(hour)+':'+'0'+str(minute)+':'+'0'+str(second))
                                    new_record=str(hour)+':'+'0'+str(minute)+':'+'0'+str(second)
                                if hour<10 and minute>=10 and second<10:
                                    label2.config(text='0'+str(hour)+':'+str(minute)+':'+'0'+str(second))
                                    new_record='0'+str(hour)+':'+str(minute)+':'+'0'+str(second)
                                if hour<10 and minute<10 and second>=10:
                                    label2.config(text='0'+str(hour)+':'+'0'+str(minute)+':'+str(second))
                                    new_record='0'+str(hour)+':'+'0'+str(minute)+':'+str(second)
                                if hour>=10 and minute<10 and second>=10:
                                    label2.config(text='0'+str(hour)+':'+str(minute)+':'+'0'+str(second))
                                    new_record='0'+str(hour)+':'+str(minute)+':'+'0'+str(second)
                                t1=t2
                except TclError:                    
                    return None
            thread1=threading.Thread(target=n)
            thread1.start()
            root1=Toplevel()
            root1.resizable(False, False)
            if v.get()==0:
                root1.title('EASY')
                root1.iconbitmap("sudoku_easy.ico")
            if v.get()==1:
                root1.title('MEDIUM')
                root1.iconbitmap("sudoku_medium.ico")
            if v.get()==2:
                root1.title('HARD')
                root1.iconbitmap("sudoku_hard.ico")
            if v.get()==3:
                root1.title('HELL')
                root1.iconbitmap("sudoku_hard.ico")
            a=Canvas(root1,width=775,height=775,bg='white')
            a.pack()
            img=PhotoImage(file='paused.gif')
            for i in range(1,10):
                for j in range(1,10):
                    a.create_rectangle(65+60*(i-1),65+60*(j-1),65+60*i,65+60*j,outline='grey')
            a.create_rectangle(60,60,610,610)
            a.create_rectangle(65,65,605,605)
            for i in range(3):
                for j in range(3):
                    a.create_rectangle(65+180*i,65+180*j,65+180*(i+1),65+180*(j+1))
            a_row=[['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '']]
            b_col=[['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '']]
            c_jiugongge=[['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '']]
            def pailie():
                d=random.randint(0,8)
                e=random.randint(0,8)
                r.append([d,e])
                a_row[d][e]=str(origin1[d][e])
            if v.get()==0:
                for i in range(45):
                    pailie()
            if v.get()==1:
                for i in range(38):
                    pailie()
            if v.get()==2:
                for i in range(30):
                    pailie()
            for i in range(9):
                for j in range(9):
                    a.create_text(65+30*(2*i+1),65+30*(2*j+1),text=a_row[j][i],font = ('Helvetica', '30'),fill='blue')
            def b():
                for i in range(9):
                    for j in range(9):
                        b_col[i][j]=a_row[j][i]
                for i in range(3):
                    c_jiugongge[0][i]=a_row[0][i]
                    c_jiugongge[0][i+3]=a_row[1][i]
                    c_jiugongge[0][i+6]=a_row[2][i]
                    c_jiugongge[1][i]=a_row[0][i+3]
                    c_jiugongge[1][i+3]=a_row[1][i+3]
                    c_jiugongge[1][i+6]=a_row[2][i+3]
                    c_jiugongge[2][i]=a_row[0][i+6]
                    c_jiugongge[2][i+3]=a_row[1][i+6]
                    c_jiugongge[2][i+6]=a_row[2][i+6]
                    c_jiugongge[3][i]=a_row[3][i]
                    c_jiugongge[3][i+3]=a_row[4][i]
                    c_jiugongge[3][i+6]=a_row[5][i]
                    c_jiugongge[4][i]=a_row[3][i+3]
                    c_jiugongge[4][i+3]=a_row[4][i+3]
                    c_jiugongge[4][i+6]=a_row[5][i+3]
                    c_jiugongge[5][i]=a_row[3][i+6]
                    c_jiugongge[5][i+3]=a_row[4][i+6]
                    c_jiugongge[5][i+6]=a_row[5][i+6]
                    c_jiugongge[6][i]=a_row[6][i]
                    c_jiugongge[6][i+3]=a_row[7][i]
                    c_jiugongge[6][i+6]=a_row[8][i]
                    c_jiugongge[7][i]=a_row[6][i+3]
                    c_jiugongge[7][i+3]=a_row[7][i+3]
                    c_jiugongge[7][i+6]=a_row[8][i+3]
                    c_jiugongge[8][i]=a_row[6][i+6]
                    c_jiugongge[8][i+3]=a_row[7][i+6]
                    c_jiugongge[8][i+6]=a_row[8][i+6]
            b()
            def q():
                global new_record
                w=0
                for i in range(9):
                    for j in range(9):
                       if '' ==a_row[i][j]:
                           w=w+1
                if w==0:
                    pre=open('previous','r')
                    previous=pre.read()
                    pre.close()
                    pre=open('previous','w')
                    new_long=int(new_record[0:2])*60*60+int(new_record[3:5])*60+int(new_record[6:])
                    if v.get()==0:
                        pre_long=int(previous[4:6])*60*60+int(previous[7:9])*60+int(previous[10:12])
                        if new_long<pre_long:                                       
                            previous=previous[0:4]+new_record+previous[12:]
                            answer = askokcancel("Congretulation!","New Record"+new_record+'\nNew Game?',parent=root1)
                        if new_long>=pre_long:
                            answer = askokcancel("Complete","New Game?",parent=root1)                        
                    if v.get()==1:
                        pre_long=int(previous[19:21])*60*60+int(previous[22:24])*60+int(previous[25:27])
                        if new_long<pre_long:                                       
                            previous=previous[0:19]+new_record+previous[27:]
                            answer = askokcancel("Congretulation!","New Record"+new_record+'\nNew Game?',parent=root1)
                        if new_long>=pre_long:
                            answer = askokcancel("Complete","New Game?",parent=root1)
                    if v.get()==2:
                        pre_long=int(previous[32:34])*60*60+int(previous[35:37])*60+int(previous[38:40])
                        if new_long<pre_long:                                       
                            previous=previous[0:32]+new_record+previous[40:]
                            answer = askokcancel("Congretulation!","New Record"+new_record+'\nNew Game?',parent=root1)
                        if new_long>=pre_long:
                            answer = askokcancel("Complete","New Game?",parent=root1)
                    if v.get()==3:
                        pre_long=int(previous[45:47])*60*60+int(previous[48:50])*60+int(previous[51:])
                        if new_long<pre_long:                                       
                            previous=previous[0:45]+new_record
                            answer = askokcancel("Congretulation!","New Record"+new_record+'\nNew Game?',parent=root1)
                        if new_long>=pre_long:
                            answer = askokcancel("Complete","New Game?",parent=root1)
                    pre.write(previous)
                    pre.close()
                    new_record=''                        
                    if answer:
                        root0.destroy()
                        GUI()
                    else:
                        root0.destroy()
            def h():               
                button1.config(state=NORMAL)
                button2.config(state=NORMAL)
                button3.config(state=NORMAL)
                button4.config(state=NORMAL)
                button5.config(state=NORMAL)
                button6.config(state=NORMAL)
                button7.config(state=NORMAL)
                button8.config(state=NORMAL)
                button9.config(state=NORMAL)
                button10.config(state=NORMAL)
                if z[0]>=0 and z[0]<=2 and z[1]>=0 and z[1]<=2:
                    c=0
                if z[0]>=3 and z[0]<=5 and z[1]>=0 and z[1]<=2:
                    c=1
                if z[0]>=6 and z[0]<=8 and z[1]>=0 and z[1]<=2:
                    c=2
                if z[0]>=0 and z[0]<=2 and z[1]>=3 and z[1]<=5:
                    c=3
                if z[0]>=3 and z[0]<=5 and z[1]>=3 and z[1]<=5:
                    c=4
                if z[0]>=6 and z[0]<=8 and z[1]>=3 and z[1]<=5:
                    c=5
                if z[0]>=0 and z[0]<=2 and z[1]>=6 and z[1]<=8:
                    c=6
                if z[0]>=3 and z[0]<=5 and z[1]>=6 and z[1]<=8:
                    c=7
                if z[0]>=6 and z[0]<=8 and z[1]>=6 and z[1]<=8:
                    c=8
                for i in range(9):
                    if str(i+1) in a_row[z[1]] or str(i+1) in b_col[z[0]] or str(i+1) in c_jiugongge[c]:
                        y=i+1
                        if y==1:
                            button1.config(state=DISABLED) 
                        if y==2:
                            button2.config(state=DISABLED)
                        if y==3:
                            button3.config(state=DISABLED)
                        if y==4:
                            button4.config(state=DISABLED)
                        if y==5:
                            button5.config(state=DISABLED)
                        if y==6:
                            button6.config(state=DISABLED)
                        if y==7:
                            button7.config(state=DISABLED)
                        if y==8:
                            button8.config(state=DISABLED)
                        if y==9:
                            button9.config(state=DISABLED)
            def h1():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='1',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='1',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='1'
                    b()
                    h()
                q()
                return
            button1=Button(root1,text='1',width=2,font = ('Helvetica', '22'),bd=3,command=h1)
            a.create_window(130,675,window=button1)
            def h2():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='2',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='2',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='2'
                    b()
                    h()
                q()
                return 
            button2=Button(root1,text='2',width=2,font = ('Helvetica', '22'),bd=3,command=h2)
            a.create_window(180,675,window=button2)
            def h3():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='3',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='3',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='3'
                    b()
                    h()
                q()
                return 
            button3=Button(root1,text='3',width=2,font = ('Helvetica', '22'),bd=3,command=h3)
            a.create_window(230,675,window=button3)
            def h4():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='4',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='4',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='4'
                    b()
                    h()
                q()
                return 
            button4=Button(root1,text='4',width=2,font = ('Helvetica', '22'),bd=3,command=h4)
            a.create_window(280,675,window=button4)
            def h5():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='5',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='5',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='5'
                    b()
                    h()
                q()
                return 
            button5=Button(root1,text='5',width=2,font = ('Helvetica', '22'),bd=3,command=h5)
            a.create_window(330,675,window=button5)
            def h6():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='6',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='6',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='6'
                    b()
                    h()
                q()
                return 
            button6=Button(root1,text='6',width=2,font = ('Helvetica', '22'),bd=3,command=h6)
            a.create_window(380,675,window=button6)
            def h7():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='7',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='7',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='7'
                    b()
                    h()
                q()
                return 
            button7=Button(root1,text='7',width=2,font = ('Helvetica', '22'),bd=3,command=h7)
            a.create_window(430,675,window=button7)
            def h8():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='8',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='8',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='8'
                    b()
                    h()
                q()
                return 
            button8=Button(root1,text='8',width=2,font = ('Helvetica', '22'),bd=3,command=h8)
            a.create_window(480,675,window=button8)
            def h9():
                global z
                if z[0]!=-1:
                    if a_row[z[1]][z[0]]=='':
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='9',font = ('Helvetica', '30'))
                    if a_row[z[1]][z[0]]!='':
                        a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                        a.create_text(65+30*(2*z[0]+1),65+30*(2*z[1]+1),text='9',font = ('Helvetica', '30'))
                    a_row[z[1]][z[0]]='9'
                    b()
                    h()
                q()
                return 
            button9=Button(root1,text='9',width=2,font = ('Helvetica', '22'),bd=3,command=h9)
            a.create_window(530,675,window=button9)
            def h10():
                global z,num
                if z[0]!=-1:
                    a.create_rectangle(65+30*(2*z[0])+2,65+30*(2*z[1])+2,65+30*(2*z[0]+2)-2,65+30*(2*z[1]+2)-2,outline='white',fill='white')
                    a_row[z[1]][z[0]]=''
                    b()
                    h()                              
            button10=Button(root1,text='DEL',font = ('Helvetica', '22'),bd=3,command=h10)
            a.create_window(700,575,window=button10)
            label1=Label(root1,text='TIME',font = ('Helvetica', '22'),bg='white')
            a.create_window(700,105,window=label1)
            label2=Label(root1,text='00:00:00',font = ('Helvetica', '14'),bg='white',width=10)
            a.create_window(700,155,window=label2)
            label3=Label(root1,text='BEST',font = ('Helvetica', '22'),bg='white')
            a.create_window(700,255,window=label3)            
            label4=Label(root1,text=record,font = ('Helvetica', '14'),bg='white',width=10)
            a.create_window(700,305,window=label4)
            def h11():
                global k,image,red,z
                while True:
                    if k==0:
                        k=1
                        image=a.create_image(325,325,image = img)
                        button1.config(state=DISABLED)
                        button2.config(state=DISABLED)
                        button3.config(state=DISABLED)
                        button4.config(state=DISABLED)
                        button5.config(state=DISABLED)
                        button6.config(state=DISABLED)
                        button7.config(state=DISABLED)
                        button8.config(state=DISABLED)
                        button9.config(state=DISABLED)
                        button10.config(state=DISABLED)
                        button11.config(text='START')
                        break
                    if k==1:
                        k=0
                        button1.config(state=NORMAL)
                        button2.config(state=NORMAL)
                        button3.config(state=NORMAL)
                        button4.config(state=NORMAL)
                        button5.config(state=NORMAL)
                        button6.config(state=NORMAL)
                        button7.config(state=NORMAL)
                        button8.config(state=NORMAL)
                        button9.config(state=NORMAL)
                        button10.config(state=NORMAL)
                        button11.config(text='PAUSE')
                        a.delete(image)
                        if [z[1],z[0]] in r:
                            if z[0]!=-1:
                                a.delete(red)
                                red=a.create_rectangle(65+30*(2*z[0])+1,65+30*(2*z[1])+1,65+30*(2*z[0]+2)-1,65+30*(2*z[1]+2)-1,outline='red')
                                button1.config(state=DISABLED)
                                button2.config(state=DISABLED)
                                button3.config(state=DISABLED)
                                button4.config(state=DISABLED)
                                button5.config(state=DISABLED)
                                button6.config(state=DISABLED)
                                button7.config(state=DISABLED)
                                button8.config(state=DISABLED)
                                button9.config(state=DISABLED)
                                button10.config(state=DISABLED)
                        else:
                            if z[0]!=-1:
                                a.delete(red)
                                red=a.create_rectangle(65+30*(2*z[0])+1,65+30*(2*z[1])+1,65+30*(2*z[0]+2)-1,65+30*(2*z[1]+2)-1,outline='red')
                                h()
                        break
            button11=Button(root1,text='PAUSE',font = ('Helvetica', '22'),bd=3,command=h11)
            a.create_window(700,475,window=button11)
            def click1(event):
                global z,k,red,r,e
                if event.x>=65 and event.x<=605 and event.y>=65 and event.y<=605 and k==0:
                    z=[(event.x-65)/60,(event.y-65)/60]                   
                    if [z[1],z[0]] in r:
                        a.delete(red)
                        red=a.create_rectangle(65+30*(2*z[0])+1,65+30*(2*z[1])+1,65+30*(2*z[0]+2)-1,65+30*(2*z[1]+2)-1,outline='red')
                        button1.config(state=DISABLED)
                        button2.config(state=DISABLED)
                        button3.config(state=DISABLED)
                        button4.config(state=DISABLED)
                        button5.config(state=DISABLED)
                        button6.config(state=DISABLED)
                        button7.config(state=DISABLED)
                        button8.config(state=DISABLED)
                        button9.config(state=DISABLED)
                        button10.config(state=DISABLED)
                    else:
                        a.delete(red)
                        red=a.create_rectangle(65+30*(2*z[0])+1,65+30*(2*z[1])+1,65+30*(2*z[0]+2)-1,65+30*(2*z[1]+2)-1,outline='red')
                        h()
            root1.bind('<Button-1>',click1)
    Button(root0,text='   start   ',command=f,width=6).grid(columnspan=4)    
    root0=mainloop()
    

GUI()
    


    
