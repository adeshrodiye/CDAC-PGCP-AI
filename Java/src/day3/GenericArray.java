package day3;

import day2.Employee;
import day2.Student;

import java.util.Arrays;

public class GenericArray {
    public static void main(String[] args) {
        Object[] objects = new Object[2];

        Employee e = new Employee(1,"Adesh");
        objects[0] = e;
        objects[1] = new String("Akash");

        System.out.println(Arrays.toString(objects));
    }
}