import tkinter
from tkinter import *
from tkinter.ttk import *
from typing import Counter
from PIL import ImageTk, Image
from tkinter import FALSE

# window design

root = tkinter.Tk()
root.geometry("800x600")
root.title("Live Cricket Score")
root.configure(bg="#ECF0F3")
root.resizable(height=FALSE, width=FALSE)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)


# Button style

sto = Style()

sto.configure('L.TButton', font= ('Segoe UI', 22), foreground='#8B298E')
sto.configure('N.TButton', font= ('Segoe UI', 22) ,foreground='#E4058C')
sto.configure('E.TButton', font= ('Segoe UI', 22), foreground='#F89D6D')
sto.configure('S.TButton', font= ('Segoe UI', 14), foreground='#1595EB')
sto.configure('D.TButton', font= ('Segoe UI', 12), foreground='#6F0545')
sto.configure('R.TButton', font= ('Segoe UI', 12), foreground='#E0B12F')



# Frame on home screen raising

def show_frame(frame):
    frame.tkraise()


# Frame definition

frame1 = tkinter.Frame(root, bg="#ECF0F3")
frame2 = tkinter.Frame(root, bg="#ECF0F3")
frame3 = tkinter.Frame(root, bg="#ECF0F3")
frame4 = tkinter.Frame(root, bg="#ECF0F3")


for frame in (frame1,frame2, frame3,frame4):
    frame.grid(row=0, column=0, sticky='nsew')



# ====================== Frame one Code (Home Screen) =========================


# Heading

mainhead= tkinter.Label(frame1,text="Interactive Cricket Score Board", fg='#8B298E', font=("Segoe UI", 30),bg="#ECF0F3")
mainhead.place(relx=0.5, rely = 0.1 , anchor="center") 
          
# Image 

img = ImageTk.PhotoImage(Image.open("src/cric.png"))  
panel = tkinter.Label(frame1, image = img)
panel.place(relx = 0.5, rely = 0.4 , anchor="center")


# Links (Buttons)

b1 = Button(frame1, text ="Live", style='L.TButton', command= lambda: show_frame(frame2))
b1.place(relx = 0.01, rely = 0.8,anchor="w")

b2 = Button(frame1, text ="Own Match", style='N.TButton' , command= lambda: show_frame(frame3))
b2.place(relx = 0.5, rely = 0.8,anchor="center")

b3 = Button(frame1, text ="Exit", style='E.TButton', command = root.destroy)
b3.place(relx = 0.99, rely = 0.8, anchor="e")




# ====================== Frame Two Code (Live Match Screen) ========================


livehead= tkinter.Label(frame2,text="Live Matches", fg='#8B298E', font=("Segoe UI", 30))
livehead.place(relx=0.5, rely = 0.08 , anchor="center")


line1 = tkinter.Label(frame2,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg='#ECF0F3' )
line1.place(relx=0.5, rely = 0.15 , anchor="center")


# Match one -------------------------


match1= tkinter.Label(frame2,text="    CSK vs RCB [IPL T20]", fg='#F89D6D', font=("Segoe UI", 16),bg="#ECF0F3")
match1.place(relx=0.0, rely = 0.2 , anchor="w")

score1= tkinter.Label(frame2,text="RCB 108/9 (18.4)", fg='#061625', font=("Segoe UI", 16),bg="#ECF0F3")
score1.place(relx=0.4, rely = 0.2 , anchor="w")

bscore = Button(frame2, text ="Full scorecard", style='S.TButton', command= lambda: show_frame(frame4))
bscore.place(relx = 0.9, rely = 0.2,anchor="e")


# Match Two -------------------------


