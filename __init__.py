#
# imMes
#
# Copyright (c) 2020 Aliaksandr Sazankou
# itmakers.cz
#
# imMes is free software
# you can redistribute it and do not modify it
#

from imMes.Web import imMesWeb
from imMes.Plc import imMesPlc

__author__ = "Aliaksandr Sazankou"
__email__ = "sazankou.a@gmail.com"
__copyright__ = "Copyright (c) 2020 Aliaksandr Sazankou"
__license__ = "GPLv3 (or later)"

TCP_IP = '192.168.3.251'
TCP_PORT = 7071
TCP_BUFFER = 9192
#received


try:
	pyMesWeb.init('127.0.0.2')
	print("Webapp is run...")
except:
	print("Webapp cannot run...")




try:
	pyMesPlc.init(TCP_IP, TCP_PORT, TCP_BUFFER)
	print("Plc reader is run...")
except:
	print("Plc reader cannot run...")

