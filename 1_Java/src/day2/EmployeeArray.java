package day2;

import java.util.Scanner;

public class EmployeeArray {

    private Employee[] employees = new Employee[2];

    private Scanner sc = new Scanner(System.in);

    void populateEmployee(){
        for (int i = 0; i< employees.length; i++) {
            System.out.println("Please Enter id and name");
            int id = sc.nextInt();
            String name = sc.next();
            Employee employee = new Employee(id,name);
            employees[i] = employee;
        }
    }
    void displayEmployee(){
        for (Employee e: employees){
//            System.out.println("Employee details -> "+ e.getId() + " " + e.getName());
            System.out.println(e);

        }
    }
}
