class Task:
    def __init__(self, name: str, due_date: str, comments=None, completed=False):
        self.due_date = due_date
        self.name = name
        if not comments:
            self.comments = comments
        self.comments = []
        self.completed = completed

    def change_name(self, new_name: str) -> str:
        if not self.name == new_name:
            self.name = new_name
            return self.name
        return 'Name cannot be the same.'

    def change_due_date(self, new_date: str) -> str:
        if not self.due_date == new_date:
            self.due_date = new_date
            return self.due_date
        return 'Date cannot be the same.'

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return 'Cannot find comment.'

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"
