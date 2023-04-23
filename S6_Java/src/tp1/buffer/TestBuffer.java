package tp1.buffer;

public class TestBuffer {

    private static boolean testsMemoire32() {
        boolean allGood = true;
        try {
            BufferGen buffer = new BufferGen(new Memoire32());
            buffer.push(Byte.valueOf("4"));
            buffer.pop();
            buffer.push(Byte.valueOf("5"));
            buffer.push(Byte.valueOf("9"));
            byte b = buffer.getHead();
            b = buffer.getTail();
        } catch (Exception e) {
            allGood = false;
        }
        return allGood;
    }

    private static boolean testsPuce64() {
        boolean allGood = true;
        try {
            BufferGen buffer = new BufferGen(new Puce64());
            buffer.push(Byte.valueOf("4"));
            buffer.pop();
            buffer.push(Byte.valueOf("5"));
            buffer.push(Byte.valueOf("9"));
            byte b = buffer.getHead();
            b = buffer.getTail();
        } catch (Exception e) {
            allGood = false;
        }
        return allGood;
    }

    public static void main(String[] args) {
        if (testsMemoire32()) {
            System.out.println("Tests passed for the 32 memory");
        } else {
            System.out.println("Tests did not pass for the 32 memory");
        }
        if (testsPuce64()) {
            System.out.println("Tests passed for the 64 memory");
        } else {
            System.out.println("Tests did not pass for the 64 memory");
        }
    }
}
