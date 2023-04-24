package tutorial2;

import java.util.Iterator;

public abstract class List<E extends Comparable<E>> implements Iterable<List<E>> {
    ListIterator<E> iterator;

    abstract int length();

    abstract boolean contains(E e);


    abstract List find(E e);

    abstract E max();

    abstract List<E> getNext();

    abstract E getElem();

    public Iterator<List<E>> iterator() {
        return new ListIterator<>(this);
    }

    public int count(E e) {
        if (this.getElem() != null) {
            if(this.getElem().equals(e)){
                return 1 + this.getNext().count(e);
            }
            else{
                return this.getNext().count(e);
            }
        } else {
            return 0;
        }
    }
}
