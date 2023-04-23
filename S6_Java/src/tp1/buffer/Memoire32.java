package tp1.buffer;

/**
 * This class simulates a 32 bytes memory chip. Read and
 * write never fail (we use only the 5 last bits of the
 * address).
 */


public class Memoire32 implements IMemoire {


    protected byte[] t = new byte[32];

    public void set(int addr, byte val) {
        t[addr % 32] = val;
    }

    public byte get(int addr) {
        return t[addr % 32];
    }


}
