#include<stdlib.h>
#include<stdio.h>
#include<stdbool.h>
 //para usar bolleanos en c
long fLong(int n){
     long first=0;
     long second=1;
     long returnsorce=0;
     int i = 0;
     for (i = 0; i < n-1; i++)
      {
         returnsorce=(long) (first+second);
         second=first;
         first=returnsorce;
     }
     return returnsorce;
}
short fShort(int n){
      short first=0;
      short second=1;
      short returnsorce=0;
      int i = 0;
      for (i = 0; i < n-1; i++) 
      {
          returnsorce=(short) (first+second);
          second=first;
          first=returnsorce;
      }
      return returnsorce;
}
int fInt(int n){
    int first=0;
    int second=1;
    int returnsorce=0;
    int i = 0;
    for (i = 0; i < n-1; i++)
     {
        returnsorce=(int) (first+second);
        second=first;
        first=returnsorce;
    }
    return returnsorce;
}

bool salir(){
     int opt=-1;
     do {            
        printf("Desea salir\n\t-1 Si\n\t-2 No\n");
        scanf("%i",&opt);
        if (opt<1 || opt>2) {
                        printf("-------------------------------------\n");
                        printf("Por favor indicar una opcion correcta\n");
        }
     }while (opt<1 || opt>2);
     if(opt==1)
     {
           system("cls");
           return true;
     }else{
           system("cls");
           return false;
     }
}
int main(){
    int opt=-1;
    bool exit=false;
    while (!exit) 
    {            
          do
           {            
                 printf("Indique con que tipo de dato desea trabajar\n\t-1 Short\n\t-2 Long\n\t-3 Long\n");
                 scanf("%i",&opt);
                 if(opt<1 || opt>3){
                        system("cls");
                        printf("-------------------------------------\n");
                        printf("Por favor indicar una opcion correcta\n");
                 }
          }
          while (opt<1 || opt>3);
            int n=3;
            switch(opt)
            {
                    case 1:
                        while(fShort(n)>0)
                        {
                            n++;
                        }
                        system("cls");
                        printf("Hizo Overflow en n=%i\n",n);
                        exit=salir();
                        
                    break;

                    case 2:
                        while(fInt(n)>0)
                        {
                            n++;
                        }
                        system("cls");
                        printf("Hizo Overflow en n=%i\n",n);
                        exit=salir();
                    break;

                    case 3:
                        while(fLong(n)>0)
                        {
                            n++;
                        }
                        system("cls");
                        printf("Hizo Overflow en n=%i\n",n);
                        exit=salir();
                    break;

                    default:
                        system("cls");
                        printf("Error opcion");
                        exit=true;
                    break;
        }
    }
    system("pause");
    return 0;
}
//basado en el ejemplo de http://www.aprendeaprogramar.com/mod/forum/discuss.php?d=675

