package EmployeeDetails;

import java.util.ArrayList;
import java.util.List;

public class TestEmployee {
    public static void main(String[] args) {
        List<Employee> employees = new ArrayList<>();

        employees.add(new Engineer("Alice","R&D",5000.0));
        employees.add(new Manager("Bob","Operations","Cloud Migration"));
        employees.add(new Engineer("Charlie", "QA",10000.0));
        employees.add(new Manager("Diana","HR","Employee portal Revamp"));

        System.out.println("Employee Collection");
        for (Employee e: employees){
            System.out.println(e);
        }
    }
}
