// utils classes

class Mediator{

  constructor(){

  }

  mediate(observable, object){

  }
}

class Observable {

  constructor(){
    this.observers = [];
    this.state = false;
  }

  addObservers(observer){
    this.observers.push(observer);
  }

  notifyObservers(object = null){

    if(this.state == true){
      this.state = false;

      for(let i = 0; i < this.observers.length; i++) {
        this.observers[i].update(this, object);
      }
    }
  }

  clearObservers(){
    this.observers = [];
  }

  setChanged(){
    this.state = true;
  }

  removeObserver(observer){
    for(i = 0; i < this.observers.length; i++) {
      if(this.observers[i] === observer){
        this.observers.splice(i, 1);
      }
    }
  }
}

class Observer {
  constructor(){

  }

  update(observable, object){

  }
}
