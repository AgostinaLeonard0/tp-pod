package domain;

public class AmarilloDescendente extends Amarillo {
	
	public AmarilloDescendente(Semaforo semaforoAsociado){
		super(semaforoAsociado);
	}
	
	public void cambiarColor(){
		semaforoAsociado.setColor(new Verde(semaforoAsociado));
	}
	
}
