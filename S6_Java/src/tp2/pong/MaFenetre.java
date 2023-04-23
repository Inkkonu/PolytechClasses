package tp2.pong;

import javax.swing.*;

public class MaFenetre extends JFrame {
    MaFenetre(){
        setSize(320,200+50);
        pan = new Panneau(new Pulsar()) ;
        /*	pan = new Paneau(new Pulsar()) ; */
        setContentPane(pan) ;
    }

    JPanel pan ;

}
