#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ Replace an element of a copied list at a specific position"""
    if idx < 0 and idx > (len(my_list) -1):
        return (my_list)
    copy = []
    for i in my_list:
        copy.append(i)
    copy[idx] = element
    return (copy)
