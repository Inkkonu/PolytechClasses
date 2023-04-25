package pw1.buffer;

public class BufferGen {

    private IMemoire chip;
    private int length;
    private int head;

    public BufferGen(IMemoire chip) {
        this.chip = chip;
        this.head = -1;
        this.length = 0;
    }

    public void push(byte val) {
        if (this.head == -1) {
            this.head = 0;
            this.length++;
            this.chip.set(head, val);
        } else {
            this.chip.set(head + length, val);
            this.length++;
        }
    }

    public byte pop() throws NullPointerException {
        if (length == 0) {
            throw new NullPointerException("No element in the buffer");
        } else {
            this.head = this.head + 1;
            this.length--;
            return this.chip.get(this.head - 1);
        }

    }

    public byte getTail() throws NullPointerException {
        if (length == 0) {
            throw new NullPointerException("No element in the buffer");
        } else {
            return this.chip.get(head + length - 1);
        }

    }

    public byte getHead() throws NullPointerException {
        if (length == 0) {
            throw new NullPointerException("No element in the buffer");
        } else {
            return this.chip.get(head);
        }
    }

    @Override
    public String toString() {
        String s = "";
        for (int i = head; i < head + length; i++) {
            s = s + this.chip.get(i) + " ";
        }
        return s;
    }
}
