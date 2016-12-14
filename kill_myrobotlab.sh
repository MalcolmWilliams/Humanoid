#!/bin/bash
ps -ef | grep myrobotlab | awk '{print $2}' | xargs kill
#ps -ef | grep lasershark_jack | awk '{print $2}' | xargs kill
#sometimes doesnt work. in this case use kill -9 "pid_to_kill"
