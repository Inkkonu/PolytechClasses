package state;

public class E1 implements State {

    private final WordConstructor wordConstructor;

    public E1(WordConstructor wordConstructor) {
        this.wordConstructor = wordConstructor;
    }

    @Override
    public void addA() {
        wordConstructor.getStringBuilder().append("a");
        wordConstructor.setState(new E2(wordConstructor));
    }

    @Override
    public void addB() {
        wordConstructor.getStringBuilder().append("b");
        wordConstructor.setState(new E3(wordConstructor));
    }

    @Override
    public String toString() {
        return "E1";
    }
}
