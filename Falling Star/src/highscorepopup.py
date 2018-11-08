'''
Created on Nov 1, 2018

@author: Rebecca
'''
import json
import os
import tkinter as tk
from tkinter import ttk

class HighScorePopup:
    '''
    Display final score and top 10 list in a popup window. Prompt user for name
    if score makes the top 10 list, and allow user to choose to restart or quit game.
    
    '''
    def load_scores(self):
        try:
            with open(self.folder+self.filename, 'r') as f:
                self.highscores = json.load(f)
                print('High score list loaded')
        except IOError as e:
            print('Error opening high score file: {}'.format(e))
    
    def save_scores(self):
        try:
            with open(self.folder+self.filename, 'w') as f:
                json.dump(self.highscores, f)
                print('High score list saved')
        except IOError as e:
            print('Error opening high score file: {}'.format(e))
        
    def __init__(self, root, close_callback, restart_callback, score, fn='fallingstar.highscores.json'):
        '''
        Constructor
        '''
        self.close_callback = close_callback
        self.restart_callback = restart_callback
        self.finalscore = score
        self.folder = "data/"
        self.filename = fn
        self.highscores = []
        
        os.makedirs(self.folder, exist_ok=True)
        self.load_scores()
        self.show(root)
        
    def show(self, root):
        self.window = tk.Toplevel()
        self.window.title('Game Over')
        self.window.transient(root)
        self.window.geometry('371x165')
    
        hs = tk.Text(self.window, height=10, width=25)
    
        def topscores():
            """ returns list of top ten scores """
            scoreList = []
            for entry in self.highscores:
                scoreList.append(entry['score'])
            return scoreList
                
        def showscores():
            # text.delete index=line.column
            hs.delete(1.0, tk.END)
            for i, entry in enumerate(self.highscores):
                hs.insert(tk.END, '{0: >3}: {1: >15} {2:04d}'.format(i+1, entry['name'], entry['score']))
    
        def add_score(name, score):           
            numscores = len(self.highscores)
            if numscores > 0:
                for i, entry in enumerate(self.highscores):
                    if entry['score'] < score:
                        print('inserting {} at index {}'.format({'score': score, 'name': name}, i))
                        self.highscores.insert(i, {'score': score, 'name': name})
                        # Cut number 11 from list if necessary
                        if numscores == 10:
                            del(self.highscores[10])
                        break
                else:
                    # Exited loop without break, so new score is less than all current entries.
                    # Add new score at end of list
                    print('appending {} to existing list'.format({'score': score, 'name': name}))
                    self.highscores.append({'score': score, 'name': e.get()})
            else:
                print('appending {} to empty list'.format({'score': score, 'name': name}))
                self.highscores.append({'score': score, 'name': name})
            
            self.save_scores()
            showscores()
    
        m = tk.Label(self.window, text='Final Score: {}'.format(self.finalscore), width=15)
        m.config(font=('times', 12, 'bold'))
        m.grid(row=1, column=1, columnspan=2)
    
        if len(self.highscores) < 10 or self.finalscore > min(topscores()):
            msg = tk.Message(self.window, text='You have achieved a place on the High Scores List!', aspect=400)
            msg.grid(row=2, column=1, columnspan=2)
            
            l = ttk.Label(self.window, text='Enter name:')
            l.grid(row=3, column=1)
            e = ttk.Entry(self.window, width=13)
            e.grid(row=3, column=2)
            e.focus()
            b = ttk.Button(self.window, text='Add score', width=12, command=lambda:[b.state(["disabled"]),add_score(e.get(), self.finalscore)])
            b.grid(row=4, column=1)
            
        p = ttk.Button(self.window, text='Play Again', width=12, command=lambda:[self.window.destroy(), self.restart_callback()])
        p.grid(row=5, column=1)
        # Without calling callback within lambda, it executes immediately upon loading which is broken!
        q = ttk.Button(self.window, text='Quit', width=12, command=lambda:[self.close_callback()])
        q.grid(row=5, column=2)
    
        hs.grid(row=1, column=3, rowspan=5)
    
        if len(self.highscores) > 0:
            showscores()
        else:
            hs.insert(tk.END, 'High scores list is empty')
            
    def close(self):
        self.window.destroy()
        
def test():
    root = tk.Tk()


    hs = HighScorePopup(root, None, None, 100, fn='test.json')
    assert(len(hs.highscores) == 0)
    assert(hs.finalscore == 100)
    os.remove('test.json')
    
if __name__ == '__main__':
    test()

    
        
        
        
        