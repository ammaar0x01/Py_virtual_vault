"""
controller_video.py
===================
"""
from flask import render_template, request, redirect, url_for, flash, Blueprint   

from dependencies.Tools import Tools 
from dependencies._constants import DTO, CATEGORIES, DEFAULT_USER  
from .Filter import Filter 
# ----------------------------

webpage_blueprint = Blueprint('controller_webpage', __name__)
# ----------------------------


# ---GET---
# ---POST---
@webpage_blueprint.route("/webpages", methods=["GET", "POST"])
def webpages_get(): 
# def webpages_get_post(): 
    if request.method == "GET": 
        data = DTO.get_all_records("Saved_webpage")
        data = data[:10]
        num_of_pages = len(data)
        return render_template(
            "webpages.html", 
            data_str=data,  
            num_of_pages=num_of_pages, 
            filter_fav="All",
            filter_category="All", 
            webpage_count="10", 
            categories=CATEGORIES 
        )
    
    else:
        webpage_name = request.form["webpage-name"]
        webpage_url = request.form["webpage-url"]
        webpage_type = request.form["webpage-type"]
        is_fav = request.form.get("is-favorite")
        is_fav = True if is_fav == "yes" else False  
        user_id = DEFAULT_USER[0]
        print(webpage_name, webpage_url, is_fav, webpage_type, user_id)
        
        if Tools.verify_not_YT_URL(webpage_url) == "Valid URL": 
            record = (webpage_name, webpage_url, is_fav, webpage_type, user_id)
            DTO.insert_record_auto("Saved_webpage", record)
            flash("New webpage added", "info")
            return redirect(url_for('controller_webpage.webpages_get'))
        
        elif Tools.verify_not_YT_URL(webpage_url) == "Do not enter a YouTube URL": 
            flash("Do not enter a YouTube URL", "info")
            return redirect(url_for('controller_webpage.webpages_get'))
    
        print("\n***Invalid URL***")
        flash("Invalid URL", "error")
        return redirect(url_for('controller_webpage.webpages_get'))
# ----------------------------

### filter 
@webpage_blueprint.route("/webpages-filter", methods=["POST"])
def webpages_post_filter(): 
    is_fav = request.form.get("all-or-fav")
    num_of_webpages_req = request.form.get("num-of-webpages")
    filter_item = request.form.get("category")

    return Filter.filter_webpages(is_fav, num_of_webpages_req, filter_item)
# ----------------------------


# ---PUT---
@webpage_blueprint.route("/update-webpage/<int:id>", methods=["POST","GET"])
def webpages_put(id):
    webpage = DTO.get_record("Saved_webpage", "webpage_id", id)

    if request.method == "POST": 
        link = request.form["update-webpage-url"]
        name = request.form["update-webpage-name"]
        category = request.form["update-webpage-type"]
        is_fav = request.form.get("update-is-favorite")
        is_fav = True if is_fav == "yes" else False  

        if Tools.verify_URL(link): 
            update_cols = ["webpage_name", "webpage_link", "webpage_category", "is_favorite"]
            update_values = [name, link, category, is_fav]
            DTO.update("Saved_webpage", "webpage_id", id, update_cols, update_values)
            flash("Webpage details updated")
            return redirect(url_for("controller_webpage.webpages_get"))
    
        else: 
            flash("Invalid URL")
            return render_template(
                "update-webpage.html", 
                webpage=webpage, 
                categories=CATEGORIES 
            )

    # video = DTO.get_record("Saved_webpage", "webpage_id", id)
    # return render_template('update-webpage.html', webpage=webpage)
    return render_template(
        "update-webpage.html", 
        webpage=webpage, 
        categories=CATEGORIES 
    )
# # ----------------------------


# ---DELETE---     
@webpage_blueprint.route("/delete-webpage/<int:id>", methods=["GET"])
def webpages_delete(id): 
    DTO.delete("Saved_webpage", "webpage_id", id)
    flash("Webpage details deleted")
    return redirect(url_for("controller_webpage.webpages_get"))
# ======================================
