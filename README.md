Juego docker  (Adivinar numero del 1-100) 

Instrucciones: 

1) Descargar el zip del proyecto en el boton de color verde "<> Code"
2) Una vez descargado el zip lo descomprimimos y obtenedremos una carpeta llamada "ProyectoDocker-main"
3) Dentro de esa carpeta tendremos otra carpeta llamada "dockergame" esta es la importante y la movemos al escritorio.
4) Una vez en el escritorio abrimos esa carpeta y copiamos la ruta de esta en mi caso queda algo como "C:\Users\Alan Lomeli\OneDrive\Escritorio\dockergame"
5) Abrimos lo que seria la applicacion de Docker Desktop y abrimos la terminal de esta.
6) En la terminal vamos a escribir cd y la ruta que habiamos guardado ejemplo: cd "C:\Users\Alan Lomeli\OneDrive\Escritorio\dockergame"
7) Una vez detectada la ruta escribimos lo siguiente: docker-compose up --build  
   para que se builden los servicios definidos dentro del docker-compose.yml
9) En el docker podremos ver los builds de cliente y servidor y el container del dockergame ponemos todo en pausa y los re-activamos
10) Dentro de la terminal copiamos lo siguiente: docker exec -it cliente_juego bash
    y lo pegamos con click pegar dentro de la terminal oot@cc18aab755cb:/app#:
11) Luego que nos aparezca esto copiamos y pegamos de la misma manera: python client.py
12) Y ya podremos jugar a adivniar el numero con el siguiente comando: guess "numero"
    ejemplo guess 50 
14) Con esto nos aparecera que es menor si el numero es mas chico al que pusimos o mayor si es mas grande el numero. 

Y listo hasta que encontremos el numero se acaba y nos dira en cuantos intentos los descubrimos! 

   
