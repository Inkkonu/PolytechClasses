package pw7;

public class ClassToClone implements Cloneable {

    protected int i;

    public ClassToClone(int i) {
        this.i = i;
    }

    @Override
    public String toString() {
        return String.valueOf(this.i);
    }

    @Override
    public ClassToClone clone() {
        return new ClassToClone(this.i);
    }

    @Override
    public void finalize() throws Throwable {
        System.out.println("Finalize is called yo");
        super.finalize();
    }

    public static void main(String[] args) {
        ClassToClone c = new ClassToClone(3);
        System.out.println(c);
        System.out.println(c.getClass().getName());
        Object c2 = c.clone();
        System.out.println(c2);
        System.out.println(c2.getClass().getName());
    }
}
