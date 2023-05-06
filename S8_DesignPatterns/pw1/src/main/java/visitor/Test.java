package visitor;

import java.util.ArrayList;
import java.util.Arrays;

public class Test {
    public static void main(String[] argv) {
        Statement p = new Assignment(
                new VariableRef("y"),
                new BinExpression(new VariableRef("x"), "*", new Integer(4)));

        ArrayList<Statement> list = new ArrayList<>();
        list.add(p);

        /*
        while(x==2){
            if(y<2)
                x=x+2
            else
                y=y+1
        }
        */
        Statement testWhileConditional = new While(new BinExpression(new VariableRef("x"), "==", new Integer(2)),
                new Block(new ArrayList<>(Arrays.asList(new Conditional(new BinExpression(new VariableRef("y"), "<", new Integer(2)),
                        new Block(new ArrayList<>(Arrays.asList(new Assignment(new VariableRef("x"),
                                new BinExpression(new VariableRef("x"), "+", new Integer(2)))))),
                        new Block(new ArrayList<>(Arrays.asList(new Assignment(new VariableRef("y"),
                                new BinExpression(new VariableRef("y"), "+", new Integer(1)))))))))));

        list.add(testWhileConditional);

        ProgramNode s = new Block(list);

        Visitor v = new VisitorPrint();
        s.accept(v);

        Visitor v1 = new VisitorCount();
        s.accept(v1);

    }
}
