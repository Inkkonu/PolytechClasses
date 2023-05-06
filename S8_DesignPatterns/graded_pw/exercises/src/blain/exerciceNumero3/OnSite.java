package blain.exerciceNumero3;

public class OnSite implements Strategy{

    @Override
    public double getPriceWithTaxes(Waffle waffle) {
        return waffle.getTaxFreePrice() * 1.2;
    }
}
