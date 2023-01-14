import digitalio
import board
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# define
POUT_PORT = [board.GP22, board.GP26, board.GP27]
PIN_PORT = [board.GP16, board.GP17, board.GP18, board.GP19]
KEYCODEMAX = len(POUT_PORT) * len(PIN_PORT)

# global
kbd = Keyboard(usb_hid.devices)
led = None
pout = []
pin = []
keyState = 0
keyChange = 0
keyTurnOn = 0
keyTurnOff = 0

# init
def init():
	global led, pout, pin, keyChange, keyTurnOn, keyTurnOff

	# pico led
	led = digitalio.DigitalInOut(board.LED)
	led.direction = digitalio.Direction.OUTPUT
	led.value = True

	# out pin line
	for _pout_port in POUT_PORT:
		p = digitalio.DigitalInOut(_pout_port)
		p.direction = digitalio.Direction.OUTPUT
		p.value = True
		pout.append(p)

	# in pin line
	for _pin_port in PIN_PORT:
		p = digitalio.DigitalInOut(_pin_port)
		p.direction = digitalio.Direction.INPUT
		p.pull = digitalio.Pull.UP
		pin.append(p)

# check pin
def checkPin():
	global keyState, keyChange, keyTurnOn, keyTurnOff

	# check key pin
	keyState0 = 0
	c = 0
	for _pout in pout:
		_pout.value = False
		for _pin in pin:
			if _pin.value==False:
				keyState0 |= ( 1 << c )
			c += 1
		_pout.value = True

	# check keypress
	keyChange = keyState ^ keyState0
	keyTurnOn = keyChange & keyState0
	keyTurnOff = keyChange & (~keyState0)

	# debug
#	print( 'state:'  + getBitString(keyState0) + ' change:'  + getBitString(keyChange) + ' turnon:'  + getBitString(keyTurnOn) + ' turnoff:'  + getBitString(keyTurnOff) )

	keyState = keyState0

# check bit
def checkBit( target, bit ):
	ret = False
	if target & ( 1 << bit ):
		ret = True
	return ret

# print bit
def getBitString( target ):
	global KEYCODEMAX

	str = ''
	for keycode in range(KEYCODEMAX):
		ret = checkBit( target, keycode )
		if ret:
			str = '1' + str
		else:
			str = '0' + str
	return str

