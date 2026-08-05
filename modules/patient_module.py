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
                                honorific_title,
                                patient_name,
                                patient_age,
                                patient_age_type,
                                patient_gender,
                                patient_phone,
                                patient_email,
                                patient_address
                            ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (
                               data["p_id"],
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