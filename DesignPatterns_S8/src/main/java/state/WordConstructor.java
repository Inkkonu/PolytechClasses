package state;

import lombok.Getter;
import lombok.Setter;

public class WordConstructor {

    @Getter
    private final StringBuilder stringBuilder;
    @Getter
    @Setter
    private State state;

    public WordConstructor() {
        this.stringBuilder = new StringBuilder();
        this.state = new E1(this);
    }

    public void addA() {
        state.addA();
    }

    public void addB() {
        state.addB();
    }

    public String getWord() {
        return stringBuilder.toString();
    }
}
