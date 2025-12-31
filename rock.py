from tkinter import *
import random
rps = Tk()
rps.geometry("300x300")
rps.title("Rock Paper Scissor")

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def choice_to_number(choice):
    rps= {'rock':0, 'paper': 1, 'scissor':2}
    return rps[choice]

def number_to_choice(number):
    rps = {0:'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def result(human_choice,comp_choice):
    global user_score
    global comp_score
    user =choice_to_number(human_choice)
    comp= choice_to_number(comp_choice)
    if(user == comp): 
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        user_score += 1
    else:
        print("Computer wins")
        comp_score = comp_score + 1
    text_area= Text(master = rps, font= ("arial", 15, "italic bold"), relief= RIDGE, bg= "#033642", fg= "white", width=26)
    text_area.grid(column= 0, row =4)
    answer = "Your choice: {uc} \nComputer's Choice: {cc} \n Your Score: {u}\n  Computer Score: {c}".format(uc=user_choice,
                                                                                                         cc= comp_choice, u = user_score, c= comp_score)
    text_area.insert(END, answer)

def rock():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)



def paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)



def scissor():
    global user_choice
    global comp_choice
    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


button_rock= Button(text = "     ROCK        ",bg = "#808487", font= ("arial",15,"italic bold"), relief= RIDGE,
                    activebackground = "#05945B", activeforeground = "white", width = 24, command = rock)
button_rock.grid(column = 0, row =1 )
button_paper= Button(text = "     PAPER        ",bg = "#F2EECB", font= ("arial",15,"italic bold"), relief= RIDGE,
                    activebackground = "#05945B", activeforeground = "white", width = 24, command = paper)
button_paper.grid(column=0, row= 2)
button_scissor= Button(text = "     SCISSOR        ",bg = "#067D22", font= ("arial",15,"italic bold"), relief= RIDGE,
                    activebackground = "#05945B", activeforeground = "white", width = 24, command= scissor)
button_scissor.grid(column=0, row=3)

rps.mainloop()




