import time
import numpy as np
from PIL import ImageGrab
from PIL import Image
import PiCamera


# Initialize the PiCamera
camera = PiCamera()

# Capture the first image
camera.capture('/path/to/screenshot1.jpg')
time.sleep(3)

# Capture the second image
camera.capture('/path/to/screenshot2.jpg')

#after the raspberry pi has recorded it looks at how different the first and last frames were


screenshot1_path = r"C:\Users\fhh19\OneDrive\Documents\fred's folder\backup\fredpythonprojects_old2\python_school\raspberry_pi_school\img\screenshot1.png"
screenshot = ImageGrab.grab()
screenshot.save(screenshot1_path)

time.sleep(3)

screenshot2_path = r"C:\Users\fhh19\OneDrive\Documents\fred's folder\backup\fredpythonprojects_old2\python_school\raspberry_pi_school\img\screenshot2.png"
screenshot = ImageGrab.grab()
screenshot.save(screenshot2_path)



# Open the screenshot and the reference image
screenshot_img = Image.open(screenshot1_path)
reference_img = Image.open(screenshot2_path)

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




#if the first frame has a big enough difference with the last then start recording else delete and do it again
