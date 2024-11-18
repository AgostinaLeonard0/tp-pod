package domain;

public abstract class Color {
	protected Semaforo semaforoAsociado;
	
	public Color(Semaforo semaforoAsociado){
		this.semaforoAsociado = semaforoAsociado;
	}
	
	public abstract void cambiarColor();
}
