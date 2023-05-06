package blain.exerciceNumero1;

public class Test {

    public static void main(String[] args) {
        Component c = new Box("Box");
        c = new Soldier(c);
        c = new Soldier(c);
        c = new Soldier(c);
        c = new Tank(c);
        c = new Flag(c);

        System.out.println(c.getDescription() + "\n" + c.getPrice());
    }
}
