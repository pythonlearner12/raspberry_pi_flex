import time
import numpy as np
from PIL import Image
from picamera import PiCamera


def capture_image(file_path):
    with PiCamera() as camera:
        # Adjust camera settings if needed (optional)
        # camera.resolution = (width, height)
        # camera.rotation = rotation_angle

        # Capture an image
        camera.capture(file_path)


def compare_images(img_path1, img_path2):
    screenshot_img = Image.open(img_path1)
    reference_img = Image.open(img_path2)

    # Convert the images to arrays
    screenshot_arr = np.array(screenshot_img)
    reference_arr = np.array(reference_img)

    diff_arr = np.abs(screenshot_arr - reference_arr)
    diff_img = Image.fromarray(diff_arr.astype(np.uint8))

    # Calculate the root-mean-square (RMS) error
    rms = np.sqrt(np.mean(diff_arr ** 2))

    screenshot_img.show()
    reference_img.show()
    diff_img.show()
    print(rms)

    return rms


while True:
    screenshot1_path = "/home/pi/screenshot1.jpg"
    screenshot2_path = "/home/pi/screenshot2.jpg"

    # Capture the first screenshot
    capture_image(screenshot1_path)

    time.sleep(1)

    # Capture the second screenshot
    capture_image(screenshot2_path)

    # Compare the images
    rms_difference = compare_images(screenshot1_path, screenshot2_path)

    # Example condition based on RMS difference
    if rms_difference > 0:

        with PiCamera() as camera:
            # Start recording a video
            camera.start_recording('video.h264')
            time.sleep(10)
            camera.stop_recording()

    else:
        print("No significant difference. Discarding images.")
