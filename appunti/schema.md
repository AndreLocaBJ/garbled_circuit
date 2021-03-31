# Il protocollo di Yao

- Una funzione convertita in un circuito booleano
- 2 partecipanti A e B
- Una funzione f(a,b) dove:
	- a: input di A
	- b: input di B

Un circuito booleano è composto da più operatori logici collegati tra loro generando un reticolo.

Per ogni operatore logico dovremmo andare a scegliere:

- 2 chiavi per ogni ingresso: corrispondenti al valore 0 e 1 di ogni input
- 2 chiavi per l'uscita: rappresentanti l'output 0 e 1

## Funzionamento

![](/home/andrea/Documenti/Tesi/appunti/media/05.png)

A critta ogni riga della tabella della verità crittando utilizzando le chiavi degli ingressi corrispndenti ai valori booleani scelti.

| X    | Y    | Z    | Tabella Crittata       |
| ---- | ---- | ---- | ---------------------- |
| 0    | 0    | 0    | $E_{k_{ox}}(E_{k_{oy}}(K_{0z}))$ |
| 0    | 1    | 0    | $E_{k_{ox}}(E_{k_{1y}}(K_{0z}))$ |
| 1    | 0    | 0    | $E_{k_{1x}}(E_{k_{oy}}(K_{0z}))$ |
| 1    | 1    | 1    | $E_{k_{1x}}(E_{k_{1y}}(K_{1z}))$ |

Dopo la crittatura la tabella viene permutata randomicamente e successivamente inviata a B

![](/home/andrea/Documenti/Tesi/appunti/media/01.png)

In questo modo B non riesce a capire quale elemento corrisponde al valore originale

A questo punto A invia a B la chiave corrispondente al suo bit di input

![](/home/andrea/Documenti/Tesi/appunti/media/02.png)

Le chiavi sono stringhe casuali, in questo modo B non riesce a capire di che bit si tratta (0 o 1).

A e B utilizzano la tecnica di **Oblivious Transfer Protocol**, così facendo:

- A invia le de 2 chiavi corrispondenti ai 2 valori delle chiavi inserite inizialmente da B
- In questo protocollo B invia in input solo il suo bit di input per quell'ingresso

![](/home/andrea/Documenti/Tesi/appunti/media/03.png)

Da chi che A ha inviato a B nelle ultime 2 trasmissioni B è in grado di ricostruire (decrittare) uno degli output

![](/home/andrea/Documenti/Tesi/appunti/media/04.png)

Facendo questo passando per tutti i gate B riesce a valutare l'intero circuito ma non saprà mai per tutto il tragitto se i bit che ha scoperto sono 0 o 1. Alla fine della computazione di tutti i gate B chiede ad A il valore dell'ultimo output e A le risponde se è 0 o 1

# Free XOR gates

## Setting and Preliminaries

Per questo studio sono stati utilizzati circuiti booleani aciclici con $k$ gate e un *fan-out* ( numero di porte logiche che possono essere collegate alla sua uscita) arbitrario. I gate $G_1,...,G_k$ sono ordinati topologicamente.

### Notazione

- $\in_R$: campionamento casuale uniforme(?)
- $||$: concatenazione di stringhe di bit
- $\langle a,b \rangle$: vettore a 2 componenti
  - Rappresentazione in bit del vettore $a||b$
- $W_c = g(W_a,W_b)$: Gate a 2 input $G$ che computa una funzione $g: \{0,1\}^2 \rarr \{0,1\}$ con input gli ingressi $W_a$ e $W_b$ e output $W_c$.
- $N$: parametro di sicurezza
- $S$: set infinito
- $X = \{X_s\}_{s\in S}$ : quindi $X$ rappresenta un elemento del set $S$
- Se prendessimo una coppia $X = \{X_s\}_{s\in S}$ e $Y = \{Y_s\}_{s\in S}$ da $S$ essi risulterebbero computazionalmente equivalenti.

### Nomenclatura operazioni

- **RO**, Random Oracle: funzione di hash che trasforma $\{0,1\}^* \mapsto \{0,1\}^N$
- **OT**, Oblivius Transfer:  è un protocollo a due parti. Il mittente $P_1$ ha due segreti $m_0 , m _1$ e il destinatario $P_2$ ha un bit di selezione $i \in \{0, 1\}$. Alla fine del protocollo, $P_2$ apprende $m_i$  ma nulla su $m_{1-i}$ e $P_1$ non apprende nulla su $i$.
- **GC**, Yao’s Garbled Circuit: visto sopra

## Il protocollo

Invece che fare come nel classico GC in questa nuova versione vengono scelti un $W_c$ casuale una volta sola e applichiamo la confusione sugli ingressi dei gate, quindi: $\forall i:w^1_i=w^0_i  \oplus R$.

### Costruzione del circuito

- Le porte NOT possono essere implementate "gratuitamente" semplicemente eliminandole e invertendo la corrispondenza dei valori dei fili e dei garbugli. Non consideriamo quindi ulteriormente le porte NOT.
- Prendiamo tutti gli XOR-gate con n > 2 ingressi e li sostituiamo con con n - 1 XOR-gate a due ingressi.
- Gli altri gate vengono trattati normalmente utilizzando un tabelle con $2^n$ entrate permutate casualmente.