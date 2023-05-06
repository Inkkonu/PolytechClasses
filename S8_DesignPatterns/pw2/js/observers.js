class PrintObserver extends Observer {

    constructor() {
        super();
    }

    action(observable, object) {
        console.log(observable.getValue());
    }
}

class ViewObserver extends Observer {

    constructor(view) {
        super();
        this.view = view;
    }

    action(observable, object) {
        this.view.inputField.value = observable.getValue();
    }
}

class DisableWidgetsObserver extends Observer {

    constructor(view) {
        super();
        this.view = view;
    }

    action(observable, object) {
        if (observable.isActive()) {
            this.view.inputField.disabled = false;
            this.view.plusButton.disabled = observable.getValue() === 10;
            this.view.minusButton.disabled = observable.getValue() === 0;
        } else {
            this.view.inputField.disabled = true;
            this.view.plusButton.disabled = true;
            this.view.minusButton.disabled = true;
        }
    }
}

class SynchronizeObserver extends Observer {

    constructor(model1, model2) {
        super();
        this.model1 = model1;
        this.model2 = model2;
    }

    action(observable, object) {
        if (observable === this.model1) {
            this.model2.setValue(10 - this.model1.getValue());
        } else {
            this.model1.setValue(10 - this.model2.getValue());
        }
    }
}