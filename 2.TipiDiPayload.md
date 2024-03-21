 - - - - - 
Ci sono due tipi di Payload:

# Payload Staged
> questo è un tipo di payload diviso in due o più fasi. La prima fase è un **piccolo frammento** di codice che viene inviato alla destinazione, il cui scopo è stabilire una connessione sicura tra l'attaccante e la macchina di destinazione. Una volta stabilita la connessione, l'utente malintenzionato invia la seconda fase del payload, ovvero il payload effettivo dell'attacco. Questo approccio consente agli aggressori di aggirare misure di sicurezza aggiuntive, poiché il payload effettivo non viene inviato fino a quando non viene stabilito.

- - - - - -
# Payload NON-Staged
> si tratta di un tipo di payload che viene inviato come una singola entità e non è diviso in più fasi. L'intero payload viene inviato alla destinazione **in un singolo pacchetto** e viene eseguito immediatamente dopo essere stato ricevuto. Questo approccio è più semplice rispetto a Payload Staged, ma è anche più facile da rilevare per i sistemi di sicurezza, poiché tutto il codice dannoso viene inviato in una volta sola.
- - - - - 

*È importante notare che il tipo di payload utilizzato in un attacco dipenderà dall'obiettivo e dalle misure di sicurezza implementate. In generale, i payload a fasi sono più difficili da rilevare e sono preferiti dagli attaccanti, mentre i payload non a fasi sono più facili da implementare ma sono anche più facili da rilevare.*

#### [__VIDEO YOUTUBE__](https://youtu.be/QbkisKsWs7k?si=RxmuWJp3g_d86B-L)
