import tsharkuse
from config import conf
pythcheck=conf.PythonVer()
pythcheck.pytCheck()
configfile=conf.LocateConfigFile()
configfile.readFile()
paths=conf.ReadPaths()
paths.getpaths()
num=paths.DECIDE
#using tshark module now
def decision(number):
	if number=="1":
		readpcap=tsharkuse.TsharkRead()
		readpcap.checkread()
		readpcap.readincsv()
	if number=="2":
		capturetraffic=tsharkuse.TsharkWrite()
		capturetraffic.capturelive()
decision(num)
