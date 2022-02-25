from flask import jsonify

USER=[

]
class To_dict:
    async def one_object_to_dict(user):
        curr_user={
            "name":user.name,
            "team":user.team,
            "price":user.price  
            }

        return curr_user

    async def to_dict(response):
        
        for user in response:

            curr_user={
            "name":user.name,
            "team":user.team,
            "price":user.price  
            }

            USER.append(curr_user)

        return jsonify(USER)