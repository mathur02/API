from cricket import db

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(50))
    team=db.Column(db.String(20))
    price=db.Column(db.Integer())

    def __init__(self,team,price,name):
        self.name=name
        self.team=team
        self.price=price
