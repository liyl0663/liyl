class BearToy:
    def __init__(self,nm,size,color):
        self.name = nm
        self.size = size
        self.color = color
    def sing(self):
        print('I am %s,lalala' % self.name)

if __name__ == '__main__':
    tidy = BearToy('Tidy','Middle','White')
    print(tidy.size,tidy.color)
    big_bear = BearToy('xd','Large','Brown')
    print(big_bear.size,big_bear.color)
    tidy.sing()
    big_bear.sing()