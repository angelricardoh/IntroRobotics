"""
Example to move robot forward for 10 seconds
Use "python3 run.py [--sim] example1" to execute
"""
from my_robot import MyRobot


class Run:
    def __init__(self, factory):
        """Constructor.

        Args:
            factory (factory.FactoryCreate)
        """
        self.create = factory.create_create()
        self.time = factory.create_time_helper()
        self.my_robot = MyRobot(self.create, self.time)

    def run(self):
        self.create.start()
        self.create.safe()

        # forward
        self.my_robot.forward(1, 0.1)

        # forward & backward
        self.my_robot.backward(1, 0.1)

        # turn left
        self.my_robot.turn_left(1, 0.182)
        self.my_robot.forward(1, 0.1)

        # turn right
        self.my_robot.turn_right(1, 0.182)
        self.my_robot.forward(1, 0.1)
        self.my_robot.turn_right(1, 0.182)

        # drive and stop in 10 seg
        self.create.drive_direct(100, 100)
        self.my_robot.stop(10)

        # drive and stop inmediately
        self.my_robot.turn_right(1, 0.182)
        self.create.drive_direct(100, 100)
        self.my_robot.stop()

