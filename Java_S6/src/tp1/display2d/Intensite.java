package tp1.display2d;

class Intensite {

    int v;

    public Intensite(int i) {
        if (i < 0 || i > 3) {
            throw new IndexOutOfBoundsException();
        } else {
            v = i;
        }
    }

    public int get() {
        return v;
    }
}
    
