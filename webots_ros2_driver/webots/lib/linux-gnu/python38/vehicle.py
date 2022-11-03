# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import sys
import os
if os.name == 'nt' and sys.version_info >= (3, 8):  # we need to explicitly list the folders containing the DLLs
    webots_home = os.environ['WEBOTS_HOME']
    os.add_dll_directory(os.path.join(webots_home, 'lib', 'controller'))
# MSYS2_HOME should be set by Webots or ~/.bash_profile
# if not set, we are in the case of an extern controller and a regularly installed version of Webots
    msys64_root = os.environ['MSYS2_HOME'] if 'MSYS2_HOME' in os.environ else os.path.join(webots_home, 'msys64')
    cpp_folder = os.path.join(msys64_root, 'mingw64', 'bin', 'cpp')
    if not os.path.isdir(cpp_folder):  # development environment
        cpp_folder = os.path.join(msys64_root, 'mingw64', 'bin')
    os.add_dll_directory(cpp_folder)



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _vehicle
else:
    import _vehicle

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import controller
class Driver(controller.Supervisor):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    INDICATOR_OFF = _vehicle.Driver_INDICATOR_OFF
    INDICATOR_RIGHT = _vehicle.Driver_INDICATOR_RIGHT
    INDICATOR_LEFT = _vehicle.Driver_INDICATOR_LEFT
    SPEED = _vehicle.Driver_SPEED
    TORQUE = _vehicle.Driver_TORQUE
    DOWN = _vehicle.Driver_DOWN
    SLOW = _vehicle.Driver_SLOW
    NORMAL = _vehicle.Driver_NORMAL
    FAST = _vehicle.Driver_FAST

    def __init__(self):
        _vehicle.Driver_swiginit(self, _vehicle.new_Driver())

    @staticmethod
    def getDriverInstance():
        return _vehicle.Driver_getDriverInstance()
    __swig_destroy__ = _vehicle.delete_Driver

    @staticmethod
    def isInitialisationPossible():
        return _vehicle.Driver_isInitialisationPossible()

    def step(self):
        return _vehicle.Driver_step(self)

    def setSteeringAngle(self, steeringAngle):
        return _vehicle.Driver_setSteeringAngle(self, steeringAngle)

    def getSteeringAngle(self):
        return _vehicle.Driver_getSteeringAngle(self)

    def setCruisingSpeed(self, speed):
        return _vehicle.Driver_setCruisingSpeed(self, speed)

    def getTargetCruisingSpeed(self):
        return _vehicle.Driver_getTargetCruisingSpeed(self)

    def getCurrentSpeed(self):
        return _vehicle.Driver_getCurrentSpeed(self)

    def setThrottle(self, throttle):
        return _vehicle.Driver_setThrottle(self, throttle)

    def getThrottle(self):
        return _vehicle.Driver_getThrottle(self)

    def setBrakeIntensity(self, intensity):
        return _vehicle.Driver_setBrakeIntensity(self, intensity)

    def getBrakeIntensity(self):
        return _vehicle.Driver_getBrakeIntensity(self)

    def setIndicator(self, state):
        return _vehicle.Driver_setIndicator(self, state)

    def setHazardFlashers(self, state):
        return _vehicle.Driver_setHazardFlashers(self, state)

    def getIndicator(self):
        return _vehicle.Driver_getIndicator(self)

    def getHazardFlashers(self):
        return _vehicle.Driver_getHazardFlashers(self)

    def setDippedBeams(self, state):
        return _vehicle.Driver_setDippedBeams(self, state)

    def setAntifogLights(self, state):
        return _vehicle.Driver_setAntifogLights(self, state)

    def getDippedBeams(self):
        return _vehicle.Driver_getDippedBeams(self)

    def getAntifogLights(self):
        return _vehicle.Driver_getAntifogLights(self)

    def getRpm(self):
        return _vehicle.Driver_getRpm(self)

    def getGear(self):
        return _vehicle.Driver_getGear(self)

    def setGear(self, gear):
        return _vehicle.Driver_setGear(self, gear)

    def getGearNumber(self):
        return _vehicle.Driver_getGearNumber(self)

    def getControlMode(self):
        return _vehicle.Driver_getControlMode(self)

    def setWiperMode(self, mode):
        return _vehicle.Driver_setWiperMode(self, mode)

    def getWiperMode(self):
        return _vehicle.Driver_getWiperMode(self)

    def setBrake(self, brake):
        return _vehicle.Driver_setBrake(self, brake)

    def setWipersMode(self, mode):
        return _vehicle.Driver_setWipersMode(self, mode)

    def getWipersMode(self):
        return _vehicle.Driver_getWipersMode(self)

