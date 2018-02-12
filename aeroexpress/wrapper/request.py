class PersonalInfo(object):
    def __init__(self, first_name: str, patronymic_name: str, surname: str, doc_type: str, doc_number: str):
        self.first_name = first_name
        self.patronymic_name = patronymic_name
        self.surname = surname
        self.doc_type = doc_type
        self.doc_number = doc_number


class PersonalInfoWrapper(object):
    def __init__(self, personal_info: 'list of PersonalInfo'):
        self.personal_info = personal_info

    @property
    def request(self):
        personal_info = []
        for item in self.personal_info:
            personal_info.append({
                'firstName': item.first_name,
                'patronymicName': item.patronymic_name,
                'surname': item.surname,
                'docType': item.doc_type,
                'docNumber': item.doc_number
            })
        return {'personalInfo': personal_info}