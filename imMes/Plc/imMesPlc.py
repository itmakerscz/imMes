#
# imMes
#
# Copyright (c) 2021 Aliaksandr Sazankou
# itmakers.cz
#
# imMes is free software
# you can redistribute it and do not modify it
#

import socket
import json
from pymongo import MongoClient


__author__ = "Aliaksandr Sazankou"
__email__ = "sazankou.a@gmail.com"
__copyright__ = "Copyright (c) 2021 Aliaksandr Sazankou"
__license__ = "GPLv3 (or later)"

global data_array

def d(data_line, data_bit = None):
    if data_bit is None:
        return data_show(data_array[data_index(data_line)])
    else:
        return data_show(data_array[data_index(data_line)])[data_index(data_bit)]

def data_show(data_in):
    return data_in[-8:] + data_in[:-8]

def data_index(data_address_in):
    return data_address_in - 2513

def data_bin_array(data_in):
    data_binary = ''.join(format(data_hex, '0>8b') for data_hex in data_in)
    data_array_len = 16
    return [data_binary[y-data_array_len:y] for y in range(data_array_len, len(data_binary) + data_array_len, data_array_len)]




def init(imMesHost, imMesPort, imMesBuffer):
    #
    imMesDbClient = MongoClient('127.0.0.1', 27017)
    imMesDb = imMesDbClient['IMMES']
    imMesDbCollection = imMesDb['IMDATA']



    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.settimeout(120)
        s.bind((imMesHost, imMesPort))
        s.listen(1)
        #
        while True:
            try:
                conn, addr = s.accept()
            except socket.error as e:
                print("Connection accept error: " + str(e))
                break

            try:
                data = conn.recv(imMesBuffer)
            except socket.error as e:
                print("Data received error: " + str(e))
                break

            data_array = data_bin_array(data)
            #
            imMesDbRecord = {
                '_id': 1,
                'target': int(d(6010), 2),
                'actual': int(d(6008), 2),
                'remains': (int(d(6010), 2) - int(d(6008), 2)),
                'prod_act' : int(d(7005),2),
                'prod_last' : int(d(7004),2),
                'shiftok' : int(d(6012),2),
                'cameranok' : int(d(6016),2),
                'voltagenok' : int(d(6014),2),
                'total' : int((d(7007)+d(7006)),2)
            }

            imMesDbCollection.insert_one(imMesDbRecord)
            #json_data = {'target' : int(d(6010),2), 'actual' :  int(d(6008),2), 'remains' : (int(d(6010),2)-int(d(6008),2)),
            #             'prod_act' : int(d(7005),2), 'prod_last' : int(d(7004),2), 'shiftok' : int(d(6012),2), 'cameranok' : int(d(6016),2),
            #             'voltagenok' : int(d(6014),2), 'total' : int((d(7007)+d(7006)),2)}
            #
            #outfile = open('/data/data.json')
            #json.dump(json_data, outfile, indent = 2)
            #print(json.dumps(json_data, indent = 2))

            if data:
                conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, 1)
                # conn.sendall(data)
            else:
                conn.close()
                break
    except:
        print("Unknown Interrupt")
        pass

#if __name__ == "__main__":
	# Data monitor should start as soon as the app is started.
	# init()