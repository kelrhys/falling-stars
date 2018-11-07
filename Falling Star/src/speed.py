'''
Created on Nov 2, 2018

@author: Rebecca
'''
import random
import time
import gameobject as g
import gametimer as t

class Speed(g.GameObject, t.GameTimer):
    '''
    Speed (lightning) canvas object. Subclasses GameObject to provide canvas object ID,
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
        self.objID = self.canvas.create_polygon(.15*self.width+xoff, .4*self.height+yoff, self.width+xoff, 0+yoff, 
                                                .7*self.width+xoff, .30*self.height+yoff, .95*self.width+xoff, .25*self.height+yoff,
                                                .7*self.width+xoff, .50*self.height+yoff, .95*self.width+xoff, .45*self.height+yoff,
                                                0+xoff, self.height+yoff, .45*self.width+xoff, .55*self.height+yoff,
                                                .1*self.width+xoff, .65*self.height+yoff, .4*self.width+xoff, .4*self.height+yoff,
                                                outline='orange', fill='gold', width=2)
        self.uptime = random.randint(1, 10)
        print('Displaying speed for {} seconds'.format(self.uptime))
        self.start_time = time.time()
            
    def update(self):
        """ Handle speed display and activation expiration. Returns
        True if speed activation has expired, False otherwise """
        expired = self.setExpiration(self.displayed)
        if expired:
            self.canvas.delete(self.objID)
            self.objID = None
            print('Deleted speed')
            return False
        
        expired = self.setExpiration(self.isActive)
        if expired:
            print('Deactivated speed')
            
        return expired
    
    def handleCollision(self):
        """ Deletes speed image and starts speed activation timer. Return True """
        self.canvas.delete(self.objID)
        self.objID = None
        self.uptime = random.randint(1, 10)
        print('Activating speed for {} seconds'.format(self.uptime))
        return self.setActive()
    
