#!/bin/bash
#note you need to install screen
screen java -jar mrl/myrobotlab.jar -service gui GUIService python Python -invoke python execFile ../test.py
