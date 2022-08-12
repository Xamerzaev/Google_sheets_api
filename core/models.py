from core import db

# модель таблицы


class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer(), primary_key=True)  # ИД столбца
    order = db.Column(db.Integer(), nullable=False)  # номер заказа
    dollar = db.Column(db.Integer(), nullable=False)  # стоимость в долларах
    supply = db.Column(db.Date(), nullable=False)  # сроки поставки

    def __init__(self, order, dollar, supply):
        self.order = order
        self.dollar = dollar
        self.supply = supply

    def __repr__(self):
        return self.order
