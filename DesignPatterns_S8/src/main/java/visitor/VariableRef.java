package visitor;

public class VariableRef extends Expression {
    private String name;

    public VariableRef(String name) {
        super();
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public void accept(Visitor v) {
        v.visit(this);
    }
}
