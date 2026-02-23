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
    
