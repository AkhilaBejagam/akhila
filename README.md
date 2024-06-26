##  Histogram of an Image
   Defination: An image histogram is a type of histogram that acts as a graphical representation of the tonal distribution in a digital image. It plots the number of pixels for each tonal value. By
         looking at the histogram for a specific image a viewer will be able to judge the entire tonal distribution at a glance.

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

  

    
  

## Webcam

A webcam is a video camera that is connected to a computer or other device, typically via a USB port, and is used to capture and transmit video over the internet.

uses of webcam

1.Live Streaming

2.Motion Capture

3.Video Recording

## Required libraries

  open cv

## program    

 1.  imports the OpenCV library, which is a popular library used for computer vision tasks.

         import cv2
     
 2. cv2.VideoCapture(0):It initializes a video capture object. The argument 0 specifies that the default camera should be used for capturing video. If you have multiple cameras connected,

        you can specify the index of the camera you want to use 

               video = cv2.VideoCapture(0)

  3. it checks  the video capture object is successfully initialized. If it fails to initialize, it prints an error.
     
         if (video.isOpened() == False):  
 
         print("Error reading video file")
     
 4. Defining the size ( width & height) of the vedio frame
    
        frame_width = int(video.get(3))
    
        frame_height = int(video.get(4)) 
   
        size = (frame_width, frame_height)

5. The output is saved in filename.avi 
   

    result = cv2.VideoWriter('cam.avi',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 

6. Now, here in the while loop it captures each  frames from the video stream until a break condition is met.
    
     while(True): 

    ret, frame = video.read()
   
 7. It checks the frames was read successfully
  
    if ret == True:  
  
8.result.write(frame): If a frame was successfully read, this line writes the frame to the output video file using the write() method of the VideoWriter object.

        result.write(frame)
   
        cv2.imshow('Frame', frame) 

        if cv2.waitKey(1) & 0xFF == ord('s'): 
            break
  
    else: 
        break

video.release() 

9.resultrelease(): VideoWriter object, ensuring that the output video file is properly closed.

result.release() 

10. close all the frame
    
cv2.destroyAllWindows() 
   
print("The video was successfully saved") 

## output

https://github.com/AkhilaBejagam/akhila/assets/169047515/64f27fe7-3ac8-46cc-ae8d-b9d4f8d876d1

## print10numbers

Here the program explains about printing of first 10 numbers and in each iteration ,printing the sum of current and previous number

num = list(range(10))

       It create a list called num containing numbers from 0 to 9 using the range()
       
previousNum = 0

         Then, it initializes a variable previousNum to 0.
         
for i in num:

          Next,it enter in to a for loop where it iterates through each element  i in the list num
          
    sum = previousNum + i
    
          Inside the loop, it calculates the sum of the current number i and the previous number previousNum, stores it in a variable called sum,
          
    print('Current Number '+ str(i) + 'Previous Number' + str(previousNum) + 'is ' + str(sum))
    
           Then it prints out  that includes the current number, the previous number, and the sum.
           
    previousNum= i

    Finally, it updates the previousNum variable to be equal to the current number i before moving to the next iteration of the loop.

   ## Output of the program

Current Number 0Previous Number0is 0

Current Number 1Previous Number0is 1

Current Number 2Previous Number1is 3

Current Number 3Previous Number2is 5

Current Number 4Previous Number3is 7

Current Number 5Previous Number4is 9

Current Number 6Previous Number5is 11

Current Number 7Previous Number6is 13

Current Number 8Previous Number7is 15

Current Number 9Previous Number8is 17
   

       


## Boundingboxes
 A bounding box, also known as a bounding volume or bounding region, is a geometric shape that encloses or surrounds an object or a group of objects in a digital image.

 ## Use of Boundingboxes
 Allowing machine learning models to identify and localize objects within an image

## Required libraries

    os - The os library in Python provides a way to interact with the operating system, allowing you to perform various tasks related to file and directory manipulation, environment variables, and           system information retrieval
    
    csv - CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database 
    
    pil - PIL stands for Python Imaging Library, and it's the original library that enabled Python to deal with images

    ## progam
    
1. import libraries
   
     import os

     import csv

    from PIL import Image,ImageDraw
   
2. Reading the  paths

csv_file = "/home/akhila-bejagam/Downloads/7622202030987_bounding_box.csv"

image_dir = "/home/akhila-bejagam/Downloads/7622202030987"

output_dir = "/home/akhila-bejagam/Downloads/7622202030987_with_boxes"
 
3. Directory creation
    
os.makedirs(output_dir, exist_ok=True)


4.specifying draw_boxes,crop _image function

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
    
5. processing csv file

   with open(csv_file, 'r') as file:

    csv_reader = csv.DictReader(file)
   
  6. Iterates over each row in the CSV file. For each row:
  
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

       7.  Images are saved using the save()


        
   ## input

   ![7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/AkhilaBejagam/akhila/assets/169047515/dd9fea9a-f284-49f3-84d1-d1cc591750a2)

   



   ## output 1 Draw box

   ![full_7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/AkhilaBejagam/akhila/assets/169047515/ff067dbe-9bb7-4e94-8e12-6d896f3f5200)



    

   ## output 2 crop image

   ![0_7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/AkhilaBejagam/akhila/assets/169047515/cd29b10f-8a2a-4e7f-8617-4c2f3b202013)

  
    



    

     






