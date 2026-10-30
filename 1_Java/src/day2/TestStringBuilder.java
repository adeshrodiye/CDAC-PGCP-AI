package day2;

public class TestStringBuilder {
    public static void main(String[] args) {
        String s1 = "Adesh";
        StringBuilder sb = new StringBuilder(s1);
        sb.reverse();
        System.out.println(sb.toString());
        System.out.println(s1);
        sb.delete(2,4);
        System.out.println(sb);
    }
}

