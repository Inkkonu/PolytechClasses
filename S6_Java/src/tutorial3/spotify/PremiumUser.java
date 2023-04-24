package tutorial3.spotify;

public class PremiumUser extends User {

    public PremiumUser(int userID, String username, CreditCard creditCard, MailAddress mail) {
        super(userID, username, creditCard, mail);
    }

    public PremiumUser(FreeUser user) {
        super(user.userID, user.username, user.favoriteTracks, user.creditCard, user.mail);
    }

    public User becomeFree() {
        return new FreeUser(this);
    }

    public User becomePremium() {
        return this;
    }

    public void reset() {
    }

    public boolean payMonthlyFees() {
        return this.creditCard.pay(this.PREMIUM_PRICE);
    }

    @Override
    public String toString() {
        return super.toString() + ", Membership : Premium";
    }
}
