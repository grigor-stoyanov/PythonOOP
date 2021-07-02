class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed:
            if not self.language == new_language:
                old_language = self.language
                self.language = new_language
                return f'{self.name} switched from {old_language} to {new_language}'
            return f'{self.name} already knows {new_language}'
        return f'{self.name} needs {skills_needed - self.skills} more skills'


programmer = Programmer("Lemmy", "Python", 100)
print(programmer.watch_course('Best C#', 'C#', 20))
