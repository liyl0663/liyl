class BearToy:
    def __init__(self,nm,size,color):
        self.name = nm
        self.size = size
        self.color = color
    def sing(self):
        print('I am %s,lalala' % self.name)
class NewBearToy(BearToy):
    def __init__(self,nm,size,color,material):
        super(NewBearToy,self).__init__(nm,size,color)
        self.material = material
    def run(self):
        print('Running...')
    def sing(self):
        print('Wow~~~')

if __name__ == '__main__':
    b1 = NewBearToy('xionge','Large','Brown','cotton')
    print(b1.material)
    b1.sing()
    b1.run()
