#george was here
#tanner was here
#mira was here

class tile():
    
    def __init__(self, x ,y, passable):
        self.xint = x
        self.yint = y
        self.passablebool = passable

class entrance():
    def __init__(self, border ,tiles):
        
        self.tilesarray = tiles 
        self.borderval = border 

class abstractTile():
    
    def __init__(self, tiles, entrances):

        self.tilesarry= tiles 
        self.entrancesarray = entrance


## does this work?
