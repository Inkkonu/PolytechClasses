package state;

public class Test {

    public static void main(String[] args) {
        System.out.println("Building abbba");
        WordConstructor wordConstructor = new WordConstructor();
        wordConstructor.addA();
        wordConstructor.addB();
        wordConstructor.addB();
        wordConstructor.addB();
        wordConstructor.addA();
        System.out.println("Final word : " + wordConstructor.getWord());
        System.out.println("Final state : " + wordConstructor.getState());

        System.out.println();

        System.out.println("Building bbaab");
        wordConstructor = new WordConstructor();
        wordConstructor.addB();
        wordConstructor.addB();
        wordConstructor.addA();
        wordConstructor.addA();
        wordConstructor.addB();
        System.out.println("Final word : " + wordConstructor.getWord());
        System.out.println("Final state : " + wordConstructor.getState());

    }
}
