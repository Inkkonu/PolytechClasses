package tutorial3.spotify;

import tutorial3.spotify.exceptions.Forbidden;
import tutorial3.spotify.exceptions.SongAlreadyInFavorites;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

public abstract class User {

    protected final int MAXIMUM_TRACKS_PER_DAY = 3;
    protected final int PREMIUM_PRICE = 10;

    protected int userID;
    protected String username;
    protected List<Integer> favoriteTracks;
    protected CreditCard creditCard;
    protected MailAddress mail;

    public User(int userID, String username, MailAddress mail) {
        this.userID = userID;
        this.username = username;
        this.mail = mail;
        this.favoriteTracks = new ArrayList<>();
        this.creditCard = null;
    }

    public User(int userID, String username, CreditCard creditCard, MailAddress mail) {
        this.userID = userID;
        this.username = username;
        this.mail = mail;
        this.favoriteTracks = new ArrayList<>();
        this.creditCard = creditCard;
    }

    public User(int userID, String username, List<Integer> favoriteTracks, CreditCard creditCard, MailAddress mail) {
        this.userID = userID;
        this.username = username;
        this.favoriteTracks = favoriteTracks;
        this.creditCard = creditCard;
        this.mail = mail;
    }

    public abstract void reset();

    public abstract User becomeFree();

    public abstract User becomePremium();

    public void listen(int id) {
        try {
            String song = MusicBank.getFile(id);
            System.out.println("Now listening to : " + song);
        } catch (Forbidden e) {
            System.out.println("This song is not available in your country");
        } catch (NoSuchElementException e) {
            System.out.println("This song does not exist");
        }
    }

    public void addToFavorites(int id) {
        try {
            MusicBank.getFile(id);
            if (this.favoriteTracks.contains(id)) {
                throw new SongAlreadyInFavorites();
            }
            this.favoriteTracks.add(id);
            System.out.println("Song added to your favorites !");
        } catch (Forbidden e) {
            System.out.println("This song is not available in your country.");
        } catch (NoSuchElementException e) {
            System.out.println("This song does not exist.");
        } catch (SongAlreadyInFavorites songAlreadyInFavorites) {
            System.out.println("This song is already in your favorites.");
        }
    }

    public void showFavoriteTracks() {
        System.out.println("Your favorite tracks :");
        for (int id : this.favoriteTracks) {
            try {
                System.out.println("- " + MusicBank.getFile(id));
            } catch (Forbidden | NoSuchElementException e) {
                System.out.println("Oops, you have an unavailable song in your favorites : " + id);
            }
        }
    }

    @Override
    public String toString() {
        return "ID : " + this.userID + ", Username : " + this.username;
    }
}
