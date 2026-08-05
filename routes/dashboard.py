from flask import Blueprint, render_template
from modules.patient_module import get_all_patients


auth_routes = Blueprint('main', __name__)


@auth_routes.route("/dashboard")
def dashboard():
    # Perform the read operation
    patients_data = get_all_patients()
    
    # Pass the data to the template
    return render_template('dashboard.html', active_page='dashboard', patients=patients_data)