package visitor;

import lombok.Getter;
import lombok.Setter;

public class Conditional extends Statement {

    @Getter
    @Setter
    private Expression condition;

    @Getter
    @Setter
    private Block thenPart;
    @Getter
    @Setter
    private Block elsePart;

    public Conditional(Expression condition, Block thenPart, Block elsePart) {
        super();
        this.condition = condition;
        this.thenPart = thenPart;
        this.elsePart = elsePart;
    }

    @Override
    public void accept(Visitor v) {
        v.visit(this);
    }
}
