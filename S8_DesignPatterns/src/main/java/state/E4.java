package state;

public class E4 implements State {

    private final WordConstructor wordConstructor;

    public E4(WordConstructor wordConstructor) {
        this.wordConstructor = wordConstructor;
    }

    @Override
    public void addA() {
        throw new IllegalStateException("Cannot add 'a', reached final state");
    }

    @Override
    public void addB() {
        throw new IllegalStateException("Cannot add 'b', reached final state");
    }

    @Override
    public String toString() {
        return "E4";
    }
}
