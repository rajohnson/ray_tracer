import collections
import tqdm

RGB = collections.namedtuple("RGB", "r g b")


def output_ppm(filename: str, image: list[list[RGB]], max_intensity: int = 255) -> None:
    image_width = len(image[0])
    image_height = len(image)

    with open(filename, "w") as f:
        f.write("P3\n")
        f.write(f"{image_width} {image_height}\n")
        f.write(f"{max_intensity}\n")
        for row in tqdm.tqdm(image):
            for pixel in row:
                f.write(
                    f"{int(pixel.r * max_intensity)} {int(pixel.g* max_intensity)} {int(pixel.b* max_intensity)}\n"
                )


if __name__ == "__main__":

    img_width = 256
    img_height = 256

    image = [
        [RGB(r / img_width, g / img_height, 0) for r in range(img_width)]
        for g in range(img_height)
    ]
    output_ppm("output.ppm", image)
