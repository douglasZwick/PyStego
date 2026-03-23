"""
config.py
| **Author:** Doug Zwick
| **Last edited:** March 23, 2026

Defines the Config class, which stores configuration settings to be used by a
Codec instance. See codec.py for details.
"""


ChannelBits = tuple[int, int, int]
Bands = tuple[str, str, str]


class Config:
  """
  Stores configuration settings for a Codec instance.

  **Static Data:**
  - SUPPORTED_BANDS *(list[tuple[str, str, str]])*: A list of all supported
    "bands" image configurations. If an image's bands aren't in this list, it
    cannot be used.
  
  **Instance Data:**
  - bits_per_channel *(tuple[int, int, int])*: Defines how many bits of data
    should be read from or encoded into a single pixel, per band. The standard
    band order is R, G, B. For example, `(1, 1, 2)` indicates an encoding with
    one bit of data in the red band, one bit in the green band, and two bits in
    the blue band.
  - start_pixel *(int)*: Where in the image the reading or writing process
    should start. The image is considered as a one-dimensional list of pixels,
    starting at zero in the top-left corner.
  """
  SUPPORTED_BANDS: list[Bands] = [
    ("R", "G", "B"),
  ]

  bits_per_channel: ChannelBits
  start_pixel: int

  def __init__(self, bits_per_channel: ChannelBits, start_pixel: int = 0) -> None:
    self.bits_per_channel = bits_per_channel
    self.start_pixel = start_pixel
