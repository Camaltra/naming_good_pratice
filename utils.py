types = ["Action", "Animation", "Drame"]
recent = 2010

from to_not_show import fake_query

def recup_elem_db(type):
    # session.query(eval(type)).all()
    return fake_query()
