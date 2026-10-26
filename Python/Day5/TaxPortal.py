from abc import ABC, abstractmethod
from typing import override
from numba.cuda.printimpl import print_item
from EmployeePortal import Employee

class Taxpayer(ABC):
    def __init__(self, pan):
        self._pan = pan

    @abstractmethod
    def calculate_tax(self):
        pass

    def __str__(self):
        return f'{self._pan}'

class Consultant(Taxpayer):
    def __init__(self, pan):
        super().__init__(pan)

    def calculate_tax(self):
        return

class SalariedEmployee(Employee,Taxpayer):
    def __init__(self, emp_id, name, basic, pan):
        Employee.__init__(self,emp_id,name)
        Taxpayer.__init__(self,pan)
        self._basic = basic

    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da

    @override
    def calculate_tax(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return tax

    def calculate_net(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return gross - tax

class Manager(SalariedEmployee):
    def __init__(self,emp_id,name,basic,allowance,pan):
        super().__init__(emp_id,name,basic,pan)
        self._allowance = allowance

    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da + self._allowance

class Payroll:
    @staticmethod
    def display_gross(e: Employee):
        print(f"Gross sal for the month : {e.calculate_gross()}")

    @staticmethod
    def display_net(e: SalariedEmployee):
        print(f"Net sal for the month : {e.calculate_net()} ")

    @staticmethod
    def display_tax(payer: Taxpayer):
        print(f'Tax:{payer.calculate_tax()}')

se = SalariedEmployee(3423,'ad',50000,'GAKPR2348')
print(se)
Payroll.display_tax(se)

c = Consultant('GAKPR2348')
Payroll.display_tax(c)