package day2;

public class Wrapper {

    public static void main(String[] args) {
        Integer i = 5;
        Integer i1 = new Integer(5);

        Integer i2 = Integer.valueOf("7"); //object created &
        int i3 = Integer.parseInt("7");

        if (i == i1)
            System.out.println("i == i1 -> True");
        else
            System.out.println("i == i1 -> False");

        if (i.equals(i1))
            System.out.println("i.equals(i1) -> True");
        else
            System.out.println("i.equals(i1) -> False");

        if (i2 == i3)
            System.out.println("i2 == i3 -> True");
        else
            System.out.println("i2 == i3 -> False");

        if (i2.equals(i3))
            System.out.println("i2.equals(i3) -> True");
        else
            System.out.println("i2.equals(i3) -> False");

    }
}
