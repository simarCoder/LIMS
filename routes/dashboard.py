from flask import Blueprint, render_template

auth_routes = Blueprint('main', __name__)

@auth_routes.route("/dashboard")
def dashboard():
    return render_template('dashboard.html',active_page='dashboard')