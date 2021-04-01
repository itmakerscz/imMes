#
# imMes
#
# Copyright (c) 2020 Aliaksandr Sazankou
# itmakers.cz
#
# imMes is free software
# you can redistribute it and do not modify it
#

from __future__ import division
import time
from flask import Flask, Response, request, render_template
from random import gauss
import threading
from pymongo import MongoClient

__author__ = "Aliaksandr Sazankou"
__email__ = "sazankou.a@gmail.com"
__copyright__ = "Copyright (c) 2020 Aliaksandr Sazankou"
__license__ = "GPLv3 (or later)"


# imMes
# app initialize
imMes = Flask(__name__)


# imMesDbGet
# read last data from database
class imMesDbGet(object):
	def __init__(self):
		self.data = 0
		# imMesDbClient = MongoClient('127.0.0.1', 27017)
		# imMesDb = imMesDbClient['IMMES']
		# imMesDbCollection = imMesDb['IMDATA']
		# self.data = imMesDbCollection.find().sort({'_id': -1}).limit(1)

	def generate_values(self):
		while True:
			time.sleep(.1)
			yield gauss(0, 1)

	def monitor(self, report_interval = 1):
		imMesDbClient = MongoClient('127.0.0.1', 27017)
		imMesDb = imMesDbClient['IMMES']
		imMesDbCollection = imMesDb['IMDATA']
		# for x in self.generate_values():
		self.data = 4


imMesStream = imMesDbGet()


@imMes.route('/')
def index():
	if request.headers.get('accept') == 'text/event-stream':
		def events():
			while True:
				yield "data: %s\n\n" % (imMesStream.data)
				time.sleep(.1)

		return Response(events(), content_type = 'text/event-stream')
	return render_template('index.html', )


def init(imMesHost):
	# imMesStream start
	imMesThread = threading.Thread(target = imMesStream.monitor)
	imMesThread.start()
	try:
		imMes.run(host = imMesHost)
	except:
		print("Webapp cannot start...")

#if __name__ == "__main__":
	# Data monitor should start as soon as the app is started.
	# init()