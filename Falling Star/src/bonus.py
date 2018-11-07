'''
Created on Nov 2, 2018

@author: Rebecca
'''
import random
import gameobject as g
import gametimer as t

class Bonus(g.GameObject, t.GameTimer):
    '''
    Rectangular canvas object with 'Bonus' text label. Subclasses GameObject to
    provide canvas object ID, movement updates and collision handling.
    '''

    def __init__(self, canvas, width, height):
        '''
        Constructor
        '''
        g.GameObject.__init__(self, canvas, width, height, mywidth=50, myheight=50)
        t.GameTimer.__init__(self)
        self.bonusTag = 'btag'
        self.uptime = 3
        self.add()
        
    def add(self):
        # Create objID object with embedded text label
        self.objID = self.canvas.create_rectangle(self.canvas_width/2, self.canvas_height/2, self.canvas_width/2+self.width,  self.canvas_height/2+self.height/2,
                                     outline='gold', fill='gold')
        self.canvas.create_text(self.canvas_width/2+5, self.canvas_height/2+5, text='Bonus', font=('Helvetica', '10'), anchor='nw')
        self.canvas.addtag_overlapping(self.bonusTag, self.canvas_width/2, self.canvas_height/2, self.canvas_width/2+self.width,  self.canvas_height/2+self.height/2)
            
    def update(self):
        """ updates bonus object position on canvas """
        # Reset to normal color after "flashing" during collision
        self.canvas.itemconfigure(self.objID, outline='gold', fill='gold')
        
        self.setExpiration(self.isActive)
            
        # Move across screen from right to left
        self.canvas.move(self.bonusTag, -3, 0)
        
        # After reaching left side of canvas, reset to right side
        if (self.canvas.bbox(self.objID)[0] <= 0):
            bonus_bbox = self.canvas.bbox(self.objID)
            y = random.randint(-bonus_bbox[1], self.canvas_width-bonus_bbox[3]-self.height/2)
            self.canvas.move(self.bonusTag, self.canvas_width-self.width, y)
            
    def handleCollision(self):
        """ Returns True if not already active, False otherwise """
        activated = self.setActive()
        if activated:
            # "Flash" objID object to indicate activation
            self.canvas.itemconfigure(self.objID, outline='white', fill='white')
        return activated
        