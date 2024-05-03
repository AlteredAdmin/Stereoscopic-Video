from PIL import Image
import cv2
import numpy as np

def create_stereoscopic_video(image_path, output_path, shift=5, duration=10, fps=30):
    # Load the image
    image = Image.open(image_path)

    # Create left and right images
    left_image = image.copy().transform(image.size, Image.AFFINE, (1, 0, shift, 0, 1, 0))
    right_image = image.copy().transform(image.size, Image.AFFINE, (1, 0, -shift, 0, 1, 0))

    # Convert images to numpy array for OpenCV
    left_image_np = np.array(left_image)
    right_image_np = np.array(right_image)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (left_image_np.shape[1], left_image_np.shape[0]))

    # Create frames for the video
    for _ in range(duration * fps):
        video.write(left_image_np if _ % 2 == 0 else right_image_np)

    # Release the video writer
    video.release()

# Example usage
create_stereoscopic_video('path_to_your_image.jpg', 'output_video.mp4')
