package tp2.pong;

import java.awt.*;
import java.lang.Math;

public class Pulsar extends Palet {

    private int taille;

    public Pulsar() {
        super();
        taille = 0;
    }

    @Override
    public Rectangle getRect() {
        Rectangle rect = new Rectangle(x, y, (int) (20 * Math.random()), (int) (20 * Math.random()));
        taille++;
        return rect;
    }
}
