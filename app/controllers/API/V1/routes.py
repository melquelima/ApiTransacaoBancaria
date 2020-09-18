from app import app
from app.models import *
from app.models.DB.tables import *
from app.models.tools.required import schema_required
from app.models.API.requiredObjects import *
from app.models.API.logicflow import LogicDeposito,LogicSaque,LogicSaldo,LogicStatus

@app.route("/V1/contas/<int:idConta>/deposito",methods=["POST"])
@schema_required(deposito)
def depositar(fields,idConta):
    cnt = Contas.query.get(idConta)
    lgc = LogicDeposito(cnt,fields["valor"])
    return lgc


@app.route("/V1/contas/<int:idConta>/saque",methods=["POST"])
@schema_required(deposito)
def sacar(fields,idConta):
    cnt = Contas.query.get(idConta)
    lgc = LogicSaque(cnt,fields["valor"])
    return lgc


@app.route("/V1/contas/<int:idConta>/saldo")
def saldo(idConta):
    cnt = Contas.query.get(idConta)
    lgc = LogicSaldo(cnt)
    return lgc


@app.route("/V1/contas/<int:idConta>/status",methods=["POST"])
@schema_required(statusConta)
def status(idConta,fields):
    cnt = Contas.query.get(idConta)
    lgc = LogicStatus(cnt,fields["flagAtivo"])
    return lgc


