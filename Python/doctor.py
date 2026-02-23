import person import Person 
import medicalcenter from MedicalCenter

class Doctor(Person):
    
    def __init__(self, name, address, specialty, years_experience, center):
        super().__init__(name, address)
        self._specialty = specialty
        self._years_experience = years_experience
        self._center = center

    def get_specialty(self):
        return self._specialty

    def get_years_experience(self):
        return self._years_experience

    def get_center(self):
        return self._center

    def __str__(self):
        center_name = self._center.get_name() if self._center else ""
        return (
            f"Doctor Name: {self._name}\n"
            f"Address: {self._address}\n"
            f"Specialty: {self._specialty}\n"
            f"Years of Experience: {self._years_experience}\n"
            f"Works at: {center_name}"
        )
