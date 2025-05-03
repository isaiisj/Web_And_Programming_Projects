public abstract class Figura {

    // numero de lados
    private int noLados;

    // Tipo de figura
    String tipoFigura;

    // Constructor
    Figura(int noLados){
        this.noLados=noLados;
    }

    // metodo abstarcto para calcular area de figura
    public abstract double calcularArea();

    public int getNoLados(){
        return noLados;
    }

    public void displayFigureDetails() {
        System.out.println("Tipo Figura: " + tipoFigura);
        System.out.println("No. Lados: " + noLados);
        System.out.println("Area: " + calcularArea());
    }

}
