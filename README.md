# mobmsg 

A library to encode/decode the mobile messaging components(mobile number, cutomer id, sms id)

See the sample outputs [here](./sample_output.md)

### How to install

Open terminal and type the following 

```
pip install mobmsg
```

### Steps to use the package

* import the **mobmsg** module

* instantiate the MobileMessage class by passing 3 parameters.

Parameters can be strings or integers. 

1st parameter is a 10 digit **mobile number**

2nd parameter is a 5 digit **customer id** & 

3rd parameter is a 5 digit **sms id**.

* Call encode() method on instantiated object.

* Call decode() method on instantiated object.

* Finally call details() method on instantiated object.

### A Simple usage of the mobmsg package from interactive Python terminal

```python
MacBook-Pro:~ admin$ python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mobmsg
>>> msg = mobmsg.MobileMessage(7353787704, 45654, 45464)
>>> msg.encode()
>>> msg.decode()
>>> msg.details()
========================== ORIGINAL DATA ============================
Mobile number :  7353787704
Customer id   :  45654
SMS id        :  45464
Combined data :  73537877044565445464

====== ENCODED DATA from 73537877044565445464========
Encoded message        :  J;Y]G`P_n
Encoded message length :  10

====== DECODED DATA from J;Y]G`P_n =====================
Decoded message        :  7353787744565445464
Decoded message length :  19
Mobile number          :  7353787744
Customer id            :  56544
SMS id                 :  5464
>>> 
```

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