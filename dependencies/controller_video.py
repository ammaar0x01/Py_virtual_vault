"""
controller_video.py
===================
"""
from flask import render_template, request, redirect, url_for, flash, Blueprint   

from dependencies.Tools import Tools 
from dependencies._constants import DTO, DEFAULT_USER
from .Filter import Filter 
# ----------------------------

video_blueprint = Blueprint('controller_video', __name__)
# ----------------------------


# ---GET---
@video_blueprint.route("/videos")
def videos_get(): 
    data = (DTO.get_all_records("Video"))
    data = data[0:10]
    num_of_videos = len(data)
    return render_template(
        "videos.html", 
        video_data=data, 
        num_of_videos=num_of_videos, 
        filter_fav="All",
        filter_category="All", 
        video_count="10"
    )
# ----------------------------


# ---POST---
### Add a video
@video_blueprint.route("/videos", methods=["POST"])
def videos_post(): 
    video_name = request.form["video-name"]
    video_url = request.form["video-url"]
    video_type = request.form["video-type"]
    is_fav = request.form.get("is-favorite")
    is_fav = True if is_fav == "yes" else False  
    user_id = DEFAULT_USER[0]
    print(video_name, video_url, is_fav, video_type, user_id)
    
    if Tools.verify_YT_video(video_url): 
        record = (video_name, video_url, is_fav, video_type, user_id)
        DTO.insert_record_auto("Video", record)
        flash("New video added")
        return redirect(url_for('controller_video.videos_get'))

    print("\n***Invalid URL***")
    flash("Invalid YouTube URL")
    return redirect(url_for('controller_video.videos_get'))

### Filter 
@video_blueprint.route("/videos-filter", methods=["POST"])
def videos_post_filter(): 
    filter_item = request.form.get("category")
    is_fav = request.form.get("all-or-fav")
    num_of_videos_req = request.form.get("num-of-videos")

    return Filter.filter_videos(is_fav, num_of_videos_req, filter_item)
# ----------------------------


# ---PUT---
@video_blueprint.route("/update-video/<int:id>", methods=["POST","GET"])
def videos_put(id):
    video = DTO.get_record("Video", "video_id", id)

    if request.method == "POST": 
        link = request.form["update-video-url"]
        name = request.form["update-video-name"]
        category = request.form["update-video-type"]
        is_fav = request.form.get("update-is-favorite")
        is_fav = True if is_fav == "yes" else False  

        if Tools.verify_YT_video(link): 
            update_cols = ["video_name", "video_link", "video_category", "is_favorite"]
            update_values = [name, link, category, is_fav]
            DTO.update("Video", "video_id", id, update_cols, update_values)
            flash("Video details updated")
            return redirect(url_for("controller_video.videos_get"))
    
        else: 
            flash("Invalid YouTube URL")
            return render_template("update-video.html", video=video)

    return render_template('update-video.html', video=video)
# ----------------------------


# ---DELETE---     
@video_blueprint.route("/delete-video/<int:id>", methods=["GET"])
def videos_delete(id): 
    DTO.delete("Video", "video_id", id)
    flash("Video details deleted")
    return redirect(url_for("controller_video.videos_get"))
# ======================================
