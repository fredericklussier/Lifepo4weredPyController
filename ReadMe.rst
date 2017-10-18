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


Our intention is to design an oriented object access to the lifepo4wered-pi3 data module during runtime application.

reference: http://lifepo4wered.com/lifepo4wered-pi3.html

Using the Raspbery Pi zero in many projects, I found this product
very usefull. So to help my child and python colleagues, we design this. 

You can find here the documentation of the lifepo4wered product:
http://lifepo4wered.com/files/LiFePO4wered-Pi3-Product-Brief.pdf.

Status
------
In development

Installation
------------
.. code-block:: batch

    pip install lifepo4weredPyController

You have to install the LiFePO4wered-Pi drivers and CLI applications,
please read https://github.com/xorbit/LiFePO4wered-Pi.

and then, set a environment path variable that give access to the lifepo4wered driver. 
The best way is to set the LD_LIBRARY_PATH:
    
.. code-block:: batch

    echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/your/custom/path/" >> ~/.bashrc

Dependencies
^^^^^^^^^^^^
This setup will install does too:
* tinyPeriodicTask>=1.3.1
* observablePy>=0.2.2
* lifepo4weredPy>=0.1.0

Features (working on)
---------------------
* Oriented object definition
* Observable elements, so subscribed observers will know when data change
* Periodically read data, 
* Python 3.5 and 3.6
* Hardly tested

Detail
^^^^^^

classes
"""""""
The idea is to use oriented object mechanism to control the LiFePO4wered-Pi variables.
We have distributated LiFePO4wered-Pi variables in different classes:

* Battery (VBAT)
* Led (LED_STATE)
* Touch (TOUCH_STATE)
* WakeTimer (WAKE_TIME)
* USBPowerSource (VIN)

**What about others variables?**
  Well! must of them, we just not there yet.
  But we think that some of variables are factoring issue (not to use in a runtime environment) 
  and the provided CLI works perfectly for them. 
  Like:
  
  * I2C_REG_VER
  * I2C_ADDRESS
  * DCO_RSEL
  * DCO_DCOMOD
  * CFG_WRITE
 

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

        # keep main process alive, so observers will receive changes
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        myLifepo4wered.ceaseReading()
        print('stopped!')

        lifepo4weredPyController.WakeTimer.wakeUp = 60  # boot in 1 hour after shutdown
 
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
| rate'                         | na        | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+

'rate: return the level of the battery power based on the shutdown 
data value as the 0 reference.


+-------------------------------------------------------------------------------+
| **USBPowerSource**                                                            |
+===============================+===========+============+======================+
| **properies**                 | **aka**   | **access** | **Periodicaly read** |
+-------------------------------+-----------+------------+----------------------+
| voltage                       | VIN       | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+
| pluggedIn'                    | na        | read only  | True                 |
+-------------------------------+-----------+------------+----------------------+

'pluggedIn: Mention is the usb connector is plug to a power source


+-------------------------------------------------------------------------------+
| **Led**                                                                       |
+-------------------------------+-----------+------------+----------------------+
| **properies**                 | **aka**   | **access** | **Periodicaly read** |
+===============================+===========+============+======================+
| state                         | LED_STATE | read/write | True                 |
+-------------+-----------------+-----------+------------+----------------------+
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


+---------------------------------------------------------------------------------+
| **Touch**                                                                       |
+===============================+=============+============+======================+
| **properies**                 | **aka**     | **access** | **Periodicaly read** |
+-------------------------------+-------------+------------+----------------------+
| state                         | TOUCH_STATE | read only  | true                 |
+-------------------------------+-------------+------------+----------------------+


+-------------------------------------------------------------------------------+
| **WakeTimer**                                                                 |
+===============================+===========+============+======================+
| **properies**                 | **aka**   | **access** | **Periodicaly read** |
+-------------------------------+-----------+------------+----------------------+
| wakeUp                        | WAKE_TIME | read/write | False                |
+-------------------------------+-----------+------------+----------------------+
Note: As the documentation states, the WAKE_TIME value is not saved in flash, 
so it needs be set by a user program every time before the
Raspberry Pi shuts down.
