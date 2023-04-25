package pw1.display2d;

import java.util.Random;

public class TextSimulator implements IDisplay {

    int nbl;
    int nbc;


    Random random = new Random();


    public int nbLines() {
        return nbl;
    }

    public int nbColumns() {
        return nbc;
    }

    Intensity[][] tab;

    public TextSimulator(int l, int c) {
        nbl = l;
        nbc = c;
        tab = new Intensity[l][c];
        for (int i = 0; i < nbl; i++) {
            for (int j = 0; j < nbc; j++) {
                tab[i][j] = new Intensity(random.nextInt(4));
            }
        }
        display();
    }

    public void put(IPoint p, Intensity i) {
        tab[p.getX()][p.getY()] = i;
        display();
    }

    void display() {
        StringBuilder s = new StringBuilder(2 * nbl * (nbc + 1));

        for (int n = 0; n < nbl; n++) {
            for (Intensity i : tab[n]) {
                switch (i.get()) {
                    case 0:
                        s.append(' ');
                        break;
                    case 1:
                        s.append('.');
                        break;
                    case 2:
                        s.append('_');
                        break;
                    case 3:
                        s.append('*');
                }
                s.append(' ');
            }
            s.append('\n');
        }

        System.out.println(s);

    }

}
