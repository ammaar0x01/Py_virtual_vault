-- YF; YouTube Favorites; bookmarks 
-- --------------------------------

CREATE TABLE IF NOT EXISTS User(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_name TEXT NOT NULL, 
    user_password TEXT NOT NULL  
);

CREATE TABLE IF NOT EXISTS Task(
    task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    task_text TEXT NOT NULL, 
    task_details TEXT, 
    is_priority BOOLEAN,
    is_repetitive BOOLEAN,
    creation_date TEXT, 
    -- task_status TEXT, -- completed, in-prgress, not-started
    user_id INTEGER, 
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS Channel(
    channel_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    channel_name TEXT NOT NULL, 
    channel_link TEXT NOT NULL, 
    is_favorite BOOLEAN, 
   
    user_id INTEGER, 
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS Video(
    video_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    video_name TEXT NOT NULL, 
    video_link TEXT NOT NULL, 
    is_favorite BOOLEAN, 
    video_category TEXT,  
 
    user_id INTEGER, 
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS Saved_webpage(
    webpage_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    webpage_name TEXT NOT NULL, 
    webpage_link TEXT NOT NULL, 
    is_favorite BOOLEAN, 
    webpage_category TEXT,  

    user_id INTEGER, 
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);
