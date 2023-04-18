package composite;

public abstract class Node {

    public abstract boolean evaluate();

    public abstract void accept(Visitor visitor);
}
