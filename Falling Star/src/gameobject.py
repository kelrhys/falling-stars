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
        raise RuntimeError('add method has not been implemented')
                
    def displayed(self):
        return self.objID
    
    def getID(self):
        """ Returns canvas object ID """
        return self.objID
    
    def update(self):
        """ Updates object state and/or position on canvas """
        raise RuntimeError('update method has not been implemented')
            
    def handleCollision(self):
        """ Performs actions required when game detects collision with this object.
        Return True if object actually collided, False otherwise """
        raise RuntimeError('handleCollision method has not been implemented')
