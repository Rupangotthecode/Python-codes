#Startup idea!
from abc import ABC, abstractmethod

class StartupPlan(ABC):
    @abstractmethod
    def infrastructure(self):
        pass

    @abstractmethod
    def capital(self):
        pass

    @abstractmethod
    def human_resources(self):
        pass

class JointStartupPlan(StartupPlan):
    def infrastructure(self):
        print("First month's discussion about the infrastructure of the work area.")

    def capital(self):
        print("First month's discussion about capital and funding.")

    def human_resources(self):
        print("First month's discussion about human resources.")

    def implement(self):
        print("Three months later, they started implementing the plan.")

joint_plan = JointStartupPlan()
joint_plan.infrastructure() 
joint_plan.capital()        
joint_plan.human_resources()
joint_plan.implement() 