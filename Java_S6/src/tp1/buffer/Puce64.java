package tp1.buffer;

/**
 * This class simulates a 64 bytes memory chip. Fails on
 * bad addresses.
 */


public class Puce64 implements IMemoire {


    protected byte[] t = new byte[64];

    public void set(int addr, byte val) throws IndexOutOfBoundsException {
        if (addr < 0 || addr >= 64) {
            throw new IndexOutOfBoundsException();
        } else {
            t[addr] = val;
        }
    }

    /**
     * Read. Fails on bad addresses (addr<0 or addr>63).
     */
    public byte get(int addr) {
        if (addr < 0 || addr >= 64) {
            throw new IndexOutOfBoundsException();
        } else {
            return t[addr % 64];
        }
    }


}
