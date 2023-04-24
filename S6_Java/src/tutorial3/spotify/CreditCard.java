package tutorial3.spotify;

public class CreditCard {

    int number;
    int date;
    int pictogram;

    public CreditCard(int number, int date, int pictogram) {
        this.number = number;
        this.date = date;
        this.pictogram = pictogram;
    }

    /**
     * Pay the given amount with this card.
     *
     * @return A boolean indicating if the payment was successful.
     */
    public boolean pay(int amount) {
        System.out.println("Card number " + this.number + " : debited " + amount + ".");
        return true;
    }

}

