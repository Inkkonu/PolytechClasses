package visitor;

public abstract class Statement extends ProgramNode {

    public abstract void accept(Visitor v);
}
