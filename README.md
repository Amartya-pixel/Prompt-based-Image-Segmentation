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
Some examples of the generated outputs
<div align="center">
  <h2>One chair</h2>
   <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/b30964ea771f5c711442273fbaef4324f90410ac/assets/images/chair.jpg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/676eb450b150178bda25966de3456fc1bfee834a/assets/images/reconstructed.jpg" alt="Original" width="300" style="margin-right: 20px;">
  
</div>

<div align="center">
  <h2>Flower vase</h2>
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/74102fb2720655f6b9acd40b007e488c40dff8c3/assets/images/flower%20vase.jpg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/7b7a71bc5d8f7cc8ef86d6c5399967cde1f3fb56/assets/images/generated.png" alt="Segment 1" width="300" style="margin-right: 20px;">
</div>


<div align="center">
  <h2>Cat and dog</h2>
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/6a299fd94739a42c37ace517380fa6b31696312a/assets/images/cat_dog.jpg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/6a299fd94739a42c37ace517380fa6b31696312a/assets/images/reconstructed_cat.jpg" alt="Segment 1" width="300" style="margin-right: 20px;">
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/6a299fd94739a42c37ace517380fa6b31696312a/assets/images/reconstructed_dog.jpg" alt="Segment 2" width="300">
</div>

<div align="center">
  <h2>Some more real world application</h2>
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/0a4df38e527813dfae2e66f5d7f89dbe3a0095df/assets/images/my_example.jpg" alt="Original" width="300" style="margin-right: 20px;">
  <img src="https://github.com/Amartya-pixel/Avataar.ai-Assignment/blob/0a4df38e527813dfae2e66f5d7f89dbe3a0095df/assets/images/reconstructed_car.jpg" alt="Segment" width="300" style="margin-right: 20px;">
  
</div>

## References
[1.](https://docs.ultralytics.com/models/yolov8/#key-features)






