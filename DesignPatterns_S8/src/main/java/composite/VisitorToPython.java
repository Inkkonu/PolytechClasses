package composite;

public class VisitorToPython extends Visitor {


    @Override
    public void visit(True t) {
        System.out.print("True");
    }

    @Override
    public void visit(False f) {
        System.out.print("False");
    }

    @Override
    public void visit(Not n) {
        System.out.print("not(");
        n.getNode().accept(this);
        System.out.print(")");
    }

    @Override
    public void visit(And a) {
        System.out.print("(");
        a.getLeft().accept(this);
        System.out.print(" and ");
        a.getRight().accept(this);
        System.out.print(")");
    }

    @Override
    public void visit(Or o) {
        System.out.print("(");
        o.getLeft().accept(this);
        System.out.print(" or ");
        o.getRight().accept(this);
        System.out.print(")");
    }
}
