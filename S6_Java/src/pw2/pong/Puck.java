package pw2.pong;

import java.awt.Rectangle;

public class Puck implements MovingObject {

    int x;
    int y;

    int vx;
    int vy;

    int margin;

    Puck() {
        x = 30;
        y = 30;
        vx = 2;
        vy = 2;
        margin = 15;
    }


    boolean exit_x(int px) {
        return (px < (margin)) || (px > (320 - margin));
    }

    boolean exit_y(int py) {
        return (py < (margin)) || (py > (200 - margin));
    }

    public void move() {
        if (exit_x(x + vx)) {
            vx = (-1) * vx;
        } else {
            x = x + vx;
        }

        if (exit_y(y + vy)) {
            vy = (-1) * vy;
        } else {
            y = y + vy;
        }
    }


    public Rectangle getRect() {
        return new Rectangle(x, y, 10, 10);
    }

}
