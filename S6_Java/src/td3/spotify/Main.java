package td3.spotify;

import td3.spotify.exceptions.InvalidMailAddressFormat;

public class Main {

    public static void main(String[] args) {
        try{
            User user = new FreeUser(1, "Kiki", new MailAddress("kiki@gmail.com"));
            user.addToFavorites(3);
            user.addToFavorites(1);
            System.out.println(user.favoriteTracks);
        } catch (InvalidMailAddressFormat e){
            System.out.println("The mail isn't good :(");
        }

    }
}
