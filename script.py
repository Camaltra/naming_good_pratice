from utils import recup_elem_db, recent, types

def display(object):
    print(object.name, object.schle, object.strs)
    

def decision(array):
    while True:
        type = input("Your input:")
        if type in types:
            break

    a = []

    for elem in array:
        if elem.schle:
            if elem.type == type:
                if elem.yr >= recent:
                    a.append(e)
            else:
                if elem.strs == 5:
                    a.append(e)

    a = sorted(a, key=lambda x: x.yr, reverse=True)

    display(a[0])

if __name__ == "__main__":

    elems = recup_elem_db(type="Atw")

    decision(elems)

    