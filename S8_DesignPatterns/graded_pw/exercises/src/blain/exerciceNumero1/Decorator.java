package blain.exerciceNumero1;

public abstract class Decorator extends Component{

    private Component component;
    protected String name;
    protected float price;

    public Decorator(Component component, String name, float price){
        this.component = component;
        this.name = name;
        this.price = price;
    }

    public float getPrice(){
        return component.getPrice();
    }

    public String getDescription(){
        return component.getDescription();
    }
}
