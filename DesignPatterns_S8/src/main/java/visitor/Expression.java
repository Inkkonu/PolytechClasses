package visitor;

public abstract class Expression extends ProgramNode {
    public abstract void accept(Visitor v);
}
