package decorator;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Test {

    public static void main(String[] args) {
        List<Integer> l1 = new CantRemoveElementDecorator<>(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(l1);
        System.out.println(l1.remove(4));
        System.out.println(l1.add(6));
        System.out.println(l1);

        System.out.println();

        List<Integer> l2 = new LimitNumberElementsDecorator<>(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)), 5);
        System.out.println(l2);
        System.out.println(l2.remove(4));
        System.out.println(l2.add(6));
        System.out.println(l2.add(7));
        System.out.println(l2);
    }
}
