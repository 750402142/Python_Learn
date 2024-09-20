
class Record:

    def __init__(self,date,id_cord,money,province):
        self.date = date
        self.id_cord = id_cord
        self.money = money
        self.province = province
    def __str__(self):
        return f"{self.date},{self.id_cord},{self.money},{self.province}"