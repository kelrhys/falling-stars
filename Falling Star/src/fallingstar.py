import tkinter as tk
import time
import random
import highscorepopup as hs
import bonus
import shield
import stars
import speed

""" TODO: 
Enhancements: checkin to github, shoot stars!?, try images, consecutive bonus bonus """

# Global declarations
root = tk.Tk()
root.title("Falling Star")
window_width = 400
window_height = 400
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canvas.pack()
score=0
running = True
bonusHandle = None
shieldHandle = None
starsHandle = None
speedHandle = None
ship = None
scoreText = None
default_speed = 5
fast_speed = 10
distance = default_speed

def setup():
    global bonusHandle, shieldHandle, starsHandle, speedHandle, ship, scoreText
    global running, score, distance
    running = True
    score=0
    distance=default_speed
    
    """ Create graphics objects and place them in initial starting positions """

    # Create initial stars 
    starsHandle = stars.Stars(canvas, window_width, window_height)
    for _ in range(3):
        starsHandle.add('blue')
            
    # Create bonus object 
    bonusHandle = bonus.Bonus(canvas, window_width, window_height)
    
    # Create ship
    ship_height=25
    ship_width=25
    ship_start_y=window_height-ship_height
    ship = canvas.create_polygon(ship_width/2, ship_start_y, ship_width, ship_height+ship_start_y, 0, ship_height+ship_start_y,
                                 outline='white', fill='green')
    
    # Create score
    scoreText = canvas.create_text(window_width-30, window_height-20, text='0', font=('Courier', '20'), fill="white")

    # Create shield handle for later use - does not display yet
    shieldHandle = shield.Shield(canvas, window_width, window_height)
    
    # Create speed handle for later use - does not display yet
    speedHandle = speed.Speed(canvas, window_width, window_height)
    
# Handle keyboard control of ship movement
def key(event):
    if not running:
        return
    
    if event.keysym == 'Up':
        if (canvas.coords(ship)[1] > 2):
            canvas.move(ship, 0, -distance)
    elif event.keysym == 'Down':
        if (canvas.coords(ship)[3] < window_height-2):
            canvas.move(ship, 0, distance)
    if event.keysym == 'Left':
        if (canvas.coords(ship)[4] > 2):
            canvas.move(ship, -distance, 0)
    if event.keysym == 'Right':
        if (canvas.coords(ship)[2] < window_width-2):
            canvas.move(ship, distance, 0)

# Handle closing application
def close_app():
    # app event loop state
    global running
    print('closing app')
    running = False
    root.destroy()

def restart_game():
    canvas.delete('all')
    setup()
    game_action_loop()

def get_collision():
    """ Returns list of object(s) ship collided with or False if no collision """
    coords = canvas.bbox(ship)
    overlap = canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])
    if len(overlap) == 1:
        # No collision - overlap always includes ship itself
        return False
    else:
        # return list of collided object IDs (not including ship)
        ship_index = overlap.index(ship)
        collisions = overlap[:ship_index] + overlap[ship_index+1:]
        return collisions

def game_action_loop():
    global score, running, distance
    
    drop_count=0
    sleep_time=.05
    
    # Game action loop
    while running:
        # Redraw canvas; update score and counter
        canvas.update()
        canvas.itemconfigure(scoreText, text=score)
        drop_count += 1

        # Randomly display shield 
        if drop_count % random.randint(1, 200) == 0:
            # Shield must not be displayed or actively protecting ship before adding new one
            if not shieldHandle.isActive() and not shieldHandle.displayed():
                shieldHandle.add()

        # update() returns True if ship shield protection has expired
        if shieldHandle.update():
            canvas.itemconfigure(ship, fill='green')
            
        # Randomly display lightning speed
        if drop_count % random.randint(1, 400) == 0:
            # Speed must not be displayed or active before adding new one
            if not speedHandle.isActive() and not speedHandle.displayed():
                speedHandle.add()

        # update() returns True if speed activation has expired
        if speedHandle.update():
            canvas.itemconfigure(ship, outline='white')
            distance = default_speed

        # Speed up object movement and add more stars
        # as game goes on, to make it get harder
        if drop_count % 200 == 0:
            starsHandle.add('red')
            if sleep_time > .0005:
                sleep_time -= .0005
        time.sleep(sleep_time)

        # Stars update() returns number of stars that reached bottom during update
        score += starsHandle.update()

        bonusHandle.update()
        
        # Handle collisions
        collidedList = get_collision()
        if collidedList:
            #print('Ship collided with {} - len: {}!'.format(collidedList, len(collidedList)))

            if bonusHandle.getID() in collidedList and not bonusHandle.isActive():
                bonusHandle.handleCollision()
                print('Collided with bonus - score 10 points!')
                score += 10
                
            if shieldHandle.getID() in collidedList:
                shieldHandle.handleCollision()
                # Change ship to silver while shield activated
                canvas.itemconfigure(ship, fill='silver')
                
            if speedHandle.getID() in collidedList:
                speedHandle.handleCollision()
                # Change ship outline to orange while shield activated
                canvas.itemconfigure(ship, outline='orange')
                distance = fast_speed
                
            for star in starsHandle.getID():
                if star in collidedList and not shieldHandle.isActive() :
                    running = False
                    # Game loop will exit here because new toplevel window is created
                    """ Display final score and top 10 list in a popup window. Prompt user for name
                    if score makes the top 10 list, and allow user to choose to restart or quit game. """
                    hs.HighScorePopup(root, close_app, restart_game, score)

""" Main code execution """
# Setup game
setup()

# Register for application close event
root.protocol("WM_DELETE_WINDOW", close_app)
# Register for key press events
root.bind("<Key>", key)

# Start game
game_action_loop()

# tkinter loop for handling mouse and key events
root.mainloop()
