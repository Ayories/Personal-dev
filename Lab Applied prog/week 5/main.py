from medicalcenter import MedicalCenter
from doctor import Doctor
from patient import Patient, InPatient, OutPatient

def main():
    center = MedicalCenter("Eaton Wood Medical Center", "12 Eaton Road, Birmingham")
    doctor_john = Doctor("John", "5 Kingsway, Birmingham", "General Practice", 7, center)
    patient_fred = Patient("Fred", "21 Oak Street, Birmingham", ["Cough", "Fever"], doctor_john, center)
    
    print("=== Patient ===")
    print(patient_fred)
    print()

    inpatient = InPatient(
        "Mary",
        "9 Maple Avenue, Birmingham",
        ["Asthma"],
        doctor_john,
        center,
        "Ward 3",
        "2026-02-22"
    )

    outpatient = OutPatient(
        "Sam",
        "44 Pine Close, Birmingham",
        ["Back pain"],
        doctor_john,
        center,
        "2026-02-25"
    )

    print("=== InPatient ===")
    print InPatient
    print()

    print("=== OutPatient ===")
    print OutPatient
    print()
    
