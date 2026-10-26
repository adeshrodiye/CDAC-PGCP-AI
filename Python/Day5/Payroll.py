from  EmployeePortal import (Employee, SalariedEmployee, ContractEmployee, Manager)
from  TaxPortal import Taxpayer
class Payroll:
    @staticmethod
    def display_gross(e:Employee):
        print(f"Gross sal for the month : {e.calculate_gross()}")

    @staticmethod
    def display_net(e:SalariedEmployee):
        print(f"Net sal for the month : {e.calculate_net()} ")
    #
    # @staticmethod
    # def display_tax(payer: Taxpayer):
    #     print(f'Tax:{payer.calculate_tax()}')

se = SalariedEmployee(345,'ABC',100000)
se1 = SalariedEmployee(101,'BBC',80000)
me = Manager(378,"CCC",120000,20000)
ce = ContractEmployee(978,"DDD",80,500)

print(se)
Payroll.display_gross(se)
Payroll.display_net(se)
print(se1)
Payroll.display_gross(se1)
Payroll.display_net(se1)
print(me)
Payroll.display_gross(me)
Payroll.display_net(me)
print(ce)
Payroll.display_gross(ce)
