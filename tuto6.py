class Student(object):
    """Simple representation of a university student."""


    def __init__(self, name, student_num, degree):
        """Create a student with a name.
        Parameters:
        name (str): The student's name.
        """


        self._name = name
        self._student_num = student_num
        self._degree = degree


    def get_name(self):
        """(str) Returns the name of the student."""


        return self._name


    def get_student_num(self):
        return self._student_num


    def get_degree(self):
        return self._degree


    def set_degree(self, new_degree):
        self._degree = new_degree


    def get_first_name(self):
        first, space, last = self.get_name().partition(" ")
        return first


    def get_last_name(self):
        return self._get_name().partition(" ")[-1]


    def email(self):
        email = "{}.{}@uq.net.au".format(self.get_first_name(),
                                         self.get_last_name())

        """email = self.get_first_name() + "." + \
                self.get_last_name() + "@uq.net.au"
        """
        return email


    def __str__(self):
        output = "{} ({}, {}, {})".format(self._name,
                                          self.get_email(),
                                          self._student_num,
                                          self._degree)
        return output


    def __repr__(self):
        return "Student('{}', {}, '{}')".format(self._name,
                                                self._student_num,
                                                self._degree)


def check_students(students):
    seen_student_num = []

    for student in students:
        if student.get_student_num() in seen_student_num:
            # seen this student num before -> invalid
            return False

        seen_student_num.append(student.get_student_num())

    return True


