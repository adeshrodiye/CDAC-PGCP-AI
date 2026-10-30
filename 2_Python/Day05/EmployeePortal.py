from abc import abstractmethod, ABC

from distributed.utils_comm import retry
from typing_extensions import override

class Employee(ABC):
    def __init__(self,emp_id,name):
        self._emp_id = emp_id
        self._name = name

    @abstractmethod
    def calculate_gross(self):
        pass

    def __str__(self):
        return f'Employee Data ID: {self._emp_id}, Name : {self._name}'

# super - superclass implementaion, initializing member of sc
# is a relationship & change in behavior
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, basic):
        super().__init__(emp_id, name)
        self._basic = basic


    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da

    def calculate_net(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return gross - tax

class Manager(SalariedEmployee):
    def __init__(self,emp_id,name,basic,allowance):
        super().__init__(emp_id,name,basic)
        self._allowance = allowance

    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da + self._allowance


class ContractEmployee(Employee):
    def __init__(self, emp_id, name,rate,hour):
        super().__init__(emp_id, name)
        self._rate = rate
        self._hour = hour

    def calculate_gross(self):
        return self._rate * self._hour






