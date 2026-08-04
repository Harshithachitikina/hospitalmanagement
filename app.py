from flask import Flask, render_template
import sqlite3


app = Flask(__name__)
db_name = 'hospital.db'

def init__db():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute('''
    create table if not exists users(
    UID Integer primary key AUTOINCREMENT,
    UNAME Text not NULL,
    Email Text check(email like '%@gmail.com'),
    Phone Text not null,
    Role Text DEFAULT 'demo_use',
    Specialization Text DEFAULT 'NA',
    Experience Integer default 2,
    Salary Real default 5000
    );
   ''')
    cursor.execute('Select count(*) from users')
   
    if cursor.fetchone()[0] == 0:

        # Array of user records featuring diverse roles (Surgeons, General Doctors, Compounders, Maintenance Staff)
        seed_users = [

            # Surgeon Doctors
            (
                "Dhanush",
                "DH@gmail.com",
                "8901239016",
                "surgeon doctor",
                "Cardio & Neuro",
                12,
                150000,
            ),
            (
                "Lingaran",
                "LM@gmail.com",
                "8901239023",
                "surgeon doctor",
                "Gynecologist & Orthopedic",
                10,
                135000,
            ),
            (
                "Suresh",
                "SH@gmail.com",
                "8912349016",
                "surgeon doctor",
                "Cardio & Neuro",
                8,
                120000,
            ),
            # General Doctors
            (
                "Dr. Ramesh",
                "ramesh.doc@gmail.com",
                "9876543210",
                "general doctor",
                "General Medicine",
                6,
                85000,
            ),
            (
                "Dr. Anitha",
                "anitha.med@gmail.com",
                "9876543211",
                "general doctor",
                "Pediatrics",
                5,
                80000,
            ),
            # Therapists
            (
                "Chiranjeevi",
                "MStar@gmail.com",
                "8901239123",
                "Therapist",
                "Psychiatrist",
                15,
                95000,
            ),
            # Compounders
            (
                "Rajesh Kumar",
                "rajesh.c@gmail.com",
                "9123456780",
                "compounder",
                "Pharmacy & Doses",
                4,
                30000,
            ),
            (
                "Sunitha Rao",
                "sunitha.comp@gmail.com",
                "9123456781",
                "compounder",
                "First Aid & Dressing",
                3,
                28000,
            ),
            # Maintenance Staff
            (
                "Venkatesh",
                "venky.maint@gmail.com",
                "9000111222",
                "maintainerStaff",
                "Sanitation & Hygiene",
                5,
                22000,
            ),
            (
                "Kalyan",
                "kalyan.maint@gmail.com",
                "9000111223",
                "maintainerStaff",
                "Equipment Maintenance",
                7,
                25000,
            ),
        ]

        
        cursor.executemany(''' 
           Insert into users (UNAME, Email , Phone, role,Specialization, Experience, Salary)
    
           values(?,?,?,?,?,?,?)
           ''',seed_users)
        conn.commit()
    conn.close()


@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute('select * from users; ')
    dataRecords = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html' , users=dataRecords)



if __name__ == "__main__":
    init__db()
    app.run(debug=True)