'''
Created on Nov 2, 2018

@author: Rebecca
'''
import random
import time
import tkinter as tk
import gameobject as g
import gametimer as t

class Shield(g.GameObject, t.GameTimer):
    '''
    Shield canvas object. Subclasses GameObject to provide canvas object ID,
    movement updates and collision handling.
    '''

    def __init__(self, canvas, width, height):
        '''
        Constructor
        '''
        g.GameObject.__init__(self, canvas, width, height, mywidth=50, myheight=50)
        t.GameTimer.__init__(self)
        
    def add(self):
        xoff = random.randint(0, self.canvas_width-self.width)
        yoff = random.randint(0, self.canvas_height-self.height)
        '''
        self.objID = self.canvas.create_polygon(0+xoff, 5+yoff, self.width/2+xoff, 0+yoff, self.width+xoff, 5+yoff, self.width/2+xoff, self.height+yoff,
                                       outline='white', fill='gold')
        '''
        self.shieldImage = tk.PhotoImage(file="../img/goldshield.gif")
        self.objID = self.canvas.create_image(xoff, yoff, image=self.shieldImage, anchor=tk.NW)
        
        self.uptime = random.randint(1, 10)
        print('Displaying shield for {} seconds at {},{}'.format(self.uptime, xoff, yoff))
        self.start_time = time.time()
            
    def update(self):
        """ Handle shield display and activation expiration. Returns
        True if activation has expired, False otherwise """
        expired = self.setExpiration(self.displayed)
        if expired:
            self.canvas.delete(self.objID)
            self.objID = None
            print('Deleted shield')
            return False
                
        expired = self.setExpiration(self.isActive)
        if expired:
            print('Deactivated shield')
        
        return expired
            
    def handleCollision(self):
        """ Deletes shield image and starts shield activation timer. Return True """
        self.canvas.delete(self.objID)
        self.objID = None
        self.uptime = random.randint(1, 10)
        print('Activating shield for {} seconds'.format(self.uptime))
        return self.setActive()
    
