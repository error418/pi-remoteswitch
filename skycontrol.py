#!/usr/bin/env python

import skywriter
import signal
import requests
from intertechno import Intertechno

#some_value = 5000

#@skywriter.move()
#def move(x, y, z):
#  print( x, y, z )

URL = 'http://192.168.0.133:5000/send'

intertechno = Intertechno()

# state container for toggling FM switches
states = {
        'NS': False,
        'SN': False,
        'WE': False,
        'EW': False
}

@skywriter.flick()
def flick(start, finish):
  print('flick event', start, finish)

  if (start == 'north' and finish == 'south'):
    states['NS'] = not states['NS']
    code = { 'syscode' : 'B', 'devicecode' : 1, 'state' : 1 if states['NS'] == True else 0}
    print("... and there will be light. sending", code)
    r = requests.post(URL, data = code )

  if (start == 'south' and finish == 'north'):
    #code = intertechno.translate('A', 1, states['SN'] = not states['SN'])
    print("no action assigned")
    #requests.post(URL, data = { data: code })

  if (start == 'west' and finish == 'east'):
    #code = intertechno.translate('A', 1, states['WE'] = not states['WE'])
    print("no action assigned")
    #requests.post(URL, data = { data: code })

  if (start == 'east' and finish == 'west'):
    #code = intertechno.translate('A', 1, states['EW'] = not states['EW'])
    print("no action assigned")
    #requests.post(URL, data = { data: code })

#@skywriter.airwheel()
#def spinny(delta):
#  global some_value
#  some_value += delta
#  if some_value < 0:
#       some_value = 0
#  if some_value > 10000:
#    some_value = 10000
#  print('Airwheel:', some_value/100)

@skywriter.double_tap()
def doubletap(position):
  print('Double tap!', position)

#@skywriter.tap()
#def tap(position):
#  print('Tap!', position)

#@skywriter.touch()
#def touch(position):
#  print('Touch!', position)

signal.pause()
