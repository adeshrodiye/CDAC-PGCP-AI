package day2;

public class TestString {
    public static void main(String[] args) {
        String s1 = "Adesh";
        String s2 = "Adesh";
        String s3 = new String("Adesh");
        String s4 = new String("Adesh");


        if (s1 == s2)
            System.out.println("s1 == s2 -> True");
        else
            System.out.println("s1 == s2 -> False");

        if (s1.equals(s2))
            System.out.println("s1.equals(s2) -> True");
        else
            System.out.println("s1.equals(s2) -> False");


        if (s3 == s4)
            System.out.println("s3 == s4 -> True");
        else
            System.out.println("s3 == s4 -> False");

        if (s3.equals(s4))
            System.out.println("s3.equals(s4) -> True");
        else
            System.out.println("s3.equals(s4) -> False");


        if (s1 == s4)
            System.out.println("s1 == s4 -> True");
        else
            System.out.println("s1 == s4 -> False");

        if (s1.equals(s4))
            System.out.println("s1.equals(s4) -> True");
        else
            System.out.println("s1.equals(s4) -> False");


        s3 = s1;
        if (s1 == s3)
            System.out.println("s1 == s3 -> True");
        else
            System.out.println("s1 == s3 -> False");

        if (s1.equals(s3))
            System.out.println("s1.equals(s3) -> True");
        else
            System.out.println("s1.equals(s3) -> False");

        String s5 = "Hello";
        String s6 = s5.concat("World");
        System.out.println(s6);


    }
}
