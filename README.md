# mobmsg 

A library to encode/decode the mobile messaging components(mobile number, cutomer id, sms id)

See the sample outputs [here](./sample_output.md)

### How to install

Open terminal and type the following 

```
pip install mobmsg
```

### Steps to use the package

* import **mobmsg** module

* instantiate the MobileMessage class by passing 3 parameters.

	* Parameters can be strings or integers. 

	* 1st parameter is a 10 digit **mobile number**

	* 2nd parameter is a 5 digit **customer id** & 

	* 3rd parameter is a 5 digit **sms id**.

* Call **encode()** method on instantiated object.

* Call **decode()** method on instantiated object.

* Finally call **details()** method on instantiated object.

### A Simple usage of the mobmsg package from interactive Python terminal

You can pass parameters as **strings** or **integers** or as a combination of both

```python
>>> import mobmsg
>>> msg = mobmsg.MobileMessage("6565786545", "45654", "45464")
>>> msg.encode()
>>> msg.decode()
>>> msg.details()
========================== ORIGINAL DATA ============================
Mobile number :  6565786545
Customer id   :  45654
SMS id        :  45464
Combined data :  65657865454565445464

====== ENCODED DATA from 65657865454565445464========
Encoded message        :  BGYQBG`P_n
Encoded message length :  10

====== DECODED DATA from BGYQBG`P_n =====================
Decoded message        :  65657865454565445464
Decoded message length :  20
Mobile number          :  6565786545
Customer id            :  45654
SMS id                 :  45464
>>> 
```

Another sample

```python
>>> import mobmsg
>>> msg = mobmsg.MoblileMessage(9772254140, 56575, 56565)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'MoblileMessage'
>>> msg = mobmsg.MobileMessage(9772254140, 56575, 56565)
>>> msg.encode()
>>> msg.decode()
>>> msg.details()
========================== ORIGINAL DATA ============================
Mobile number :  9772254140
Customer id   :  56575
SMS id        :  56565
Combined data :  97722541405657556565

====== ENCODED DATA from 97722541405657556565========
Encoded message        :  bN$9=RX[jo
Encoded message length :  10

====== DECODED DATA from bN$9=RX[jo =====================
Decoded message        :  97722541405657556565
Decoded message length :  20
Mobile number          :  9772254140
Customer id            :  56575
SMS id                 :  56565
>>> 
```