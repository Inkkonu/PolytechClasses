package state;

public class E2 implements State {

    private final WordConstructor wordConstructor;

    public E2(WordConstructor wordConstructor) {
        this.wordConstructor = wordConstructor;
    }

    @Override
    public void addA() {
        wordConstructor.getStringBuilder().append("a");
        wordConstructor.setState(new E4(wordConstructor));
    }

    @Override
    public void addB() {
        wordConstructor.getStringBuilder().append("b");
    }

    @Override
    public String toString() {
        return "E2";
    }
}