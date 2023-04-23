package visitor;

import lombok.Setter;
import lombok.Getter;

public class While extends Statement {

    @Getter
    @Setter
    private Expression condition;

    @Getter
    @Setter
    private Block body;

    public While(Expression condition, Block body) {
        super();
        this.condition = condition;
        this.body = body;
    }

    @Override
    public void accept(Visitor v) {
        v.visit(this);
    }
}