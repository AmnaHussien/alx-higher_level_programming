class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        " initialization "
        if id is not None:
            id = id-1
        else:
            Base.__nb_objects += 1
