package abstractfactory;

public class FactoryMetropolis implements AbstractFactory {

    @Override
    public GoodGuy createGoodGuy() {
        return new Superman();
    }

    @Override
    public BadGuy createBadGuy() {
        return new CryptonMan();
    }

}
