"""
_constants.py
=============
"""

# DATABASE_PATH = "dependencies//_database_test1.db"
DATABASE_PATH = "dependencies//_database0.db"
# ------------------------------

from dependencies.Database_transfer import Database_transfer

DTO = Database_transfer(DATABASE_PATH)
DEFAULT_USER = DTO.user 
# ------------------------------

CATEGORIES = [
    "Audiobook", 
    "Backing-track", 
    "Education", 
    "Entertainment", 
    "Music", 
    "Fitness", 
    "Food", 
    "Animation", 
    # "Shorts", 
    "Tutorial", 
    "Other"
]
# ------------------------------
