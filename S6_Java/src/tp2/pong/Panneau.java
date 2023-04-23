package tp2.pong;

import javax.swing.* ;
import java.awt.* ;

public class Panneau extends JPanel {

    Panneau(MovingObject p){
        super();
        this.p=p ;
    }

    MovingObject p ;

    @Override
    public void paintComponent (Graphics g){
        final Rectangle r = p.getRect() ;
        g.setColor(Color.BLUE);
        g.fillRect (r.x, r.y, r.width, r.height);
        p.deplace() ;
    }

}
