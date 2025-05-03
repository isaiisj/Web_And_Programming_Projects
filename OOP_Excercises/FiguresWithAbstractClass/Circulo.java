public class Circulo extends Figura {

    private double r;

    Circulo(double r) {

        super(0);
        tipoFigura = "Circulo";
        if (r <= 0){
            throw new RuntimeException("El valor del radio es menor que 0");
        }else{
            this.r = r;
        }

    }

    @Override
    public double calcularArea() {
        return Math.PI * Math.pow(r, 2);
    }

    public double circunferencia(){
        return 2 * Math.PI * r;
    }

    @Override
    public void displayFigureDetails() {
        super.displayFigureDetails();
        System.out.println("Circunferencia " + circunferencia());
    }
}
