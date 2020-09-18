
from schema import Schema, And, Use, Optional, SchemaError,Or
from datetime import datetime as dt

def check(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError as a:
        print(a.code)
        return False

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

conf_schema = Schema({
    'nome': And(Use(str),LEN_H_THEN(0)),
    'cpf': And(Use(str),VALIDCPF),
    'dataNascimento':And(Use(str),Use(TO_DATE("%d/%m/%Y"))),
    'conta':{
        'limiteSaqueDiario': Or(int, float),
        'flagAtivo':bool,
        'tipoConta':int
    }
})

conf = {
    'nome': "a",
    'cpf': "08639614440",
    'dataNascimento':"01/01/1991",
    'conta':{
        'limiteSaqueDiario':0,
        'flagAtivo':True,
        'tipoConta':1
    }
}

print(check(conf_schema, conf))


# entrada = \
# {
#     cliente:{
#         nome:[str,v.NOT_NULL_EMPTY]
#         cpf:[str,v.NOT_NULL_EMPTY]
#         dns: [,]
#     },
#     conta:{
#     saldo:
#     limiteSaqueDiario:
#     ativo:
#     tipoConta:
#     dataCriacao:
#     }
# }

