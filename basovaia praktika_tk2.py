import tkinter as tk
file = open("k.txt", "r")
def inst():
    t = tk.Label(text="Внимание!! В ответ требуется ввести полное значение", font='Arial 10 bold')
    t.pack()
window = tk.Tk()
window.title("Обычный тест")
window.geometry("500x200")
score = 0
false=0
allq=0
close=0
def start():
        global line,out,proc,false,allq,close
        line = file.readline()
        line = line.rstrip()
        close += 1
        if close==1:
            window.destroy()
        else:
            close+=1
        if line=='':
            allq=score+false
            print(int((score/allq)*100))
            win = tk.Tk()
            win.title("Результаты теста")
            win.geometry("450x300")
            out = tk.Label(win, text='Вы ответили правильно на '+ str(score)+' вопросов.',font='Arial 12')
            out.pack()
            proc= tk.Label(win, text='Процент правильных ответов =  '+ str(int((score/allq)*100))+' %', font='Arial 12')
            proc.pack()            
            x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
            y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
            win.wm_geometry("+%d+%d" % (x, y))
        else:

            root = tk.Tk()
            root.geometry('400x400')
            root.title('q.txt')
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
                    false += 1
                    root.destroy()
                    start()

                else:
                    print('Да.')                    
                    score += 1
                    start()
                    root.destroy()
            sub = tk.Button(root, text="Принять", command=submit)
            sub.pack()





greet = tk.Label(window, text="Тест" ,font='Arial 16')
greet.pack()
startButton = tk.Button(window, command=start, text="Начать тест")
startButton.pack()
instr = tk.Button(window, text="Инструкция", command=inst)
instr.pack()

end = tk.Button(window, text="Завершить", command=window.destroy)
end.pack()


x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))
window.mainloop()
