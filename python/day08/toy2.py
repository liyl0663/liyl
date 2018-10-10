class vendor:
    def __init__(self,phone,mail):
        self.phone = phone
        self.mail = mail

class BearToy:
    def __init__(self,nm,size,color,phone,mail):
        self.name = nm
        self.size = size
        self.color = color
        self.cj = vendor(phone,mail)
    def sing(self):
        print('%s lalala' % self.name)

if __name__ == '__main__':
    tadi = BearToy('tadi','middle','green','123456789','tadi@tedu.cn')
    print(tadi.name,tadi.size,tadi.cj.phone)

