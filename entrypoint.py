#!/usr/local/bin/python
import time
import os
import sys
#### Prepare functions for prettier output
def msg(message):
    print ("\033[92m INFO [{}] ---> {}\033[0m".format(time.strftime("%H:%M:%S"), message))
def warn(message):
    print ("\033[93m WARN [{}] ---> {}\033[0m".format(time.strftime("%H:%M:%S"), message))
def err(message):
    print ("\033[91m ERR  [{}] ---> {}\033[0m".format(time.strftime("%H:%M:%S"), message))
    sys.exit(1)

msg("Running codefresh plugin {}".format(os.getenv('CF_PLUGIN_NAME', "undefined")))
# #### Check for required environment variables
if os.getenv("PLUGIN_RESULT") == None:
    err("Need to set PLUGIN_RESULT")

msg ("Environment variable PLUGIN_RESULT is: {}".format(os.getenv("PLUGIN_RESULT")))
msg ("Codefresh account is {}".format(os.getenv("CF_ACCOUNT", "undefined")))

if os.getenv("PLUGIN_RESULT") == "SUCCESS":
    msg ("Requested PLUGIN_RESULT is SUCCESS. Have a great day!")
else:
    err ("Requested PLUGIN_RESULT is {}. Failing.".format(os.getenv("PLUGIN_RESULT")))