package domain;

public class Verde extends Color {
	
	public Verde(Semaforo semaforoAsociado){
		super(semaforoAsociado);
	}
	
	@Override
	public String toString() {
		return "Verde";
	}

	public void cambiarColor(){
		semaforoAsociado.setColor(new AmarilloAscendente(semaforoAsociado));
	}
}
