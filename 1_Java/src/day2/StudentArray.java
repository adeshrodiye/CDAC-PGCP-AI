package day2;

import java.util.Scanner;

public class StudentArray {

    private Student[] students = new Student[2];
    private Scanner sc = new Scanner(System.in);

    void populateStudent() {
        for (int i = 0; i < students.length; i++) {
            System.out.println("Please Enter rollno and name");
            int rollno = sc.nextInt();
            String name = sc.next();
            Student student = new Student(rollno, name);
            students[i] = student;
        }
    }

    void displayStudent() {
        for (Student s : students) {
//            System.out.println("Student details -> " + s.getRollno() + " " + s.getName());
            System.out.println(s);
        }
    }
}