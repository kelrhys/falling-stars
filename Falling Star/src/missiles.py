'''
Created on Nov 8, 2018

@author: Rebecca
'''
import gameobject as g

class Missiles(g.GameObject):
    '''
    Missiles canvas object. Subclasses GameObject to provide canvas object ID,
    movement updates and collision handling.
    '''

    def __init__(self, canvas, width, height):
        '''
        Constructor
        '''
        super().__init__(canvas, width, height, mywidth=3, myheight=8)
        self.objList = []
        self.distance = -5
    
    def add(self, x, y):
        """ Add a missile at specified coordinates. """
        missile = self.canvas.create_rectangle(x, y, self.width+x, self.height+y, 
                                       outline='white', fill='grey')
        self.objList.append(missile)
    
    def remove(self, objID):
        self.canvas.delete(objID)
        self.objList.remove(objID)
                   
    def getID(self):
        """ Returns list of canvas object IDs """
        return self.objList
            
    def update(self):
        """ Move missiles up on screen. If it reaches top of screen, delete """      
        for item in self.objList:
            self.canvas.move(item, 0, self.distance)
            item_bbox = self.canvas.bbox(item)
            if (item_bbox[1] <= 0):
                self.remove(item)
            
    def handleCollision(self):
        """ Returns True """
        return True

    
    