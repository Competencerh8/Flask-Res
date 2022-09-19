from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("Index.html")


 
if __name__ == "__main__":
    app.run_server(debug=True)