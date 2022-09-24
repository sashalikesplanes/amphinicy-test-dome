class Patient:
    def __init__(self, name):
        self.name = name
        self.next_patient = None
        

class Veterinarian:
    def __init__(self):
        # Initialise the queue
        self.first_patient = None
        self.last_patient = None

    def accept(self, petName):
        new_patient = Patient(petName)
        if self.first_patient is None:
            self.first_patient = new_patient
            self.last_patient = new_patient
        else:
            self.last_patient.next_patient = new_patient
            self.last_patient = new_patient
        

    def heal(self):
        if self.first_patient is None or self.last_patient is None:
            raise IndexError('No patients in queue')
        current_patient = self.first_patient
        self.first_patient = current_patient.next_patient
        return current_patient.name

if __name__ == "__main__":
    veterinarian = Veterinarian()
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal())
    print(veterinarian.heal())
