# Stereoscopic Video Creation from a Single Image

This guide explains a Python script that simulates a stereoscopic video effect using a single static image. Stereoscopic videos create the illusion of depth by presenting two slightly different images to each of the viewer's eyes.

## Requirements

To run this script, you need Python installed on your system along with the following libraries:
- PIL (Python Imaging Library): For image manipulation.
- OpenCV: For video processing.
- numpy: For handling image data.

You can install these with the following command:
```bash
pip install pillow opencv-python numpy
```

## Script Breakdown

### Importing Libraries

```python
from PIL import Image
import cv2
import numpy as np
```

- `PIL` is used for basic image operations like opening and transforming images.
- `cv2` (OpenCV) is used for creating and manipulating video files.
- `numpy` is used to convert images into a format that OpenCV can work with.

### Function Definition

```python
def create_stereoscopic_video(image_path, output_path, shift=5, duration=10, fps=30):
```

This function takes the following parameters:
- `image_path`: Path to the input image.
- `output_path`: Path where the output video will be saved.
- `shift`: Number of pixels to shift the image for creating the stereoscopic effect. Default is 5 pixels.
- `duration`: Duration of the video in seconds.
- `fps`: Frames per second in the output video.

### Loading and Manipulating the Image

```python
image = Image.open(image_path)
left_image = image.copy().transform(image.size, Image.AFFINE, (1, 0, shift, 0, 1, 0))
right_image = image.copy().transform(image.size, Image.AFFINE, (1, 0, -shift, 0, 1, 0))
```

- The image is opened and two copies are made: one shifted to the left and the other to the right using an affine transformation.

### Creating the Video

```python
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_path, fourcc, fps, (left_image_np.shape[1], left_image_np.shape[0]))
```

- A `VideoWriter` object is created with the specified codec (`mp4v`), frame rate, and dimensions.

### Generating Video Frames

```python
for _ in range(duration * fps):
    video.write(left_image_np if _ % 2 == 0 else right_image_np)
```

- Frames are added to the video by alternating between the left and right shifted images.

### Finalizing the Video

```python
video.release()
```

- The video file is finalized and saved to the specified output path.

## Usage Example

```python
create_stereoscopic_video('path_to_your_image.jpg', 'output_video.mp4')
```

This function call will generate a video named `output_video.mp4` using the image at `path_to_your_image.jpg`, shifting images by 5 pixels, running for 10 seconds at 30 fps.

## Conclusion

This script provides a basic implementation of a stereoscopic effect using Python. For more advanced and realistic 3D effects, further sophisticated techniques would be required.
