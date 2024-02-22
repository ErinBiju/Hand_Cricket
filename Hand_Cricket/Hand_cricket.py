import random
from tkinter import *
import random as r
import keyboard


class Player:
    def __init__(self, name, wicket, runs, toss='Bating'):
        self.name = name
        self.wicket = wicket
        self.runs = runs
        self.toss = toss


class Toss:
    def __init__(self, frame, next_frame, human):
        self.frame = frame
        self.next_frame = next_frame
        self.human = human
        self.toss_Button = Button(self.frame, text="Bating", width=12, height =8, command=self.toss, bg= "#c3f550",fg ="black",borderwidth=10, relief=SUNKEN, activebackground="#93DC5C", font=("Arial",30))
        self.toss_Button.pack()
        confirm_Button = Button(self.frame, command=self.go_to_play, text="Confirm", relief=RAISED, borderwidth= 3, width= 25, height=1)
        confirm_Button.pack()
        self.count=0
    def go_to_play(self):
        self.next_frame.pack()
        self.frame.destroy()
    def toss(self):
        if self.count % 2 !=0:
            self.toss_Button.config(text="Bating")
            self.human.toss = 'Bating'
        else:
            self.toss_Button.configure(text="Bowling")
            self.human.toss = 'Bowling'
        self.count += 1

class Match_result:
    def __init__(self, frame, human=None, bot=None):
        self.frame = frame
        self.human = human
        self.bot = bot
        self.Who_won_label = Label(self.frame, text="Press 'Show Result'", width=25, height=8, bg="#c3f550", fg="black", borderwidth=10, relief=SUNKEN, font=("Times new Roman", 30))
        self.Who_won_label.pack()
        self.relive_button = Button(frame, text="Show Result", command=self.result, relief=RAISED, borderwidth= 3)
        self.relive_button.pack()
        self.Final_Runs_label = Label(self.frame, text="", width=50, bg='#cccccc',relief=SUNKEN)

    def result(self):
        self.relive_button.pack_forget()
        self.Final_Runs_label.config(text=f'Runs: Bot {self.bot.runs} | Human {self.human.runs}')

        if self.human.runs > self.bot.runs:
            self.Who_won_label.config(text="You Won \n - Seems like Victory \n is in your Blood")
        elif self.bot.runs > self.human.runs:
            self.Who_won_label.config(text="Roses are Red,\n the Sky is blue, \n You LOST to a Bot \n & how are You ?")
        elif self.bot.runs == self.human.runs:
            self.Who_won_label.config(text="Its a Tie")
        else:
            print("Error 404")
        self.Final_Runs_label.pack()




