#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This simulate the lifepo4wered SO for testing porpose. 
It allow performing unit tests event if lifepo4wered device
is not plugged.
"""

def access_lifepo4wered(eLiFePO4weredVar, access_mask):
    """
    Determine if the specified variable can be accessed in the 
    specified manner (read, write or both)
    """
    return True

def read_lifepo4wered(eLiFePO4weredVar):
    """
    Read data from LiFePO4wered/Pi
    """
    return 10

def write_lifepo4wered(eLiFePO4weredVar, value):
    """
    Write data to LiFePO4wered/Pi
    """
    return value