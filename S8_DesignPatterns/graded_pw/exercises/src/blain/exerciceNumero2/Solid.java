package blain.exerciceNumero2;

public class Solid implements State{

    private Water water;

    public Solid(Water water) {
        this.water = water;
    }


    @Override
    public void fusion() {
        System.out.println("Solid to liquid.");
        water.setState(new Liquid(water));
    }

    @Override
    public void solidification() {
        System.out.println("Solid water can't solidification.");
    }

    @Override
    public void evaporation() {
        System.out.println("Solid water can't evaporation.");
    }

    @Override
    public void condensation() {
        System.out.println("Solid water can't condensation.");
    }

    @Override
    public void sublimation() {
        System.out.println("Solid to gaz.");
        water.setState(new Gazeous(water));
    }

    @Override
    public void solidCondensation() {
        System.out.println("Solide water can't solid condensation.");
    }
}
