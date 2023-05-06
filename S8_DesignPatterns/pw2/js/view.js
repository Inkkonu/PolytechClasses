class View {

    constructor() {

        this.div = document.createElement('div');

        this.minusButton = document.createElement('button');
        this.minusButton.innerHTML = '-';

        this.plusButton = document.createElement('button');
        this.plusButton.innerHTML = '+';

        this.inputField = document.createElement('input');
        this.inputField.type = 'number';

        this.checkbox = document.createElement('input');
        this.checkbox.type = 'checkbox';
        this.checkbox.checked = true;

        this.p = document.createElement('p');
        this.p.innerHTML = $.i18n('title');

        this.div.appendChild(this.minusButton);
        this.div.appendChild(this.plusButton);
        this.div.appendChild(this.inputField);
        this.div.appendChild(this.checkbox);
        this.div.appendChild(this.p);


        let nodeParent = document.querySelector('#outer');
        nodeParent.appendChild(this.div);
    }
}
