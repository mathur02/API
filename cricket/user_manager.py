
from flask import jsonify
from cricket import db
from cricket.model import User

users=[
    {
        "name":"gaurv"
    }
]

class UserManager:

    @classmethod
    async def get_all_user(cls):
        all_user=User.query.all()
        return all_user


    @classmethod
    async def get_team_from_db(cls,payload):
        name=payload
        for user in users:
            if user['name']==name:
                return user

        user= User.query.filter_by(name=name).first()
        curr_user={
            "name":user.name,
            "team":user.team,
            "price":user.price
        }

        users.append(user)

        return user
   
    @classmethod
    async def post_user(cls,payload):
        team=payload.get('team')
        name=payload.get('name')
        price=payload.get('price')

        user=User(team=team,name=name,price=price)
        db.session.add(user)
        db.session.commit()
        return {"success":"successfully added player"}

    @classmethod
    async def delete_user(cls,payload):
        curr_user = User.query.filter_by(name=payload).first()
        db.session.delete(curr_user)
        db.session.commit()
        return {"message":"successfully deleted"}
    
    @classmethod
    async def update_user(cls,payload):
        curr_user=User.query.filter_by(name=payload.get("name")).first()
        if curr_user:
            curr_user.team=payload.get('team')
            curr_user.name=payload.get('name')
            curr_user.price=payload.get('price')
            db.session.commit()
            return {"message":"user was sucwssfully updated"}
        else:
            response=await cls.post_user(payload)
            return response






