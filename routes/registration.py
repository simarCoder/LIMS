from flask import Blueprint, request, redirect, url_for
from modules.patient_module import add_patient

reg_routes = Blueprint('reg',__name__ ,url_prefix="/reg")

@reg_routes.route("/register", methods =["POST"])
def register_patient():
    
    data = {
        "title" : request.form.get("honorificTitle"),
        "p_id" : request.form.get("patientId"),
        "p_name" : request.form.get("patientName"),
        "p_age" : request.form.get("patientAge"),
        "p_age_type" : request.form.get("patientAgeType"),
        "p_gender" : request.form.get("patientGender"),
        "p_phone" : request.form.get("patientPhNum"),
        "p_email" : request.form.get("patientEmail"),
        "p_address": request.form.get("patientAddress"),
    }

    print(data)
    add_patient(data)
    print("done data transfering from model to here.")
    return redirect(url_for("main.dashboard"))

