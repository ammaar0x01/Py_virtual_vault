"""
main.py
=======
"""
from flask import Flask, render_template


from dependencies \
    import (
        essentials_blueprint, 
        video_blueprint,
        channel_blueprint, 
        task_blueprint, 
        webpage_blueprint, 
        Record  
    ) 
# ---------------------

app = Flask(__name__) 
app.secret_key = "this is not a secret"

### Added blueprints / controllers 
app.register_blueprint(essentials_blueprint)
app.register_blueprint(video_blueprint)
app.register_blueprint(channel_blueprint)
app.register_blueprint(task_blueprint)
app.register_blueprint(webpage_blueprint)

@app.errorhandler(404)
def error_page_not_found(error):
    return render_template("404.html"), 404 


if __name__ == "__main__":
    Record.log_file()
    Record.back_up_important_files()
    app.run(debug=True)

# -------------------------------------     
