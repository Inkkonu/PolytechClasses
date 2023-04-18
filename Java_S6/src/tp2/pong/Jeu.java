package tp2.pong;

import javax.swing.* ;

public class Jeu {

    public static void main(String[] args){
        System.setProperty("sun.java2d.opengl", "true"); /* pour animation fluide */
        MaFenetre fen = new MaFenetre() ;
        fen.setVisible(true);
        fen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        while (true){

            fen.repaint() ; /* avec fen.repaint, la fenetre est effacee avant le paint,
				   avec pan.repaint, on garde la memoire de ce qui a été dessiné avant. */

            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}
