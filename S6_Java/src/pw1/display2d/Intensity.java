package pw1.display2d;

class Intensity {

    int v;

    public Intensity(int i) {
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
    
