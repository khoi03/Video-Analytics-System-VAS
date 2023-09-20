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

**Notably,** you can change to another Yolov8 model by modifying `model_name` in `app.py`. However, I recommend to use the nano Yolov8 model(yolov8n.pt) to enhance the execution time.

## 2.Overview

### i. UI
This section illustrates the website's layout and its functions

- **Home page:**
![UI](https://github.com/khoi03/Video-Analytics-System-VAS/assets/80579165/81dc3226-477e-49cd-9d2c-bb626321dc20)

- **Upload page:**
![UI1](https://github.com/khoi03/Video-Analytics-System-VAS/assets/80579165/0a68fcab-2caa-43f9-a19f-5cc35b4c1063)

### ii. Example outputs
This section overviews the results of the provided example which can be found in the `Examples` folder. You can find the full video ouputs via [this link](https://uithcm-my.sharepoint.com/:f:/g/personal/20521482_ms_uit_edu_vn/Er_pwTn7ha5DvdpITQX-KUQBy9RaG0wLr13y-c38OwjpiA?e=R2J9ob).

#### a. Example Video
![example1](https://github.com/khoi03/Video-Analytics-System-VAS/assets/80579165/1cdb0308-a6c8-4046-b325-2f5d14834898)

#### b. Example URL 1
![example2](https://github.com/khoi03/Video-Analytics-System-VAS/assets/80579165/2c72a61a-da82-48d0-b917-20dc4af1dfe7)
