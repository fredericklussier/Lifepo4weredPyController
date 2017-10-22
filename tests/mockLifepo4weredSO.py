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
    if eLiFePO4weredVar == 9:  # VIN
        return 5000
    elif eLiFePO4weredVar == 10:  # VBAT
        return 3300
    elif eLiFePO4weredVar == 3:  # TOUCH_STATE
        return 0
    else:
        return 10


def write_lifepo4wered(eLiFePO4weredVar, value):
    """
    Write data to LiFePO4wered/Pi
    """
    return value
