package tutorial2;

public class Main {

    public static void main(String[] args) {
        List<String> l = new Cell<>("Kiki", new Cell<>("Victor", new Cell<>("Loic", new Empty<>())));
        System.out.println("Length : " + l.length());
        System.out.println("Max : " + l.max());
        System.out.println("Loic appears " + l.count("Loic") + " time(s)");
        ListIterator<String> listIter = new ListIterator<>(l);
        while(listIter.hasNext()){
            System.out.print(l);
            l = listIter.next();
        }
    }
}
