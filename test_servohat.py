import sys
import getopt
from adafruit_servokit import ServoKit
from time import sleep

# import board
# import busio
# import adafruit_pca9685
# i2c = busio.I2C(board.SCL, board.SDA)
# hat = adafruit_pca9685.PCA9685(i2c)

def main(argv):
    kit = ServoKit(channels=16)

    servo = 0
    angle = 0
    try:
        opts, args = getopt.getopt(argv,"hs:a:",["servo=","angle="])
    except getopt.GetoptError:
        print('test.py -s <servo> -a <angle>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -s <servo> -a <angle>')
            sys.exit()
        elif opt in ("-s", "--servo"):
            servo = int(arg)
        elif opt in ("-a", "--angle"):
            angle = int(arg)
        print('Servo: ', servo)
        print('Angle: ', angle)
                                                 

    # Tower Pro SG-5010
    # https://www.adafruit.com/product/155
    #
    # To control with an Arduino, we suggest connecting the orange control
    # wire to pin 9 or 10 and using the Servo library included with the
    # Arduino IDE (see here for an example sketch). Position "0" (1.5ms
    # pulse) is middle, "90" (~2ms pulse) is all the way to the right,
    # "-90" (~1ms pulse) is all the way to the left.
    #
    # Note that the default servo pulse widths (usually 1ms to 2ms) may
    # not give you a full 180 degrees of motion. In that case, check if
    # you can set your servo controller to custom pulse lengths and try
    # 0.75ms to 2.25ms. You can try shorter/longer pulses but be aware
    # that if you go too far you could break your servo!

    # Tower Pro SG-5010 
    kit.servo[0].activation_range = 180
    kit.servo[0].set_pulse_width_range(750, 2500)

    # kit.servo[0].angle = 180
    #sleep(2)
    #kit.servo[0].angle = 0

    kit.servo[servo].angle = angle


if __name__ == "__main__":
    main(sys.argv[1:])
