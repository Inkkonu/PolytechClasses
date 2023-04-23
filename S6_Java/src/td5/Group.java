package td5;

import java.awt.Graphics2D;
import java.util.ArrayList;
import java.util.List;

public class Group implements Figure{

    protected List<Figure> figures;

    public Group(Figure... figures){
        this.figures = new ArrayList<>();
        for(Figure f : figures){
            this.figures.add(f);
        }
    }

    @Override
    public void draw(Graphics2D g) {
        for(Figure f : this.figures){
            f.draw(g);
        }
    }
}
