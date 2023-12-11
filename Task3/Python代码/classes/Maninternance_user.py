class Maninternance_user:
    def __init__(self, task_id, user_id):
        self.task_id = task_id
        self.user_id = user_id

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id
