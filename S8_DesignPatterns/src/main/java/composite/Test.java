package composite;

public class Test {

    public static void main(String[] args) {
        //Implement a test for this formula : ((True OR False) AND ( False AND True)) OR (NOT False)
        Node n = new Or(new And(new Or(new True(), new False()), new And(new False(), new True())), new Not(new False()));
        Visitor v1 = new VisitorToPython();
        Visitor v2 = new VisitorToC();
        n.accept(v1);
        System.out.println();
        n.accept(v2);

        System.out.println();

        //Implement a test for this formula : (NOT(True)) OR (NOT(False))
        Node n2 = new Or(new Not(new True()), new Not(new False()));
        Visitor v3 = new VisitorToPython();
        Visitor v4 = new VisitorToC();
        n2.accept(v3);
        System.out.println();
        n2.accept(v4);
    }
}
