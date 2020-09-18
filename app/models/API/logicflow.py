
from app.models.DB.tables import *

def LogicDeposito(cntObj:Contas,valor:(int,float)):
    if cntObj:
        if cntObj.flagAtivo:
            if valor <=0: return "value not allowed!",400
            cntObj.saldo +=  valor
            Transacoes(cntObj.idConta,valor).save()
            cntObj.update()
            return "Value was successfully submitted!"
        else:
            return "Account is inactive please contact your manager!",400
    else:
        return "Account not found!",400


def LogicSaque(cntObj:Contas,valor:(int,float)):
    if cntObj:
        if cntObj.flagAtivo:
            if valor <=0: return "value not allowed!",400
            if valor > cntObj.saldo: return "no sufficient funds!",400

            cntObj.saldo -=  valor
            Transacoes(cntObj.idConta,valor *-1).save()
            cntObj.update()
            return "Value was successfully decreased!"
        else:
            return "Account is inactive please contact your manager!",400
    else:
        return "Account not found!",400


def LogicSaldo(cntObj:Contas):
    if cntObj:
        return {"saldo":cntObj.saldo}
    else:
        return "Account not found!",400


def LogicStatus(cntObj:Contas,flag:bool):
    if cntObj:
        cntObj.flagAtivo = flag
        cntObj.update()
        return "Account status was changed successfully!",400
    else:
        return "Account not found!",400

