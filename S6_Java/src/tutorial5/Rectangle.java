package tutorial5;

import java.awt.Graphics2D;

public class Rectangle implements Figure {

    protected int x;
    protected int y;
    protected int width;
    protected int height;

    Rectangle(int x, int y, int w, int h) {
        this.x = x;
        this.y = y;
        this.width = w;
        this.height = h;
    }

    public void draw(Graphics2D g) {
        g.drawRect(x, y, width, height);
    }
}
