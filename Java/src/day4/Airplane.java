package day4;

public class Airplane implements IFly{

    @Override
    public void fly() {
        System.out.println("Airplane Fly");
    }

    @Override
    public void land() {
        return;
    }
}
