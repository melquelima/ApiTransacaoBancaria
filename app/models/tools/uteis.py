from flask import request
from functools import wraps
import jwt


def token_required():
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            token = None
            fields = request.args.to_dict()

            if 'token' in fields:
                token = fields['token']
            
            if not token:
                return "Token is missing!",400
            try:
                data = jwt.decode(token,app.config['SECRET_KEY'])
                return function(*args, **kwargs)
            except:
                return "Token inválido!",400
        return wrapper
    return decorator