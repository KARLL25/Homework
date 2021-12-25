import tkinter as tk
file = open("k.txt", "r")
def inst():
    t = tk.Label(text="В ответ требуется ввести полное значение", font='Arial 10 bold')
    t.pack()
w = tk.Tk()
w.title("Тест по математике")
w.geometry("400x150")
w['bg']='#FFC0CB'
score= 0
false=0
q=0
cl=0
def start():
        global line,out,pr,false,q,cl
        line = file.readline()
        line = line.rstrip()
        cl += 1
        if cl==1:
            w.destroy()
        else:
            cl+=1
        if line=='':
            q=score+false
            print(int((score/q)*100))
            win = tk.Tk()
            win.title("Результаты теста")
            win.geometry("400x250")
            win['bg']='#FFFFE0'
            out = tk.Label(win, text='Вы ответили правильно на '+ str(score)+' вопросов.',font='Arial 12',justify='center')
            out.pack()
            pr= tk.Label(win, text='Процент правильных ответов =  '+ str(int((score/q)*100))+' %', font='Arial 12',justify='center')
            pr.pack()            
            x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
            y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
            win.wm_geometry("+%d+%d" % (x, y))
        else:

            root = tk.Tk()
            root.geometry('300x200')
            root.title('Вопросики')
            root['bg']='#E0FFFF'
            q = tk.Label(root, text=line)
            q.pack()
            line = file.readline()
            line = line.rstrip()
            a = tk.Label(root, text=""+line)
            a.pack()
            line = file.readline()
            line = line.rstrip()
            b = tk.Label(root, text=""+line)
            b.pack()
            line = file.readline()
            line = line.rstrip()
            c = tk.Label(root, text=""+line)
            c.pack()
            ans = tk.Entry(root, width=40)
            x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
            y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
            root.wm_geometry("+%d+%d" % (x, y))
            ans.pack()
            def submit():
                global otvet,score,false
                otvet = str(ans.get())
                line = file.readline()
                line = line.rstrip()
                if otvet != line:
                    print('Нет.',line)
                    false+= 1
                    root.destroy()
                    start()

                else:
                    print('Да.')                    
                    score += 1
                    start()
                    root.destroy()
            sub = tk.Button(root, text="Принять", command=submit)
            sub.pack()





greet = tk.Label(w, text="Тест" ,font='Arial 16')
greet.pack()
startButton = tk.Button(w, command=start, text="Начать тест")
startButton.pack()
instr = tk.Button(w, text="Инструкция", command=inst)
instr.pack()

end = tk.Button(w, text="Завершить", command=w.destroy)
end.pack()


x = (w.winfo_screenwidth() - w.winfo_reqwidth()) / 2
y = (w.winfo_screenheight() - w.winfo_reqheight()) / 2
w.wm_geometry("+%d+%d" % (x, y))
w.mainloop()
