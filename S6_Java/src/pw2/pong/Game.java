package pw2.pong;

import javax.swing.*;

public class Game {

    public static void main(String[] args) {
        System.setProperty("sun.java2d.opengl", "true"); /* for a fluid animation */
        MyWindow window = new MyWindow();
        window.setVisible(true);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        while (true) {

            window.repaint(); /* with window.repaint, the window is cleared before drawing the new frame,
                   with pan.repaint, we keep in memory what has been drawn before */

            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}
