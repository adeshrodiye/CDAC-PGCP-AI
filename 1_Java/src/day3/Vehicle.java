package day3;

public class Vehicle {

    private int id;
    protected int speed;
    protected final int numberofTyre = 4;

    Vehicle(int speed){
        id=10;
        this.speed = speed;
    }

    public static void doNothing(){
        System.out.println("Vehicle doNothing");
    }

    public void honk(){
        System.out.println("BEEP");
    }
}
