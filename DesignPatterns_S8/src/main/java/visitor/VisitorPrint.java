package visitor;

public class VisitorPrint extends Visitor {
    @Override
    public void visit(BinExpression e) {
        e.getLhs().accept(this);
        System.out.print(e.getOperator());
        e.getRhs().accept(this);
    }

    @Override
    public void visit(Integer i) {
        System.out.print(i.getValue());
    }

    @Override
    public void visit(VariableRef v) {
        System.out.print(v.getName());
    }

    @Override
    public void visit(Assignment a) {
        a.getVar().accept(this);
        System.out.print("=");
        a.getRhs().accept(this);
        System.out.println();
    }

    @Override
    public void visit(Conditional c) {
        System.out.print("if(");
        c.getCondition().accept(this);
        System.out.print("){\n\t");
        c.getThenPart().accept(this);
        System.out.print("}\nelse {\n\t");
        c.getElsePart().accept(this);
        System.out.print("}");
    }

    @Override
    public void visit(Print p) {
        p.getPrint().accept(this);
    }

    @Override
    public void visit(Read r) {
        r.getVar().accept(this);
    }

    @Override
    public void visit(While w) {
        System.out.print("while(");
        w.getCondition().accept(this);
        System.out.print("){\n\t");
        w.getBody().accept(this);
        System.out.print("}");
    }

    @Override
    public void visit(Block b) {
        b.getStatements().forEach(s -> s.accept(this));

    }
}
