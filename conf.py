import sys
import yaml
import logging
from pathlib import Path
class PythonVer:
  def pytCheck(self):
    if sys.version_info[0] < 3:
      raise Exception("Must be using Python 3")

class LocateConfigFile:
  """Reads the YAML config file for path variables"""
  allyml=""
  def readFile(self):
    try:
      with open('./config/configfile.yml','r') as yf:
        LocateConfigFile.allyml=yaml.load(yf)
    except FileNotFoundError:
      print("hello!") 

class ReadPaths(LocateConfigFile):
  """Allocate variables their respective paths"""
  TSHARK_PATH=""
  READ_CAPTUREFILE=""
  OUTPUT_FILE_NAME=""
  OUTPUT_DIR=""
  INTERFACE_NO=""
  
  DECIDE=""
  def getpaths(self):
    for listing in LocateConfigFile.allyml:
      try:
        ReadPaths.DECIDE=LocateConfigFile.allyml['DECIDE']
        ReadPaths.TSHARK_PATH=LocateConfigFile.allyml['TSHARK_PATH']
        ReadPaths.READ_CAPTUREFILE=LocateConfigFile.allyml['READFROM']
        ReadPaths.OUTPUT_FILE_NAME=LocateConfigFile.allyml['OUTPUT_FILE_NAME']
        ReadPaths.OUTPUT_DIR=LocateConfigFile.allyml['OUTPUT_DIR']
        ReadPaths.INTERFACE_NO=LocateConfigFile.allyml['INTERFACE_NO']
        # Catch all YAMLErrors
      except yaml.YAMLError:
        print("hello1")
class CheckPaths(ReadPaths):
  """Check if the paths given by the user is correct or not"""
  OUTPUT_PATH=""
  def checkPathTshark(self):
    try:
      my_file=Path(ReadPaths.TSHARK_PATH)
      my_abs_path = my_file.resolve()
    except FileNotFoundError:
      print("hello1")
  def checkOutputLocation(self):
    try:
      CheckPaths.OUTPUT_PATH=ReadPaths.OUTPUT_DIR+ReadPaths.OUTPUT_FILE_NAME
      my_file=Path(ReadPaths.OUTPUT_DIR)
      my_abs_path = my_file.resolve()
    except FileNotFoundError:
      print("hello1")