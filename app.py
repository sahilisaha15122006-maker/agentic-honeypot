from gemini_ai import analyze_login
from flask import Flask, render_template,request
from datetime import datetime
import json
import os

app=Flask(__name__)

LOG_FILE=os.path.join("logs","activity.json")
os.makedirs("logs",exist_ok=True)

@app.route("/", methods=["GET","POST"])
def login():
    message=None

    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        log_data={
            "username":username,
            "password":password, 
            "time":str(datetime.now())

        }

        try:
            with open(LOG_FILE, "r") as f:
                data=json.load(f)
        except:
            data=[]

        data.append(log_data)
        analysis=analyze_login(log_data)
        print("\n===GEMINI ANALYSIS===") 
        print(analysis)
        print("======================\n")

        with open(LOG_FILE, "w") as f:
            json.dump(data,f, indent=4)

        message="Invalid credentials"

    return render_template("login.html", message=message)

if __name__=="__main__":
    app.run(debug=True)