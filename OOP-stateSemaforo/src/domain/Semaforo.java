package domain;

public class Semaforo {
	Color colorActual;
	
	public Semaforo() {
		colorActual = new Rojo(this);
	}
	
	public String cambiarColor() {
		String stringDelColor = null;
		
		colorActual.cambiarColor();
		stringDelColor = colorActual.toString();
		
		return stringDelColor;
	}

	public void setColor(Color colorActual) {
		this.colorActual = colorActual;
	}
	
}