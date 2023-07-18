'''
Builder

The builder patterns aims to separate the construction of a complex object from its representation i.e. its actual class. Creation of the object will be achieved entirely through its relevant builder class.

Note that the class may have many different builders for different types of similar object. In the example below, the Robot class has an android builder and an autonomous car builder. Each will ensure the correct attributes are set on the final product e.g. the autonomous car is wheeled, with camera detection systems. The builder may also take in optional attributes like a name, if the main class / abstract classes allow it.
'''

from abc import ABC, abstractmethod


class Robot:

    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal:
            string += "BIPEDAL "
        if self.quadripedal:
            string += "QUADRIPEDAL "
        if self.flying:
            string += "FLYING ROBOT "
        if self.wheeled:
            string += "ROBOT ON WHEELS\n"
        else:
            string += "ROBOT\n"

        if self.traversal:
            string += "Traversal modules installed:\n"

        for module in self.traversal:
            string += "- " + str(module) + "\n"

        if self.detection_systems:
            string += "Detection systems installed:\n"

        for system in self.detection_systems:
            string += "- " + str(system) + "\n"

        return string


class BipedalLegs:
    def __str__(self):
        return "two legs"


class QuadripedalLegs:
    def __str__(self):
        return "four legs"


class Arms:
    def __str__(self):
        return "four legs"


class Wings:
    def __str__(self):
        return "wings"


class Blades:
    def __str__(self):
        return "blades"


class FourWheels:
    def __str__(self):
        return "four wheels"


class TwoWheels:
    def __str__(self):
        return "two wheels"


class CameraDetectionSystem:
    def __str__(self):
        return "cameras"


class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"


class RobotBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass


class AndroidBuilder(RobotBuilder):

    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())


class AutonomousCarBuilder(RobotBuilder):

    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.wheeled = True
        self.product.traversal.append(FourWheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())


class Director:

    def make_android(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


director = Director()
builder = AndroidBuilder()
object = director.make_android(builder)
print(object)
