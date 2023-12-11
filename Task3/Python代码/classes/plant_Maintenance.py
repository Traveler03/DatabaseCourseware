class plant_Maintenance:
    def __init__(self, plant_id, task_id):
        self.plant_id = plant_id
        self.task_id = task_id

    def get_plant_id(self):
        return self.plant_id

    def set_plant_id(self, plant_id):
        self.plant_id = plant_id

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id
