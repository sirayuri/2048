import tkinter as tk
import random
import time

#マスの情報取得
def acquisition():
    
    itidan_box =[
        [entry1_1.get(), entry1_2.get(), entry1_3.get(), entry1_4.get()],
        [entry2_1.get(), entry2_2.get(), entry2_3.get(), entry2_4.get()],
        [entry3_1.get(), entry3_2.get(), entry3_3.get(), entry3_4.get()],
        [entry4_1.get(), entry4_2.get(), entry4_3.get(), entry4_4.get()]
    ] 

    return itidan_box

def list_space():
    itidan_list =[
        [entry1_1,entry1_2,entry1_3,entry1_4],
        [entry2_1,entry2_2,entry2_3,entry2_4],
        [entry3_1,entry3_2,entry3_3,entry3_4],
        [entry4_1,entry4_2,entry4_3,entry4_4]
    ]

    return itidan_list

#隣り合う数字を検索(横)
def nextto(k,no1,no2,itidan_box):
    if itidan_box[k][no1]==itidan_box[k][no2]:
        return 1
    else:
        return 0

#隣り合う数字を検索(縦)
def nexttovertical(k,no1,no2,itidan_box):
    if itidan_box[no1][k]==itidan_box[no2][k]:
        return 1
    else:
        return 0

#左隣が空白か判定
def nextleftblank(k,no1,itidan_box):
    if no1-1<0:
        return 0
    elif itidan_box[k][no1-1]=="":
        return 1
    else:
        return 2

#右隣が空白か判定
def nextblank(k,no1,itidan_box):
    if no1+1>3:
        return 0
    elif itidan_box[k][no1+1]=="":
        return 1
    else:
        return 2

#上が空白か判定
def nextupblank(k,no1,itidan_box):
    if no1-1<0:
        return 0
    elif itidan_box[no1-1][k]=="":
        return 1
    else:
        return 2

#下が空白か判定
def nextdownblank(k,no1,itidan_box):
    if no1+1>3:
        return 0
    elif itidan_box[no1+1][k]=="":
        return 1
    else:
        return 2

#埋まっているマスを検索(横)
def fill(k,itidan_box):
    fill_list=[]
    for i in range(4):
        if itidan_box[k][i]!="":
            fill_list.append(i)
    return fill_list       

#埋まっているマスを検索(縦)
def fillvertical(k,itidan_box):
    fill_list=[]
    for i in range(4):
        if itidan_box[i][k]!="":
            fill_list.append(i)
    return fill_list

#初期マス
def sinkirand():
    itian_list = list_space()
    for i in range(2):
        ent = random.randint(0,3)
        ent1= random.randint(0,3)

        if itian_list[ent][ent1].get()!="":
            itian_list[ent][ent1].delete(0, tk.END)
            sinkirand()
        else:
            itian_list[ent][ent1].insert(tk.END,"2")

#ランダムなマスに数字を生成
def rand():
    ent = random.randint(0,3)
    ent1= random.randint(0,3)
    itidan_list=list_space()
    if random.randint(1,6)==1:
        suuti=4
    else:
        suuti=2

    if itidan_list[ent][ent1].get()!="":
        rand()
    else:
        itidan_list[ent][ent1].insert(tk.END,str(suuti))

#上移動
def up():
    
    itidan_box = acquisition()

    itidan_list = list_space()

    for k in range(4):
        for i in range(3):
                itidan_box=acquisition()
                fill_list=fillvertical(k,itidan_box)
                no1=len(fill_list)
                for i in range(no1):
                    if nextupblank(k,fill_list[i],itidan_box)==1:
                        print("空いてるよ")
                        itidan_list[fill_list[i]-1][k].insert(tk.END,str(itidan_box[fill_list[i]][k]))
                        itidan_list[fill_list[i]][k].delete(0,tk.END)
                    else:
                        print("空きがないよ")
        fill_list=fillvertical(k,itidan_box)
        no1=len(fill_list)

        fi3= 200000

        for j in range(0,no1):
            if j+1>no1-1:
                continue
            
            fi1= fill_list[j]
            fi2= fill_list[j+1]
            
            if fi3+1==fi1:
                print("コンティニューしました。")
                continue
            elif nexttovertical(k,fi1,fi2,itidan_box)==1:
                print("隣はおなじ数字です")
                itidan_list[fi1][k].delete(0,tk.END)
                itidan_list[fi2][k].delete(0,tk.END)
                itidan_list[fi1][k].insert(tk.END,int(itidan_box[fi2][k])+int(itidan_box[fi1][k]))
                fi3 = fi1
            else:
                print("隣は違う数字です")
        
        itidan_bx=acquisition()
        fill_lis=fillvertical(k,itidan_bx)
        no=len(fill_lis)
        for i in range(no):
            if nextupblank(k,fill_lis[i],itidan_bx)==1:
                print("空いてるよ")
                        
                itidan_list[fill_lis[i]-1][k].insert(tk.END,str(itidan_bx[fill_lis[i]][k]))
                itidan_list[fill_lis[i]][k].delete(0,tk.END)
            else:
                print("空きがないよ")

    time.sleep(0.1)
    rand()
   
