package day6;

import com.sun.source.doctree.SeeTree;

import java.util.HashSet;
import java.util.Set;

public class TestSet {
    public static void main(String[] args) {
        Set<Integer> integerSet = new HashSet<>();

        integerSet.add(5);
        integerSet.add(15);
        integerSet.add(25);
        integerSet.add(35);

        System.out.println(integerSet);

        integerSet.add(5);

        System.out.println(integerSet);
    }
}
