package pw2.pong;

import javax.swing.*;

public class MyWindow extends JFrame {

    JPanel pan;

    MyWindow() {
        setSize(320, 200 + 50);
        pan = new Panel(new Pulsar());
        /*	pan = new Paneau(new Pulsar()) ; */
        setContentPane(pan);
    }

}
