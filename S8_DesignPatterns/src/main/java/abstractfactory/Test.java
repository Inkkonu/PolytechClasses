package abstractfactory;

public class Test {

    public static void main(String[] args) {
        AbstractFactory factoryArkham = new FactoryArkham();
        System.out.println("In Arkham City : " + factoryArkham.createGoodGuy() + " fights " + factoryArkham.createBadGuy());

        AbstractFactory factoryNewYork = new FactoryNewYork();
        System.out.println("In New York City : " + factoryNewYork.createGoodGuy() + " fights " + factoryNewYork.createBadGuy());

        AbstractFactory factoryMetropolis = new FactoryMetropolis();
        System.out.println("In Metropolis : " + factoryMetropolis.createGoodGuy() + " fights " + factoryMetropolis.createBadGuy());
    }
}