#下移動
def down():
    itidan_box = acquisition()

    itidan_list = list_space()

    for k in range(4):
        for i in range(3):
            itidan_box=acquisition()
            fill_list=fillvertical(k,itidan_box)
            no1=len(fill_list)
            for i in range(no1):
                if nextdownblank(k,fill_list[no1-1-i],itidan_box)==1:
                    print("空いてるよ")
                    itidan_list[fill_list[no1-1-i]+1][k].insert(tk.END,str(itidan_box[fill_list[no1-1-i]][k]))
                    itidan_list[fill_list[no1-1-i]][k].delete(0,tk.END)
                else:
                    print("空きがないよ")
        
        fill_list=fillvertical(k,itidan_box)
        no1=len(fill_list)

        fi3= 20000

        for j in range(0,no1):
            if no1-1-j <0 or no1-j>no1-1:
                continue
            fi1= fill_list[no1-j]
            fi2= fill_list[no1-1-j]
            
            if fi3-1==fi1:
                continue
            elif nexttovertical(k,fi1,fi2,itidan_box)==1:
                print("隣はおなじ数字です")
                itidan_list[fi1][k].delete(0,tk.END)
                itidan_list[fi2][k].delete(0,tk.END)
                itidan_list[fi1][k].insert(tk.END,int(itidan_box[fi2][k])+int(itidan_box[fi1][k]))
                fi3 = fi1
            else:
                print("隣は違う数字です")

        itidan_bx=acquisition()
        fill_lis=fillvertical(k,itidan_bx)
        no=len(fill_lis)
        for i in range(no):
            if nextdownblank(k,fill_lis[no-1-i],itidan_bx)==1:
                print("空いてるよ")
                        
                itidan_list[fill_lis[no-1-i]+1][k].insert(tk.END,str(itidan_bx[fill_lis[no-1-i]][k]))
                itidan_list[fill_lis[no-1-i]][k].delete(0,tk.END)
            else:
                print("空きがないよ")

    time.sleep(0.1)
    rand()

#左移動
def left():
    itidan_box = acquisition()

    itidan_list = list_space()

    for k in range(4):
        for i in range(3):
                itidan_box=acquisition()
                fill_list=fill(k,itidan_box)
                no1=len(fill_list)
                for i in range(no1):
                    if nextleftblank(k,fill_list[i],itidan_box)==1:
                        print("空いてるよ")
                        itidan_list[k][fill_list[i]-1].insert(tk.END,str(itidan_box[k][fill_list[i]]))
                        itidan_list[k][fill_list[i]].delete(0,tk.END)
                    else:
                        print("空きがないよ")
        fill_list=fill(k,itidan_box)
        no1=len(fill_list)

        fi3= 20000

        for j in range(0,no1):
            if j+1>no1-1:
                continue
            
            fi1= fill_list[j]
            fi2= fill_list[j+1]
            
            if fi3+1==fi1:
                continue
            elif nextto(k,fi1,fi2,itidan_box)==1:
                print("隣はおなじ数字です")
                itidan_list[k][fi1].delete(0,tk.END)
                itidan_list[k][fi2].delete(0,tk.END)
                itidan_list[k][fi1].insert(tk.END,int(itidan_box[k][fi2])+int(itidan_box[k][fi1]))
                fi3 = fi1
            else:
                print("隣は違う数字です")
        
        itidan_bx=acquisition()
        fill_lis=fill(k,itidan_bx)
        no=len(fill_lis)
        print(no)
        for i in range(no):
            if nextleftblank(k,fill_lis[i],itidan_bx)==1:
                print("空いてるよ")
                        
                itidan_list[k][fill_lis[i]-1].insert(tk.END,str(itidan_bx[k][fill_lis[i]]))
                itidan_list[k][fill_lis[i]].delete(0,tk.END)
            else:
                print("空きがないよ")

    time.sleep(0.1)

    rand()

