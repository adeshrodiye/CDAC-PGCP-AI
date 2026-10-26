package EmployeeDetails;

public class Engineer extends Employee{
    double incentive;

    public Engineer(String name, String department, double incentive ){
        super(name, department);
        this.incentive = incentive;
    }
    @Override
    public String toString(){
        return  "Engineer [Name = " + name + ", Department = " + department + ", incentive = " + incentive + "]";
    }
}
