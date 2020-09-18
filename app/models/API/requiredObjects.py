
from schema import Schema, And, Use, Optional, SchemaError,Or
from ..tools.required import LEN_H_THEN,VALIDCPF,TO_DATE

statusConta2 = Schema({
    'idConta': int,
    'flagAtivo':bool
})

statusConta = Schema({
    'flagAtivo':bool
})

contaId = Schema({
    'idConta': int
})

deposito = Schema({
    'valor': Or(int, float)
})

deposito2 = Schema({
    'valor': Or(int, float),
    'idConta':int
})

new_acc = Schema({
    'nome': And(str,LEN_H_THEN(0)),
    'cpf': And(str,VALIDCPF),
    'dataNascimento':And(str,Use(TO_DATE("%d/%m/%Y"))),
    'conta':{
        'limiteSaqueDiario': Or(int, float),
        'flagAtivo':bool,
        'tipoConta':int
    }
})