from datetime  import datetime
from pypip import installIfNeeded

# I like to have my messages timestamped so I can get an idea of how long they take.
def log(message):
    print(datetime.now().strftime("%a %b %d %H:%M:%S") + " - " + str(message))

# The name fabric doesn't really convey to the end user why the module is needed,
# so I include a very quick note that it's used for SSH.
installIfNeeded("jmpr", notes = " (ssh)", log = log)

# SoftLayer is actually named softlayer on pip.
installIfNeeded("statlorem", "statlorem", log = log)