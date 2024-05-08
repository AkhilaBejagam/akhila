##  Histogram

   Defination: A histogram is a type of chart that shows the frequency distribution of data points across a continuous range of numerical values.
   
 ## Uses of Histogram
    1. Image Processing
    
    2. Data Analysis
    
    3.Machine Learning

 ## Install Following Packages
 
    numpy, opencv, matplotlib
  
    pip install numpy opencv-python matplotlib
 
## Example Program

1.import libraries

    import numpy as np

    import cv2 as cv

    from matplotlib import pyplot as plt

2. Read Image: It reads an image from the specified file path  using OpenCV's imread() function
 
      img = cv.imread("/home/akhila-bejagam/Downloads/nature.jpeg")

3. Write Image :It writes the read image to another location using OpenCV's imwrite() function
 
      cv.imwrite("/home/akhila-bejagam/Desktop/experiment/n.jpeg",img)

4. Assertion: It  check if the image is successfully read. If the image is not read (i.e., img is None), it raises an assertion error with the message "file could not be read,check with os.path.exists()".
 
      assert img is not None, "file could not be read,check with os.path.exists()"

 5.Histogram Calculation and Plotting: It calculates the histogram for each color channel rgb using OpenCV's calcHist() function.
 
        color = ('b','g','r')

        for i, col in enumerate(color):

         histr = cv.calcHist([img],[i],None,[256],[0,256])
 
 6.The histograms are then plotted using Matplotlib's plot() function
 
       plt.plot(histr,color=col)

       plt.xlim([0,256])

7.Display Histograms: Matplotlib's show() function is used to display the plotted histograms.

         plt.show()
  
  ## Input

  ![nature](https://github.com/AkhilaBejagam/akhila/assets/169047515/06e0e9e9-7cf8-4fc2-9219-e981481176c9)

  ## output 

  ![histogram](https://github.com/AkhilaBejagam/akhila/assets/169047515/4ea5cadc-be3a-42dc-8892-13cc570e894c)

  

    
  

## capturevedio
```
# import the opencv library 
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()
```
## print10numbers
```
num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number' + str(previousNum) + 'is ' + str(sum))
    previousNum= i
```

## boundingboxes
```
import os
import csv
from PIL import Image,ImageDraw
csv_file = "/home/akhila-bejagam/Downloads/7622202030987_bounding_box.csv"
image_dir = "/home/akhila-bejagam/Downloads/7622202030987"
output_dir = "/home/akhila-bejagam/Downloads/7622202030987_with_boxes"
os.makedirs(output_dir, exist_ok=True)


def draw_boxes(image, boxes):
    draw = ImageDraw.Draw(image)
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        draw.rectangle([left, top, right, bottom], outline="red")
    return image
def crop_image(image, boxes):
    cropped_images = []
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        cropped_img = image.crop((left, top, right, bottom))
        cropped_images.append(cropped_img)
    return cropped_images


with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        image_name = row['filename']
        image_path = os.path.join(image_dir, image_name)
        output_path = os.path.join(output_dir, image_name)
        image = Image.open(image_path)
        boxes = [{'left': row['xmin'], 'top': row['ymin'], 'right': row['xmax'], 'bottom': row['ymax']}]
        cropped_images = crop_image(image, boxes)
        for i, cropped_img in enumerate(cropped_images):
            cropped_img.save(os.path.join(output_dir, f"{i}_{image_name}"))  
        full_image_with_boxes = draw_boxes(image, boxes)
        full_image_with_boxes.save(os.path.join(output_dir, f"full_{image_name}"))
```





