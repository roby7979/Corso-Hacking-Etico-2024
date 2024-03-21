 - - - - -
 # REVERSE SHELL
 > Si tratta di una tecnica che consente a un utente malintenzionato di connettersi a un computer remoto da un computer di sua proprietà. In altre parole, viene stabilita una connessione tra il computer compromesso e il computer dell'utente malintenzionato. Ciò si ottiene eseguendo un programma dannoso o un'istruzione specifica sulla macchina remota che stabilisce la connessione alla macchina dell'attaccante, consentendogli di assumere il controllo della macchina remota.

- - - - - 
# BIND SHELL
>  Questa tecnica è l'opposto di Reverse Shell, poiché invece di essere la macchina compromessa a connettersi alla macchina dell'utente malintenzionato, è l'utente malintenzionato che si connette alla macchina compromessa. L'utente malintenzionato è in ascolto su una determinata porta e il computer compromesso accetta la connessione in ingresso su tale porta. L'utente malintenzionato ha quindi accesso alla console della macchina compromessa, consentendogli di prenderne il controllo.
- - - - - 
# FORWARD SHELL
>  Questa tecnica viene utilizzata quando non è possibile stabilire connessioni inverse o di binding a causa delle regole del firewall implementate nella rete. Si ottiene attraverso l'uso di mkfifo, che crea un file FIFO (named pipe), che viene utilizzato come una sorta di "console simulata" interattiva attraverso la quale l'attaccante può operare sulla macchina remota. Invece di stabilire una connessione diretta, l'utente malintenzionato reindirizza il traffico attraverso il file FIFO, consentendo la comunicazione bidirezionale con il file FIFO.
 - - - - - 

 ### [__VIDEO YOTUBE__](https://youtu.be/HIMsUqdtpW4?si=404qgAqhkjOpQ1Wp)
