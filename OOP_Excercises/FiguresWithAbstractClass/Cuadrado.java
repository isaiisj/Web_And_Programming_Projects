public class Cuadrado extends Rectangulo{

    private int lado;

    public Cuadrado(int lado) {
        super(lado,lado);
        this.lado = lado;
        tipoFigura = "Cuadrado";
    }

    @Override
    public double calcularArea() {
        return lado*lado;
    }
}
