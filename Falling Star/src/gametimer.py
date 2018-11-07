'''
Created on Nov 2, 2018

@author: Rebecca
'''
import time

class GameTimer:
    '''
    Superclass for game timer.
    '''
    def __init__(self):
        self.uptime = 0
        self.start_time = None
        self.active = False
        print('GameTimer init')

    def isActive(self):
        return self.active
    
    def setExpiration(self, expirationMethod):
        """ Returns True if active time has expired, False otherwise """
        if expirationMethod():
            elapsed = time.time() - self.start_time
            if elapsed > self.uptime:
                self.active = False
                return True
        return False
        
    def setActive(self):
        """ Returns True if not already active, False otherwise """
        if not self.isActive():
            self.active = True
            self.start_time = time.time()
            return True
        else:
            return False