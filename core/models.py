from core import db
from datetime import datetime


class Table(db.Model):
    __tablename__ = "tables"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order = db.Column(db.Integer, nullable=False)
    dollar = db.Column(db.Float, nullable=False)
    supply = db.Column(db.Date, nullable=False)

    def __init__(self, order: int, dollar: float, supply: datetime):
        """Конструктор для создания объекта Table.

        Args:
            order (int): Номер заказа.
            dollar (float): Стоимость в долларах.
            supply (datetime): Сроки поставки.
        """
        self.order = order
        self.dollar = dollar
        self.supply = supply

    def __repr__(self):
        return f"Table(id={self.id}, order={self.order}, dollar={self.dollar}, supply={self.supply.strftime('%Y-%m-%d')})"
