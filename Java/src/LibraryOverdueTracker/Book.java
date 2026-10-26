package LibraryOverdueTracker;

import java.time.LocalDate;
import java.util.Objects;

public class Book {
    public String isbn;
    public String title;
    public LocalDate date;

    public Book(String isbn, String title, LocalDate date){
        this.isbn = isbn;
        this.title = title;
        this.date = date;
    }

    public String getIsbn() {
        return isbn;

    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    // Two books are equal if and only if their isbn fields are equal.
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Book)) return false;
        Book other = (Book) o;
        return Objects.equals(this.isbn, other.isbn);
    }

    @Override
    public int hashCode() {
        return Objects.hash(isbn);
    }

    @Override
    public String toString() {
        return "Book{isbn='" + isbn + "', title='" + title + "', dueDate=" + date + "}";
    }
}

