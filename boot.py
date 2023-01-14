import digitalio
import board
import storage
import usb_cdc

# if you want to develop, connect GP16 to GND ( be pressing switch of keycode 0x00 ) and boot pico
# curcuit memo
# GP16(PULLUP) - keycode:0x00 - DI(->) - GP22(OUT)

# check keycode 0x00
is_develop = False

pout = digitalio.DigitalInOut(board.GP22)
pout.direction = digitalio.Direction.OUTPUT
pout.value = False

pin = digitalio.DigitalInOut(board.GP16)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

if pin.value == False:
	is_develop = True

pout.deinit()
pin.deinit()

if is_develop == False:
	storage.disable_usb_drive()
	usb_cdc.disable()