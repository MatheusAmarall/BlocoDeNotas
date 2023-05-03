from infra.configs.connection import DBConnectionHandler
from infra.entities.nota import Nota

class NotaRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Nota).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Nota).filter(Nota.id == id).first()
            return data

    def insert(self, titulo, texto, prioridade, data_criacao):
        with DBConnectionHandler() as db:
            try:
                data_insert = nota = Nota(titulo=titulo, data_criacao=data_criacao, texto=texto, prioridade=prioridade)
                db.session.add(data_insert)
                db.session.commit()
                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Nota).filter(Nota.id == id).delete()
                db.session.commit()
                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

    def update(self, id, titulo, texto, prioridade):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Nota).filter(Nota.id == id).update({'titulo' : titulo, 'texto' : texto, 'prioridade' : prioridade})
                db.session.commit()
                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

