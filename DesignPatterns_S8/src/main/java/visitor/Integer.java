package visitor;

public class Integer extends Expression {
    private int value;

    public Integer(int v) {
        this.value = v;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    @Override
    public void accept(Visitor v) {
        v.visit(this);
    }
}
