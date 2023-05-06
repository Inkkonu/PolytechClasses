// implementation class

class Model extends Observable {


    constructor() {
        super();
        this.str = "";
    }

    setStr(str) {
        if (str !== this.str) {
            this.str = str;
            super.setChanged();
            this.notifyObservers();
        }
    }

    getStr() {
        return this.str;
    }

    plus() {
        this.setStr(this.str + "a");
    }

    minus() {
        this.setStr(this.str.slice(0, -1));
    }

    reset() {
        this.setStr("");
    }
}
