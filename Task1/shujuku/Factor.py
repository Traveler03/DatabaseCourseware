from DAO import alia_DAO,dao,fig_DAO,plant_DAO,plant_fig_DAO,plant_pest_DAO
from classes import alia,fig,plant,plant_fig,plant_pest
from datetime import date
class dao_factory(object):
    instance=None
    def __init__(self):
        pass
    def new__(cTs,*args,**kwargs):
        if dao_factory._instance is None:
            dao_factory._instance=object.__new_(dao_factory,*args,**kwargs)
        return dao_factory.  instance

    def create(setf,name):#创建相应的类型
        sample=""
        if(name=="alia"):
            sample = alia_DAO.alia_dao_Impl()
            sample.__int__()
        elif(name=="fig"):
            sample = fig_DAO.fig_dao_Impl()
            sample.__int__()
        elif(name=="plant"):
            sample = plant_DAO.plant_dao_Impl()
            sample.__int__()
        elif (name == "plant_fig"):
            sample = plant_fig_DAO.plant_fig_dao_Impl()
            sample.__int__()
        elif (name == "plant_pest"):
            sample = plant_pest_DAO.plant_pest_dao_Impl()
            sample.__int__()
        return sample
FC=dao_factory()
Work=FC.create("alia")
new_plant=alia.alia()
current_date = date.today()
new_plant.__int__(plant_id="K002",alias="月季花")
Work.insert(new_plant)

