#!/usr/bin/env python
#
# Test script for controlling a servo motor via a raspberry pi servo hat.
#
# See:
# https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/overview
#

import sys
import getopt
from adafruit_servokit import ServoKit
from time import sleep

def main(argv):
    kit = ServoKit(channels=16)

    servo = 0
    angle = 0
    pw_min = 1000
    pw_max = 2000
    actuation_range = 180
    try:
        opts, args = getopt.getopt(argv,"hs:a:m:M:r:",["servo=","angle=","min=","max=","range="])
    except getopt.GetoptError:
        print('test_servohat.py -s <servo> -a <angle> -m <min_pw> -M <max_pw> -r <actuator_range>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test_servohat.py -s <servo> -a <angle> -m <min_pw> -M <max_pw> -r <actuator_range>')
            print('  -s <servo>   servo id number (0-15) on the servo hat')
            print('  -a <angle>   angle to drive servo to')
            print('  -m <min_pw>  minimum pulse width in microseconds (default 1000)')
            print('  -M <max_pw>  minimum pulse width in microseconds (default 2000)')
            print('  -r <range>   range of motion in degrees (default 180)')
            sys.exit()
        elif opt in ("-s", "--servo"):
            servo = int(arg)
        elif opt in ("-a", "--angle"):
            angle = int(arg)
        elif opt in ("-m", "--min"):
            pw_min = int(arg)
        elif opt in ("-M", "--max"):
            pw_max = int(arg)
        elif opt in ("-r", "--range"):
            actuation_range = int(arg)

    print('Servo: ', servo)
    print('Angle: ', angle)
    print('Actuation Range: ', actuation_range)
    print('Pulse Width Range: ', pw_min, "-", pw_max)

    # Tower Pro SG-5010 
    # https://www.adafruit.com/product/155
    # actuation_range = 180
    # set_pulse_width_range(750, 2400)
    # really only gets about 170 degrees total rotation

    # HiTec HS-785HB Servo
    # https://www.servocity.com/hs-785hb-servo
    # set_puse_range(685, 2070)
    # actuation_range = 2160 (6 * 360)
    # gets 6 full rotations, rated for up to 8 full rotations

    kit.servo[servo].actuation_range = actuation_range
    kit.servo[servo].set_pulse_width_range(pw_min, pw_max)
    kit.servo[servo].angle = angle


if __name__ == "__main__":
    main(sys.argv[1:])
