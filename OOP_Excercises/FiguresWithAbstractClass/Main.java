import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        Rectangulo rectangulo = new Rectangulo(4,3);
        Cuadrado cudarado = new Cuadrado(5);
        System.out.println("Introduzca un radio para el Circulo: ");

        int radio;
        try{
            radio = scanner.nextInt();
        } catch (Exception e){
            System.out.println("Valor invalido\n");
            radio = 10;
        }

        Circulo circulo = new Circulo(radio);

        List<Figura> listaFiguras = new ArrayList<>();
        listaFiguras.add(circulo);
        listaFiguras.add(rectangulo);
        listaFiguras.add(cudarado);

        for (Figura figura : listaFiguras) {
            figura.displayFigureDetails();
            System.out.println();
        }
    }
}
