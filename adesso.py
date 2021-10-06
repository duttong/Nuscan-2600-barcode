#! /usr/bin/env python

""" Simple test code for the Adesso 2600U handheld barcode scanner
    programming guide: https://www.adesso.com/download/user-manual/nuscan_2800u.pdf
    To access a /dev/tty serial port, you need to scan the "Serial Port" barcode on 
      page 19 of the manual listed above.
    Geoff Dutton 210927
"""

import sys
import serial
from time import sleep

DEFAULT_PORT = '/dev/tty.usbmodem14701'


def connect():
    try:
        ser = serial.Serial(DEFAULT_PORT, timeout=0.2, baudrate=9600, bytesize=8, parity='N', stopbits=1)
    except serial.serialutil.SerialException:
        sys.stderr.write(f'Could not connect to serial port: {DEFAULT_PORT}\n')
        quit()
        
    print('Ready to scan\n')
    return ser

def listen(ser):
    while True:
        try:
            r = ser.read(100).decode()
        except KeyboardInterrupt:
            quit()
            
        if len(r) > 1:
            print(f'bytes read: {len(r)} decoded: {r[:-1]}')
            ser.reset_input_buffer()
        sleep(.1)
            
ser = connect()
listen(ser)
