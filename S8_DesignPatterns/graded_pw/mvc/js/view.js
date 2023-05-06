class View {

    constructor() {

        this.div = document.createElement('div');

        this.resetButton = document.createElement('button');
        this.resetButton.innerHTML = 'Reset';

        this.plusAButton = document.createElement('button');
        this.plusAButton.innerHTML = '+a';

        this.minusAButton = document.createElement('button');
        this.minusAButton.innerHTML = '-a';
        this.minusAButton.disabled = true;

        this.inputField = document.createElement('input');

        this.div.appendChild(this.resetButton);
        this.div.appendChild(this.plusAButton);
        this.div.appendChild(this.minusAButton);
        this.div.appendChild(this.inputField);


        let nodeParent = document.querySelector('#outer');
        nodeParent.appendChild(this.div);

    }
}