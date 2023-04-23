package abstractfactory;

public class FactoryArkham implements AbstractFactory {

    @Override
    public GoodGuy createGoodGuy() {
        return new Batman();
    }

    @Override
    public BadGuy createBadGuy() {
        return new Joker();
    }

}
