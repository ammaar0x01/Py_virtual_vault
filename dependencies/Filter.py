"""
Filter.py
=========
"""
from flask import render_template, redirect, url_for, flash   

from dependencies._constants import DTO, CATEGORIES  
# ----------------------------


class Filter(): 
    """
    Used to filter videos and webpages
    """
    # ---help from robot
    @staticmethod
    def filter_videos(is_fav, num_of_videos_req, filter_item) -> str:
        print("\nFiltering videos...")

        ### NOT Favorites
        if is_fav == "All":
            if filter_item == "All":
                data = DTO.get_all_records("Video")
            else:
                data = DTO.get_records("Video", "video_category", filter_item)
        # --------------------------------
        
        ### Favorites
        elif is_fav == "Favorites":
            if filter_item == "All":
                data = DTO.get_records("Video", "is_favorite", True)
            else:
                # data = DTO.get_fav_videos("Video", "video_category", filter_item)
                data = DTO.get_fav("Video", "video_category", filter_item)
        # --------------------------------

        else:
            flash("An error has occurred")
            return redirect(url_for('controller_video.videos_get'))
        # --------------------------------
    
        ### Apply video limit
        if num_of_videos_req != "All":
            data = data[:int(num_of_videos_req)]

        flash("Filter applied")
        return render_template(
            "videos.html",
            video_data=data,
            num_of_videos=len(data),
            filter_fav=is_fav,
            filter_category=filter_item,
            video_count=num_of_videos_req
        )
        # ===================================


    @staticmethod
    def filter_webpages(is_fav, num_of_pages, filter_item) -> str:
        print("\nFiltering webpages...")

        ### NOT Favorites
        if is_fav == "All":
            if filter_item == "All":
                data = DTO.get_all_records("Saved_webpage")
            else:
                data = DTO.get_records("Saved_webpage", "webpage_category", filter_item)
        # --------------------------------
        
        ### Favorites
        elif is_fav == "Favorites":
            if filter_item == "All":
                data = DTO.get_records("Saved_webpage", "is_favorite", True)
            else:
                data = DTO.get_fav("Saved_webpage", "webpage_category", filter_item)
        # --------------------------------

        else:
            flash("An error has occurred")
            return redirect(url_for('controller_webpage.webpages_get'))
        # --------------------------------
    
        ### Apply video limit
        if num_of_pages != "All":
            data = data[:int(num_of_pages)]

        flash("Filter applied")
        return render_template(
            "webpages.html",
            data_str=data,
            num_of_pages=len(data),
            filter_fav=is_fav,
            filter_category=filter_item,
            webpage_count=num_of_pages, 
            categories=CATEGORIES 
        )
        # ===================================

# ------------------------------------------------------
