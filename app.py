from flask import Flask, render_template, request
import json

app = Flask(__name__)

# טוען נתוני שיעורים מקובץ JSON
with open("lessons.json", "r", encoding="utf-8") as file:
    lessons = json.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    lesson_info = None
    if request.method == "POST":
        lesson_name = request.form.get("lesson").strip().lower()
        lesson_info = lessons.get(lesson_name, "לא נמצאה הכנה לשיעור זה.")
    return render_template("index.html", lesson_info=lesson_info)

if __name__ == "__main__":
    app.run(debug=True)