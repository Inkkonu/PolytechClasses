package pw2.pong;

import javax.swing.*;
import java.awt.*;

public class Panel extends JPanel {

    MovingObject p;

    Panel(MovingObject p) {
        super();
        this.p = p;
    }

    @Override
    public void paintComponent(Graphics g) {
        final Rectangle r = p.getRect();
        g.setColor(Color.BLUE);
        g.fillRect(r.x, r.y, r.width, r.height);
        p.move();
    }

}