class Play_control:
    def __init__(self, frame, next_frame, human, bot, match_result):
        self.frame = frame
        self.next_frame = next_frame
        self.match_result = match_result
        self.human = human
        self.bot = bot
        self.display_label = Label(master=frame,text="Instruction: \n Press any Number \n b/w 1 to 6  when \n 'NOW' is shown \n on the screen", width=15, height=8, bg="#c3f550", fg="black", borderwidth=10, relief=SUNKEN, activebackground="#93DC5C", font=("Arial", 30))
        self.display_label.pack()
        self.Score_label = Label(master=frame,text="Runs: Bot 0 | You 0 ", width=50, relief=SUNKEN, bg="#cccccc")
        self.Score_label.pack()
        self.wicket_label = Label(master=frame,text = "Wicket: Bot 1 | You 1", width=50, relief=SUNKEN, bg="#cccccc")
        self.wicket_label.pack()
        self.start_button = Button(master=frame, text="GO", command=self.count_down, width=25, relief=RAISED, borderwidth=3)
        self.start_button.pack(padx=5, pady=5)
        self.human_NowPlaying_label = Label(master=frame,text ="Press Go to Start", width=50,relief= SUNKEN, bg="#cccccc", fg ="blue")
        self.human_NowPlaying_label.pack()

        self.time = 3
        self.play_value = 2

    def match_over(self):
        print("Match is Over")
        self.match_result.human = self.human
        self.match_result.bot = self.bot
        self.match_result.frame = self.next_frame
        self.next_frame.pack()
        self.frame.pack_forget()
    def bating(self):
        bot_show_bating = r.randint(1, 6)
        human_show_bating = keyboard.read_key()
        l = ['1','2','3','4','5','6']
        if human_show_bating in l:
            display = "Bot: " + str(bot_show_bating) + " | Player:" + human_show_bating
            self.human_NowPlaying_label.config(text="You are Bating")

            if self.human.wicket > 0:
                if str(bot_show_bating) != str(human_show_bating):
                    self.human.runs += int(human_show_bating)
                    self.Score_label.config(text=f'Runs: Bot {self.bot.runs} | You {self.human.runs}')
                    print("your runs:", self.human.runs)
                elif str(bot_show_bating) == str(human_show_bating):
                    print("You Lost a Wicket")
                    self.human.wicket -= 1
                    self.wicket_label.config(text=f'Wicket: Bot {self.bot.wicket} | You {self.human.wicket}')
                    if self.human.wicket == 0:
                        self.play_value -= 1
                        self.human.toss = 'Bowling'
                        self.human_NowPlaying_label.config(text="Your Wicket is Over")
            if (self.play_value == 1) and (self.human.runs > self.bot.runs) and self.human.toss == 'Bating':
                self.match_over()
            self.display_label.config(fg="black",text=display)
        else:
            self.tease()
    def tease(self):
        i = random.randrange(1,5)
        match i:
            case 1:
                self.display_label.config(text = "Error 404: \n Player Brain \n not Found \n *Invalid Input*")
            case 2:
                self.display_label.config(text="Player Brain \n is not Braining \n *Invalid Input*")
            case 3:
                self.display_label.config(text="Brain cells \n left the chat  \n *Invalid Input*")
            case 4:
                self.display_label.config(text="Bro failed\n Math \n  *Invalid Input*")

    def bowling(self):
        bot_show = r.randint(1, 6)
        human_show = keyboard.read_key()
        l = ['1', '2', '3', '4', '5', '6']
        if human_show in l:
            display = "Bot: " + str(bot_show) + " | Player:" + human_show
            self.human_NowPlaying_label.config(text="You are Bowling")
            if self.bot.wicket > 0:
                if str(bot_show) != str(human_show):
                    self.bot.runs += int(bot_show)
                    print("Bot runs",self.bot.runs)
                    self.Score_label.config(text=f'Runs: Bot {self.bot.runs}| You {self.human.runs}')
                    # self.Score_label.update()
                elif str(bot_show) == str(human_show):
                    print("Bot Lost a wicket")
                    self.bot.wicket -= 1
                    self.wicket_label.config(text=f'Wicket: Bot {self.bot.wicket} | You {self.human.wicket}')
                    if self.bot.wicket == 0:
                        self.play_value -= 1
                        self.human.toss = 'Bating'
                        self.human_NowPlaying_label.config(text="Bot's Wicket is over")
            if (self.play_value == 1) and (self.bot.runs > self.human.runs) and self.human.toss == 'Bowling':
                self.match_over()
            self.display_label.config(fg="black", text=display)
        else:
            self.tease()

    def play(self):

        if self.play_value == 0:
            self.match_over()
        else:
            if self.human.toss == 'Bating':
                print("You are Bating")
                self.bating()
            else:  # self.human.toss == "Bowling":  human.toss = bowling
                print("You are Bowling")
                self.bowling()



    def count_down(self):
        self.display_label.config(fg="Red", text=str(self.time))
        self.time -= 1
        if self.time >= 0:
            self.display_label.after(1000, self.count_down)
        else:
            self.display_label.config(text="NOW")
            self.display_label.update()
            self.time = 3
            self.play()






class App:
    def __init__(self):
        window = Tk()
        img = PhotoImage(file='icon.png')
        window.iconphoto(False,img)
        window.title("Hand Cricket")

        label_Eb = Label(window,text="EB",width=8, height=5, bg="#c3f550", fg="black", borderwidth=10, relief=SUNKEN, font=("Times New Roman", 60))
        label_Eb.pack()
        label_Eb.update()
        label_Eb.after(2500)
        label_Eb.pack_forget()

        toss_frame= Frame(master=window,height =500,width =250)
        toss_frame.pack(padx=5,pady=5)
        play_frame = Frame(master=window)
        result_frame = Frame(master=window)

        human = Player('human', 1, 0)
        bot = Player('bot',1,0)

        match_result = Match_result(result_frame)
        toss_display = Toss(toss_frame, play_frame,human)
        play_display = Play_control(play_frame,result_frame,human,bot,match_result)

        window.mainloop()

App()

