package day4;

public class ThrowException {
    void withdraw(double amount, double balance) {
        if (amount > balance) {
            throw new IllegalArgumentException(
                    "Insufficient funds");   // creates AND raises the exception
        }
        balance -= amount;
    }

    public static void main(String[] args) {
        ThrowException throwException = new ThrowException();
        try{
            throwException.withdraw(1000,100);
        }
        catch (IllegalAccessError e){
            System.out.println(e.getMessage());
        }
    }
}
