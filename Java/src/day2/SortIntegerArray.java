package day2;

import java.util.Arrays;

public class SortIntegerArray {

    public static void main(String[] args){
        int[] ints = {3,7,1,10};

//        System.out.println(ints);
        System.out.println(Arrays.toString(ints));

        Arrays.sort(ints);
        System.out.println(Arrays.toString(ints));

        String[] strings = {"XX", "Y", "X"};
        Arrays.sort(strings);
        System.out.println(Arrays.toString(strings));

        int[] newInts = Arrays.copyOf(ints, 6);
        System.out.println(Arrays.toString(newInts));

        System.out.println(Arrays.binarySearch(ints,4));
    }
}
