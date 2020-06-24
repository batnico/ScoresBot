import tingbot
from tingbot import *

# setup code here

screen.fill(color='black')
screen.text('Bienvenue sur l\'application ScoresBot',color='yellow',align='top',font_size=25)
screen.image("Pong.png", align="bottom", max_width=220, max_height=170)

state = {'scoreA' : 0, 'scoreB' : 0, 'colorA' : 'black', 'colorB' : 'black', 'fin' : 0}

@after(seconds=5)
def initialize():
    screen.fill(color='white')

    if state['fin']==1:
        if state['scoreB'] > state['scoreA']:
            state['colorB'] = 'blue'
            screen.text("--> a gagne !", xy=(160,170), color="red")
        elif state['scoreB'] < state['scoreA']:
            state['colorA'] = 'blue'
            screen.text("<-- a gagne !", xy=(160,170), color="red")
        else:
             screen.text("egalite !")
             
        screen.rectangle(xy=(150,220), size=(125,25), color="blue")
        screen.text("Rejouer !", xy=(160,220), font_size=15, color="white")
    else:
        screen.rectangle(xy=(150,220), size=(125,25), color="blue")
        screen.text("Fin du game !", xy=(160,220), font_size=15, color="white")
        
    screen.text("Score actuel", xy=(160,20), font_size=40, color="black")
    screen.text(state['scoreA'], xy=(80,120), font_size=95, color=state['colorA'])
    screen.line(start_xy=(160,50), end_xy=(160,200), color="black", width=5)
    screen.text(state['scoreB'], xy=(240,120), font_size=95, color=state['colorB'])
 
    screen.update()

    
@right_button.press
def on_right():
    state['scoreB'] = state['scoreB'] + 1
    initialize()
    
@left_button.press
def on_right():
    state['scoreA'] = state['scoreA'] + 1
    initialize()
    
@midright_button.press
def on_right():
    if state['scoreB'] > 0:
        state['scoreB'] = state['scoreB'] - 1
        initialize()
    
@midleft_button.press
def on_right():
    if state['scoreA'] > 0:
        state['scoreA'] = state['scoreA'] - 1
        initialize()

@touch(xy=(150,220), size=(125,30), align="left")
def on_touch(xy, action):
    if action == "down":
        if state["fin"] == 0:
            state["fin"] = 1
        else:
            state["fin"] = 0
            state["scoreA"] = 0
            state["scoreB"] = 0
            state["colorA"] = "black"
            state["colorB"] = "black"

        initialize()

tingbot.run()
