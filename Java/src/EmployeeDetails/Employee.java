package EmployeeDetails;

public class Employee {
    String name;
    String department;

    public Employee(String name, String department){
        this.name = name;
        this.department = department;
    }
    @Override
    public String toString(){
        return  "Employee[Name=" + name + ", Department = " + department + "]";
    }

}
