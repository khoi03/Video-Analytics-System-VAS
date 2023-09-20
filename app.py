from flask import Flask, redirect, request, url_for, render_template, make_response
from flask_uploads import UploadSet, configure_uploads, ALL
import os
from pytube import YouTube
from vas import VAS
import time 

app = Flask(__name__)


@app.route("/")
def get_start():
    video_filename = None
    cache_buster = int(time.time()) 
    response = make_response(render_template("index.html", video_filename=video_filename, cache_buster=cache_buster))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

# Configure the "videos" UploadSet to handle video uploads
videos = UploadSet("videos", ALL)
app.config["UPLOADED_VIDEOS_DEST"] = "static/uploads"  # Specify the upload directory
configure_uploads(app, videos)

@app.route('/upload', methods=['POST', 'GET'])
def upload_video():
    video_name = "UploadedVideo.mp4"
    video_path = os.path.join(app.config["UPLOADED_VIDEOS_DEST"], video_name)
    # Check if the POST request contains a file
    if 'video' in request.files:
        video_file = request.files['video']
        if video_file.filename == '':
            return "No selected video file."
        
        # Check if the file is an allowed video file type (e.g., mp4)
        allowed_extensions = {'mp4'}
        if not video_file.filename.endswith(tuple(allowed_extensions)):
            return "Unsupported file format."

        # Save the uploaded video file to a folder (e.g., 'uploads')
        if not os.path.exists(app.config["UPLOADED_VIDEOS_DEST"]):
            os.makedirs(app.config["UPLOADED_VIDEOS_DEST"])

        video_file.save(video_path)
    else:
        video_url = request.form.get('video_url')

        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(app.config["UPLOADED_VIDEOS_DEST"],video_name)
    
    model_name = request.form.get('model_size')
    analyzed_video = VAS(model_name, video_path)
    analyzed_video()
    video_filename = 'static/annotatedVideo/output.mp4'
    cache_buster = int(time.time())
    
    return render_template("index.html", video_filename=video_filename, cache_buster=cache_buster)


if __name__ == "__main__":
    app.run()