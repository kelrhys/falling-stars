'''
Created on Nov 2, 2018

@author: Rebecca
'''

class GameObject:
    '''
    Superclass/interface for canvas game objects. Provides interface for 
    getting canvas object id, movement updates and collision handling.
    '''
    def __init__(self, canvas, width, height, mywidth, myheight):
        self.canvas = canvas
        self.canvas_width = width
        self.canvas_height = height
        self.width = mywidth
        self.height = myheight
        self.objID = None
        print('GameObject init')

    def add(self):
        # Display gameobject
        return True
        
    def displayed(self):
        return self.objID
    
    def getID(self):
        """ Returns canvas object ID or list of IDs as needed """
        return self.objID
    
    def move(self, x, y):
        self.canvas.move(self.objID, x, y)
        
    def update(self):
        """ Updates object state and/or position on canvas """
        return True
            
    def handleCollision(self):
        """ Performs actions required when game detects collision with this object.
        Return True if object actually collided, False otherwise """
        return True
