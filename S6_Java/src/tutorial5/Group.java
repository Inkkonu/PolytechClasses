package tutorial5;

import java.awt.Graphics2D;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Group implements Figure {

    protected List<Figure> figures;

    public Group(Figure... figures) {
        this.figures = new ArrayList<>();
        Collections.addAll(this.figures, figures);
    }

    @Override
    public void draw(Graphics2D g) {
        for (Figure f : this.figures) {
            f.draw(g);
        }
    }
}
