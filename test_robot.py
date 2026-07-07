import time
from robot.serial_controller import RobotController

robot = RobotController(port="COM9")

robot.move_forward()

time.sleep(3)

robot.stop()