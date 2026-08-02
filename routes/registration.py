from flask import Blueprint, request, redirect, url_for

reg_routes = Blueprint('reg',__name__ ,url_prefix="/reg")

@reg_routes.route("/register", methods =["POST"])
def register_patient():
    title = request.form.get("honorificTitles")
    p_id = request.form.get("patientId")
    p_name = request.form.get("patientName")

    print(title, p_id, p_name)

    return redirect(url_for("main.dashboard"))

