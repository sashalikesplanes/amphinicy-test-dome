from collections import namedtuple

def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """ 
    # Store the records as tuple of (record type, record value)
    record_list = []
    for record in records:
        for entry in record._asdict().items():
            record_list.append(entry)

    # Create the Patient named tuple with appropriate fields
    Patient = namedtuple('Patient', [record_type for record_type, _ in record_list])
    # Create the patient instance
    return Patient._make([record_value for _, record_value in record_list])

    
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                   
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
  
print(merge(personal_details, complexion))
