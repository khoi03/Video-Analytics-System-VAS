# Video Analytics System(VAS)

## Introduction
This task aims to create a simple web-based Video Analytics System (VAS) to analyze content from videos with the following inputs and outputs:
- **Input:**
   - Any YouTube video URL
   - Upload a video from a local computer
  
- **Ouput:** Analyzing basic video content and display results on the web while playing the video. For example:
   - Counting people and other objects in each frame and presenting the results synchronized while playing the video;
   - Illustrating a canvas that exhibits detected objects (bounding box and object name) in each frame, synchronized with the video.

## Table of contents:

1. [Approach](https://github.com/khoi03/Video-Analytics-System-VAS#1approach)

2. [To run VAS](https://github.com/khoi03/Video-Analytics-System-VAS#2-to-run-vas)

3. [Overview](https://github.com/khoi03/Video-Analytics-System-VAS#3overview)

   1. [UI](https://github.com/khoi03/Video-Analytics-System-VAS#i-ui)

   2. [Example results](https://github.com/khoi03/Video-Analytics-System-VAS#ii-example-results)
   
      1. [Example Video](https://github.com/khoi03/Video-Analytics-System-VAS#a-example-video)
         
      2. [Example URL 1](https://github.com/khoi03/Video-Analytics-System-VAS#b-example-url-1)

## 1. Approach
In this task, I utilize `Flask`, a Python framework, to develop a basic website, while employing `YOLOv8` model for content analysis in videos. Furthermore, in order to handle Youtube URLs, I employ `pytube` library for downloading YouTube Videos.
**Notably,** all results in the [Example results](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#iiexample-results) section were obtained using the nano YOLOv8 model(yolov8n.pt). Furthermore, if you have a strong GPU, you may consider using a larger YOLOv8 model, which provides more accurate predictions but takes longer to process.

## 2. To run VAS
I recommend creating an anaconda environment:
```
conda create --name vas python=3.9
```

Then, install Python requirements:
```
pip install -r requirements.txt
```
Finally, from the `vas` project root, run:
```
python app.py
```

## 3. Overview

### i. UI
This section illustrates the website's layout and its functions

- **Home page:**
![UI](/Media/UI.png)

- **Upload page:**
![UI1](/Media/UI1.png)

### ii. Example results
This section provides an overview of the results from the provided examples located in the `Examples` folder. Furthermore, please access the complete video outputs by following [this link](https://uithcm-my.sharepoint.com/:f:/g/personal/20521482_ms_uit_edu_vn/Er_pwTn7ha5DvdpITQX-KUQBy9RaG0wLr13y-c38OwjpiA?e=R2J9ob).

#### a. Example Video
![example1](/Media/example1.gif)

#### b. Example URL 1
![example2](/Media/example2.gif)

#### c. Example URL 2
![example3](/Media/example3.gif)

#### d. Example URL 3
![example4](/Media/example4.gif)

#### e. Example URL 4
![example5](/Media/example5.gif)
