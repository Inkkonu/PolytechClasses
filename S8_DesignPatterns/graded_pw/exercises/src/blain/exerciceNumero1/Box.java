package blain.exerciceNumero1;

public class Box extends Component{

    private String name;

    public Box(String name){
        this.name = name;
    }

    @Override
    public float getPrice(){
        return 0.0f;
    }

    @Override
    public String getDescription(){
        return name;
    }
}
