package composite;

import lombok.Getter;

public class And extends Operand {

    @Getter
    private Node left;
    @Getter
    private Node right;

    public And(Node left, Node right) {
        this.left = left;
        this.right = right;
    }


    @Override
    public boolean evaluate() {
        return left.evaluate() && right.evaluate();
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
