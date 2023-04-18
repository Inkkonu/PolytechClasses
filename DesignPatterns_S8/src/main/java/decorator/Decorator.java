package decorator;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public abstract class Decorator<E> implements List<E> {

    protected List<E> component;

    public Decorator(List<E> component) {
        this.component = component;
    }


    public int size() {
        return this.component.size();
    }


    public boolean isEmpty() {
        return this.component.isEmpty();
    }


    public boolean contains(Object o) {
        return this.component.contains(o);
    }


    public Iterator<E> iterator() {
        return this.component.iterator();
    }


    public Object[] toArray() {
        return this.component.toArray();
    }


    public <T> T[] toArray(T[] a) {
        return this.component.toArray(a);
    }


    public boolean add(E e) {
        return this.component.add(e);
    }


    public boolean remove(Object o) {
        return this.component.remove(o);
    }


    public boolean containsAll(Collection<?> c) {
        return this.component.containsAll(c);
    }


    public boolean addAll(Collection<? extends E> c) {
        return this.component.addAll(c);
    }


    public boolean addAll(int index, Collection<? extends E> c) {
        return this.component.addAll(index, c);
    }


    public boolean removeAll(Collection<?> c) {
        return this.component.removeAll(c);
    }


    public boolean retainAll(Collection<?> c) {
        return this.component.retainAll(c);
    }


    public void clear() {
        this.component.clear();
    }


    public E get(int index) {
        return this.component.get(index);
    }


    public E set(int index, E element) {
        return this.component.set(index, element);
    }


    public void add(int index, E element) {
        this.component.add(index, element);
    }


    public E remove(int index) {
        return this.component.remove(index);
    }


    public int indexOf(Object o) {
        return this.component.indexOf(o);
    }


    public int lastIndexOf(Object o) {
        return this.component.lastIndexOf(o);
    }


    public ListIterator<E> listIterator() {
        return this.component.listIterator();
    }


    public ListIterator<E> listIterator(int index) {
        return this.component.listIterator(index);
    }

    public List<E> subList(int fromIndex, int toIndex) {
        return this.component.subList(fromIndex, toIndex);
    }

    @Override
    public String toString() {
        return this.component.toString();
    }
}
