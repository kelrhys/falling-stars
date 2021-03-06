'''
Created on Nov 2, 2018

@author: Rebecca
'''
import random
import gameobject as g

class Stars(g.GameObject):
    '''
    Stars canvas object. Subclasses GameObject to provide canvas object ID,
    movement updates and collision handling.
    '''

    def __init__(self, canvas, width, height):
        '''
        Constructor
        '''
        super().__init__(canvas, width, height, mywidth=40, myheight=40)
        self.objList = []
    
    def create(self, color):
        """ Create 5-point star """
        factor=5
        star = self.canvas.create_polygon(self.width/2, 0, self.width/2+factor, self.height/2-factor,
                                    self.width, self.height/2-factor, self.width/2+factor, self.height/2+factor,
                                    (self.width/4)*3+factor, self.height, self.width/2, (self.height/4)*3,
                                    self.width/4-factor, self.height, self.width/2-factor, self.height/2+factor,
                                    0, self.height/2-factor, self.width/2-factor, self.height/2-factor,
                                    outline='white', fill=color)
        return star

    def add(self, color):
        """ Add a star with specified color to top of screen. Stars are placed randomly across top of screen. """
        star = self.create(color)
        self.objList.append(star)
    
        x = random.randint(0, self.canvas_width-self.width)
        self.canvas.move(star, x, 0)
               
    def remove(self, objID):
        self.canvas.delete(objID)
        self.objList.remove(objID)
        
    def getID(self):
        """ Returns list of canvas object IDs """
        return self.objList
            
    def update(self):
        """ Drop stars; if star reaches bottom of screen, move star to top of screen
        Returns the number of stars that reached bottom of screen """
        reached_bottom = 0
        for star in self.objList:
            self.canvas.move(star, 0, random.randint(1,5))
            star_bbox = self.canvas.bbox(star)
            if (star_bbox[3] >= self.canvas_height):
                x = random.randint(-star_bbox[0], self.canvas_width-star_bbox[2]-self.width)
                self.canvas.move(star, x, -self.canvas_height)
                reached_bottom += 1
        return reached_bottom
            
    def handleCollision(self):
        """ Returns True """
        return True

    