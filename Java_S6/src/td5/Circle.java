package td5;

import java.awt.Graphics2D;

public class Circle implements Figure{

    protected int x;
    protected int y;
    protected int width;

    public Circle(int x, int y, int width) {
        this.x = x;
        this.y = y;
        this.width = width;
    }

    public void draw(Graphics2D g) {
        g.drawOval(x, y, width, width);
    }
}
