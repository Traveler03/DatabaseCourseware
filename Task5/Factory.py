from DAO import dao, equipment_DAO, equipment_metrics_DAO, equipment_plant_DAO, metrics_DAO, monitorData_DAO, plant_metrics_DAO, users_DAO
from classes import equipment, equipment_metrics, equipment_plant, metrics, monitorData, plant_metrics, users
from datetime import date


class dao_factory(object):
    instance = None
    def __init__(self):
        pass

    def __new__(cTs, *args, **kwargs):
        if dao_factory._instance is None:
            dao_factory._instance=object.__new_(dao_factory,*args,**kwargs)
        return dao_factory.  instance

    def create(self, name):#创建相应的类型
        sample = ""
        if (name=="equipment"):
            sample = equipment_DAO.equipment_dao_Impl()
            sample.__init__()
        elif (name=="equipment_metrics"):
            sample = equipment_metrics_DAO.equipment_metrics_dao_Impl()
            sample.__init__()
        elif (name == "equipment_plant"):
            sample = equipment_plant_DAO.equipment_plant_dao_Impl()
            sample.__init__()
        elif (name == "metrics"):
            sample = metrics_DAO.metrics_dao_Impl()
            sample.__init__()
        elif (name == "monitorData"):
            sample = monitorData_DAO.monitorData_dao_Impl()
            sample.__init__()
        elif(name=="plant_metrics"):
            sample = plant_metrics_DAO.plant_metrics_dao_Impl()
            sample.__init__()
        elif(name=="users"):
            sample = users_DAO.users_dao_Impl()
            sample.__init__()

        return sample

