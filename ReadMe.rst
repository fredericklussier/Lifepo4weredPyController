Lifepo4weredPyController
========================

.. image:: https://travis-ci.org/fredericklussier/Lifepo4weredPyController.svg?branch=master
    :target: https://travis-ci.org/fredericklussier/Lifepo4weredPyController

.. image:: https://coveralls.io/repos/github/fredericklussier/Lifepo4weredPyController/badge.svg?branch=master
    :target: https://coveralls.io/github/fredericklussier/Lifepo4weredPyController?branch=master

.. image:: https://api.codeclimate.com/v1/badges/809cf25fc925a3ed8ef2/maintainability
   :target: https://codeclimate.com/github/fredericklussier/Lifepo4weredPyController/maintainability
   :alt: Maintainability

.. image:: https://badge.fury.io/py/lifepo4weredPyController.svg
    :target: https://badge.fury.io/py/lifepo4weredPyController


Our intention is to design an oriented object access to the lifepo4wered-pi3 data module.

reference: http://lifepo4wered.com/lifepo4wered-pi3.html

Using the Raspbery Pi zero in many projects, I found this product
very usefull. So to help my child and python colleagues, we design this. 

You can find here the documentation of the lifepo4wered product:
http://lifepo4wered.com/files/LiFePO4wered-Pi3-Product-Brief.pdf.

Status
------
Operation room: working hard to design pieces

Installation
------------
If you want to use this wrapper, you need:

Not yet, but we will have one, soon.

To dowload and install the LiFePO4wered-Pi drivers and CLI applications,
please read https://github.com/xorbit/LiFePO4wered-Pi.

Features (working on)
---------------------
* Oriented object definition
* Observable elements, so subscribed observers will know when data change
* Periodically read data, 
* Python 3 
* Hardly tested

Draft:
^^^^^^
This is what we thing of...

classes
"""""""
The idea is to use oriented object mechanism to control the LiFePO4wered-Pi variables.
We have distributate LiFePO4wered-Pi variables in different classes:

* Battery (VBAT, VBAT_SHDN, VBAT_MIN, VBAT_BOOT)
* Led (LED_STATE)
* Touch (Touch...)
* USBPowerSource ()

**What about others variables?**
  Well! we think that they are factoring variables not to use in a runtime environment. 

basic usage
*****************

.. code-block:: python

    import time
    import lifepo4weredPyController

    @lifepo4weredPyController.battery.observeElement("rate")
    def printRate(previous, actual):
        print("previously:{0}, now:{1}".format(previous, actual))

    try:
        print(lifepo4weredPyController.battery.voltage)

        # keep main process open, so observer will receive changes
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        myLifepo4wered.ceaseReading()
        print('stopped!')

        lifepo4weredPyController.bootUp = 60  # boot in 1 minute after shoutdown
 
Legendary
*********
* **properies:** name of class property
* **aka:** name used by the LiFePO4wered-Pi variables
* **access:** provide the access of the data of the variable. read means it reads the data from LiFePO4wered and write means it writes value to LiFePO4wered.
* **Periodicaly read:** at interval, this data is read so observers will be notified of any changes
* **na:** not applicable


+-------------------------------------------------------------------------------+
| **Battery**                                                                   |
+-------------------------------+-----------+------------+----------------------+
| **properies**                 | **aka**   | **access** | **Periodicaly read** |
+===============================+===========+============+======================+
| voltage                       | VBAT      | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+
| shutdownVoltageLevel          | VBAT_SHDN | read/write | False                |
+-------------------------------+-----------+------------+----------------------+
| emergencyShutdownVoltageLevel | VBAT_MIN  | read/write | False                |
+-------------------------------+-----------+------------+----------------------+
| allowedToBootVoltageLevel     | VBAT_BOOT | read/write | False                |
+-------------------------------+-----------+------------+----------------------+
| rate'                         | na        | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+

'rate: Will give the battery pourcentage


+-------------------------------------------------------------------------------+
| **USBPowerSource**                                                            |
+===============================+===========+============+======================+
| **properies**                 | **aka**   | **access** | **Periodicaly read** |
+-------------------------------+-----------+------------+----------------------+
| voltage                       | VIN       | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+
| pluggedIn'                    | na        | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+

'pluggedIn: Will mention is the usb connector is plug to a power source


+-------------------------------------------------------------------------------+
| **Led**                                                                       |
+-------------------------------+-----------+------------+----------------------+
| **properies**                 | **aka**   | **access** | **Periodicaly read** |
+===============================+===========+============+======================+
| state                         | LED_STATE | read/write | True                 |
+-------------------------------+-----------+------------+----------------------+
| **methods** |                                                                 |
+-------------+-----------------------------------------------------------------+
| on          | set on the led                                                  |
+-------------+-----------------------------------------------------------------+
| off         | set off the led                                                 |
+-------------+-----------------------------------------------------------------+
| pulse       | led pulsing                                                     |
+-------------+-----------------------------------------------------------------+
| flash       | led flashing                                                    |
+-------------+-----------------------------------------------------------------+
