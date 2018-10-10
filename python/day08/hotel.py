class Hotel:
    def __init__(self,room=200,cf=1.0,br=15):
        self.room = room
        self.cf = cf
        self.br = br
    def cacl(self,days=1):
        return (self.room * self.cf + self.br) * days

if __name__ == '__main__':
    std_room =  Hotel()
    print(std_room.cacl())
    print(std_room.cacl(2))
    big_room = Hotel(room=230,cf = 0.9)
    print(big_room.cacl())
    print(big_room.cacl(2))