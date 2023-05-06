package composite;

public class True extends Value {

    public True() {
        value = true;
    }

    @Override
    public boolean evaluate() {
        return true;
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }


}
