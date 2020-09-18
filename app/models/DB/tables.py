from app import db
from sqlalchemy import Float,Column,Integer,String,ForeignKey,DateTime,Time,Boolean
from datetime import datetime as dt


class Contas(db.Model):
    __tablename__ = "contas"

    idConta             = Column(Integer,primary_key=True)
    idPessoa            = Column(Integer,ForeignKey('pessoas.idPessoa'),nullable=False)
    saldo               = Column(Float,nullable=False)
    limiteSaqueDiario   = Column(Float,nullable=False)
    flagAtivo           = Column(Boolean,nullable=False)
    tipoConta           = Column(Integer,nullable=False)
    dataCriacao         = Column(DateTime,nullable=False)
    pessoa              = db.relationship("Pessoas",foreign_keys=idPessoa)

    def __init__(self,idPessoa,saldo,limiteSaqueDiario,flagAtivo,tipoConta,dataCriacao=dt.now()):
        self.idPessoa           = idPessoa    
        self.saldo              = saldo
        self.limiteSaqueDiario  = limiteSaqueDiario            
        self.flagAtivo          = flagAtivo    
        self.tipoConta          = tipoConta    
        self.dataCriacao        = dataCriacao        

    def save(self):
        db.session.add(self)
        self.update()

    def update(self):
        db.session.commit()
    
    def constructor(p,obj):
        obj2 = obj.copy()
        obj2["saldo"] = 0
        return Contas(p.idPessoa,obj2["saldo"],obj2["limiteSaqueDiario"],obj2["flagAtivo"],obj2["tipoConta"])


class Pessoas(db.Model):
    __tablename__ = "pessoas"

    idPessoa            = Column(Integer,primary_key=True)
    nome                = Column(String,nullable=False)
    cpf                 = Column(Float,nullable=False)
    dataNascimento      = Column(DateTime,nullable=False)

    def __init__(self,nome,cpf,dataNascimento):
        self.nome            = nome 
        self.cpf             = cpf
        self.dataNascimento  = dataNascimento                  

    def save(self):
        db.session.add(self)
        self.update()

    def update(self):
        db.session.commit()

    def constructor(obj):

        return Pessoas(obj["nome"],obj["cpf"],obj["dataNascimento"])


class Transacoes(db.Model):
    __tablename__ = "transacoes"

    idTransacao         = Column(Integer,primary_key=True)
    idconta             = Column(Integer,ForeignKey('contas.idConta'),nullable=False)
    valor               = Column(Float,nullable=False)
    dataTransacao       = Column(DateTime,nullable=False)

    def __init__(self,idconta,valor,dataTransacao=dt.now()):   
        self.idconta        = idconta 
        self.valor          = valor
        self.dataTransacao  = dataTransacao                  

    def save(self):
        db.session.add(self)
        self.update()

    def update(self):
        db.session.commit() 
