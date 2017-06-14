# mobmsg 

A library to encode/decode the mobile messaging components(mobile number, cutomer id, sms id)

See the sample outputs [here](./sample_output.md)

**A Sample output**

```python
========================== ORIGINAL DATA ============================
Mobile number :  8461935858
Customer id   :  48345
SMS id        :  98765
Combined data :  84619358584834598765

====== ENCODED DATA from 84619358584834598765========
Encoded message        :  T=]::0";WA
Encoded message length :  10

====== DECODED DATA from T=]::0";WA =====================
Encoded message        :  84619358584834598765
Encoded message length :  20
Mobile number          :  8461935858
Customer id            :  48345
SMS id                 :  98765
```