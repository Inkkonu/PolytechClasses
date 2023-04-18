package visitor;

public abstract class Visitor {

    public abstract void visit(BinExpression e);

    public abstract void visit(Integer i);

    public abstract void visit(VariableRef v);

    public abstract void visit(Assignment a);

    public abstract void visit(Conditional c);

    public abstract void visit(Print p);

    public abstract void visit(Read r);

    public abstract void visit(While w);

    public abstract void visit(Block b);
}
