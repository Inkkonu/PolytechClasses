package composite;

import lombok.Getter;

public class Not extends Operand{

    @Getter
    private Node node;

    public Not(Node node) {
        this.node = node;
    }

    @Override
    public boolean evaluate() {
        return !node.evaluate();
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
