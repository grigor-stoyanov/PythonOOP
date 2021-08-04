import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student('test')

    def test_student_init(self):
        self.assertEqual(self.student.name, 'test')
        self.assertEqual(self.student.courses, {})

    def test_student_init_with_course(self):
        student = Student('test2', {'java': [1, 2], 'php': []})
        self.assertEqual('test2', student.name)
        self.assertEqual({'java': [1, 2], 'php': []}, student.courses)

    def test_enroll_existing_course(self):
        self.student.courses = {'java': ['first_note']}

        self.assertEqual(self.student.enroll('java', ['second_note', 'third_note'], ''),
                         'Course already added. Notes have been updated.')
        self.assertEqual(self.student.courses, {'java': ['first_note', 'second_note', 'third_note']})

    def test_enroll_new_course_with_notes(self):
        self.assertEqual(self.student.enroll('php', ['first_note'], 'Y'),
                         "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {'php': ['first_note']})

    def test_enroll_new_course_no_notes(self):
        self.assertEqual(self.student.enroll('python', ['test'], 'n'),
                         "Course has been added.")
        self.assertEqual(self.student.courses, {'python': []})

    def test_update_course_notes(self):
        self.student.courses = {'java': ['note1']}
        self.assertEqual(self.student.add_notes('java', 'note2'),
                         "Notes have been updated")
        self.assertEqual(self.student.courses, {'java': ['note1', 'note2']})

    def test_update_non_existing_course_notes_raises(self):
        with self.assertRaises(Exception) as e:
            self.student.add_notes('java', 'note2')
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))

    def test_leave_course(self):
        self.student.courses = {'java': [], 'python': []}
        self.assertEqual(self.student.leave_course('java'),
                         "Course has been removed")
        self.assertEqual(self.student.courses, {'python': []})

    def test_leave_non_existing_course_raises(self):
        with self.assertRaises(Exception) as e:
            self.student.leave_course('java')
        self.assertEqual('Cannot remove course. Course not found.', str(e.exception))


if __name__ == '__main__':
    unittest.main()
