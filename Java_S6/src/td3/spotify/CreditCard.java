package td3.spotify;/* Pour les accents : javadoc -public -charset utf8 CarteBancaire.java */

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
     * Déclenche un paiement sur cette carte.
     *
     * @return Le booléen renvoyé indique si la transaction a réussi ou échoué.
     */
    public boolean paye(int montant) {
        System.out.println("Card number " + this.number + " : debited " + montant + ".");
        return true;
    }

}

