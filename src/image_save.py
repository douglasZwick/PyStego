from PIL import Image


def save_image(img: Image.Image, output_path: str) -> None:
  img.save(output_path)
