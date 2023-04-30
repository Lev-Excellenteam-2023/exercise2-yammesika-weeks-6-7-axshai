import PIL.Image

IMAGE_PATH = r"code.png"
BLACK_RGB_VAL = (1, 1, 1)


def decode_code_from_image(image_path):
    """
     Decodes a code from an image file.
    :param image_path: The path to the image file.
    :return: The encrypted string in the image
    """
    with PIL.Image.open(image_path) as image:
        image = image.convert('RGB')
        width = image.size[0]
        height = image.size[1]
        black_pixels_chr = [chr(line) for column in range(width) for line in range(height) if
                            image.getpixel((column, line)) == BLACK_RGB_VAL]
        return "".join(black_pixels_chr)


if __name__ == "__main__":
    print(decode_code_from_image(IMAGE_PATH))
