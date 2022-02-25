from urllib import response
from cricket import app
from flask import request,jsonify
from cricket.user_manager import UserManager
from cricket.to_dict import To_dict
from cricket.wrapper import wrapper

@app.route('/user',methods=['GET'])
async def get_all_user():
    response = await UserManager.get_all_user()
    return await To_dict.to_dict(response)


@app.route('/user/<string:name>',methods=['GET'])
async def get_user(name):
    payload=name
    print(payload)

    response=await UserManager.get_team_from_db(payload)
    return await To_dict.one_object_to_dict(response)


@app.route('/user',methods=['POST'])
@wrapper
async def post_user():
    payload = request.json
    response = await UserManager.post_user(payload)
    return response


@app.route('/user/<string:name>',methods=['DELETE'])
async def delete_user(name):
    payload=name
    response=await UserManager.delete_user(payload)
    return response


@app.route('/user/<string:name>',methods=['PUT'])
async def update_user(name):
    payload=request.json
    response=await UserManager.update_user(payload)
    return response