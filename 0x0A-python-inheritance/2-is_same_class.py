#!/usr/bin/python3
def is_same_class(obj, a_class):
    if obj isinstance(a_class):
        return (f"{obj} is an instance of the {a_class}")
    else:
        return(False)
