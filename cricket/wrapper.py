from flask import request

def wrapper(func):

   async def validator(*args,**kwargs):
        payload = request.json

        if payload['name'] and payload['team'] and payload['price']:
            return await func(*args,**kwargs)
        else:
            return {"error":"missing arguments"}
   return validator