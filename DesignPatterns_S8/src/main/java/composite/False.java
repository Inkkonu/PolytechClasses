package composite;

public class False extends Value {

    public False() {
        value = false;
    }

    @Override
    public boolean evaluate() {
        return false;
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
