import collections

RGB = collections.namedtuple("RGB", "r g b")


def output_ppm(filename: str, image: list[list[RGB]], max_intensity: int = 255) -> None:
    image_width = len(image[0])
    image_height = len(image)

    with open(filename, "w") as f:
        f.write("P3\n")
        f.write(f"{image_width} {image_height}\n")
        f.write(f"{max_intensity}\n")
        for row in image:
            for pixel in row:
                f.write(f"{pixel.r} {pixel.g} {pixel.b} ")
            f.write("\n")


if __name__ == "__main__":
    image = [
        [RGB(255, 0, 0), RGB(0, 255, 0), RGB(0, 0, 255)],
        [RGB(255, 255, 255), RGB(0, 0, 0), RGB(140, 140, 140)],
    ]
    output_ppm("output.ppm", image)
