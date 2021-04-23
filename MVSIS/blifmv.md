# BLIF-MV

BLIF-MV è un linguaggio specifico per descrivere sistemi gerarchici con non determinismo. Un sistema può essere composto da più sistemi che interagiscono e comunicano tra loro.

## Sintassi

### Modelli

Un modello è un sistema che può essere utilizzato per definire un sistema gerarchico. Ogni BLIF-MV contiene più definizioni, ogni modello deve essere specificato. Un modello è dichiarato nel seguente modo

```
.model <model-name>
.inputs <input-list>
.outputs <output-list>
<command>
...
<command>
.end
```

### Variabili multi valore
Una variabile multi valore può assumere un numero finito di valori. Ne esistono di 2 tipi:

1. **Variabili enumerative**: variabili con un dominio do $n$ interi ${0,1,...,n-1}$
    - ```.mv <variable-name-list> <number-of-values>```
        - ```<variable-name-list```: lista di variabili dichiarate
        - ```number-of-values```: numero naturale che specifica il valore di $n$
        - es. ```.mv x,y 3.```
2. **Symbolic variables**: la variabile prende un set di valori arbitrari
    - ```.mv <variable-name-list> <number-of-values> <value-list>```
    - ```variable-name-list```: lista di variabili dichiarate
    - ```value-list```: lista di possibili valori che può assumere la variabile
    - es. ```.mv x,y 3 red green blue.```

Se le variabili non sono precedute da ```.mv``` vengono considerate variabili booleane

### Tabelle

Una tabella è una rappresentazione astratta di un gate. Prende i valori in input e genera un output basandosi sulle sue regole. La tabella enumera simbolicamente tutte le combinazioni di valori valide tra gli input e gli output.

```
.table <in-1> <in-2> ... <in-n> -> <out-1> <out-2>... <out-m>
<relation>
...
<relation>
```

- $in-1,...,in-n$: sono i nomi delle variabili di ingresso nella tabella definiti
- $out-1,...,out-n$: sono i nomi delle variabili di output della tabella
- -> opzionale se la tabella ha un singolo output
- ```relation``` combinazione degli $n$ input con gli $m$ output

```
.mv x,y 4
.table x -> y
!2 {1-3}
- 0
2 (0,3)
```

Le relazioni specificate in questa tabella sono: $[(0,1,3) \times (1,2,3)] \cup [(0,1,2,3) \times (0)] \cup [(2) \cup (0,3)]$

#### = Construct

Assegnamento del valore di una variabile ad un'altra variabile

```
.table x -> y
- =x
```

In questo caso sto dicendo che il valore di $y$ dovrebbe essere uguale a $x$.

#### Default output

A volte è conveniente definire un output predefinito per i modelli di input non specificati in una data relazione. A questo scopo viene utilizzato il costrutto .default

```
.mv x1,x2,y1,y2 2
.table x1 x2 -> y1 y2
.default 0 0
```
