package visitor;

import lombok.Getter;

public class VisitorCount extends Visitor {

    @Getter
    private int countWhile = 0;
    @Getter
    private int countConditional = 0;
    @Getter
    private int countAssignment = 0;
    @Getter
    private int countPrint = 0;
    @Getter
    private int countRead = 0;

    @Override
    public void visit(BinExpression e) {

    }

    @Override
    public void visit(Integer i) {

    }

    @Override
    public void visit(VariableRef v) {

    }

    @Override
    public void visit(Assignment a) {
        countAssignment++;
    }

    @Override
    public void visit(Conditional c) {
        countConditional++;
        c.getThenPart().accept(this);
        c.getElsePart().accept(this);
    }

    @Override
    public void visit(Print p) {
        countPrint++;
    }

    @Override
    public void visit(Read r) {
        countRead++;
    }

    @Override
    public void visit(While w) {
        countWhile++;
        w.getBody().accept(this);
    }

    @Override
    public void visit(Block b) {
        b.getStatements().forEach(s -> s.accept(this));
    }


}
