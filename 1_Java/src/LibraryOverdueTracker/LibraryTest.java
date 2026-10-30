package LibraryOverdueTracker;

import java.time.LocalDate;
import java.util.List;

public class LibraryTest {
    public static void main(String[] args) {
        LibraryTest libTest = new LibraryTest();
        Library lib = new Library();

        try {
            lib.addBook(new Book("978-1", "Clean Code", LocalDate.of(2026, 1, 10));
            lib.addBook(new Book("978-2", "Effective Java", LocalDate.of(2026, 1, 5));
            lib.addBook(new Book("978-3","Core Java", LocalDate.of(2026,3,5));
        }catch (DuplicateBookException e){
            System.out.println(e.getMessage());
        }

        try{
            lib.returnBook("978-99");
        }catch (BookNotFoundException e){
            System.out.println(e.getMessage());
        }
        List<Book> listBook = 
    }
}
