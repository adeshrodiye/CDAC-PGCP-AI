package day3;

    public class Car extends Vehicle{

        String name;

        Car(int speed, String name){
            super(speed);
            this.name = name;
        }

        Car(int speed){
//            super(speed);
            this(speed,"Hector");

        }
        public static void donothing(){
            System.out.println("Car donothing");
        }
        public void honk(){
            System.out.println("POMPOM");
        }
        public void engine(){
            System.out.println("Car Engine");
        }
}
