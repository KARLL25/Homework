from datetime import datetime as dt
#from tkinter import *

class Eat():    # статусы, если он поел или наоборот
    death="death"
    hungry="hungry"
    normal="normal"
    better="better"
    overfeeded="overfeeded"
    
class Mood(): # статусы, если зверьку выделили внимание или наоборот
    desperate="desperate"
    sad="sad"
    normal="normal"
    fine="fine"
    happy="happy"

class Animal(): # зверёк в его полном обличии

    def __init__(self,name="Марсик", eat_timeout=10,play_timeout=10):
        self.__name=name
        self.__eat_timeout=eat_timeout
        self.__play_timeout=play_timeout
        self.__count_eat=0
        self.__count_games=0
        self.__birth=dt.now()
        self.__state=Mood.normal
        self.__food_status=Eat.normal
        

    def control_eat(self):   # отслеживание голодный он или нет
        overdue=self.__eat_timeout
        time_without_eat=(dt.now()-self.__birth).total_seconds()-self.__count_eat*overdue
        hunger= time_without_eat
        if (hunger < overdue) and (hunger > (overdue*-1)):
            self.__food_status=Eat.normal
        if (hunger > (overdue * -2 )) and (hunger < (overdue * -2)):
            self.__food_status=Eat.better
        if (hunger < -(overdue * 2)) and (hunger > (overdue * -3)):
            self.__food_status=Eat.overfeeded
        if hunger < (overdue * -3):
            self.__food_status=Eat.death
            print(self.__name,"Умер от избытка еды")
            breakpoint()
        if (hunger > overdue) and (hunger < (overdue * 2)):
            self.__food_status=Eat.hungry
        if (hunger > (overdue * 3)):
            self.__food_status=Eat.death
            print(self.__name,"Умер от недостатка еды")
            breakpoint()


    def control_mood(self): # отслеживание настроения зверька
        out = self.__play_timeout
        play_timeout=(dt.now()-self.__birth).total_seconds()-self.__count_games * out
        chill =play_timeout
        if (chill < out) and (chill > (out * -1)):
            self.__state=Mood.normal
        if (chill > (out * -2)) and (chill < (out * -1)):
            self.__state=Mood.fine
        if (chill < -(out * -2)) and (chill > (out * -3)):
            self.__state=Mood.happy
        if chill > (out * 3):
            print(self.__name,"Впал в депрессию")
            breakpoint()
        if (chill > out) and (chill < (out*2)):
            self.__state=Mood.sad
        if (chill < (out * 3)) and (chill > (2 * out)):
            self.__state=Mood.desperate

    def result(self):
        Animal.control_eat(self)
        Animal.control_mood(self)
        print(self.__food_status)
        print(self.__state)

    def food(self, count=0):
        count
        self.__count_eat=self.__count_eat + count
        Animal.control_eat(self)
        print(self.__food_status)

    def games(self):
        self.__count_games+=1
        Animal.control_mood(self)
        print(self.__state)


m= Animal()
print("1 - покормить зверушку","2 - поиграть со зверушкой","3 - посмотреть статус зверушки"
      ,"4 - покинуть игру")
while True:
    a= int(input())
    if a == 1:
        print("сколько еды?")
        m.food(float(input()))
        continue
    elif a == 2:
        print("Питомец поиграл с вами")
        m.games()
        continue
    elif a == 3:
        m.result()
        continue
    elif a == 4:
        print("Вы завершили программу")
        break
    else:
        continue


##root=Tk()
##root.title("Tamagochi")
##root.geometry("500x500")

##def feed(self, count=0):
##        count
##        self.__count_eat=self.__count_eat + count
##        Animal.control_eat(self)
##        print(self.__food_status)
##
##feed = Button(root,text="Покормить", font=20, command=feed)
##feed.pack(side=BOTTOM)
##feed.place(x=40, y=430)
##
##status = Button(root,text="Посмотреть статус", font=20)
##status.pack(side=BOTTOM)
##status.place(x=170, y=430)
##
##play = Button(root, text="Поиграть", font=20)
##play.pack(side=BOTTOM)
##play.place(x=360, y=430)
##
##end = Button(root, text="Поиграть", font=20)
##end.pack(side=BOTTOM)
##end.place(x=360, y=430)
##
##root.mainloop

    
            

    
    
