from app import app
from app.models import *
from app.models.tools.uteis import *
from app.models.DB.tables import *
from app.models.tools.required import schema_required
from app.models.API.requiredObjects import *

#nao existe uma tratativa para habilitar contas quando bloqueadas
#nao existe um metodo de segurança


@app.route("/")
def home():
    return "OK"


@app.route("/createAcount",methods=["POST"])
@schema_required(new_acc)
def create_account(fields):
    p = Pessoas.constructor(fields)
    p.save()
    c = Contas.constructor(p,fields["conta"])
    c.save()
    return "Account was created!"

