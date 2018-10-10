class Data:
    def __init__(self,year,month,date):
        self.year = year
        self.month = month
        self.date = date

    @classmethod
    def create_date(cls,str_date):
        year,month,date = map(int,str_date.split('-'))
        return cls(year,month,date)
    @staticmethod
    def is_date_valid(str_date):
        year,month,date = map(int,str_date.split('-'))
        return year < 4000 and 0 < month < 13 and 0 < date < 32

if __name__ == '__main__':
    print(Data.is_date_valid('4000-10-2'))
    d2 = Data.create_date('2018-10-1')
    print(d2.year,d2.month,d2.date)