# Avataar.ai-Assignment
## Problem statement
Problem Statement: Edit pose of an object in a scene
Recent advancement in generative AI has led to a development of a lot of creative workflows. One
such workflow is to use generative AI techniques for editing product photographs after they have
been shot at a studio, for example to polish the scene for displaying the product on an e-commerce
website. One such post-production editing requirement could be editing the pose of the object by
rotating it within the same scene.
This problem statement involves two tasks - for the eventual goal of developing technology for a
user-friendly pose edit functionality. The first task is to segment an object (defined by a user given
class prompt) in a given scene. This enables the ‘user-friendly’ part of the problem statement. The
second task is to edit the pose of the object by taking user poses (e.g. Azimuth +10 degrees, Polar -5
degrees). The final generated scene should look realistic and composite.
Note: We do not expect you to train or fine-tune your own models, but use existing models (including
the amazing one you have in your skull) and creatively find solutions to the two tasks.
### Tasks.
Task 1 : This task is to write an executable code that takes the input scene and the text prompt
from the command line argument and outputs an image with a red mask on all pixels where
the object (denoted in the text prompt) was present.

##### Installations
1. Create a virtual environment in your system.
2. Downnload the repository (either by git clone or zip download). You can use the git clone command and follow the given instructions -
  ```
git clone https://github.com/Amartya-pixel/Avataar.ai-Assignment.git
cd Avataar.ai-Assignment/
```
3. Install the required dependencies using the given below command.
   ```
   pip install -r requirements.txt
   ```
4. Install the yolov8 model check points. The script uses "yolov8m-seg.pt" check points. Use this link ``` https://docs.ultralytics.com/models/yolov8/#key-features``` for download.
5. Place the data in the respective folder.
6. Run the command.
```
python yolo_script.py --image ./example.jpg --class "chair" --output ./generated.png
```

## Output
![Chair]([https://github.com/username/repository/raw/main/image.jpg](https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/main/assets/images/chair.jpg))

