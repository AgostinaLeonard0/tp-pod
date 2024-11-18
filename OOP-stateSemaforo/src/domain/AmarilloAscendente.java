package domain;

public class AmarilloAscendente extends Amarillo {
	
	public AmarilloAscendente(Semaforo semaforoAsociado){
		super(semaforoAsociado);
	}
	
	public void cambiarColor(){
		semaforoAsociado.setColor(new Rojo(semaforoAsociado));
	}
	
}
