from app import app
from app.models import *
from app.models.tools.uteis import *
from app.models.DB.tables import *
from app.models.tools.required import schema_required
from app.models.API.requiredObjects import *
from app.models.API.logicflow import LogicDeposito,LogicSaque,LogicSaldo,LogicStatus

@app.route("/V2/contas/deposito",methods=["POST"])
@schema_required(deposito2)
def depositar2(fields):
    cnt = Contas.query.get(fields["idConta"])
    lgc = LogicDeposito(cnt,fields["valor"])
    return lgc


@app.route("/V2/contas/saque",methods=["POST"])
@schema_required(deposito2)
def sacar2(fields):
    cnt = Contas.query.get(idConta)
    lgc = LogicSaque(cnt,fields["valor"])
    return lgc


@app.route("/V2/contas/saldo")
@schema_required(contaId)
def saldo2(fields):
    cnt = Contas.query.get(fields["idConta"])
    lgc = LogicSaldo(cnt)
    return lgc


@app.route("/V2/contas/status",methods=["POST"])
@schema_required(statusConta2)
def status2(fields):
    cnt = Contas.query.get(fields["idConta"])
    lgc = LogicStatus(cnt,fields["flagAtivo"])
    return lgc


