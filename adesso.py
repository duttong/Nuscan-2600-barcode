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


class Scanner():

    def __init__(self):
        self.ser = self.connect()

    def connect(self):
        """ default options for a serial connection """
        try:
            ser = serial.Serial(DEFAULT_PORT, timeout=0.1, baudrate=9600, bytesize=8, parity='N', stopbits=1)
        except serial.serialutil.SerialException:
            sys.stderr.write(f'Could not connect to serial port: {DEFAULT_PORT}\n')
            quit()
        return ser

    def listen(self, size=100):
        """ continuous listen to serial port mode """
        while True:
            try:
                r = self.ser.read(size).decode()
            except KeyboardInterrupt:
                quit()
            
            if len(r) > 1:
                print(f'bytes read: {len(r)} decoded: {r[:-1]}')
                self.ser.reset_input_buffer()
            sleep(.1)
            
    def read(self, size=100):
        r = self.ser.read(size).decode()
        if len(r) > 1:
            self.ser.reset_input_buffer()
            return r[:-1]       # strip off \n
        else:
            return None


if __name__ == '__main__':

    s = Scanner()
    print('Ready to scan barcodes. Press Ctrl-C to quit.')
    s.listen()
