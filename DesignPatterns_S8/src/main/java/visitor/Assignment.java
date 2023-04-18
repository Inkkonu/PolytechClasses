package visitor;

public class Assignment extends Statement {
    private Expression rhs;
    private VariableRef var;

    public Assignment(VariableRef var, Expression rhs) {
        super();
        this.rhs = rhs;
        this.var = var;
    }

    public Expression getRhs() {
        return rhs;
    }

    public void setRhs(Expression rhs) {
        this.rhs = rhs;
    }

    public VariableRef getVar() {
        return var;
    }

    public void setVar(VariableRef var) {
        this.var = var;
    }

    @Override
    public void accept(Visitor v) {
        v.visit(this);
    }
}
