#!/usr/bin/python3
"""
Module for a class that prevents dynamic attributes creation
"""


class LockedClass():
    """"
    Prevent the user from instantiating new LockedClass attributes for anyth    ing but attributes called 'first_name'.  

    """"
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
