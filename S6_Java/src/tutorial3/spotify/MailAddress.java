package tutorial3.spotify;

import tutorial3.spotify.exceptions.InvalidMailAddressFormat;

import java.util.Arrays;

public class MailAddress {

    private String suffix;
    private String prefix;
    private String domain;

    public MailAddress(String suffix, String prefix, String domain) {
        this.suffix = suffix;
        this.prefix = prefix;
        this.domain = domain;
    }

    public MailAddress(String fullMail) throws InvalidMailAddressFormat {
        String[] parts = fullMail.split("@");
        if (parts.length != 2 || Arrays.asList(parts).contains("")) {
            throw new InvalidMailAddressFormat();
        }
        this.suffix = parts[0];
        parts = parts[1].split("\\.");
        if (parts.length < 2 || Arrays.asList(parts).contains("")) {
            throw new InvalidMailAddressFormat();
        }
        this.prefix = "";
        for (int i = 0; i < parts.length - 1; i++) {
            this.prefix += parts[i] + ".";
        }
        this.prefix = this.prefix.substring(0, this.prefix.length() - 1);
        this.domain = parts[parts.length - 1];
    }

    @Override
    public String toString() {
        return this.suffix + "@" + this.prefix + "." + this.domain;
    }
}
