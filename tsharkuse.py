from config import conf
import subprocess
from pathlib import Path 
import os
class TsharkRead:
  #path variables of class TsharkRead
  tpath=""
  opath=""
  rpath=""
  def checkread(self):
    #logging.info("Checking file for reading")
    try:
      #creating instances of classes to get and chedck paths
      readinglocation=conf.ReadPaths()
      readinglocation.getpaths()
      outputfilepath=conf.CheckPaths()
      outputfilepath.checkPathTshark()
      outputfilepath.checkOutputLocation()

      TsharkRead.tpath=readinglocation.TSHARK_PATH
      my_file=Path(readinglocation.READ_CAPTUREFILE)
      my_abs_path = my_file.resolve()
    except FileNotFoundError:
      print("ERROR NO SUCH PCAP FILE FOUND ")
  def readincsv(self):
    #FOR READING PCAP FILES
    readinglocation=conf.ReadPaths()
    readinglocation.getpaths()
    outputfilepath=conf.CheckPaths()
    outputfilepath.checkPathTshark()
    outputfilepath.checkOutputLocation()
    TsharkRead.tpath=readinglocation.TSHARK_PATH
    TsharkRead.rpath=readinglocation.READ_CAPTUREFILE
    TsharkRead.opath=outputfilepath.OUTPUT_PATH
    
    tshark =open(os.path.join(TsharkRead.opath), "w")
    subprocess.Popen([TsharkRead.tpath,"-r",TsharkRead.rpath,"-T"+"fields","-e","frame.time","-e","frame.number","-e","eth.dst","-e","ip.src","-e","ip.dst","-E","header=y", "-E","separator=','","-E", "quote=d" ,"-E","occurrence=f"], stdout =tshark)
    tshark.close()
    return 0;   
class TsharkWrite:
  tpath=""
  opath=""
  def capturelive(self):
    #LIVE CAPTURE
    readinglocation=conf.ReadPaths()
    TsharkWrite.tpath=readinglocation.TSHARK_PATH
    outputfilepath=conf.CheckPaths()
    TsharkWrite.opath=outputfilepath.OUTPUT_PATH
    tshark =open(os.path.join(TsharkWrite.opath), "w")
    subprocess.Popen([TsharkWrite.tpath,"-T"+"fields","-e","frame.time","-e","frame.number","-e","eth.dst","-e","ip.src","-e","ip.dst","-E","header=y", "-E","separator=','","-E", "quote=d" ,"-E","occurrence=f"], stdout =tshark)    
    tshark.close()
    return 0;