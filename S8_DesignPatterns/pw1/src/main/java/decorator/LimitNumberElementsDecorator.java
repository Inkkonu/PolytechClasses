package decorator;

import java.util.Collection;
import java.util.List;

public class LimitNumberElementsDecorator<E> extends Decorator<E> {

    private int maximumNumberOfElements;

    public LimitNumberElementsDecorator(List<E> component, int maximumNumberOfElements) {
        super(component);
        this.maximumNumberOfElements = maximumNumberOfElements;
    }

    @Override
    public boolean add(E e) {
        if (this.component.size() < this.maximumNumberOfElements) {
            return this.component.add(e);
        } else {
            return false;
        }
    }

    @Override
    public void add(int index, E element) {
        if (this.component.size() < this.maximumNumberOfElements) {
            this.component.add(index, element);
        }
    }

    @Override
    public boolean addAll(Collection<? extends E> c) {
        boolean hasChanged = false;
        while (this.component.size() < this.maximumNumberOfElements && c.iterator().hasNext()) {
            this.component.add(c.iterator().next());
            hasChanged = true;
        }
        return hasChanged;
    }

    @Override
    public boolean addAll(int index, Collection<? extends E> c) {
        boolean hasChanged = false;
        while (this.component.size() < this.maximumNumberOfElements && c.iterator().hasNext()) {
            this.component.add(index, c.iterator().next());
            index++;
            hasChanged = true;
        }
        return hasChanged;
    }
}