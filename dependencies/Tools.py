"""
Tools.py
========
"""
import os 
from datetime import datetime 
import shutil
# -------------------------------------

class Tools(): 
    '''
    Contains general static methods
    '''
    # types of YT URLs 
    # https://youtu.be/j51P7GmQSCA
    # https://youtu.be/j51P7GmQSCA?t=310
    # https://www.youtube.com/watch?v=j51P7GmQSCA
    # 

    @staticmethod   
    def verify_URL(URL:str) -> bool: 
        if "https://" in URL: 
            return True 
        return False 

    @staticmethod   
    def verify_not_YT_URL(URL:str) -> str: 
        if "https://" in URL and "youtu" not in URL: 
            return "Valid URL"
        elif "https://" in URL and "youtu" in URL: 
            return "Do not enter a YouTube URL"
        return "Invalid URL"
    
    @staticmethod   
    def verify_YT_URL(youtube_URL:str) -> bool: 
    # def verify_YT_channel(youtube_URL:str) -> bool: # use this instead? 
        # if "https://" in youtube_URL and "youtube.com" in youtube_URL: 
        if "https://" in youtube_URL and "youtu" in youtube_URL: 
            return True 
        return False 
    
    @staticmethod   
    def verify_YT_video(youtube_URL:str) -> bool: 
        if "https://" in youtube_URL and "youtu" in youtube_URL and "be" in youtube_URL: 
        # if "https://" in youtube_URL and "youtube.com" in youtube_URL and "watch" in youtube_URL: 
            return True 
        return False 
    
    @staticmethod
    def normalise_video_URL(youtube_URL_abnormal:str) -> str:  
        # p = "https://www.youtube.com/watch?v=RvDsX1fz9EQ&pp=ygUFbmV4cG8%3D"
        # print(p)
        # print(len(p))

        # # print(p[31::])
        # print(p[0:31])
        # print(p[0:43])

        if len(youtube_URL_abnormal) >= 43: 
            pure_URL = (youtube_URL_abnormal[0:43])
            return pure_URL 
        return youtube_URL_abnormal 

    #  https://www.youtube.com/watch?v=RvDsX1fz9EQ&pp=ygUFbmV4cG8%3D

    @staticmethod 
    def convert_to_hyperlink(string:str):
        print(string)
        print(list(string))
        print(len(list(string)))

        for word in string:
            print(word) 

        if "https" in string:
            print("hyperlink")
            print(f"<a href='{string}' target='_blank'>{string}</a>")

    @staticmethod
    def install_pip_package():
        print("Installing Python packages...")
        import sys 
        if os.name == "nt": 
            os.system("pip install Flask")
            os.system("pip install sqlalchemy")

        else:
            os.system("python3 -m pip install Flask")

# -------------------------------------
# print("xxxxxxxxxx")
# p = "https://www.youtube.com/watch?v=RvDsX1fz9EQ&pp=ygUFbmV4cG8%3D"

# print(Tools.normalise_video_URL(p))


class Record():
    '''
    Contains static methods related to writing or reading data 
    '''
    @staticmethod 
    def _backup_destination(destination_dir="_backup_YnT/") -> None: 
        '''
        Checks if the backup destination dir exists, 
        creates the dir if it doesn't exist
        '''
        current_dir = os.getcwd()
        if current_dir[0] == "C": 
            os.chdir("/")
        else: 
            os.chdir("C:") 

        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)
            print(f"Making dir '{destination_dir}'...")

     
        os.chdir(f"{destination_dir}")
        os.system(f"attrib +h {destination_dir}")
        print(f"\n***Navigated to '{destination_dir}'")
        

    @staticmethod 
    def backup_file(file:str, backup_dest="C:/_backup_YnT/") -> bool: 
        '''
        copies a file to another location
        '''
        if os.path.exists(file):
            shutil.copy(file, backup_dest)
            print(f"***File copied ({file})")
            return True 
        print(f"***File not found ({file})")
        return False 
    
    @staticmethod 
    def read_file(filename:str) -> str: 
        file = open(filename, "r")
        data = file.read()
        file.close()
        return data
     
    @staticmethod 
    def write_to_file(filename:str, data:str) -> None:
        file = open(filename, "w")
        file.write(data)
        file.close()
        
    @staticmethod 
    def append_to_file(filename:str, data:str) -> None:
        file = open(filename, "a")
        file.write(data)
        file.close()

    @staticmethod 
    def log_file(message="User launched the app") -> None: 
        '''
        write to log file
        '''
        log = open("_log.log", "a")
        log.write(f"\n{message}\n") 
        log.write(str(datetime.now())) 
        log.write("\n")
        log.close()
                   
    @staticmethod 
    def back_up_important_files() -> None:
        '''
        Copies the important files to another location
        '''
        if (os.name) == "nt": 
            cd = os.getcwd()
            print("WIndows NT OS")
            Record._backup_destination()
            os.chdir(cd)
        
            Record.backup_file(file="_log.log")
            Record.backup_file(file="dependencies//_schema.sql")
            Record.backup_file(file="dependencies//_database_test.db")
            Record.backup_file(file="dependencies//_database0.db")
            
            ### hide directory
            os.system(f"attrib +h C:/_backup_yf")
            print("***Files backed up***\n\n")
            
# -------------------------------------
