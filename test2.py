import picamera
import time

# Set the output file path
output_path = '/path/to/your/output/video.h264'

# Set the video duration in seconds
video_duration = 2


camera = picamera.PiCamera()
# Set the resolution (optional)
camera.resolution = (1920, 1080)  # Adjust the resolution as needed

# Start recording to the specified path
camera.start_recording(output_path)

# Record for the specified duration
time.sleep(video_duration)

# Stop recording
camera.stop_recording()

camera.close()



#if the first frame has a big enough difference with the last then start recroding else delete and do it again
