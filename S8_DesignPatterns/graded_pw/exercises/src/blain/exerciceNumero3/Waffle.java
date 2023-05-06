package blain.exerciceNumero3;

public class Waffle {

    private double taxFreePrice;

    private Strategy strategy;

    public Waffle() {
        this.taxFreePrice = 10;
        this.strategy = new OnSite();
    }

    public double getTaxFreePrice() {
        return taxFreePrice;
    }

    public double getPriceWithTaxes() {
        return strategy.getPriceWithTaxes(this);
    }

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }
}
