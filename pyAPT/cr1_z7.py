from __future__ import absolute_import, division
from .controller import Controller

class CR1_Z7(Controller):
  """
  A controller for a PRM1 rotation stage
  """
  def __init__(self,*args, **kwargs):
    super(PRM1, self).__init__(*args, **kwargs)

    # Same as for prm1 as initial guess
    # Note that these values should be pulled from the APT User software,
    # as they agree with the real limits of the stage better than
    # what the website or the user manual states
    self.max_velocity = 0.3 # units?
    self.max_acceleration = 0.3 # units?

    # from http://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=4134&pn=CR1-Z7#2446
    # encoder counts per revoultion of the motor output shaft: 48
    # max rotation velocity: 6deg/s
    # Gear ratio: 256 / 1
    # to move 1 deg: 48*256 rounds / 360 deg =  encoder steps
    # measured value: 1919.2689
    # There is an offset off 88.2deg -> enc(0) = 88.2deg
    enccnt = 34.1333

    T = 2048/6e6

    # these equations are taken from the APT protocol manual
    self.position_scale = enccnt  #the number of enccounts per deg
    self.velocity_scale = enccnt * T * 65536
    self.acceleration_scale = enccnt * T * T * 65536

    self.linear_range = (0,360)

