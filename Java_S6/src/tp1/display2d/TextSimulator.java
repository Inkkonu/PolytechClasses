package tp1.display2d;

import java.util.Random;

public class TextSimulator implements IDisplay {

    int nbl;
    int nbc;


    Random random = new Random();


    public int nbLignes() {
        return nbl;
    }

    public int nbColonnes() {
        return nbc;
    }

    Intensite[][] tab;

    public TextSimulator(int l, int c) {
        nbl = l;
        nbc = c;
        tab = new Intensite[l][c];
        for (int i = 0; i < nbl; i++) {
            for (int j = 0; j < nbc; j++) {
                tab[i][j] = new Intensite(random.nextInt(4));
            }
        }
        display();
    }

    public void put(IPoint p, Intensite i) {
        tab[p.getX()][p.getY()] = i;
        display();
    }

    void display() {
        /* je n'affiche pas au fur et à mesure car sinon on a un flush à chaque ligne. */
        StringBuilder s = new StringBuilder(2 * nbl * (nbc + 1));

        for (int n = 0; n < nbl; n++) {
            for (Intensite i : tab[n]) {
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
