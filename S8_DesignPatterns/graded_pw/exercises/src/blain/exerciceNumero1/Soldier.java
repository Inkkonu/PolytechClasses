package blain.exerciceNumero1;

public class Soldier extends Decorator{

    public Soldier(Component component){
        super(component, "Soldier", 1.0f);
    }

    @Override
    public float getPrice(){
        return super.getPrice() + price;
    }

    @Override
    public String getDescription(){
        return super.getDescription() + " " + name;
    }
}
