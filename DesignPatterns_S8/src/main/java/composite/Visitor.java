package composite;

public abstract class Visitor {

    public abstract void visit(True t);
    public abstract void visit(False f);
    public abstract void visit(Not n);
    public abstract void visit(And a);
    public abstract void visit(Or o);
}