# Register Driver in _vehicle:
_vehicle.Driver_swigregister(Driver)

def Driver_getDriverInstance():
    return _vehicle.Driver_getDriverInstance()

def Driver_isInitialisationPossible():
    return _vehicle.Driver_isInitialisationPossible()

class Car(Driver):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    TRACTION = _vehicle.Car_TRACTION
    PROPULSION = _vehicle.Car_PROPULSION
    FOUR_BY_FOUR = _vehicle.Car_FOUR_BY_FOUR
    COMBUSTION_ENGINE = _vehicle.Car_COMBUSTION_ENGINE
    ELECTRIC_ENGINE = _vehicle.Car_ELECTRIC_ENGINE
    PARALLEL_HYBRID_ENGINE = _vehicle.Car_PARALLEL_HYBRID_ENGINE
    POWER_SPLIT_HYBRID_ENGINE = _vehicle.Car_POWER_SPLIT_HYBRID_ENGINE
    WHEEL_FRONT_RIGHT = _vehicle.Car_WHEEL_FRONT_RIGHT
    WHEEL_FRONT_LEFT = _vehicle.Car_WHEEL_FRONT_LEFT
    WHEEL_REAR_RIGHT = _vehicle.Car_WHEEL_REAR_RIGHT
    WHEEL_REAR_LEFT = _vehicle.Car_WHEEL_REAR_LEFT
    WHEEL_NB = _vehicle.Car_WHEEL_NB

    def __init__(self):
        _vehicle.Car_swiginit(self, _vehicle.new_Car())
    __swig_destroy__ = _vehicle.delete_Car

    def getType(self):
        return _vehicle.Car_getType(self)

    def getEngineType(self):
        return _vehicle.Car_getEngineType(self)

    def setIndicatorPeriod(self, period):
        return _vehicle.Car_setIndicatorPeriod(self, period)

    def getIndicatorPeriod(self):
        return _vehicle.Car_getIndicatorPeriod(self)

    def getBackwardsLights(self):
        return _vehicle.Car_getBackwardsLights(self)

    def getBrakeLights(self):
        return _vehicle.Car_getBrakeLights(self)

    def getTrackFront(self):
        return _vehicle.Car_getTrackFront(self)

    def getTrackRear(self):
        return _vehicle.Car_getTrackRear(self)

    def getWheelbase(self):
        return _vehicle.Car_getWheelbase(self)

    def getFrontWheelRadius(self):
        return _vehicle.Car_getFrontWheelRadius(self)

    def getRearWheelRadius(self):
        return _vehicle.Car_getRearWheelRadius(self)

    def getWheelEncoder(self, wheel):
        return _vehicle.Car_getWheelEncoder(self, wheel)

    def getWheelSpeed(self, wheel):
        return _vehicle.Car_getWheelSpeed(self, wheel)

    def setLeftSteeringAngle(self, angle):
        return _vehicle.Car_setLeftSteeringAngle(self, angle)

    def setRightSteeringAngle(self, angle):
        return _vehicle.Car_setRightSteeringAngle(self, angle)

    def getRightSteeringAngle(self):
        return _vehicle.Car_getRightSteeringAngle(self)

    def getLeftSteeringAngle(self):
        return _vehicle.Car_getLeftSteeringAngle(self)

    def enableLimitedSlipDifferential(self, enable):
        return _vehicle.Car_enableLimitedSlipDifferential(self, enable)

    def enableIndicatorAutoDisabling(self, enable):
        return _vehicle.Car_enableIndicatorAutoDisabling(self, enable)

# Register Car in _vehicle:
_vehicle.Car_swigregister(Car)



