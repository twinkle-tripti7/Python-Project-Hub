from PIL import Image, ImageFilter
import os


def apply_filter(image_path, filter_type):
    with Image.open(image_path) as img:
        if filter_type == 'BLUR':
            filtered_image = img.filter(ImageFilter.BLUR)
        elif filter_type == 'SHARPEN':
            filtered_image = img.filter(ImageFilter.SHARPEN)
        elif filter_type == 'CONTOUR':
            filtered_image = img.filter(ImageFilter.CONTOUR)
        elif filter_type == 'DETAIL':
            filtered_image = img.filter(ImageFilter.DETAIL)
        elif filter_type == 'GRAYSCALE':
            filtered_image = img.convert('L')
        else:
            print("Invalid filter type.")
            return None

        return filtered_image


def save_image(image, output_path):
    image.save(output_path)
    print(f"Saved filtered image to: {output_path}")


def main():
    input_path = input("Enter the path of the image file: ")

    if not os.path.exists(input_path):
        print("The specified file does not exist.")
        return

    print("Available filters: BLUR, SHARPEN, CONTOUR, DETAIL, GRAYSCALE")
    filter_type = input("Enter the filter type you want to apply: ").upper()

    filtered_image = apply_filter(input_path, filter_type)

    if filtered_image:
        output_path = input("Enter the output path to save the filtered image (including filename): ")
        save_image(filtered_image, output_path)


if __name__ == '__main__':
    main()


