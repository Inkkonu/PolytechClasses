package tp1.buffer;

/* Types primitifs : https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html */


public interface IMemoire {

    /**
     * Write the byte [val] at the adress [addr]. No
     * assumption is made on the behavior when addr is out
     * of memory.
     */
    void set(int addr, byte val);


    /**
     * Read the byte at the address [addr]. No assumption
     * is made on the behavior when addr is out of memory.
     */
    byte get(int addr);

}
