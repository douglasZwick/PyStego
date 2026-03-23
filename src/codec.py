"""
codec.py
| **Author:** Doug Zwick
| **Last edited:** March 23, 2026

Defines the Codec class, which does all the encoding and decoding (i.e., all
the steganography).
"""


from PIL import Image
from config import Config


class Codec:
  """
  Handles the decoding and encoding of data from and into Image objects.
  
  **Instance Data:**
  - config *(Config)*: A Config object that stores configuration settings for
    this Codec instance. See config.py for details.
  - mounted_image *(Image.Image)*: The Image object from and to which to read
    and write.
  """
  config: Config
  mounted_img: Image.Image | None


  def __init__(self, config: Config) -> None:
    """
    **Parameters:**
    - config *(Config)*: A Config object that defines the configuration
      settings that this codec instance will use. See config.py for details.
    """
    self.config = config
    self.mounted_img = None


  def load_image(self, img_path: str) -> None:
    img = Image.open(img_path)
    bands = img.getbands()
    if bands not in self.config.SUPPORTED_BANDS:
      raise ValueError(f"Images with bands {bands} are not supported");

    self.mounted_img = img

  
  def encode_int(self, payload: int) -> None:
    """
    Encodes a single integer into the given Image object.
    
    **Parameters:**
    - img: *(Image.Image)*: The image into which to encode the payload
    - payload: *(int)*: An integer to encode into the given image
    """
    raise NotImplementedError()


  def decode_int(self) -> int:
    raise NotImplementedError()
