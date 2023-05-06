// implementation class

class ModelInteger extends Observable {

    constructor() {
        super();
        this.value = 5;
    }

    setValue(value) {
        if (value !== this.value) {
            this.value = Math.min(Math.max(value, 0), 10); //Basically a clamp
            super.setChanged();
            this.notifyObservers();
        }
    }

    getValue() {
        return this.value;
    }

    plus() {
        this.setValue(this.value + 1);
    }

    minus() {
        this.setValue(this.value - 1);
    }
}

class ModelActivation extends ModelInteger {

    constructor() {
        super();
        this.active = true;
    }

    setActive(active) {
        if (active !== this.active) {
            this.active = active;
            super.setChanged();
            this.notifyObservers();
        }
    }

    isActive() {
        return this.active;
    }

    toggle() {
        this.setActive(!this.active);
    }
}