"""
controller_channel.py
=====================
"""
from flask import render_template, request, redirect, url_for, flash, Blueprint    

from dependencies.Tools import Tools   
from dependencies._constants import DTO, DEFAULT_USER 
# ----------------------------

channel_blueprint = Blueprint("controller_channel", __name__)
# ----------------------------


# ---GET--- 
@channel_blueprint.route("/channels")
def channels_get(): 
    data = DTO.get_all_records("Channel")
    return render_template(
        "channels.html", 
        channel_data=data, 
        fav_or_not="All"
    )
# -------------------------------------

# ---POST--- 
@channel_blueprint.route("/channels", methods=["POST"])
def channels_post(): 
    channel_name = request.form["channel-name"]
    channel_link = request.form["channel-link"]
    is_fav = request.form.get("is-favorite")
    is_fav = True if is_fav == "yes" else False  
    user_id = DEFAULT_USER[0]
    print(channel_name, channel_link, is_fav, user_id)

    if Tools.verify_YT_URL(channel_link): 
        record = (channel_name, channel_link, is_fav, user_id)
        DTO.insert_record_auto("Channel", record)
        flash("New channel added")        
        return redirect(url_for("controller_channel.channels_get"))

    print("\n***Invalid URL***")
    flash("Invalid YouTube URL")
    return redirect(url_for("controller_channel.channels_get"))

### filter 
@channel_blueprint.route("/channels-filter", methods=["POST"])
def channels_post_filter():
    is_fav = request.form.get("all-or-fav")
    print(is_fav)

    if is_fav == "All": 
        return redirect(url_for("controller_channel.channels_get"))

    data = DTO.get_records("Channel", "is_favorite", True)
    flash("Filter applied")
    return render_template(
        "channels.html", 
        channel_data=data, 
        fav_or_not="Favorites"
    )
# -------------------------------------

# ---PUT--- 
@channel_blueprint.route("/update-channel/<int:id>", methods=["POST", "GET"])
def channels_put(id):
    channel = DTO.get_record("Channel", "channel_id", id)

    if request.method == 'POST':
        link = request.form["update-channel-url"]
        name = request.form["update-channel-name"]
        is_fav = request.form.get("update-is-fav")
        is_fav = True if is_fav == "yes" else False  
        cols = ["channel_name", "channel_link", "is_favorite"]
        values = [name, link, is_fav]

        if Tools.verify_YT_URL(link): 
            DTO.update("Channel", "channel_id", id, cols, values)
            flash("Channel details updated")
            return redirect(url_for('controller_channel.channels_get'))
        else:
            flash("Invalid YouTube URL")
            return render_template("update-channel.html", channel=channel)

    return render_template('update-channel.html', channel=channel)
# -------------------------------------

# ---DELETE--- 
@channel_blueprint.route("/delete-channel/<int:id>", methods=["GET"])
def channels_delete(id):
    DTO.delete("Channel", "channel_id", id)
    flash("Channel details deleted")
    return redirect(url_for('controller_channel.channels_get'))
# ======================================
