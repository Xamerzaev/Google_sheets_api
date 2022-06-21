from core import db

class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column (db.Integer(), primary_key=True) #ИД столбца
    order  = db.Column (db.Integer(), nullable = False) # НОМЕР ЗАКАЗА
    dollar  = db.Column (db.Integer(), nullable = False) # СТОИМОСТЬ В ДОЛЛАРАХ
    supply  = db.Column (db.DateTime(), nullable = False) # СРОКИ ПОСТАВКИ

    def __init__(self, order, dollar, supply):
        self.order = order
        self.dollar = dollar
        self.supply = supply

    def __repr__(self):
        return self.order
