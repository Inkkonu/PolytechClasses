package decorator;

import java.util.Collection;
import java.util.List;

public class CantRemoveElementDecorator<E> extends Decorator<E> {
    public CantRemoveElementDecorator(List<E> component) {
        super(component);
    }

    @Override
    public boolean remove(Object o) {
        return false;
    }

    @Override
    public E remove(int index) {
        return null;
    }

    @Override
    public boolean removeAll(Collection<?> c) {
        return false;
    }

    @Override
    public boolean retainAll(Collection<?> c) {
        return false;
    }

    @Override
    public void clear() {
        // do nothing
    }
}
