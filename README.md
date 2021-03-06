# PX4FLOW_mavlink_read
read value from PX4FLOW under mavlink protocol

This is a python package used to get value from PX4FLOW sensor.

test.py is an example for using this package. To use test.py, firstly conncet the PX4FLOW to your computer via USB, then run python test.py. The tty argument in test.py is COM4 by default, you may need to change it according to your own computer respectively. Two files sample.txt & samplerad.txt will be generated into the dictionary which you save the test.py.

Mavlinkprotocol.py 

-- Used to unpack binary data under mavlink protocol into desired format. Two arguments are needed: handler and msgid.

Arguments:

-- handler: Handles the data transmission. It should has a 'read' method which will return one byte whenever is called.

-- msgid: The message ID of desired message packet. See document of mavlink protocol for more details.

Methods:

-- refresh: When it is called, looking for the next available message from handler accroding to msgid. Then update the message.

-- getvalue(fmt,lo,hi): Returns the desired field in the message packet. lo/hi indicate the start/end byte index. fmt indicate the data formation.

Pix4flowDriver.py

-- Used to get OPTICAL_FLOW and OPTICAL_FLOW_RAD message from mavlink transmission. Make sure using refresh_opticalflow and refresh_opticalflowrad methods before reading the values.

Arguments:

-- handler: Handles the data transmission. It should has a 'read' method which will return one byte whenever is called.

-- flowid: The message ID of OPTICAL_FLOW. By default it is 0x64.

-- flowradid: The message ID of OPTICAL_FLOW_RAD. By default it is 0x6A.

Methods:

-- return_XXX: Returns the value of desired field. See document of mavlink protocol for more details.

-- refresh_opticalflow: Update the OPTICAL_FLOW message.

-- refresh_opticalflowrad: Update the OPTICAL_FLOW_RAD message.

ReadPix4flow.py & test.py:

A simple example to use the package. It writes OPTICAL_FLOW data into sample.txt and OPTICAL_FLOW_RAD data into samplerad.txt
