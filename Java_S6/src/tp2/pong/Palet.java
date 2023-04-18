package tp2.pong;

import java.awt.Rectangle;

public class Palet implements MovingObject {

    int x;
    int y;

    int vx;
    int vy;

    int marge;

    Palet() {
        x = 30;
        y = 30;
        vx = 2;
        vy = 2;
        marge = 15;
    }


    boolean sortie_x(int px) {
        return (px < (0 + marge)) || (px > (320 - marge));
    }

    boolean sortie_y(int py) {
        return (py < (0 + marge)) || (py > (200 - marge));
    }

    public void deplace() {
        if (sortie_x(x + vx)) {
            vx = (-1) * vx;
        } else {
            x = x + vx;
        }

        if (sortie_y(y + vy)) {
            vy = (-1) * vy;
        } else {
            y = y + vy;
        }
    }


    public Rectangle getRect() {
        return new Rectangle(x, y, 10, 10);
    }

}
