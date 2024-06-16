import sqlite3

conn = sqlite3.connect('paid_clinic.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Пациент (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    doctor_name TEXT NOT NULL,
    diagnosis TEXT NOT NULL,
    treatment_cost REAL NOT NULL
)
''')

def add_patient(patient_name, doctor_name, diagnosis, treatment_cost):
    cursor.execute('''
    INSERT INTO Пациент (patient_name, doctor_name, diagnosis, treatment_cost)
    VALUES (?, ?, ?, ?)
    ''', (patient_name, doctor_name, diagnosis, treatment_cost))
    conn.commit()

def get_all_patients():
    cursor.execute('SELECT * FROM Пациент')
    return cursor.fetchall()

def search_patients(patient_name=None, doctor_name=None, diagnosis=None):
    query = "SELECT * FROM Пациент WHERE 1=1"
    params = []
    if patient_name:
        query += " AND patient_name=?"
        params.append(patient_name)
    if doctor_name:
        query += " AND doctor_name=?"
        params.append(doctor_name)
    if diagnosis:
        query += " AND diagnosis=?"
        params.append(diagnosis)
    cursor.execute(query, params)
    return cursor.fetchall()

def delete_patient(patient_id):
    cursor.execute("DELETE FROM Пациент WHERE id=?", (patient_id,))
    conn.commit()

def update_patient(patient_id, patient_name=None, doctor_name=None, diagnosis=None, treatment_cost=None):
    query = "UPDATE Пациент SET "
    params = []
    if patient_name:
        query += "patient_name=?, "
        params.append(patient_name)
    if doctor_name:
        query += "doctor_name=?, "
        params.append(doctor_name)
    if diagnosis:
        query += "diagnosis=?, "
        patients.append(diagnosis)
    if treatment_cost:
        query += "treatment_cost=? "
        params.append(treatment_cost)
    query = query.rstrip(", ") + " WHERE id=?"
    params.append(patient_id)
    cursor.execute(query, params)
    conn.commit()

def main_menu():
    print("Главное меню:")
    print("1. Добавить пациента")
    print("2. Поиск пациентов")
    print("3. Удалить пациента")
    print("4. Редактировать данные пациента")
    print("5. Вывести всех пациентов")
    print("6. Выход")

def add_patient_menu():
    patient_name = input("Введите имя пациента: ")
    doctor_name = input("Введите имя врача: ")
    diagnosis = input("Введите диагноз: ")
    treatment_cost = float(input("Введите стоимость лечения: "))
    add_patient(patient_name, doctor_name, diagnosis, treatment_cost)
    print("Пациент успешно добавлен!")

def search_patients_menu():
    patient_name = input("Введите имя пациента (или Enter для пропуска): ")
    doctor_name = input("Введите имя врача (или Enter для пропуска): ")
    diagnosis = input("Введите диагноз (или Enter для пропуска): ")
    patients = search_patients(patient_name, doctor_name, diagnosis)
    for patient in patients:
        print(patient)

def delete_patient_menu():
    patient_id = int(input("Введите id пациента, которого нужно удалить: "))
    delete_patient(patient_id)
    print("Пациент успешно удален!")

def update_patient_menu():
    patient_id = int(input("Введите id пациента, данные которого нужно обновить: "))
    patient_name = input("Введите новое имя пациента (или Enter для пропуска): ")
    doctor_name = input("Введите новое имя врача (или Enter для пропуска): ")
    diagnosis = input("Введите новый диагноз (или Enter для пропуска): ")
    treatment_cost = input("Введите новую стоимость лечения (или Enter для пропуска): ")
    if treatment_cost:
        treatment_cost = float(treatment_cost)
    update_patient(patient_id, patient_name, doctor_name, diagnosis, treatment_cost)
    print("Данные пациента успешно обновлены!")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            add_patient_menu()
        elif choice == 2:
            search_patients_menu()
        elif choice == 3:
            delete_patient_menu()
        elif choice == 4:
            update_patient_menu()
        elif choice == 5:
            patients = get_all_patients()
            for patient in patients:
                print(patient)
        elif choice == 6:
            conn.close()
            break
        else:
            print("Неверный выбор, попробуйте снова.")
