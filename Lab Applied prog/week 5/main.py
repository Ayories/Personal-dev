from medicalcenter import MedicalCenter
from doctor import Doctor
from patient import Patient, Inpatient, Outpatient

def main():
    center = MedicalCenter("Eaton Wood Medical Center", "12 Eaton Road, Birmingham")
    doctor_john = Doctor("John", "5 Kingsway, Birmingham", "General Practice", 7, center)
    patient_fred = Patient("Fred", "21 Oak Street, Birmingham",  doctor_john, ["Cough", "Fever"], center)
    
    print("=== Patient ===")
    print(patient_fred)
    print()

    inPatient = Inpatient(
        "Mary",
        "9 Maple Avenue, Birmingham",
        doctor_john,
        ["Asthma"],
        center,
        "Ward 3",
        "2026-02-22"
    )

    outPatient = Outpatient(
        "Sam",
        "44 Pine Close, Birmingham",
        doctor_john,
        ["Back pain"],
        center,
        "2026-02-25"
    )

    print("=== InPatient ===")
    print (inPatient)
    print()

    print("=== OutPatient ===")
    print (outPatient)
    print()
main()
    
