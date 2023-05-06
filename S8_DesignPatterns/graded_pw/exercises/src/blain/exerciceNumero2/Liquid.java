package blain.exerciceNumero2;

public class Liquid implements State{

    private Water water;

    public Liquid(Water water) {
        this.water = water;
    }

    @Override
    public void fusion() {
        System.out.print("Liquid water can't fusion.");
    }

    @Override
    public void solidification() {
        System.out.println("Liquid to solid.");
        water.setState(new Solid(water));
    }

    @Override
    public void evaporation() {
        System.out.println("Liquid to gaz.");
        water.setState(new Gazeous(water));
    }

    @Override
    public void condensation() {
        System.out.println("Liquid water can't condensation.");
    }

    @Override
    public void sublimation() {
        System.out.println("Liquid water can't sublimation.");
    }

    @Override
    public void solidCondensation() {
        System.out.println("Liquid water can't solid condensation.");
    }
}
