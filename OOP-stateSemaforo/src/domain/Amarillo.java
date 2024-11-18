package domain;

public abstract class Amarillo extends Color {
	
	public Amarillo(Semaforo semaforoAsociado){
		super(semaforoAsociado);
	}

	@Override
	public String toString() {
		return "Amarillo";
	}
	
}