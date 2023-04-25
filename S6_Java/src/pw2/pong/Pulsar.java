package pw2.pong;

import java.awt.*;
import java.lang.Math;

public class Pulsar extends Puck {

    private int size;

    public Pulsar() {
        super();
        size = 0;
    }

    @Override
    public Rectangle getRect() {
        Rectangle rect = new Rectangle(x, y, (int) (20 * Math.random()), (int) (20 * Math.random()));
        size++;
        return rect;
    }
}
