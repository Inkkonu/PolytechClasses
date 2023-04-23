package state;

public class E3 implements State {

    private final WordConstructor wordConstructor;

    public E3(WordConstructor wordConstructor) {
        this.wordConstructor = wordConstructor;
    }

    @Override
    public void addA() {
        wordConstructor.getStringBuilder().append("a");
    }

    @Override
    public void addB() {
        wordConstructor.getStringBuilder().append("b");
        wordConstructor.setState(new E4(wordConstructor));
    }

    @Override
    public String toString() {
        return "E3";
    }
}
