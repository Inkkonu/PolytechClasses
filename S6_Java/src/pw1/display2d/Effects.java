package pw1.display2d;

class Effects {

    IDisplay theDisplay;

    int x;
    int y;

    public Effects(IDisplay d) {
        theDisplay = d;
        x = d.nbLines();
        y = d.nbColumns();
    }


    public void init(Intensity v) {
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                theDisplay.put(new Point(i, j), v);
            }
        }
    }

    public void circle(int rayon) {
        int r2 = rayon * rayon;
        Intensity min = new Intensity(0);
        Intensity max = new Intensity(3);

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (i * i + j * j < r2) {
                    theDisplay.put(new Point(i, j), max);
                } else {
                    theDisplay.put(new Point(i, j), min);
                }
            }
        }
    }


}
