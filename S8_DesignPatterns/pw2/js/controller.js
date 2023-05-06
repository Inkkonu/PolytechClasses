class Controller {

    constructor(model) {

        this.view = new View();
        this.model = model;

        this.view.inputField.value = this.model.getValue();

        // update
        this.model.addObserver(new ViewObserver(this.view));
        this.model.addObserver(new PrintObserver());
        this.model.addObserver(new DisableWidgetsObserver(this.view));

        //  action
        this.view.plusButton.onclick = () => {
            this.model.plus();
        };

        this.view.minusButton.onclick = () => {
            this.model.minus();
        }

        this.view.checkbox.onchange = () => {
            this.model.toggle();
        }
    }
}

class SuperController {

    constructor(model1, model2) {
        this.controller1 = new Controller(model1);
        this.controller2 = new Controller(model2);

        let synchronizeObserver = new SynchronizeObserver(model1, model2);
        model1.addObserver(synchronizeObserver);
        model2.addObserver(synchronizeObserver);
    }
}
