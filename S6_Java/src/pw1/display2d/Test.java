package pw1.display2d;

public class Test {

    public static void main(String[] args) {
        TextSimulator ts = new TextSimulator(4, 6);
        ts.display();
        Effects eff = new Effects(ts);
        eff.circle(3);
    }
}
