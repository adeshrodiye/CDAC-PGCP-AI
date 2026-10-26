package EmployeeDetails;

public class Manager extends Employee{
    String project;

    public Manager(String name, String department, String project) {
        super(name, department);
        this.project = project;
    }
    @Override
    public String toString(){
        return  "Manager [Name = " + name + ", Department = " + department + ", project = " + project + "]";
    }
}
