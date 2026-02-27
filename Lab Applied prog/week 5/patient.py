from person import Person
from doctor import Doctor
from medicalcenter import MedicalCenter
class Patient(Person):
    def __init__(self, name: str, address: str, doctor: Doctor, medical_issues, center: MedicalCenter):
        super().__init__(name, address,)
        self.__doctor = doctor
        self.__medical_issues = medical_issues
        self.__center = center
    def set__medical_issues(self, medical_issues: str):
        self.__medical_issues = medical_issues
    def get_assigned_doctor(self) -> Doctor:
        return self.__doctor
    def get__medical_issues(self, medical_issues:str):
        return self.__medical_issues
    def get__Medical_center(self) -> MedicalCenter:
        return self.__center
    def __str__(self):
        return (
            super().__str__()+ 
            f"Medical Issues: {self.__medical_issues}\n"
            f"Doctor Details: {self.__doctor}\n"
            f"Center Details: {self.__center}"
        )
    
class Inpatient(Patient):
    def __init__(self, name, address, doctor, medical_issues, center, ward_number, admission_date):
        super().__init__(name, address, doctor, medical_issues, center)
        self.__ward_number = ward_number
        self.__admission_date = admission_date
    def __str__(self):
        return (
            super().__str__()+ "\n"
            f"Ward Number = {self.__ward_number}\n"
            f"Admission Date = {self.__admission_date}"
        )
class Outpatient(Patient):
    def __init__(self, name, address, doctor, medical_issues, center, appointment_date):
        super().__init__(name, address, doctor, medical_issues, center)
        self.__appointment_date = appointment_date 
    def __str__(self):
        return (
            super().__str__()+ "\n"
            f"Appointment Date = {self.__appointment_date}"
        )