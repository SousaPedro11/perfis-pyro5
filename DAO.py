# from flask_sqlalchemy import SQLAlchemy
#
# root_db = SQLAlchemy(session_options={'autoflush': False})

def transacao(session, objeto):
    session.add(objeto)
    session.commit()


def buscar_por_criterio(session, table, **filtros):
    return session.query(table).filter_by(**filtros).first()


def buscar_por_criterio_bool(session, table, *filtros):
    return session.query(table).filter(*filtros).first()


def busca_join_composto_com_criterio(session, table1, table2, table3, *filtro):
    return session.query(table1).join(table2).join(table3).filter(*filtro).add_entity(table2).add_entity(table3).first()


def buscar_por_join(session, table1, table2, *filtro):
    return session.query(table1).join(table2).filter(*filtro).add_entity(table2).first()


def buscar_todos(session, table, *order_by):
    return session.query(table).order_by(*order_by).all()


def buscar_todos_por_criterio(session, table, **filtros):
    return session.query(table).filter_by(**filtros).all()


def buscar_todos_por_join(session, table1, table2, *order_by, **filtro):
    return session.query(table1).join(table2).filter(**filtro).order_by(*order_by).all()


def deletar(session, objeto):
    session.delete(objeto)
    session.commit()
    session.close()
    # local_object = root_db.session.merge(objeto)
    # root_db.session.delete(local_object)
    # root_db.session.commit()
    # root_db.session.close()
