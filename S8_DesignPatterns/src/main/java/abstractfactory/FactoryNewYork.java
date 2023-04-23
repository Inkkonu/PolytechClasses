package abstractfactory;

public class FactoryNewYork implements AbstractFactory {
    @Override
    public GoodGuy createGoodGuy() {
        return new Spiderman();
    }

    @Override
    public BadGuy createBadGuy() {
        return new GreenGoblin();
    }
}
