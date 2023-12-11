class Maintenance:
    def __init__(self, task_id, task_name, time, place, task_des):
        self.task_id = task_id
        self.task_name = task_name
        self.time = time
        self.place = place
        self.task_des = task_des

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_task_name(self):
        return self.task_name

    def set_task_name(self, task_name):
        self.task_name = task_name

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_place(self):
        return self.place

    def set_place(self, place):
        self.place = place

    def get_task_des(self):
        return self.task_des

    def set_task_des(self, task_des):
        self.task_des = task_des
