from __future__ import absolute_import, division
from .controller import Controller

class Z812B(Controller):
  """
  A controller for a Z812B stage.
  """
  def __init__(self,*args, **kwargs):
    super(Z812B, self).__init__(*args, **kwargs)

    # http://www.thorlabs.co.uk/thorProduct.cfm?partNumber=MTS50/M-Z8
    # Note that these values are pulled from the APT User software,
    # as they agree with the real limits of the stage better than
    # what the website or the user manual states
    self.max_velocity = 0.26
    self.max_acceleration = 0.40

    # from website:
    # steps per revolution: 512
    # gearbox ratio: 67
    # pitch: 1 mm
    # thus to advance 1 mm you need to turn 48*256*2 times
    enccnt = 512*67
    T = 2048/6e6

    # these equations are taken from the APT protocol manual
    self.position_scale = enccnt
    self.velocity_scale = enccnt * T * 65536
    self.acceleration_scale = enccnt * T * T * 65536

    self.linear_range = (0,12)

