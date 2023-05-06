package blain.exerciceNumero2;

public class Gazeous implements State{

    private Water water;

    public Gazeous(Water water) {
        this.water = water;
    }


    @Override
    public void fusion() {
        System.out.println("Gazeous water can't fusion.");
    }

    @Override
    public void solidification() {
        System.out.println("Gazeous water can't solidification.");
    }

    @Override
    public void evaporation() {
        System.out.println("Gazeous water can't evaporation.");
    }

    @Override
    public void condensation() {
        System.out.println("Gazeous to liquid.");
        water.setState(new Liquid(water));
    }

    @Override
    public void sublimation() {
        System.out.println("Gazeous water can't sublimation.");
    }

    @Override
    public void solidCondensation() {
        System.out.println("Gazeous to solid.");
        water.setState(new Solid(water));
    }
}
