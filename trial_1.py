from sensor.logger import logging
from sensor.exception import SensorException
import sys,os

def test_logg():
     try:
          logging.info("start of the command")
          c = 3/0
          print(c)
          logging.info("end of the command")
     except Exception as e:
          logging.debug("degbus")
          raise SensorException(e,sys)


if __name__=="__main__":
     try:
        test_logg()
     except Exception as e:
          print(e)