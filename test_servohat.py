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
    pw_min = 1000
    pw_max = 2000
    actuation_range = 180
    try:
        opts, args = getopt.getopt(argv,"hs:a:m:M:r:",["servo=","angle=","min=","max=","range="])
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

    kit.servo[servo].actuation_range = actuation_range
    kit.servo[servo].set_pulse_width_range(pw_min, pw_max)
    kit.servo[servo].angle = angle


if __name__ == "__main__":
    main(sys.argv[1:])
