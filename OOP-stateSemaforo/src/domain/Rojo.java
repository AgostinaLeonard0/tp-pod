package domain;

public class Rojo extends Color {
	
	public Rojo(Semaforo semaforoAsociado){
		super(semaforoAsociado);
	}
	
	@Override
	public String toString() {
		return "Rojo";
	}

	public void cambiarColor(){
		semaforoAsociado.setColor(new AmarilloDescendente(semaforoAsociado));
	}
	
}