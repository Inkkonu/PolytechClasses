package blain.exerciceNumero2;

public class Water {

    private State state;

    public Water() {
        this.state = new Liquid(this);
    }

    public void setState(State state) {
        this.state = state;
    }

    public void fusion() {
        state.fusion();
    }

    public void solidification() {
        state.solidification();
    }

    public void evaporation() {
        state.evaporation();
    }

    public void condensation() {
        state.condensation();
    }

    public void sublimation() {
        state.sublimation();
    }

    public void solidCondensation() {
        state.solidCondensation();
    }
}
