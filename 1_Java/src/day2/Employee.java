package day2;

public class Employee {
    private int id;
    private String name;

    //constructor
    public Employee(int id, String name){
        this.id = id;
        this.name = name;
    }

    //getter
    public int getId(){
        return id;
    }
    public String getName(){
        return name;
    }

    public String toString(){
        return "Employee Details : " + this.getId() + " " + this.getName();

    }




}