#右移動
def right():
    
    itidan_box = acquisition()

    itidan_list = list_space()

    #右にずらす
    for k in range(4):
        for i in range(3):
            itidan_box=acquisition()
            fill_list=fill(k,itidan_box)
            no1=len(fill_list)
            for i in range(no1):
                if nextblank(k,fill_list[no1-1-i],itidan_box)==1:
                    print("空いてるよ")
                    itidan_list[k][fill_list[no1-1-i]+1].insert(tk.END,str(itidan_box[k][fill_list[no1-1-i]]))
                    itidan_list[k][fill_list[no1-1-i]].delete(0,tk.END)
                else:
                    print("空きがないよ")

        fill_list=fill(k,itidan_box)
        no1=len(fill_list)

        fi3= 20000

        #隣が同じ数字なら足す
        for j in range(0,no1):
            if no1-1-j <0 or no1-j>no1-1:
                continue
            fi1= fill_list[no1-j]
            fi2= fill_list[no1-1-j]
            
            if fi3-1==fi1:
                continue
            elif nextto(k,fi1,fi2,itidan_box)==1:
                print("隣はおなじ数字です")
                itidan_list[k][fi1].delete(0,tk.END)
                itidan_list[k][fi2].delete(0,tk.END)
                itidan_list[k][fi1].insert(tk.END,int(itidan_box[k][fi2])+int(itidan_box[k][fi1]))
                fi3 = fi1
            else:
                print("隣は違う数字です")

        itidan_bx=acquisition()
        fill_lis=fill(k,itidan_bx)
        no=len(fill_lis)
        for i in range(no):
            if nextblank(k,fill_lis[no-1-i],itidan_bx)==1:
                print("空いてるよ")
                        
                itidan_list[k][fill_lis[no-1-i]+1].insert(tk.END,str(itidan_bx[k][fill_lis[no-1-i]]))
                itidan_list[k][fill_lis[no-1-i]].delete(0,tk.END)
            else:
                print("空きがないよ")
    
    time.sleep(0.1)

    rand()

def print_key(event): # ③
    key = event.keysym
    
    if key =="w":
        up()
    elif key =="a":
        left()
    elif key =="d":
        right()
    elif key =="s":
        down()
#ウィンドウ作成
root=tk.Tk()
root.title("2048(うんこ)")
root.geometry("600x500")

lab=tk.Label(master=root,text="wasdでも操作できます")
lab.place(x="200",y="280")

#数字移動用のボタンを作成
up_but=tk.Button(master=root,text="up",width=10,height=3,command=up)
up_but.place(x="250",y="350")

right_but=tk.Button(master=root,text="right",width=10,height=3,command=right)
right_but.place(x="350",y="420")

down_but=tk.Button(master=root,text="down",width=10,height=3,command=down)
down_but.place(x="250",y="420")

left_but=tk.Button(master=root,text="left",width=10,height=3,command=left)
left_but.place(x="150",y="420")

#マスを生成
entry1_1=tk.Entry(master=root,width=5,font=10)
entry1_1.place(x="100",y="50")

entry1_2=tk.Entry(master=root,width=5,font=10)
entry1_2.place(x="200",y="50")

entry1_3=tk.Entry(master=root,width=5,font=10)
entry1_3.place(x="300",y="50")

entry1_4=tk.Entry(master=root,width=5,font=10)
entry1_4.place(x="400",y="50")

entry2_1=tk.Entry(master=root,width=5,font=10)
entry2_1.place(x="100",y="100")

entry2_2=tk.Entry(master=root,width=5,font=10)
entry2_2.place(x="200",y="100")

entry2_3=tk.Entry(master=root,width=5,font=10)
entry2_3.place(x="300",y="100")

entry2_4=tk.Entry(master=root,width=5,font=10)
entry2_4.place(x="400",y="100")

entry3_1=tk.Entry(master=root,width=5,font=10)
entry3_1.place(x="100",y="150")

entry3_2=tk.Entry(master=root,width=5,font=10)
entry3_2.place(x="200",y="150")

entry3_3=tk.Entry(master=root,width=5,font=10)
entry3_3.place(x="300",y="150")

entry3_4=tk.Entry(master=root,width=5,font=10)
entry3_4.place(x="400",y="150")

entry4_1=tk.Entry(master=root,width=5,font=10)
entry4_1.place(x="100",y="200")

entry4_2=tk.Entry(master=root,width=5,font=10)
entry4_2.place(x="200",y="200")

entry4_3=tk.Entry(master=root,width=5,font=10)
entry4_3.place(x="300",y="200")

entry4_4=tk.Entry(master=root,width=5,font=10)
entry4_4.place(x="400",y="200")

sinkirand()

buffer = tk.StringVar() # ①
buffer.set('')

tk.Label(root, text='').pack()
a = tk.Label(root, textvariable=buffer) # ②
a.pack()
a.bind('<Key>', print_key) # ④
a.focus_set() # ⑤


root.mainloop()