package blain.exerciceNumero1;

public class Flag extends Decorator{

    public Flag(Component component){
        super(component, "Flag", 0.5f);
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
