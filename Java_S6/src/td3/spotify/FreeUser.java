package td3.spotify;

import td3.spotify.exceptions.CreditCardDeclined;
import td3.spotify.exceptions.Forbidden;
import td3.spotify.exceptions.MaximumTracksExceeded;
import td3.spotify.exceptions.NoCreditCard;

import java.util.NoSuchElementException;

public class FreeUser extends User {

    private int tracksListenedToday;

    public FreeUser(int userID, String username, MailAddress mail) {

        super(userID, username, mail);
        this.tracksListenedToday = 0;
    }

    public FreeUser(int userID, String username, CreditCard creditCard, MailAddress mail) {

        super(userID, username, creditCard, mail);
        this.tracksListenedToday = 0;
    }

    public FreeUser(PremiumUser user){
        super(user.userID, user.username, user.favoriteTracks, user.creditCard, user.mail);
    }

    @Override
    public void listen(int id) {
        try {
            if (tracksListenedToday >= MAXIMUM_TRACKS_PER_DAY) {
                throw new MaximumTracksExceeded();
            }
            String song = MusicBank.getFile(id);
            System.out.println("Now listening to : " + song);
            tracksListenedToday++;
        } catch (Forbidden e) {
            System.out.println("This song is not available in your country.");
        } catch (NoSuchElementException e) {
            System.out.println("This song does not exist.");
        } catch (MaximumTracksExceeded maximumTracksExceeded) {
            System.out.println("You already have listened to the " + MAXIMUM_TRACKS_PER_DAY + " tracks available for today.");
            System.out.println(MusicBank.adMessage);
        }
    }

    public void reset() {
        this.tracksListenedToday = 0;
    }

    public User becomePremium() {
        try {
            if (this.creditCard == null) {
                throw new NoCreditCard();
            }
            if (!this.creditCard.paye(this.PREMIUM_PRICE)) {
                throw new CreditCardDeclined();
            }
            return new PremiumUser(this);
        } catch (NoCreditCard noCreditCard) {
            System.out.println("No credit card found. Please add one to your account to become premium.");
        } catch (CreditCardDeclined creditCardDeclined) {
            System.out.println("Your credit card has been declined. Please try again or use another one.");
        }
        return this;
    }

    public User becomeFree(){
        return this;
    }

    @Override
    public String toString(){
        return super.toString() + ", Membership : Free";
    }
}
