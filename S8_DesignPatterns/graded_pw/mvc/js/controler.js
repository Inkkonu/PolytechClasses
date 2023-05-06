class Controler {

    constructor(model) {

        this.view = new View();
        this.model = model;

        this.view.inputField.value = this.model.getStr();

        // update
        this.model.addObservers(new ViewObserver(this.view));
        this.model.addObservers(new DisableButtonObserver(this.view));
        //  action

        this.view.plusAButton.onclick = () => {
            this.model.plus();
        }

        this.view.minusAButton.onclick = () => {
            this.model.minus();
        }

        this.view.resetButton.onclick = () => {
            this.model.reset();
        }
    }
}


class ViewObserver extends Observer {

    constructor(view) {
        super();
        this.view = view;
    }

    update(observable, object) {
        this.view.inputField.value = observable.getStr();
    }
}

class DisableButtonObserver extends Observer {

    constructor(view) {
        super();
        this.view = view;
    }

    update(observable, object) {
        this.view.minusAButton.disabled = observable.getStr() === "";
    }
}