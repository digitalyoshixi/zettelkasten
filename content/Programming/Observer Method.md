---
tags:
  - programming
---
A [[Design Pattern]] useful for when we want changes in one object to modify many other objects.
![[Observer Method-20250721144105815.webp]]
Observer objects monitor a subject for changes, and will update themselves accordingly.
# Example
```java
public Subject(){
	ArrayList<Observers> observers;
	public Subject(){
		observers = new ArrayList<Observers>();
	}
	public registerObserver(Observer o){
		observers.push(o);
	}

	public int getState(){
		return state;
	}
	public void setState(int value){
		state = value;
		notifyAllObservers();
	}
	public notifyAllObservers(){
		for (obsever : observers){
			observer.update();
		}
	}
}

abstract class Observer{
	Subject subject;
}

class ObserverA extends Observer{
	public ObserverA(Subject s){
		subject = s;
		subject.registerObserver(this);
	}
	public void update(){
		System.out.println("A observed", + subject.getState());
	}
}
```