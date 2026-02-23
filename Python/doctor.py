import person import Person 
import medicalcenter from MedicalCenter

class Doctor(Person):
    
    def __init__(self, name, address, specialty, years_experience, center):
        super().__init__(name, address)
        self.__specialty = specialty
        self.__years_experience = years_experience
        self.__center = center

    def get_specialty(self):
        return self._specialty

    def get_years_experience(self):
        return self.__years_experience

    def get_center(self):
        return self.__center

    def __str__(self):
        center_name = self._center.get_name() if self._center else ""
        return (
            f"Doctor Name: {self.__name}\n"
            f"Address: {self.__address}\n"
            f"Specialty: {self.__specialty}\n"
            f"Years of Experience: {self.__years_experience}\n"
            f"Works at: {center_name}"
        )
