package org.example;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        // Demanar a l'usuari el nombre d'estudiants i el nombre de noies
        System.out.print("Introdueix el nombre d'estudiants en la classe: ");
        int nombreEstudiants = scanner.nextInt();

        System.out.print("Introdueix el nombre de noies en la classe: ");
        int nombreNoies = scanner.nextInt();

        // Calcular el percentatge de nois i de noies
        float percentatgeNois = ((float) (nombreEstudiants - nombreNoies) / nombreEstudiants) * 100;
        float percentatgeNoies = ((float) nombreNoies / nombreEstudiants) * 100;

        // Mostrar els resultats per pantalla
        System.out.println("Percentatge de nois: " + percentatgeNois + "%");
        System.out.println("Percentatge de noies: " + percentatgeNoies + "%");

        // Tancar el Scanner
        scanner.close();

    }
}