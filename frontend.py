import pygame
from tkinter import *
pygame.init()
un = pygame.image.load("frontend_prog/assets/font/1.png")
deux = pygame.image.load("frontend_prog/assets/font/2.png")
trois = pygame.image.load("frontend_prog/assets/font/3.png")
quatre = pygame.image.load("frontend_prog/assets/font/4.png")
cinq = pygame.image.load("frontend_prog/assets/font/5.png")
siix = pygame.image.load("frontend_prog/assets/font/6.png")
sept = pygame.image.load("frontend_prog/assets/font/7.png")
huit = pygame.image.load("frontend_prog/assets/font/8.png")
neuf = pygame.image.load("frontend_prog/assets/font/9.png")
null = pygame.image.load("frontend_prog/assets/font/0.png")
percent = pygame.image.load("frontend_prog/assets/font/percent.png")
gpa=0
sat=0
act=0
volunteer=0
mathgrade = ""
scigrade = ""
enggrade = ""
apcourses = 0
honorscourses = 0
extracurriculars = 0
country = ""
lang = 0
root=Tk()
root.title("College Calculator")
label_1 = Label(root,text="Answer all the questions to get a percent chance of getting into college.")
label_1.pack()
GPA_label = Label(root,text="GPA (1-4)")
GPA_label.pack()
GPA_entry = Entry(root)
GPA_entry.pack()
SAT_label = Label(root,text="SAT score (0-1600)")
SAT_label.pack()
SAT_entry = Entry(root)
SAT_entry.pack()
ACT_label = Label(root,text="ACT score (0-34)")
ACT_label.pack()
ACT_entry = Entry(root)
ACT_entry.pack()
Volunteer_label = Label(root,text="Number of Volunteer Hours (0-200)")
Volunteer_label.pack()
Volunteer_entry = Entry(root)
Volunteer_entry.pack()
Mathgrade_label = Label(root,text="Math grade (A-F)")
Mathgrade_label.pack()
Mathentry = Entry(root)
Mathentry.pack()
Scilabel = Label(root,text="Science grade (A-F)")
Scilabel.pack()
Scientry = Entry(root)
Scientry.pack()
Englabel = Label(root,text="English grade (A-F)")
Englabel.pack()
Engentry = Entry(root)
Engentry.pack()
worldlabel = Label(root,text="World language years")
worldlabel.pack()
Worldentry = Entry(root)
Worldentry.pack()
APlabel = Label(root,text="Number of AP courses taken")
APlabel.pack()
APentry = Entry(root)
APentry.pack()
Honorslabel = Label(root,text="Number of Honors courses taken")
Honorslabel.pack()
Honorsentry = Entry(root)
Honorsentry.pack()
extralabel = Label(root,text="Number of extracurriculars")
extralabel.pack()
Extraentry = Entry(root)
Extraentry.pack()
countrylabel = Label(root,text="Country of Origin")
countrylabel.pack()
Countryentry = Entry(root)
Countryentry.pack()
la = []
def submit():
    la.append(float(GPA_entry.get()))
    la.append(int(SAT_entry.get()))
    la.append(int(ACT_entry.get()))
    la.append(int(Volunteer_entry.get()))
    la.append(Mathentry.get())
    la.append(Scientry.get())
    la.append(Engentry.get())
    la.append(int(Worldentry.get()))
    la.append(int(APentry.get()))
    la.append(int(Honorsentry.get()))
    la.append(int(Extraentry.get()))
    la.append(Countryentry.get())
    root.destroy()
    
Submit_button = Button(root,text="Submit",fg="green",command=submit)
Submit_button.pack()
root.mainloop()
gpa = la[0]
sat = la[1]
act = la[2]
volunteer = la[3]
mathgrade = la[4]
scigrade = la[5]
enggrade = la[6]
lang = la[7]
apcourses = la[8]
honorscourses = la[9]
extracurriculars = la[10]
country = la[11]
with open("frontend_prog/Recentdata.txt") as f:
    for i in la:
        j = str(i)
        f.write(j+"\n")
f.close()
gpa = gpa*1600
act = act*200
sat = sat*4
detractit = 0
if mathgrade != "A":
    detractit = detractit + 2000
if mathgrade == "C" or mathgrade == "D" or mathgrade == "F":
    detractit = detractit + 4000
if scigrade != "A":
    detractit = detractit + 2000
if scigrade == "C" or scigrade == "D" or scigrade == "F":
    detractit = detractit + 4000
if enggrade != "A":
    detractit = detractit + 2000
if enggrade == "C" or enggrade == "D" or enggrade == "F":
    detractit = detractit + 4000
apcourses = apcourses * 2000
if apcourses<3:
    detractit = detractit + 2000
honorscourses = honorscourses * 750
if honorscourses<3:
    detractit = detractit + 400
extracurriculars = extracurriculars * 1000
chance = (gpa+sat+act+volunteer+extracurriculars+apcourses+honorscourses-detractit)/40000
chance = chance * 100
chance = int(chance)
if chance > 100:
    chance = 100
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Calculator")
def displaychance(chancre,x,y):
    offset = 0
    for i in str(chancre):
        if i == "1":
            screen.blit(un,(x+offset,y))
        if i == "2":
            screen.blit(deux,(x+offset,y))
        if i == "3":
            screen.blit(trois,(x+offset,y))
        if i == "4":
            screen.blit(quatre,(x+offset,y))
        if i == "5":
            screen.blit(cinq,(x+offset,y))
        if i == "6":
            screen.blit(siix,(x+offset,y))
        if i == "7":
            screen.blit(sept,(x+offset,y))
        if i == "8":
            screen.blit(huit,(x+offset,y))
        if i == "9":
            screen.blit(neuf,(x+offset,y))
        if i == "0":
            screen.blit(null,(x+offset,y))
        offset = offset + 48
    screen.blit(percent,(x+offset,y))
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    displaychance(chance,100,100)
    pygame.display.update()
    
    
