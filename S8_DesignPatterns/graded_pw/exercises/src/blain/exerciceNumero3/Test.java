package blain.exerciceNumero3;

public class Test {

    public static void main(String[] args) {
        Waffle waffle = new Waffle();

        System.out.println("Waffle price without taxes : " + waffle.getTaxFreePrice());
        System.out.println("Waffle price with taxes (onsite) : " + waffle.getPriceWithTaxes());
        waffle.setStrategy(new Takeaway());
        System.out.println("Waffle price with taxes (takeaway) : " + waffle.getPriceWithTaxes());
    }
}
