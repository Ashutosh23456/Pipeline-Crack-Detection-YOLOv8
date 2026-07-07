import serial
import time


class RobotController:

    def __init__(self, port="COM9", baudrate=9600):

        self.serial = serial.Serial(port, baudrate, timeout=1)

        time.sleep(2)

        print("Arduino Connected")

    def send(self, command):

        self.serial.write((command + "\n").encode())

        print("Sent:", command)

    def move_forward(self):

        self.send("F")

    def move_backward(self):

        self.send("B")

    def turn_left(self):

        self.send("L")

    def turn_right(self):

        self.send("R")

    def stop(self):

        self.send("S")