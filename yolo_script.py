from ultralytics import YOLO
from pathlib import Path
import cv2
import random
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import argparse
model = YOLO("yolov8m-seg.pt")



class mask_image:
    def __init__(self, image_path, class_label, output_path):
        self.image_path = image_path
        self.class_label = class_label
        self.image = cv2.imread(image_path)
        self.class_id = None
        self.output_path = output_path
        self.whole_prediction()
        self.mask_image()
        self.save_image()

    #Predict all the labels
    def whole_prediction(self):
        self.results = model.predict(self.image)

    # Mask the image
    def mask_image(self):
        colors = random.choices(range(256), k=3)
        yolo_classes = list(model.names.values())
        for i in yolo_classes:
            if i == self.class_label:
                self.class_id = yolo_classes.index(i)
                break
        print(self.class_id)
        for result in self.results:
            for i, (mask, box) in enumerate(zip(result.masks.xy, result.boxes)):
                points = np.int32([mask])
                if self.class_id == int(box.cls[0]):
                    cv2.fillPoly(self.image, points, colors)
        window_name = 'image'

        # Using cv2.imshow() method
        # Displaying the image
        cv2.imshow(window_name, self.image)
        cv2.imwrite(self.output_path, self.image)

        # waits for user to press any key
        # (this is necessary to avoid Python kernel form crashing)
        cv2.waitKey(0)

        # closing all open windows
        cv2.destroyAllWindows()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Segment objects of a specific class from an image.')

    # Add arguments
    parser.add_argument('--image', type=str, required=True, help='Path to the input image')
    parser.add_argument('--class', type=str, required=True, help='Class label to segment from the image')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output image')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the arguments
    image_path = args.image
    class_label = getattr(args, 'class')
    output_path = args.output


    # Print the input and output paths for confirmation
    print(f"Input image: {image_path}")
    print(f"Class label: {class_label}")
    print(f"Output image: {output_path}")
    m = mask_image(image_path, class_label, output_path)
