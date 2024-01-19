import picamera
import time

# Set the output file path
output_path = '/path/to/your/output/video.h264'

# Set the video duration in seconds
video_duration = 10


#camera = picamera.PiCamera()

# Initialize the camera
with picamera.PiCamera() as camera:
    # Set the resolution (optional)
    camera.resolution = (1920, 1080)  # Adjust the resolution as needed

    # Start recording
    time.sleep(video_duration)

    # Record for the specified duration
    camera.wait_recording(video_duration)

    # Stop recording
    camera.stop_recording()
