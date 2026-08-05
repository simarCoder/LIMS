from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from psycopg import Binary
import sys

print(sys.executable)
print(sys.prefix)

# ===routes export==============================================================
from routes.dashboard import auth_routes
from routes.registration import reg_routes

#====== cloud DB connection =====================================================
load_dotenv()

db_url = os.getenv("DATABASE_URL")

#app starting =================================================================
app = Flask(__name__)

# REGISTERIN ROUTES ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
app.register_blueprint(auth_routes)
app.register_blueprint(reg_routes)


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

@app.route("/")
def home():
    return redirect(url_for('main.dashboard'))

# @app.route("/registration")
# def registration():
#     return render_template('registration.html')


# @app.route("/dashboard")
# def dashboard():
#     return render_template('dashboard.html',active_page='dashboard')

@app.route("/diagnose")
def diagnose():
    return render_template('diagnose.html', active_page='diagnose')

@app.route("/collectionDetails")
def collectionDetails():
    return render_template('collectionDetails.html', active_page='collectionDetails')

@app.route("/settings")
def settings():
    return render_template('settings.html', active_page='settings')

# @app.route("/register", methods=["POST"])
# def register_patient():
#     title = request.form.get("honorificTitles")
#     p_id = request.form.get("patientId")
#     p_name = request.form.get("patientName")

#     print(title, p_id, p_name)

#     return redirect(url_for("dashboard"))




if __name__ == "__main__":
    app.run(debug=True)