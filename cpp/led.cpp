// Hier binden wir WiringPi ein sowie die C-Standard Ein -/ Ausgabe
#include <wiringPi.h>
#include <stdio.h>
int main () {
// Initialisieren der WiringPi API
if ( wiringPiSetup() == -1)
return 1;
// Setze GPIO 18 (= WiringPi Pin 0) als Ausgangspin
pinMode (1, OUTPUT );
// Start einer Endlosschleife
while (1) {
// Spannung einschalten , LED leuchtet .PIN 1 >> HIGH 1
digitalWrite(1, 1);
// 1 s warten . Wartezeit wird in ms angegeben .
delay (1000) ;
// Spannung ausschalten . LED geht aus. PIN 1 >> LOW 0
digitalWrite(1, 0);
// Wieder 1 s warten
delay (1000) ;
}
}
