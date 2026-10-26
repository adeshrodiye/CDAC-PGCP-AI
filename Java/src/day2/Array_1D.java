package day2;

import java.util.Scanner;

public class Array_1D {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int [] int_array = new int[5];

        for (int i=0; i<int_array.length;i++){
            int_array[i] = sc.nextInt();
        }
        for (int i=0; i<int_array.length;i++){
            System.out.println(int_array[i]);
        }

        String [] str_array = {"Adesh","Akash"};
        System.out.println(str_array[0]);
        System.out.println(str_array[1]);

    }
}