# send keycode
def sendKeycode():
	global kbd, Keycode, time, keyState, keyTurnOn, keyTurnOff

	# keycode: 0x00
	if checkBit( keyTurnOn, 0):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.W)
		kbd.send(Keycode.O)
		kbd.send(Keycode.O)
		kbd.send(Keycode.D)
		kbd.send(Keycode.S)
		kbd.send(Keycode.T)
		kbd.send(Keycode.O)
		kbd.send(Keycode.C)
		kbd.send(Keycode.K)
		kbd.send(Keycode.ENTER)

	# keycode: 0x01
	if checkBit( keyTurnOn, 1):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.P)
		kbd.send(Keycode.E)
		kbd.send(Keycode.P)
		kbd.send(Keycode.P)
		kbd.send(Keycode.E)
		kbd.send(Keycode.R)
		kbd.send(Keycode.O)
		kbd.send(Keycode.N)
		kbd.send(Keycode.I)
		kbd.send(Keycode.SPACE)
		kbd.send(Keycode.P)
		kbd.send(Keycode.I)
		kbd.send(Keycode.Z)
		kbd.send(Keycode.Z)
		kbd.send(Keycode.A)
		kbd.send(Keycode.ENTER)

	# keycode: 0x02
	if checkBit( keyTurnOn, 2):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.C)
		kbd.send(Keycode.O)
		kbd.send(Keycode.I)
		kbd.send(Keycode.N)
		kbd.send(Keycode.A)
		kbd.send(Keycode.G)
		kbd.send(Keycode.E)
		kbd.send(Keycode.ENTER)

	# keycode: 0x03
	if checkBit( keyTurnOn, 3):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.Q)
		kbd.send(Keycode.U)
		kbd.send(Keycode.A)
		kbd.send(Keycode.R)
		kbd.send(Keycode.R)
		kbd.send(Keycode.Y)
		kbd.send(Keycode.ENTER)

	# keycode: 0x04
	if checkBit( keyTurnOn, 4):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.B)
		kbd.send(Keycode.I)
		kbd.send(Keycode.G)
		kbd.send(Keycode.D)
		kbd.send(Keycode.A)
		kbd.send(Keycode.D)
		kbd.send(Keycode.D)
		kbd.send(Keycode.Y)
		kbd.send(Keycode.ENTER)

	# keycode: 0x05
	if checkBit( keyTurnOn, 5):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.P)
		kbd.send(Keycode.H)
		kbd.send(Keycode.O)
		kbd.send(Keycode.T)
		kbd.send(Keycode.O)
		kbd.send(Keycode.N)
		kbd.send(Keycode.SPACE)
		kbd.send(Keycode.M)
		kbd.send(Keycode.A)
		kbd.send(Keycode.N)
		kbd.send(Keycode.ENTER)

	# keycode: 0x06
	if checkBit( keyTurnOn, 6):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.E)
		kbd.send(Keycode.SHIFT, Keycode.MINUS)
		kbd.send(Keycode.M)
		kbd.send(Keycode.C)
		kbd.send(Keycode.TWO)
		kbd.send(Keycode.SPACE)
		kbd.send(Keycode.T)
		kbd.send(Keycode.R)
		kbd.send(Keycode.O)
		kbd.send(Keycode.O)
		kbd.send(Keycode.P)
		kbd.send(Keycode.E)
		kbd.send(Keycode.R)
		kbd.send(Keycode.ENTER)

	# keycode: 0x07
	if checkBit( keyTurnOn, 7):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.P)
		kbd.send(Keycode.O)
		kbd.send(Keycode.W)
		kbd.send(Keycode.ENTER)

	# keycode: 0x08
	if checkBit( keyTurnOn, 8):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.S)
		kbd.send(Keycode.T)
		kbd.send(Keycode.O)
		kbd.send(Keycode.R)
		kbd.send(Keycode.M)
		kbd.send(Keycode.B)
		kbd.send(Keycode.I)
		kbd.send(Keycode.L)
		kbd.send(Keycode.L)
		kbd.send(Keycode.Y)
		kbd.send(Keycode.ENTER)

	# keycode: 0x09
	if checkBit( keyTurnOn, 9):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.R)
		kbd.send(Keycode.E)
		kbd.send(Keycode.V)
		kbd.send(Keycode.E)
		kbd.send(Keycode.A)
		kbd.send(Keycode.L)
		kbd.send(Keycode.SPACE)
		kbd.send(Keycode.M)
		kbd.send(Keycode.A)
		kbd.send(Keycode.P)
		kbd.send(Keycode.ENTER)

	# keycode: 0x0a
	if checkBit( keyTurnOn, 10):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.R)
		kbd.send(Keycode.E)
		kbd.send(Keycode.V)
		kbd.send(Keycode.E)
		kbd.send(Keycode.A)
		kbd.send(Keycode.L)
		kbd.send(Keycode.SPACE)
		kbd.send(Keycode.M)
		kbd.send(Keycode.A)
		kbd.send(Keycode.P)
		kbd.send(Keycode.ENTER)

	# keycode: 0x0b
	if checkBit( keyTurnOn, 11):
		kbd.send(Keycode.ENTER)
		time.sleep(0.15)
		kbd.send(Keycode.N)
		kbd.send(Keycode.O)
		kbd.send(Keycode.SPACE)
		kbd.send(Keycode.F)
		kbd.send(Keycode.O)
		kbd.send(Keycode.G)
		kbd.send(Keycode.ENTER)

# Main
init()
while True:
	time.sleep(0.05)
	checkPin()
	sendKeycode()
