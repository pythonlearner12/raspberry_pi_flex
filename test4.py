import time
import numpy as np
from picamera import PiCamera
from PIL import Image

# Initialize the PiCamera
camera = PiCamera()

# Capture the first image
camera.capture('/path/to/screenshot1.jpg')
time.sleep(3)

# Capture the second image
camera.capture('/path/to/screenshot2.jpg')

# Open the images
screenshot_img = Image.open('/path/to/screenshot1.jpg')
reference_img = Image.open('/path/to/screenshot2.jpg')

# Convert the images to arrays
screenshot_arr = np.array(screenshot_img)
reference_arr = np.array(reference_img)

# Calculate the absolute difference between the two images
diff_arr = np.abs(screenshot_arr - reference_arr)

# Create an image from the difference array
diff_img = Image.fromarray(diff_arr.astype(np.uint8))

# Calculate the root-mean-square (RMS) error
rms = np.sqrt(np.mean(diff_arr ** 2))

# Show the images and the difference image
screenshot_img.show()
reference_img.show()
diff_img.show()

print(rms)
