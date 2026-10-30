package day3;

public class TestInheritance {

    public static void main(String[] args) {
        Vehicle v1 = new Car(100);
        Vehicle v2 = new Car(190, "X700");

        System.out.println(v1.speed);
        Vehicle.doNothing();
        Car.donothing();

        v1.honk();
        Car c = (Car) v1;
        c.engine();
    }

}
