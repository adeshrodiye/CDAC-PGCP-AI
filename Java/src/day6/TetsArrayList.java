package day6;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class TetsArrayList {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(15);
        list.add(25);
        list.add(35);
        System.out.println("list : " + list);
//
//        list.add(0,10);
//        System.out.println(list);
//
//        System.out.println("Remove Value -> " +list.set(1,20));
//        System.out.println(list);
//
////        list.remove(100);
//        System.out.println(list.remove(4));
//        System.out.println(list);
//
//        List<Integer> list1 = new ArrayList<>();
//        list1.add(5);
//        list1.add(15);
//        System.out.println("list1 " + list1);
//
//        list.addAll(1,list1);
//        System.out.println(list);
//
//        list.retainAll(list1); //retain all values in list1 and remove all other values
//        System.out.println(list);

         //Iterator
        Iterator<Integer> it = list.iterator();

        while  (it.hasNext()){
            System.out.println(it.next());
            it.remove();
        }
        System.out.println(list);


    }
}
