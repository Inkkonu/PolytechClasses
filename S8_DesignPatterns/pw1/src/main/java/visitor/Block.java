package visitor;

import java.util.ArrayList;

public class Block extends Statement {
    private ArrayList<Statement> statements;

    public Block(ArrayList<Statement> s) {
        super();
        this.statements = s;
    }

    public ArrayList<Statement> getStatements() {
        return statements;
    }

    @Override
    public void accept(Visitor v) {
        v.visit(this);
    }
}
