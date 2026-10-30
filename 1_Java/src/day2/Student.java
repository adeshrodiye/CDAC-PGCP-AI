package day2;

public class Student {
    private int rollno;
    private String name;

    public Student(int rollno, String name){
        this.rollno = rollno;
        this.name = name;
    }
    //getter
    public int getRollno(){
        return rollno;
    }
    public String getName(){
        return name;
    }
    public String toString() {
        return "Student Details : " + this.getRollno() + " " + this.getName();
    }
}
