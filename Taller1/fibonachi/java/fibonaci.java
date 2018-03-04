
package kigama;

import java.util.Scanner;

public class Fibonacci
 {
    public static Scanner scann= new Scanner(System.in);
    
    public static byte fByte(int n){
        byte first=0;
        byte second=1;
        byte returnsorce=0;
        for (int i = 0; i < n-1; i++) {
            returnsorce=(byte) (first+second);
            second=first;
            first=returnsorce;
        }
        return returnsorce;
    }
    public static short fShort(int n){
        short first=0;
        short second=1;
        short returnsorce=0;
        for (int i = 0; i < n-1; i++) {
            returnsorce=(short) (first+second);
            second=first;
            first=returnsorce;
        }
        return returnsorce;
    }
    public static int fInt(int n){
        int first=0;
        int second=1;
        int returnsorce=0;
        for (int i = 0; i < n-1; i++) {
            returnsorce=(int) (first+second);
            second=first;
            first=returnsorce;
        }
        return returnsorce;
    }
    public static long fLong(int n){
        long first=0;
        long second=1;
        long returnsorce=0;
        for (int i = 0; i < n-1; i++) {
            returnsorce=(long) (first+second);
            second=first;
            first=returnsorce;
        }
        return returnsorce;
    }
    
    public static boolean salir(){
        int opt=-1;
        do {            
            System.out.println("Desea salir\n\t-1 Si\n\t-2 No\n");
            opt=scann.nextInt();
            if (opt<1 || opt>2) {
                System.out.println("-------------------------------------\n");
                System.out.println("Por favor indicar una opt correcta\n");
            }
        } while (opt<1 || opt>2);
        if(opt==1){
            return true;
        }else{
            return false;
        }
    }
    public static void main(String[] args) {
        int opt=-1;
        boolean salir=false;
        while (!salir) {            
            do {            
                System.out.println("Indique con que tipo de dato desea trabajar\n\t-1 Byte\n\t-2 Short\n\t-3 Int\n\t-4 Long\n");
                opt=scann.nextInt();
                if(opt<1 || opt>4){
                    System.out.println("-------------------------------------\n");
                    System.out.println("Por favor indicar una opcion correcta\n");
                }
            } while (opt<1 || opt>4);
            int n=3;
            switch(opt){
                    case 1:
                        while(fByte(n)>0){
                            n++;
                        }
                        System.out.println("Overflow en byte en n="+n);
                        salir=salir();
                        
                    break;

                    case 2:
                        while(fShort(n)>0){
                            n++;
                        }
                        System.out.println("Hizo Overflow en n="+n);
                        salir=salir();
                    break;

                    case 3:
                        while(fInt(n)>0){
                            n++;
                        }
                       System.out.println("Hizo Overflow en n="+n);
                        salir=salir();
                    break;

                    case 4:
                        while(fLong(n)>0){
                            n++;
                        }
                        System.out.println("Hizo Overflow en n="+n);
                        salir=salir();
                    break;

                    default:
                        System.out.println("Error de opcion");
                        salir=true;
                    break;
        }
    }
        
}
    
}
//basado en http://elvex.ugr.es/decsai/java/pdf/7C-Ejemplos.pdf
