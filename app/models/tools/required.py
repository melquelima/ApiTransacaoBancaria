
from datetime import datetime as dt
from functools import wraps
from flask import request

def check(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True,""
    except SchemaError as a:
        return False,a.code

def IS_STR_DATE(format):
    def fnc(date_text):
        try:
            dt.strptime(date_text, format)
            return True
        except ValueError:
            raise SchemaError(f"date format is invalid! value:('{date_text}')")
    return fnc

def LEN_H_THEN(l):
    def LEN_H_THEN(x):
        if not len(x) > l:
            raise SchemaError(f"value ('{x}') doesn't have the apropriate length!")
        else: 
            return True
    return LEN_H_THEN

def VALIDCPF(number):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in number if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        raise SchemaError(f"value ('{number}') doesn't have the apropriate length!")

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        raise SchemaError(f"value ('{number}') is not a valid CPF number!")

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            raise SchemaError(f"value ('{number}') is not a valid CPF number!")
    return True

def TO_DATE(format):
    def fnc(date_text):
        try:
            return dt.strptime(date_text, format)
        except ValueError:
            raise SchemaError(f"date format is invalid! value:('{date_text}')")
    return fnc

def GETDATA():
    try:
        xstr = lambda s: s or ""
        contentJson = "json" in xstr(request.headers.get("Content-Type"))
        if request.method == "GET":
            fields = request.args.to_dict()
        elif request.method in ["POST","PUT","DELETE","DEL","CREDIT"]:
            data = request.get_json(force=True) or request.get_json() or request.form.to_dict()
            fields =  request.json if contentJson else data
        return True,fields
    except:
        return False,""

def schema_required(schema,methods="*",out="fields"):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            

            if methods == "*" or request.method in methods:
                fields = GETDATA()
                if not fields[0]:return "json data required!",400
                fields = fields[1]
                
                try:
                    fields = schema.validate(fields)
                except SchemaError as a:
                        return a.code,400
            
                kwargs[out] = fields
                result = function(*args, **kwargs)
                return result
            else:
                kwargs[out] = []
                return function(*args, **kwargs)

        return wrapper
    return decorator

# conf = {
#     "nome": "a",
#     "cpf": "08639614440",
#     "dataNascimento":"01/01/1991",
#     "conta":{
#         "limiteSaqueDiario":0,
#         "flagAtivo":True,
#         "tipoConta":1
#     }
# }

#print(check(conf_schema, conf))

