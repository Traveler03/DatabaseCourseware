from DAO import dao,fig_DAO,plant_DAO,plant_fig_DAO,plant_pest_DAO,user_DAO,classes_DAO,region_DAO,plant_region_DAO,plant_classes_DAO
from classes import fig,plant,plant_fig,plant_pest,user,classes,region,plant_region,plant_classes
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
        if(name=="fig"):
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
        elif (name == "user"):
            sample = user_DAO.user_dao_Impl()
            sample.__int__()
        elif(name=="classes"):
            sample=classes_DAO.classes_dao_Impl()
            sample.__int__()
        elif(name=="region"):
            sample=region_DAO.region_dao_Impl()
            sample.__int__()
        elif(name=="plant_classes"):
            sample=plant_classes_DAO.plant_classes_dao_Impl()
            sample.__int__()
        elif(name=="plant_region"):
            sample=plant_region_DAO.plant_region_dao_Impl()
            sample.__int__()
        return sample
    def creatview(self,sql):
        self.connect=dao.dao.get_conn()
        cursor=self.connect().cursor()
        cursor.execute(sql)
