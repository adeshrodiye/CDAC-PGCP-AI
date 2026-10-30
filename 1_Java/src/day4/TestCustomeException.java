package day4;

public class TestCustomeException {

    public static void main(String[] args) {
//        throw new CustomeException("");
        new TestCustomeException().dosomething();

    }
    void dosomething(){
        String s = new String("Adesh");
        if (!s.equals("Adesh")) throw new CustomeException("Custome Message");

    }

}