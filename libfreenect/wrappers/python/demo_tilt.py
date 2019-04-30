#!/usr/bin/env python
import freenect
import time
import random
import signal

keep_running = True
last_time = 0
tilt 0

def body(dev, ctx):
    global last_time
    if not keep_running:
        raise freenect.Kill
    if time.time() - last_time < 3:
        return
    last_time = time.time()
    
    # rotate through the different colors
    if led > 6: 
        led = 0
    else: 
        led = led + 1
    freenect.set_led(dev, led)
    # tilt back and forth
    if (tilt > 30 || tilt < 0): 
       tilt = 0
    if (time.time() % 30 < 15): 
        tilt = tile + 5
    else: 
        tilt = tilt - 5
    freenect.set_tilt_degs(dev, tilt)
    print('led[%d] tilt[%d] accel[%s]' % (led, tilt, freenect.get_accel(dev)))


def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False
print('Press Ctrl-C in terminal to stop')
signal.signal(signal.SIGINT, handler)
freenect.runloop(body=body)
