class World:
    def __init__(self,width,height):
        self.start_platform = Platform(self,250,15)



class Platform:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y


        

        