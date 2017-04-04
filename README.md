# aws_iot_segmentation
Python helper module for segmenting big mqtt messages

### How to use it
Import the module as
```python
from aws_iot_segmentation import iot_segmentation
```

## Sender
Before sending the message on your mqtt library(paho etc) call:
```python
iot_segmentation.segment_message(message)
```
This will return a generator with the message segmented or the same message if segmentation is not required. Now, the message can be 
sent.

## Receiver
After receiving the message from the mqtt lib, feed it to the iot_segmentation module as:
```python
iot_segmentation.get_message(message)
```
This will return None or the message. Messages which are not segmented will return immediately.
None it will be returned when the message is a segment but not all arrived yet to compose the message.

It is recommended to feed all messages from mqtt to the iot_segmentation module, this way no extra logic on top of it is necessary.

BTW: it supports only strings yet(?) 

## TO DO
* ***Other data structures***
* ~~***Speed up the segmentation***~~ **done**
* ***Separate thread with callbacks on done***