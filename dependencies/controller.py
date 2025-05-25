"""
controller.py
=============
"""
from flask import render_template, Blueprint    
import os 

from dependencies._constants import DTO 
# ----------------------------

essentials_blueprint = Blueprint("controller", __name__)
# ----------------------------

@essentials_blueprint.route("/")
@essentials_blueprint.route("/cli")
def root(): 
    pc_username = (os.getlogin()) 
    return render_template("command-line.html", pc_username=pc_username)


@essentials_blueprint.route("/home")
def home(): 
    pc_username = (os.getlogin()) 
    return render_template("home.html", pc_username=pc_username)
# ======================================


# ======================================
# API
# ======================================
@essentials_blueprint.route("/api/docs")
def API_docs():
    return render_template("api-docs.html")

### Videos
@essentials_blueprint.route("/api/get/videos")
def API_get_videos(): 
    videos = DTO.get_all_records("Video")
    return { "num_of_videos": len(videos), "videos": videos }  

@essentials_blueprint.route("/api/get/videos/<category>")
def API_get_videos_by_category(category): 
    category = category.capitalize()
    videos = DTO.get_records("Video", "video_category", category)
    return {
        "category": category, 
        "num_of_videos": len(videos), 
        "videos": videos 
    }  

@essentials_blueprint.route("/api/get/video/<id>")
def API_get_video_by_id(id): 
    video = DTO.get_record("Video", "video_id", id)
    return { "video": video }


### Web-pages 
@essentials_blueprint.route("/api/get/webpages")
def API_get_webpages(): 
    webpages = DTO.get_all_records("Saved_webpage")
    return { "num_of_webpages": len(webpages), "webpages": webpages }  


@essentials_blueprint.route("/api/get/webpages/<category>")
def API_get_webpages_by_category(category): 
    category = category.capitalize()
    webpages = DTO.get_records("Saved_webpage", "webpage_category", category)
    return {
        "category": category, 
        "num_of_webpages": len(webpages), 
        "webpages": webpages 
    }  

@essentials_blueprint.route("/api/get/webpage/<id>")
def API_get_webpage_by_id(id): 
    webpage = DTO.get_record("Saved_webpage", "webpage_id", id)
    return { "webpage": webpage }
# ======================================
