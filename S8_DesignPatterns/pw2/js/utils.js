// utils classes

/ * Supposed to be an abstract class * /

class Observable {

    constructor() {
        this.state = true;
        this.observers = [];
    }

    addObserver(observer) {
        this.observers.push(observer);
    }

    notifyObservers(object = null) {
        if (this.state) {
            this.state = false;
            this.observers.forEach(observer => {
                observer.action(this, object);
            });
        }
    }

    clearObservers() {
        this.observers = [];
    }

    setChanged() {
        this.state = true;
    }

    removeObserver(observer) {
        this.observers = this.observers.filter(obs => obs !== observer);
    }
}

/ * Is supposed to be an interface * /

class Observer {
    action(observable, object) {
        throw new Error("Method action() must be implemented.");
    }
}
