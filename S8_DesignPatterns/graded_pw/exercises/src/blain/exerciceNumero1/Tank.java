package blain.exerciceNumero1;

public class Tank extends Decorator{

    public Tank(Component component){
        super(component, "Tank", 10.0f);
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
