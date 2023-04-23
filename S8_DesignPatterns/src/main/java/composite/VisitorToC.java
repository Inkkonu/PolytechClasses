package composite;

public class VisitorToC extends Visitor {


    @Override
    public void visit(True t) {
        System.out.print("1");
    }

    @Override
    public void visit(False f) {
        System.out.print("0");
    }

    @Override
    public void visit(Not n) {
        System.out.print("!(");
        n.getNode().accept(this);
        System.out.print(")");
    }

    @Override
    public void visit(And a) {
        System.out.print("(");
        a.getLeft().accept(this);
        System.out.print(" && ");
        a.getRight().accept(this);
        System.out.print(")");
    }

    @Override
    public void visit(Or o) {
        System.out.print("(");
        o.getLeft().accept(this);
        System.out.print(" || ");
        o.getRight().accept(this);
        System.out.print(")");
    }
}
