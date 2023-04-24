package tutorial2;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class ListIterator<E extends Comparable<E>> implements Iterator<List<E>> {

    List<E> cell;

    public ListIterator(List<E> cell) {
        this.cell = cell;
    }

    @Override
    public boolean hasNext() {
        try {
            cell.getNext();
            return true;
        } catch (NoSuchElementException e) {
            return false;
        }
    }

    @Override
    public List<E> next() throws NoSuchElementException {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        this.cell = cell.getNext();
        return cell;
    }
}
