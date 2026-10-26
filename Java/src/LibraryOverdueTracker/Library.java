package LibraryOverdueTracker;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Library {
    List<Book> listBook = new ArrayList<>();

    public void addBook(Book book) throws DuplicateBookException{
        for (Book it : listBook){
            if(it.getIsbn().equals(book.getIsbn())) throw new DuplicateBookException(("Book Already Exist"));
            listBook.add(book);
            System.out.println("Book added");
        }
    }
    public void returnBook(String isbn){
        for (int i = 0; i < listBook.size(); i++){
            if(listBook.get(i).getIsbn().equals(isbn)){
                listBook.remove(i);
                System.out.println("Book Removed");
            }
            else throw new BookNotFoundException("Book not found");
        }
        List<Book> getOverdueBooks(LocalDate today){
            return listBook.stream()
                    .filter(Book e -> e.getDate().isBefore(today))
                    .sorted(Comparator.comparing(Book::getDate))
                    .collect(Collectors.toList());

        }

    }
}
