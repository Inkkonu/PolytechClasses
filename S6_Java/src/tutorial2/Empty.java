package tutorial2;

import java.util.NoSuchElementException;

public class Empty<E extends Comparable<E>> extends List<E> {

    @Override
    public int length() {
        return 0;
    }

    @Override
    public boolean contains(E elem) {
        return false;
    }

    @Override
    public List find(E elem) {
        return null;
    }

    @Override
    public E max() {
        return null;
    }

    @Override
    public List<E> getNext() throws NoSuchElementException {
        throw new NoSuchElementException();
    }

    @Override
    public String toString() {
        return "Empty";
    }

    @Override
    public E getElem() {
        return null;
    }
}
