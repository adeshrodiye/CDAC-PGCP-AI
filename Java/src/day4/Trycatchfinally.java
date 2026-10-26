package day4;

import java.net.SecureCacheResponse;
import java.util.Scanner;

public class Trycatchfinally {
    public static void main(String[] args) {
        Scanner sc = null;
        try {
            sc  = new Scanner(System.in);
            int numerator,denominator;
            numerator = sc.nextInt();
            denominator = sc.nextInt();
            System.out.println(numerator/denominator);

        }
        catch (ArithmeticException e){
            System.out.println("YOU ARE DIVIDING BY ZERO...");
        }
        finally {
            System.out.println("Closing Scanner Connection");
            sc.close();
        }
    }
}
