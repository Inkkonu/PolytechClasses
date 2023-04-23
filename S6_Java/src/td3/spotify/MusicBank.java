package td3.spotify;

import td3.spotify.exceptions.Forbidden;

import java.util.NoSuchElementException;

public class MusicBank {

    private MusicBank() {
    }


    /**
     * Get music files based on their index.
     *
     * @throws Forbidden              The requested file is not available in the country.
     * @throws NoSuchElementException The requested file does not exist.
     */

    public static String getFile(int i) throws Forbidden {

        switch (i) {
            case 1:
                return "Crab Rave - Noisestorm";
            case 2:
                return "Old Time Rock & Roll - Bob Seger";
            case 3:
                return "Mosaïque - Ash";
            case 4:
                throw new Forbidden();
            case 5:
                return "Roadgame - Kavinsky";
            case 6:
                return "Paranoid - Black Sabbath";
            case 7:
                return "Smalltown Boy - Bronski Beat";
            case 8:
                return "Life Goes On - Oliver Tree";
            case 9:
                return "Shy Away - Twenty One Pilots";
            case 10:
                return "Do I Wanna Know? - Arctic Monkeys";
            default:
                throw new NoSuchElementException();
        }
    }

    static final String adMessage = "Become a premium member, it's better !";

    public static String addAd(String s) {
        return adMessage + s;
    }

} 
	
	
