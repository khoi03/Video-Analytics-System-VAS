# Video Analytics System(VAS)

## Table of contents:
1. [Introduction](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#1introduction)

2. [Overview](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#2overview)

   1. [UI](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#iui)
   
   2. [Example results](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#iiexample-results)
   
      1. [Example Video](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#a-example-video)
         
      2. [Example URL 1](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#b-example-url-1)
   
## 1.Introduction
This task aims to create a simple web-based Video Analytics System (VAS) to analyze content from videos with the following inputs and outputs:
- **Input:**
   - Any YouTube video URL
   - Upload a video from a local computer
  
- **Ouput:** Analyzing basic video content and display results on the web while playing the video. For example:
   - Counting people and other objects in each frame and presenting the results synchronized while playing the video;
   - Illustrating a canvas that exhibits detected objects (bounding box and object name) in each frame, synchronized with the video.

**Notably,** all results in the [Example results](https://github.com/khoi03/Video-Analytics-System-VAS/blob/master/README.md#iiexample-results) section were obtained using the nano Yolov8 model(yolov8n.pt). Furthermore, if you have a strong GPU, you may consider using a larger Yolov8 model, which provides more accurate predictions but takes longer to process.

## 2.Overview

### i. UI
This section illustrates the website's layout and its functions

- **Home page:**
![UI](/Media/UI.png)

- **Upload page:**
![UI1](/Media/UI1.png)

### ii. Example outputs
This section provides an overview of the results from the provided examples located in the `Examples` folder. You can access the complete video outputs via [this link](https://uithcm-my.sharepoint.com/:f:/g/personal/20521482_ms_uit_edu_vn/Er_pwTn7ha5DvdpITQX-KUQBy9RaG0wLr13y-c38OwjpiA?e=R2J9ob).

#### a. Example Video
![example1](/Media/example1.gif)

#### b. Example URL 1
![example2](/Media/example2.gif)