line2 = tkinter.Label(frame2,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line2.place(relx=0.5, rely = 0.25 , anchor="center")

match2= tkinter.Label(frame2,text="    ENG vs AUS  [ODI]", fg='#F89D6D', font=("Segoe UI", 16),bg="#ECF0F3")
match2.place(relx=0.0, rely = 0.3 , anchor="w")

score2= tkinter.Label(frame2,text="ENG 221/9 (46.2)", fg='#061625', font=("Segoe UI", 16),bg="#ECF0F3")
score2.place(relx=0.4, rely = 0.3 , anchor="w")

bscore1 = Button(frame2, text ="Full scorecard", style='S.TButton', command= lambda: show_frame(frame4))
bscore1.place(relx = 0.9, rely = 0.3,anchor="e")


# Match Three -------------------------


line3 = tkinter.Label(frame2,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line3.place(relx=0.5, rely = 0.35 , anchor="center")

match3= tkinter.Label(frame2,text="    PAK vs NZ   [ODI]", fg='#F89D6D', font=("Segoe UI", 16),bg="#ECF0F3")
match3.place(relx=0.0, rely = 0.4 , anchor="w")

score3= tkinter.Label(frame2,text="NZ  199/4 (27.3)", fg='#061625', font=("Segoe UI", 16),bg="#ECF0F3")
score3.place(relx=0.4, rely = 0.4 , anchor="w")

bscore2 = Button(frame2, text ="Full scorecard", style='S.TButton', command= lambda: show_frame(frame4))
bscore2.place(relx = 0.9, rely = 0.4,anchor="e")


# Match Four -------------------------


line4 = tkinter.Label(frame2,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line4.place(relx=0.5, rely = 0.45 , anchor="center")

match4= tkinter.Label(frame2,text="    IND vs PAK   [ODI]", fg='#F89D6D', font=("Segoe UI", 16),bg="#ECF0F3")
match4.place(relx=0.0, rely = 0.5 , anchor="w")

score4= tkinter.Label(frame2,text="IND  335/4 (47.4)", fg='#061625', font=("Segoe UI", 16),bg="#ECF0F3")
score4.place(relx=0.4, rely = 0.5 , anchor="w")

bscore3 = Button(frame2, text ="Full scorecard", style='S.TButton', command= lambda: show_frame(frame4))
bscore3.place(relx = 0.9, rely = 0.5,anchor="e")


# Match Five -------------------------


line5 = tkinter.Label(frame2,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line5.place(relx=0.5, rely = 0.55 , anchor="center")

match5= tkinter.Label(frame2,text="    AFG vs SCO   [ODI]", fg='#F89D6D', font=("Segoe UI", 16),bg="#ECF0F3")
match5.place(relx=0.0, rely = 0.6 , anchor="w")

score5= tkinter.Label(frame2,text="SCO  221/8 (43.4)", fg='#061625', font=("Segoe UI", 16),bg="#ECF0F3")
score5.place(relx=0.4, rely = 0.6 , anchor="w")

bscore4 = Button(frame2, text ="Full scorecard", style='S.TButton', command= lambda: show_frame(frame4))
bscore4.place(relx = 0.9, rely = 0.6,anchor="e")



# Home Button

bh = Button(frame2, text ="Home", style='N.TButton' , command= lambda: show_frame(frame1))
bh.place(relx = 0.5, rely = 0.9,anchor="center")




# =========================================== Frame Three Code (My scorecard Screen) =================================================


myscohead= tkinter.Label(frame3,text="My Scorecard", fg='#8B298E', font=("Segoe UI", 25),bg="#ECF0F3")
myscohead.place(relx=0.5, rely = 0.05 , anchor="center")

line1 = tkinter.Label(frame3,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line1.place(relx=0.5, rely = 0.1 , anchor="center")


# Function for selecting team name

def ent_team():
    enterteam.destroy()
    text1= team1.get()
    text2= team2.get()
    main_text = text1 + "  vs  "+ text2
    hosted= tkinter.Label(frame3, text= main_text, fg='#6F0545', font=("Segoe UI", 18),bg="#ECF0F3")
    hosted.place(relx=0.5, rely = 0.15 , anchor="center")



# Print who won the toss 



def wontoss1():
    tosst2.destroy()
    disp2 = tkinter.Label(frame3, text= team1.get() + " won the toss ", fg='#F71130', font=("Segoe UI", 12),bg="#ECF0F3")
    disp2.place(relx=0.5, rely = 0.22 , anchor="center")

def wontoss2():
    tosst1.destroy()
    disp3= tkinter.Label(frame3, text= team2.get() + " won the toss ", fg='#F71130', font=("Segoe UI", 12),bg="#ECF0F3")
    disp3.place(relx=0.5, rely = 0.22 , anchor="center")



# Function for Overs

def balls(overs):
    return round(((float(overs)-int(float(overs)))*10) + int(float(overs))*6)


def overs(balls):
    return balls/6 if not balls % 6 else (balls % 6/10 + balls // 6)




# ===================================    Team one scorecard   ===========================================


def team1_score():

    team1he= tkinter.Label(frame3,text= team1.get() + " Score : " , fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    team1he.place(relx=0.1, rely = 0.4 , anchor="center")

    inrun()




# function for increasing  run

        
def inrun():

    team1run= tkinter.Label(frame3, text="0", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    team1run.place(relx=0.22, rely = 0.4 , anchor="center")

    slash= tkinter.Label(frame3, text=" /", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    slash.place(relx=0.25, rely = 0.4 , anchor="center")

    wicket1= tkinter.Label(frame3, text="0", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    wicket1.place(relx=0.3, rely = 0.4 , anchor="center")

    bracketon= tkinter.Label(frame3, text="( ", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    bracketon.place(relx=0.34, rely = 0.4 , anchor="center")

    overt1= tkinter.Label(frame3, text="0", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    overt1.place(relx=0.38, rely = 0.4 , anchor="center")

    bracketoff= tkinter.Label(frame3, text=" )", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    bracketoff.place(relx=0.42, rely = 0.4 , anchor="center")

    Run_1 = Button(frame3, text = "+ 1", style='R.TButton',command= lambda: team1run.config(text=str(int(team1run["text"]) + 1)))
    Run_1.place(relx = 0.1, rely = 0.5,anchor="center")

    Run_2 = Button(frame3, text = "+ 2", style='R.TButton',command= lambda: team1run.config(text=str(int(team1run["text"]) + 2)))
    Run_2.place(relx = 0.25, rely = 0.5,anchor="center")

    Run_3 = Button(frame3, text = "+ 3", style='R.TButton',command= lambda: team1run.config(text=str(int(team1run["text"]) + 3)))
    Run_3.place(relx = 0.4, rely = 0.5,anchor="center")

    Run_4 = Button(frame3, text = " + 4", style='R.TButton',command= lambda: team1run.config(text=str(int(team1run["text"]) + 4)))
    Run_4.place(relx = 0.15, rely = 0.58,anchor="center")

    Run_6 = Button(frame3, text = "+ 6", style='R.TButton',command= lambda: team1run.config(text=str(int(team1run["text"]) + 6)))
    Run_6.place(relx = 0.35, rely = 0.58,anchor="center")

    Run_wide = Button(frame3, text = "         WIDE / NOBALL         ", style='R.TButton',command= lambda: team1run.config(text=str(int(team1run["text"]) + 1)))
    Run_wide.place(relx = 0.25, rely = 0.66,anchor="center")

    wicket_1 = Button(frame3, text = "Wicket", style='R.TButton',command= lambda: wicket1.config(text=str(int(wicket1["text"]) + 1)))
    wicket_1.place(relx = 0.15, rely = 0.74,anchor="center")

    ball_1 = Button(frame3, text = "+1 Ball", style='R.TButton',command= lambda: overt1.config(text=str(overs(balls(overt1["text"]) + 1))))
    ball_1.place(relx = 0.35, rely = 0.74,anchor="center")




    # Calling for next inning ========

    Run_wide = Button(frame3, text = " Inning End", style='R.TButton',command= team2_score)
    Run_wide.place(relx = 0.25, rely = 0.82,anchor="center")





# ===================================    Team Two scorecard   ===========================================


def team2_score():
    team1he= tkinter.Label(frame3,text= team2.get() + " Score : " , fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    team1he.place(relx=0.59, rely = 0.4 , anchor="center")

    inrun2()


# function for increasing  run
        
def inrun2():

    team2run= tkinter.Label(frame3, text="0", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    team2run.place(relx=0.71, rely = 0.4 , anchor="center")

    slash1= tkinter.Label(frame3, text=" /", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    slash1.place(relx=0.76, rely = 0.4 , anchor="center")

    wicket2= tkinter.Label(frame3, text="0", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    wicket2.place(relx=0.81, rely = 0.4 , anchor="center")

    bracketon= tkinter.Label(frame3, text="( ", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    bracketon.place(relx=0.85, rely = 0.4 , anchor="center")

    overt2= tkinter.Label(frame3, text="0", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    overt2.place(relx=0.89, rely = 0.4 , anchor="center")

    bracketoff= tkinter.Label(frame3, text=" )", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
    bracketoff.place(relx=0.93, rely = 0.4 , anchor="center")

    Run_1 = Button(frame3, text = "+ 1", style='R.TButton',command= lambda: team2run.config(text=str(int(team2run["text"]) + 1)))
    Run_1.place(relx = 0.58, rely = 0.5,anchor="center")

    Run_2 = Button(frame3, text = "+ 2", style='R.TButton',command= lambda: team2run.config(text=str(int(team2run["text"]) + 2)))
    Run_2.place(relx = 0.74, rely = 0.5,anchor="center")

    Run_3 = Button(frame3, text = "+ 3", style='R.TButton',command= lambda: team2run.config(text=str(int(team2run["text"]) + 3)))
    Run_3.place(relx = 0.9, rely = 0.5,anchor="center")

    Run_4 = Button(frame3, text = " + 4", style='R.TButton',command= lambda: team2run.config(text=str(int(team2run["text"]) + 4)))
    Run_4.place(relx = 0.63, rely = 0.58,anchor="center")

    Run_6 = Button(frame3, text = "+ 6", style='R.TButton',command= lambda: team2run.config(text=str(int(team2run["text"]) + 6)))
    Run_6.place(relx = 0.83, rely = 0.58,anchor="center")

    Run_wide = Button(frame3, text = "         WIDE / NOBALL         ", style='R.TButton',command= lambda: team2run.config(text=str(int(team2run["text"]) + 1)))
    Run_wide.place(relx = 0.73, rely = 0.66,anchor="center")

    wicket_1 = Button(frame3, text = "Wicket", style='R.TButton',command= lambda: wicket2.config(text=str(int(wicket2["text"]) + 1)))
    wicket_1.place(relx = 0.63, rely = 0.74,anchor="center")

    ball_1 = Button(frame3, text = "+1 Ball", style='R.TButton',command= lambda: overt2.config(text=str(overs(balls(overt2["text"]) + 1))))
    ball_1.place(relx = 0.83, rely = 0.74,anchor="center")




    # Calling for next inning ========

    Run_wide = Button(frame3, text = " Inning End", style='R.TButton',command= team1_score)
    Run_wide.place(relx = 0.73, rely = 0.82,anchor="center")




# Selecting Teams

name1= tkinter.Label(frame3,text="Team 1", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
name1.place(relx=0.1, rely = 0.15 , anchor="center")

name2= tkinter.Label(frame3,text="Team 2", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
name2.place(relx=0.9, rely = 0.15 , anchor="center")

team1 = Entry(frame3)
team1.place(relx = 0.1, rely = 0.2,anchor="center")

team2 = Entry(frame3)
team2.place(relx = 0.9, rely = 0.2,anchor="center")

enterteam = Button(frame3, text ="Confirm team Names", style='S.TButton', command= ent_team)
enterteam.place(relx = 0.5, rely = 0.2,anchor="center")

line2 = tkinter.Label(frame3,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line2.place(relx=0.5, rely = 0.25 , anchor="center")


# Toss Section 

toss= tkinter.Label(frame3,text="Toss : ", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
toss.place(relx=0.1, rely = 0.3 , anchor="center")

tosst1 = Button(frame3, text = "TEAM 1", style='D.TButton', command=wontoss1)
tosst1.place(relx = 0.22, rely = 0.3,anchor="center")

tosst2 = Button(frame3, text = "TEAM 2", style='D.TButton',command=wontoss2)
tosst2.place(relx = 0.38, rely = 0.3,anchor="center")


choose= tkinter.Label(frame3,text="First Batting : ", fg='#6F0545', font=("Segoe UI", 16),bg="#ECF0F3")
choose.place(relx=0.55, rely = 0.3 , anchor="center")

choosebat_team1 = Button(frame3, text = "Team 1", style='D.TButton', command=team1_score)
choosebat_team1.place(relx = 0.7, rely = 0.3,anchor="center")

choosebat_team2 = Button(frame3, text = "Team 2", style='D.TButton', command= team2_score)
choosebat_team2.place(relx = 0.86, rely = 0.3,anchor="center")

line3 = tkinter.Label(frame3,text="----------------------------------------------------------------------------------------------------------------------", fg='grey',bg="#ECF0F3" )
line3.place(relx=0.5, rely = 0.35 , anchor="center")



bn = Button(frame3, text ="Home", style='N.TButton' , command= lambda: show_frame(frame1))
bn.place(relx = 0.5, rely = 0.95,anchor="center")




# ============================================= Frame four Code (Scorecard Screen) ================================================


scorehead= tkinter.Label(frame4,text="Full Scorecard", fg='#8B298E', font=("Segoe UI", 30),bg="#ECF0F3")
scorehead.place(relx=0.5, rely = 0.05 , anchor="center")

line1 = tkinter.Label(frame4,text="----------------------------------------------------------------------------------------------------------------------", fg='black',bg="#ECF0F3" )
line1.place(relx=0.5, rely = 0.1 , anchor="center")

disp1= tkinter.Label(frame4,text="    CSK vs RCB [IPL T20]", fg='#F89D6D', font=("Segoe UI", 16),bg="#ECF0F3")
disp1.place(relx=0.5, rely = 0.15 , anchor="center")

scocsk= tkinter.Label(frame4,text="    CSK 191/4 (20)", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
scocsk.place(relx=0.0, rely = 0.2 , anchor="w")

scorcb= tkinter.Label(frame4,text="    RCB 108/9 (18.4)", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
scorcb.place(relx=0.0, rely = 0.25 , anchor="w")

need= tkinter.Label(frame4,text="     RCB needs 84 runs in 8 balls", fg='#F71130', font=("Segoe UI", 12),bg="#ECF0F3")
need.place(relx=0.5, rely = 0.25 , anchor="center")

line1 = tkinter.Label(frame4,text="----------------------------------------------------------------------------------------------------------------------", fg='black', bg="#ECF0F3" )
line1.place(relx=0.5, rely = 0.3 , anchor="center")

bat= tkinter.Label(frame4,text="       Batter             ", fg='#707070', font=("Segoe UI", 10),bg="#A19D9D",)
bat.place(relx=0.0, rely = 0.35 , anchor="w")

pla1= tkinter.Label(frame4,text="Ruturaj Gaikwad            c Jamieson b Chahal          Run: 33       Ball: 25", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
pla1.place(relx=0.15, rely = 0.4 , anchor="w")

pla2= tkinter.Label(frame4,text="Faf du Plessis                c Christian b Harshal           Run: 50       Ball: 41", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
pla2.place(relx=0.15, rely = 0.45 , anchor="w")

pla3= tkinter.Label(frame4,text="Shuresh Raina               c Padikkal b Harshal           Run: 24       Ball: 18", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
pla3.place(relx=0.15, rely = 0.5 , anchor="w")

pla4= tkinter.Label(frame4,text="A. Rayudu                      c Jamieson b Harshal          Run: 14       Ball: 07", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
pla4.place(relx=0.15, rely = 0.55 , anchor="w")

pla5= tkinter.Label(frame4,text="Ravi Jadeja                        Not out                             Run: 62       Ball: 28", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
pla5.place(relx=0.15, rely = 0.6 , anchor="w")

pla6= tkinter.Label(frame4,text="M.S. Dhoni                        Not out                             Run: 02       Ball: 03", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
pla6.place(relx=0.15, rely = 0.65 , anchor="w")

line1 = tkinter.Label(frame4,text="----------------------------------------------------------------------------------------------------------------------", fg='black', bg="#ECF0F3" )
line1.place(relx=0.5, rely = 0.7 , anchor="center")

extra= tkinter.Label(frame4,text="Extras                                                          6 (b 0, lb 1, w 3, nb 2, p 0)", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
extra.place(relx=0.15, rely = 0.75 , anchor="w")

total= tkinter.Label(frame4,text="Total                                                              191 (4 wkts, 20 Ov)", fg='#061625', font=("Segoe UI", 14),bg="#ECF0F3")
total.place(relx=0.15, rely = 0.8 , anchor="w")


bn1 = Button(frame4, text ="Back", style='N.TButton' , command= lambda: show_frame(frame2))
bn1.place(relx = 0.3, rely = 0.9,anchor="e")

bn2 = Button(frame4, text ="Home", style='N.TButton' , command= lambda: show_frame(frame1))
bn2.place(relx = 0.7, rely = 0.9,anchor="w")


# Function Calls

show_frame(frame1)

tkinter.mainloop()
