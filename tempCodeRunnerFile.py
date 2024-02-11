 conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Pratik@6878",
                        database="face_recognition",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(