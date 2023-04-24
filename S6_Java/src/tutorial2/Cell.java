package tutorial2;

public class Cell<E extends Comparable<E>> extends List<E> {

    protected final E elem;
    protected final List<E> next;

    Cell(E elem, List<E> next) {
        this.elem = elem;
        this.next = next;
    }

    @Override
    public int length() {
        return 1 + this.next.length();
    }

    @Override
    public boolean contains(E elem) {
        return this.elem.equals(elem) || this.next.contains(elem);
    }

    @Override
    public List<E> find(E elem) {
        if (this.elem.equals(elem)) {
            return this;
        }
        return this.next.find(elem);
    }

    @Override
    public E max() {
        E max = this.next.max();
        if (max == null || this.elem.compareTo(max) >= 0) {
            return this.elem;
        }
        return max;
    }

    @Override
    public List<E> getNext() {
        return this.next;
    }

    @Override
    public String toString() {
        return this.elem + "->";
    }

    @Override
    public E getElem() {
        return this.elem;
    }
}
