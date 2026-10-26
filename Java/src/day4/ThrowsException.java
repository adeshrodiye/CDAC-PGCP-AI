package day4;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class ThrowsException {
    void readConfigFile(String path) throws FileNotFoundException {
        FileReader reader = new FileReader("null");  // can throw IOException
        // ...read the file...
    }

    void loadSettings() throws FileNotFoundException {
        readConfigFile("config.txt");  // caller must also declare or catch it
    }

    public static void main(String[] args) {
        ThrowsException throwsException = new ThrowsException();
        try {
            throwsException.loadSettings();
        }
        catch (FileNotFoundException e){
            System.out.println(e.getMessage());
        }
    }

}
