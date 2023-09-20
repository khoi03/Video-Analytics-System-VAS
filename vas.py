from ultralytics import YOLO
import cv2 as cv 
from PIL import Image
import numpy as np
import torch
import os

class VAS:
    def __init__(self, model_name, video_path):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model_name = model_name
        self.video_path = video_path #"Example video.mp4"
        self.model = self.load_model()
        self.font = cv.FONT_HERSHEY_SIMPLEX
        self.location = (0,50)
        self.distance = (0,10)
        self.fontScale = 1
        self.fontColor = (0,0,255)
        self.lineType = 3
        
    def load_model(self):
        model = YOLO(self.model_name) #'yolov8m.pt'
        model.to(self.device)
        
        return model
    
    def predict(self, frame):
        return self.model(frame)
    
    def plot_boxes(self, results, annotated_frame):
        for r in results:
            result = r.boxes.cpu()
            key_list = r.names
            unique, counts = np.unique(result.cls, return_counts=True)
            number = dict(zip(unique,counts))
            location = (0,70)
            cv.putText(annotated_frame,'There are:', 
                            (0,50), 
                            self.font, 
                            self.fontScale,
                            self.fontColor,
                            self.lineType)
            for i in unique:
                location = (location[0],location[1]+35) 
                cv.putText(annotated_frame,'{} {}(s)'.format(number[i], key_list[int(i)]), 
                            location, 
                            self.font, 
                            self.fontScale,
                            self.fontColor,
                            self.lineType)
                
        return annotated_frame
    
    def __call__(self):
        cap = cv.VideoCapture(self.video_path)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = int(cap.get(5))
        
        output_folder = './static/annotatedVideo'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = os.path.join(output_folder, 'output.mp4')
        
        # Write frame
        size = (frame_width, frame_height)
        
        output = cv.VideoWriter(output_path,
                                cv.VideoWriter_fourcc(*'H264'),
                                fps, size)

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()
            if not success:
                break
            
            # Run YOLOv8 inference on the frame
            results = self.predict(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()
            
            count_annotated_frame = self.plot_boxes(results,annotated_frame)
            
            output.write(count_annotated_frame)
        
        output.release()
        cap.release()
        cv.destroyAllWindows()
        
# analyzed_video = VAS('yolov8m.pt', 'static/uploads/test.mp4')
# analyzed_video()