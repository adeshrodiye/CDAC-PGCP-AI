package day4;

public class NestedFinally {
    public static void main(String[] args) {
        try {
            try {
                int[] data = new int[5];
                data[10] = 1;
            }finally {
                System.out.println("Inner Cleanup");
            }
            try {
                int[] data = new int[5];
                data[10] = 1;
            }finally {
                System.out.println("2nd Inner Cleanup");
            }
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println("Caught by outer");
        } finally {
            System.out.println("Outer Cleanup");
        }
    }
}
