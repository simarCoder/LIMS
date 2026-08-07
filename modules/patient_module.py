from database import get_connection

def add_patient(data):
    # CONNECTION OPENING USING "WITH"
    with get_connection() as conn:
        print("Connection acquired")
        with conn.cursor() as cursor:
            print("Cursor acquired")
            #execute command for SQL with cursor
            
            cursor.execute("""
                            INSERT INTO patients(
                                patient_id,
                                machine_id,
                                honorific_title,
                                patient_name,
                                patient_age,
                                patient_age_type,
                                patient_gender,
                                patient_phone,
                                patient_email,
                                patient_address
                            ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (
                               data["p_id"],
                               data["machine_id"],
                               data["title"],
                               data["p_name"],
                               data["p_age"],
                               data["p_age_type"], 
                               data["p_gender"],
                               data["p_phone"],
                               data["p_email"],
                               data["p_address"],
                                 ))
            
            print("executed successfully")
            

# ====== IMPLEMENTING TO GET THE PATIENT INFO IN NEXT FUNCTION ======         
def get_all_patients():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT patient_id, honorific_title, patient_name, 
                       patient_age, patient_age_type, patient_gender, patient_phone, TO_CHAR(patient_created_at, 'DD Mon YYYY, HH12:MI AM') AS patient_created_at, machine_id
                FROM patients 
                ORDER BY patient_id ASC
            """)
            
            # Convert rows to dictionaries so they are easy to use in Jinja2 HTML templates
            columns = [col.name for col in cursor.description]
            patients = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return patients