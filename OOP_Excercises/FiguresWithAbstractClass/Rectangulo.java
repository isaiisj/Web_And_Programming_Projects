public class Rectangulo extends Figura {

    private double b;
    private double h;

    Rectangulo(int b, int h) {
        super(4);
        this.b = b;
        this.h = h;
        tipoFigura = "Rectangulo";
    }

    @Override
    public double calcularArea() {
        return b * h;
    }

}
