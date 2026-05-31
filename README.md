
# Python für Java-Entwickler – Eine kurze Einführung
Ausgangspunkt: Mehrjährige Java-Erfahrung. Ziel: Python lesen, verstehen und schreiben können.
1. Grundlegendes Sprachkonzept

    | Aspekt |	Java	| Python |
    | ----------- |:-----------:|:-----------:|
    | Paradigma	| Rein objektorientiert (mit Primitiven)	| Multi-Paradigma: OOP, funktional, prozedural| 
    | 	| stark	| stark| 
    | Typsystem	| Statisch	| Dynamisch |
    | 	| explizit (String name = "Max")	| implizit (name = "Max")| 
    | Kompilation	| Compiler → Bytecode → JVM	| Interpretiert (Bytecode → Python-VM)| 
    | Blöcke	| Geschwungene Klammern { ... }	| Einrückung definiert Blöcke |   
    
    *Wichtigster Unterschied:* Keine geschwungene Klammern, kein Semikolon. Die **Einrückung** (standardmäßig 4 Leerzeichen) bestimmt die Blockstruktur – sie ist Teil der     Syntax und nicht optional.   
    ```python
    # Keine Klammern, kein Semikolon – Einrückung regelt alles
    if x > 0:
        print("positiv")        # eingerückt = im if-Block
        print("weiter so")      # immer noch im if
    else:
        print("nicht positiv")
    print("hier bin ich draußen")  
    ```

2. Einfache Kontrollstrukturen   
   
    1. Verzweigungen: if-else   

        Java:
        ```java
        int x = 10;
        if (x > 0) {
            System.out.println("positiv");
        } else if (x == 0) {
            System.out.println("null");
        } else {
            System.out.println("negativ");
        }
        ```
        Python:
        ```python
        x = 10
        if x > 0:
            print("positiv")
        elif x == 0:                      # elif, nicht else if
            print("null")
        else:
            print("negativ")
        ```
        
        | Aspekt | Python | Java |
        |---|---|---|
        | Schlüsselworte |if, else |if, else|
        | Verzweigungskette  | `elif` (zusammengeschrieben) | `else if` (getrennt) |
        | Bedingung | `if x > 0:` – keine Klammern nötig | `if (x > 0)` – runde Klammern Pflicht |
        | Blockbegrenzung | Einrückung nach Doppelpunkt `:` | Geschwungene Klammern `{ }` |
        | Bedingungstyp | Alles: `0`, `""`, `None`, leere Listen → `False` | Nur boolean |
        | Ternary | `"ja" if x > 0 else "nein"` | `x > 0 ? "ja" : "nein"` |
        | Logische Operatoren | `and`, `or`, `not` | `&&`, `\|\|`, `!` |   
        
        *Wichtig*: In Python kann **jeder Wert** als Bedingung dienen – das ist ein großer Unterschied zu Java:
        ```python
        # Python: alles, was "falsy" ist, wird wie False behandelt
        if 0:           # False  – Die Zahl 0
        if "":          # False  – leerer String
        if []:          # False  – leere Liste
        if None:        # False  – None
        if 42:          # True   – alles andere
        ```
   
        ```java
        # Gleiches in Java nicht möglich – braucht explizite Prüfung
        String s = "";
        if (s.isEmpty()) { ... }   // explizit nötig
        ```
           
    2. For-Schleifen   
   
        Hier unterscheiden sich die Sprachen fundamental:   
        Java:   
        ```java
        // Klassische Zählschleife
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }
        
        // For-Each (enhanced for)
        int[] zahlen = {1, 2, 3, 4, 5};
        for (int z : zahlen) {
            System.out.println(z);
        }
        
        // Über Liste
        List<String> namen = Arrays.asList("Alice", "Bob");
        for (String n : namen) {
            System.out.println(n);
        }
        ```
        Python:
        ```python
        # Es gibt NUR die For-Each-Variante – keine klassische Zählschleife!
        # Stattdessen: range() für Zahlenbereiche
        for i in range(5):          # 0, 1, 2, 3, 4
            print(i)
        
        # range(start, stop, step)
        for i in range(1, 10, 2):   # 1, 3, 5, 7, 9
            print(i)
        
        # Über Liste
        namen = ["Alice", "Bob"]
        for n in namen:
            print(n)
        
        # Mit Index – enumerate() (gibt's in Java nicht nativ)
        for idx, n in enumerate(namen):
            print(f"{idx}: {n}")
        ```
        
        | Aspekt | Python | Java |
        |---|---|---|
        | Zählschleife | `for i in range(n):` | `for (int i=0; i<n; i++)` |
        | For-Each | `for x in sammlung:` | `for (T x : sammlung)` |
        | Inhalt und Index | `enumerate(sammlung)` | Manuell oder `int idx` |
        | Bereich, Intervall | `for i in range(1, 11, 2):` | `for (int i=1; i<=10; i+=2)` |
        | Iterierbarkeit | Alles mit `__iter__()` (Duck-Typing) | `Iterable`-Interface |
        | break / continue | vorhanden | vorhanden |
        | else-Block bei Schleife | `else` | Nicht vorhanden |

    3. While-Schleife   
        Die while-Schleife ist in beiden Sprachen sehr ähnlich, aber es gibt feine Unterschiede:   

        Java:   

        ```java
        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
        }
        ```
        Python:

        ```python
        i = 0
        while i < 5:
            print(i)
            i += 1          # i++ gibt es in Python nicht!
        ```

        | Aspekt | Python | Java |
        |---|---|---|
        | Syntax | `while bedingung:` + Einrückung | `while (bedingung) { ... }` |
        | Bedingungstyp | Alles: `0`, `""`, `None`, leere Listen → `False` | Nur boolean |
        | Blockbegrenzung | Einrückung nach Doppelpunkt `:` | Geschwungene Klammern `{ }` |
        | Inkrement | `i += 1`, `i -= 1` (es gibt keinen `++`/`--`-Operator) | `i++`, `i--`, `++i`, `--i` |
        | break / continue | vorhanden | vorhanden |
        | else-Block | `else` wird nach Schleifenende ausgeführt | Nicht vorhanden |

    5. Do-While-Schleife 

        Es gibt **keine** `do-while`-Schleife in Python. 
        
        ```python
        # Java: do { ... } while (bedingung);
        while True:
            # Code, der mindestens einmal laufen soll
            antwort = input("Weiter? (j/n): ")
            if antwort.lower() != 'j':
                break             # Abbruch am Ende = do-while-Verhalten
        # Oder etwas eleganter mit einer Hilfsvariablen:
        
        weiter = True
        while weiter:
            antwort = input("Weiter? (j/n): ")
            weiter = (antwort.lower() == 'j')
        ```

3. Erweiterte Kontrollstrukturen   
    1. Mehrfachverzweigung

        Java `switch` (seit Java 14 auch als Expression):

        ```java
        switch (tag) {
            case 1 -> System.out.println("Montag");
            case 6, 7 -> System.out.println("Wochenende");
            default -> System.out.println("Werktag");
        }
        ```
        Python `match-case` – eingeführt in Python 3.10 (Oktober 2021):
        
        ```python
        match tag:
            case 1:
                print("Montag")
            case 6 | 7:                   # mehrere Werte mit |
                print("Wochenende")
            case _:                       # _ = Default/Wildcard
                print("Werktag")
        ```
        Stärken von match (geht weit über switch hinaus)
        match in Python ist kein reiner switch-Ersatz, sondern Pattern Matching (wie in funktionalen Sprachen):

        ```python
        # Strukturelles Matching – Werte zerlegen
        def analysiere(punkt):
            match punkt:
                case (0, 0):
                    print("Ursprung")
                case (x, 0):
                    print(f"Auf X-Achse bei {x}")
                case (0, y):
                    print(f"Auf Y-Achse bei {y}")
                case (x, y):
                    print(f"Punkt ({x}, {y})")
        
        # Klassen-Matching
        match form:
            case Kreis(radius=r):
                print(f"Kreis: Fläche = {3.14 * r * r}")
            case Rechteck(breite=b, hoehe=h):
                print(f"Rechteck: Fläche = {b * h}")
            case _:
                print("Unbekannte Form")
        ```   

        | Aspekt | Python | Java |
        |---|---|---|
        | Schlüsselwort | `match` | `switch` |
        | Fall beendet sich | Kein `break` – automatischer Ausstieg | `break` nötig, außer bei Pfeil-Syntax |
        | Vergleichsart | Pattern Matching (Strukturen, Typen, Guards) | Nur Wertevergleiche |
        | Default-Fall | `case _:` (Wildcard) | `default:` |
        | Mehrere Werte in einem Fall | `case 1 \| 2:` (ODER-Verknüpfung) | `case 1: case 2:` (Fall-through) |

    2. Fehlerbehandlung
  
       Java:

        ```java
        try {
            int ergebnis = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Fehler: " + e.getMessage());
        } finally {
            System.out.println("Wird immer ausgeführt");
        }
        ```
        Python:
        
        ```python
        try:
            ergebnis = 10 / 0
        except ZeroDivisionError as e:
            print(f"Fehler: {e}")
        finally:
            print("Wird immer ausgeführt")
        ```

        | Aspekt | Python | Java |
        |---|---|---|
        | Schlüsselworte | `try`, `except`, `finally` | `try`, `catch`, `finally` |
        | Fehlerbindung | `except Typ as e:` | `catch (Typ e)` |
        | Blockbegrenzung | Einrückung nach Doppelpunkt `:` | Geschwungene Klammern `{ }` |
        | Beliebig viele | Mehrere `except`-Blöcke | Mehrere `catch`-Blöcke |
        | Alle fangen | `except Exception as e` | `catch (Exception e)` |        
        
5. Variablen und Datentypen
    1. Allgemeines   
        Python ist **dynamisch typisiert**. Eine Variable hat keinen festen Typ – sie bindet an ein Objekt, der Typ wird zur Laufzeit bestimmt.
        ```python
        x = 42           # int – kein "int x = 42" nötig
        x = "Hallo"      # jetzt str – legal, aber verwirrend
        ```
 
        |Datentyp | Python | Java |
        | ----------- | ----------- | ----------- |
        |Boolean-Werte |`True`, `False`	| `true`, `false` |
        | Ganzzahl-Werte | `int`	|`int` (32 Bit), `long` (64 Bit)|
        | Fließkommazahl| `float` 	|	`float`, `double` |
        | Komplexe Zahl `a + bj`| `complex` |	nicht vorhanden |    
        |„Kein Wert"|`None`	|`null`|
        |Zeichen(kette) |`str`	 (kein separater char)|	`String`, `char`|

        ```python
        # Logische Operatoren: and/or/not statt &&/||/!
        x, y = True, False
        print(x and not y)           # True
        print((x or y) == True)      # True
        
        # Arithmetik – Achtung bei Division!
        print(3 / 2)                 # 1.5  – echte Division (anders als Java!)
        print(3 // 2)                # 1    – Ganzzahldivision
        print(3 ** 2)                # 9    – Potenzoperator (gibt's in Java nicht)
        print(3 % 2)                 # 1    – Modulo (wie Java)
        print(abs(-3))               # 3    – Absolutbetrag
        print(int(3.9))              # 3    – Abschneiden, nicht Runden
        print(float(3))              # 3.0  – explizit zu float
        ```
        
        Achtung: `/` in Python liefert immer `float` (`3/2 = 1.5`). `//` ist die Ganzzahldivision. 
        Genau umgekehrt zu Java, wo `/` bei zwei `int`-Operanden die Ganzzahldivision ist.


    3. Vergleich Referenz- und Inhaltsvergleich: Python vs. Java   
   
       | Aspekt | Python | Java |
       |---|---|---|
       | **Referenzvergleich** (Identität) | `a is b` – prüft, ob beide Variablen auf dasselbe Objekt zeigen | `a == b` – prüft, ob beide Referenzen auf dasselbe Objekt zeigen |
        | **Inhaltsvergleich** (Wertegleichheit) | `a == b` – ruft `__eq__()` auf ( überschreibbar) | `a.equals(b)` – außer bei primitive Datentypen |
        | **Vergleich auf null / None** | `x is None` – immer mit `is`, nie mit `==` | `x == null` |
        | **Vergleich auf ungleich null / None** | `x is not None` – idiomatisch und bevorzugt | `x != null` |

4. Collections   
   1. Listen   

        Java:
        ```java
        List<String> list = new ArrayList<>();
        list.add("Apfel");
        list.add("Banane");
        list.add("Apfel");        // erlaubt – Duplikate
        String eins = list.get(0);
        list.set(1, "Birne");
        list.remove(0);
        int size = list.size();
        ```
        Python:
        ```python
        liste = []
        liste.append("Apfel")
        liste.append("Banane")
        liste.append("Apfel")      # erlaubt – Duplikate
        eins = liste[0]            # Index direkt per [] – kein get()
        liste[1] = "Birne"         # set direkt per Index
        del liste[0]               # oder: liste.pop(0)
        laenge = len(liste)        # len() statt .size()
        ```

        | Aspekt | Python | Java |
        |---|---|---|
        | Erzeugung | `[]` oder `list()` | `new ArrayList<>()` (Bsp.) |
        | Hinzufügen | `.append(e)` | `.add(e)` |
        | Lesen per Index | `lst[i]` – Subscript-Operator | `.get(i)` |
        | Schreiben per Index | `lst[i] = wert` | `.set(i, wert)` |
        | Länge | `len(lst)` | `.size()` |
        | Löschen per Index | `del lst[i]` oder `.pop(i)` | `.remove(i)` |
        | Löschen per Wert | `.remove(wert)` (entfernt erstes Vorkommen) | `.remove(wert)` |
        | Enthält? | `wert in lst` | `.contains(wert)` |
        | Sortieren | `lst.sort()` oder `sorted(lst)` | `Collections.sort(lst)` |
        | Vorinitialisiert | `["a", "b"]` | `Arrays.asList("a", "b")` |
        | Typisierung | Dynamisch – alles in einer Liste möglich (auch gemischt) | Generics (`List<String>`) |

        Slicing – Pythons großer Vorteil:   

        ```python
        zahlen = [0, 1, 2, 3, 4, 5]
        print(zahlen[1:4])     # [1, 2, 3]  – von Index 1 bis 3
        print(zahlen[:3])      # [0, 1, 2]  – erstes bis drittes
        print(zahlen[::2])     # [0, 2, 4]  – jedes zweite
        print(zahlen[::-1])    # [5, 4, 3, 2, 1, 0]  – umgekehrt
        ```

    2. Tuples   
       Tuples haben kein direktes Java-Äquivalent – sie sind unveränderliche (immutable) Listen:

        ```python
        punkt = (3, 4)
        print(punkt[0])          # 3
        punkt[0] = 1             # ❌ TypeError: tuple does not support assignment
        
        # Tupel auspacken (destructuring) – sehr elegant
        x, y = punkt
        print(x, y)              # 3 4

        # Variableninhalte austauschen
        x, y = y, x
        
        # Rückgabe mehrerer Werte
        def min_max(liste):
            return min(liste), max(liste)
        
        erg = min_max([5, 2, 8, 1])
        print(erg)               # (1, 8)
        mn, mx = erg
        print(mn, mx)            # 1 8
        ```

    3. Sets (Mengen)   
        Java:
        ```java
        Set<String> set = new HashSet<>();
        set.add("Apfel");
        set.add("Banane");
        set.add("Apfel");          // wird ignoriert – kein Duplikat
        boolean enthaelt = set.contains("Apfel");
        int size = set.size();
        for (String s : set) { ... }
        ```
        Python:
        ```python
        menge = set()              # leeres Set ({} wäre leeres Dict!)
        menge.add("Apfel")
        menge.add("Banane")
        menge.add("Apfel")         # wird ignoriert – kein Duplikat
        enthaelt = "Apfel" in menge
        groesse = len(menge)
        
        # Vorinitialisiert
        farben = {"rot", "blau", "grün"}
        
        # Alle Elemente durchlaufen
        for e in menge:
            print(e)
        ```
        
        | Aspekt | Python | Java |
        |---|---|---|
        | Erzeugung | `set()` oder `{1, 2, 3}` | `new HashSet<>()` |
        | Hinzufügen | `.add(e)` (gleich!) | `.add(e)` |
        | Enthält? | `e in menge` | `.contains(e)` |
        | Länge | `len(menge)` | `.size()` |
        | Löschen | `.remove(e)` oder `.discard(e)` (kein Fehler bei Nichtexistenz) | `.remove(e)` |
        | Typisierung | Dynamisch – auch gemischt | Generics `Set<String>` |
        | Ordnung | Seit Python 3.7: Einfügereihenfolge erhalten | Keine (außer `LinkedHashSet`/`TreeSet`) |
        
        *Wichtig:* `{}` ist in Python ein leeres Dictionary, kein leeres Set. Ein leeres Set muss immer `set()` heißen.

        Mengenoperationen sind in Python sehr einfach möglich:
        
        ```python
        a = {1, 2, 3, 4}
        b = {3, 4, 5, 6}
        
        print(a | b)          # Vereinigung:   {1, 2, 3, 4, 5, 6}
        print(a & b)          # Schnittmenge:  {3, 4}
        print(a - b)          # Differenz:     {1, 2}
        print(a ^ b)          # Sym. Differenz: {1, 2, 5, 6}
        
        print(a.issubset(b))      # False
        print(a.issuperset(b))    # False
        print(a.isdisjoint({5}))   # False
        ```

    4. Assoziative Arrays
       Java:

        ```java
        Map<String, Integer> map = new HashMap<>();
        map.put("Apfel", 3);
        map.put("Banane", 2);
        int wert = map.get("Apfel");           // 3
        int wert2 = map.getOrDefault("Birne", 0);  // 0 statt null
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }
        ```
        Python:
        ```python
        d = {}                              # leeres Dict
        d = {"Apfel": 3, "Banane": 2}      # vorinitialisiert
        d["Birne"] = 5                      # setzen (oder hinzufügen)
        wert = d["Apfel"]                   # 3 – KeyError wenn nicht vorhanden!
        wert2 = d.get("Birne", 0)           # 0 – sicher, mit Default
        
        # Alle Schlüssel-Wert-Paare durchlaufen
        for k, v in d.items():             # items() = entrySet()
            print(f"{k}: {v}")
        
        # Nur Schlüssel
        for k in d:                        # d.keys() geht auch
            print(k)
        
        # Nur Werte
        for v in d.values():
            print(v)
        ```

        | Aspekt | Python | Java |
        |---|---|---|
        | Erzeugung | `{}` oder `dict()` | `new HashMap<>()` (Bsp.) |
        | Wert setzen | `d[key] = wert` | `.put(key, wert)` |
        | Wert lesen | `d[key]` – löst `KeyError` aus bei fehlendem Schlüssel | `.get(key)` – gibt `null` bei fehlendem Schlüssel |
        | Sicheres Lesen | `d.get(key, default)` | `.getOrDefault(key, default)` |
        | Vorinitialisiert | `{"a": 1, "b": 2}` | `Map.of("a", 1, "b", 2)` (Java 9+) |
        | Enthält Schlüssel? | `key in d` | `.containsKey(key)` |
        | Enthält Wert? | `wert in d.values()` | `.containsValue(wert)` |
        | Länge | `len(d)` | `.size()` |
        | Löschen | `del d[key]` oder `.pop(key)` | `.remove(key)` |
        | Alle Schlüssel | `.keys()` | `.keySet()` |
        | Alle Werte | `.values()` | `.values()` |
        | Alle Paare | `.items()` → Tupel `(key, value)` | `.entrySet()` → `Map.Entry` |
        | Durchlaufen | `for k, v in d.items():` | `for (Map.Entry<K,V> e : map.entrySet()) { e.getKey(); e.getValue(); }` |
        | Typisierung | Dynamisch – Schlüssel und Werte gemischt möglich | Generics: `Map<String, Integer>` (Bsp.) |
        | Null-Schlüssel | `None` als Schlüssel erlaubt | Ein `null`-Schlüssel erlaubt |
        | Ordnung | Einfügereihenfolge erhalten (seit Python 3.7) | Keine Garantie (außer `LinkedHashMap`) |

5. List Comprehension in Python   
    Die List Comprehension ist ein prägnantes Python-Feature, das die Erzeugung von Listen aus einer bestehenden Sequenz in einer Zeile erlaubt – ohne Java-ähnliche Schleifen mit manuellem `.add()`.
    1. Grundstruktur   
        ```python
        [ausdruck for element in iterable if bedingung]
        ```

        | Teil | Bedeutung |
        |---|---|
        | Ausdruck | Was mit jedem Element passiert (kann auch das Element selbst sein) |
        | `for element in iterable` | Schleife über eine Sequenz |
        | `if bedingung` *(optional)* | Filter – nur Elemente, die die Bedingung erfüllen |

    2. Einfaches Beispiel   
        Java – etwas mühsam:   
        ```java
        List<Integer> zahlen = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> verdoppelt = new ArrayList<>();
        for (int z : zahlen) {
            verdoppelt.add(z * 2);
        }
        ```
        Python – List Comprehension:   
        ```python
        zahlen = [1, 2, 3, 4, 5]
        verdoppelt = [z * 2 for z in zahlen]
        # Ergebnis: [2, 4, 6, 8, 10]
        ```

    3. Mit Filter (entspricht `if` innerhalb der Schleife)   
        Nur gerade Zahlen verdoppeln:
        ```python
        zahlen = [1, 2, 3, 4, 5, 6]
        gerade_verdoppelt = [z * 2 for z in zahlen if z % 2 == 0]
        # Ergebnis: [4, 8, 12]
        ```
        Zum Vergleich – konventionelle Schreibweise:
        ```python
        gerade_verdoppelt = []
        for z in zahlen:
            if z % 2 == 0:
                gerade_verdoppelt.append(z * 2)
        ```

    4. Listen kombinieren   
        ```python
        farben = ["rot", "blau"]
        formen = ["kreis", "quadrat"]
        
        kombis = [f"{f} {fo}" for f in farben for fo in formen]
        # Ergebnis: ['rot kreis', 'rot quadrat', 'blau kreis', 'blau quadrat']
        ```

    5. Wichtiger Unterschied zu Java Streams   
        Java 8+ Streams sehen auf den ersten Blick ähnlich aus, sind es aber nicht:
        ```java
        // Java Stream
        List<Integer> result = list.stream()
            .filter(x -> x % 2 == 0)
            .map(x -> x * 2)
            .collect(Collectors.toList());
        ```
        ```python
        # Python List Comprehension
        result = [x * 2 for x in liste if x % 2 == 0]
        ```

        | Aspekt | Python List Comprehension | Java Stream |
        |---|---|---|
        | Ansatz | Imperativ – kompakte Schleifensyntax | Deklarativ – Pipeline aus Operationen |
        | Ausführung | Eager – erzeugt sofort die volle Liste | Lazy (erst beim Terminal-Operator) |
        | Mehrere Operationen | Einzelner Ausdruck mit `if` + `for` | `.filter().map().sorted()` (Method Chaining) |
        | Leserichtung | Verschachtelt: Ausdruck + `for` + `if` (von innen lesen) | Vorwärts: Datenquelle → filter → map → collect |

    6. Verwandte Formen: Dict Comprehension & Set Comprehension
       1. Set Comprehension
            ```python
            # Alle geraden Quadratzahlen von 0 bis 19
            gerade_quadrate = {x**2 for x in range(20) if x**2 % 2 == 0}
            print(gerade_quadrate)
            # Beispiel-Ausgabe: {0, 4, 16, 36, 64, 100, 144, 196, 256, 324}
            # (keine Duplikate – deshalb Set statt Liste)
            
            # Buchstaben aus einem Satz extrahieren (ohne Doppelte)
            satz = "Python ist grossartig"
            buchstaben = {c for c in satz if c.isalpha()}
            print(buchstaben)
            # Beispiel-Ausgabe: {'g', 'y', 'a', 't', 'i', 'n', 'P', 'o', 'r', 's'}
            ```
            Wichtig: Die Ausgabe ist ungeordnet – ein Set hat keine garantierte Reihenfolge (anders als Listen). Jeder Lauf kann eine andere Anordnung liefern.

        2. Dict Comprehension
            ```python
            # Quadratzahlen als Dictionary: Zahl → Quadrat
            quadrate = {x: x**2 for x in range(5)}
            print(quadrate)
            # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
            
            # Wörter aus einer Liste zählen (Länge → Anzahl)
            woerter = ["Hund", "Katze", "Maus", "Elefant", "Bär"]
            laengen = {w: len(w) for w in woerter}
            print(laengen)
            # {"Hund": 4, "Katze": 5, "Maus": 4, "Elefant": 7, "Bär": 3}
            
            # Bestehendes Dict transformieren – Celsius in Fahrenheit
            celsius = {"Mo": 20, "Di": 25, "Mi": 18}
            fahrenheit = {tag: (c * 9/5 + 32) for tag, c in celsius.items()}
            print(fahrenheit)
            # {"Mo": 68.0, "Di": 77.0, "Mi": 64.4}
            
            # Mit Filter – nur gerade Zahlen mit ihren Quadraten
            gerade = {x: x**2 for x in range(10) if x % 2 == 0}
            print(gerade)
            # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
            ```

    7. Gegenüberstellung d   
       ```python
        liste  = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]             – eckige Klammern
        menge  = {x**2 for x in range(5)}   # {0, 1, 4, 9, 16}             – geschwungene Klammern, ein Ausdruck
        dict   = {x: x**2 for x in range(5)} # {0: 0, 1: 1, 2: 4, ...}     – geschwungene Klammern, key: value
        ```
        Das Erkennungsmerkmal ist einfach: **ein** Ausdruck → Set. key: value-Paar → Dict.er drei Comprehension-Arten:
       


4. Objektorientierung
    1. Grundstruktur einer Klasse   

        Java:
        ```java
        public class Person {
            private String name;
            private int alter;
        
            public Person(String name, int alter) {
                this.name = name;
                this.alter = alter;
            }
        
            public void vorstellen() {
                System.out.println("Hallo, ich bin " + name);
            }
        }
        ```
        Python:
        ```python
        class Person:
            def __init__(self, name, alter):     # __init__ = Konstruktor
                self.name = name                  # self = this (explizit!)
                self.alter = alter
        
            def vorstellen(self):                 # self immer erster Parameter
                print(f"Hallo, ich bin {self.name}")
        ```
    
        | Erklärung | Python | Java |
        |---|---|---|
        | Referenz auf das aktuelle Objekt in Methoden | `self` muss explizit als erster Parameter stehen | `this` ist implizit vorhanden |
        | Sichtbarkeit von Attributen und Methoden | Keine echten Zugriffsmodifikatoren; alles ist öffentlich. Konvention: `_name` für „protected“, `__name` für „private“ (Name Mangling) | `public`, `private`, `protected` |
        | Klassenkopf und Blockstruktur | `class Person:` plus Einrückung | `class Person { ... }` |
        | Konstruktor / Initialisierung | Konstruktor heißt `__init__` | Konstruktor: `Person(...)` |
        | Objekterzeugung | `Person()` – kein `new`-Schlüsselwort | `new Person(...)` |

    2. Klassenmethoden vs. Objektmethoden (statische vs. Instanzmethoden)   
        Python nutzt Dekoratoren (`@`) statt Schlüsselwörter wie `static`.   
        
        | Erklärung | Python | Java |
        |---|---|---|
        | Methode einer konkreten Instanz | kein Dekorator; erster Parameter ist `self` | normale Instanzmethode; `this` ist implizit vorhanden |
        | Methode auf Klassenebene | `@classmethod`; erster Parameter ist `cls` (die Klasse selbst) | meist `static` plus expliziter Klassenbezug, wenn auf Klassenwerte zugegriffen wird |
        | Hilfsfunktion innerhalb einer Klasse ohne Objekt- oder Klassenbezug | `@staticmethod`; kein spezieller erster Parameter | `static` |

        ```python
        class Util:
            # Instanzmethode (Objektmethode) – arbeitet auf der Instanz
            def instanz_methode(self):
                print(f"Gehört zum Objekt: {self}")
        
            # Klassenmethode – bekommt die Klasse (cls) übergeben
            @classmethod
            def klassen_methode(cls):
                print(f"Gehört zur Klasse: {cls.__name__}")
        
            # Statische Methode – weder self noch cls
            @staticmethod
            def statische_methode():
                print("Losgelöst wie eine normale Funktion")
        ```
        Aufruf:
        ```python
        # Instanzmethode
        u = Util()
        u.instanz_methode()
        
        # Klassenmethode – über Klasse ODER Objekt
        Util.klassen_methode()
        u.klassen_methode()     # funktioniert auch, übergibt Util als cls
        
        # Statische Methode
        Util.statische_methode()
        ```
        Warum `@classmethod`? Anders als Java-`static` kennt `cls` die Vererbungshierarchie. Wenn eine Subclass die Methode aufruft, ist `cls` die Subclass – nützlich für Factory-Methoden.

    3. Sondermethoden: `__methoden__` (Dunder-Methoden)

        *Dunder* = **D**ouble **Under**score.
        Diese Methoden haben fixe Namen, die Python intern aufruft. Sie sind das Gegenstück zu überschriebenen Methoden von `Object` oder implementierten Interfaces in Java.
        
        | Dunder-Methode | Wird aufgerufen durch | Java-Äquivalent |
        |---|---|---|
        | `__init__(self, ...)` | `Person("Max", 30)` | Konstruktor |
        | `__str__(self)` | `str(obj)`, `print(obj)` | `toString()` |
        | `__repr__(self)` | `repr(obj)`, Debugger | (Debug-Darstellung) |
        | `__eq__(self, other)` | `obj1 == obj2` | `equals(Object)` |
        
    4. Overloading

        Java erlaubt Methoden-Overloading (gleicher Name, unterschiedliche Signatur):
        
        ```java
        void print(int x) { ... }
        void print(String x) { ... }
        void print(int x, String y) { ... }
        ```
        Python hat **kein** Overloading – eine Methode kann nur einmal definiert werden.
        Stattdessen nutzt Python flexible Parameter-Mechanismen:
        
        - Default-Werte (optionale Parameter)
        - *args (beliebig viele Positionsargumente → Tupel)
        - **kwargs (beliebig viele Schlüsselwort-Argumente → Dict)

        1. Default-Werte   
           Python erlaubt Default-Werte direkt in der Signatur (in Java erst seit Kurzem mit Records/Builder-Pattern oder überladenen Methoden simuliert):

            ```python
            def begruesse(name, begruessung="Hallo"):
                print(f"{begruessung}, {name}!")
            
            begruesse("Max")           # "Hallo, Max!"
            begruesse("Max", "Moin")   # "Moin, Max!"
            ```
            Position der Default-Parameter
            Default-Parameter **MÜSSEN** rechts von allen Pflichtparametern stehen:
            
            ```python
            # FALSCH – SyntaxError
            def fehler(a=1, b):
                pass
            
            # RICHTIG
            def richtig(b, a=1):
                pass
            ```

        2. *args – Beliebig viele Positionsargumente als Tupel   
            Entspricht Java-Varargs (int... zahlen):

            ```python
            def summiere(*zahlen):
                print(type(zahlen))    # <class 'tuple'>
                return sum(zahlen)
            
            print(summiere(1, 2, 3))         # 6
            print(summiere(1, 2, 3, 4, 5))   # 15
            ```
            Position: *args kommt rechts von allen festen Positionsparametern:
            
            ```python
            def protokolliere(msg, *werte):
                print(f"{msg}: {werte}")
            
            protokolliere("Zahlen", 10, 20, 30)
            # Ausgabe: "Zahlen: (10, 20, 30)"
            ```
            Entpacken mit * (Umkehrung)
            Eine Liste/ein Tupel beim Aufruf auseinanderziehen:
            
            ```python
            zahlen = [1, 2, 3]
            print(*zahlen)              # gleich: print(1, 2, 3)
            
            def sum(a, b, c):
                return a + b + c
            
            werte = [5, 10, 15]
            print(sum(*werte))          # 30
            ```

        3. **kwargs – Beliebige Schlüsselwort-Argumente als Dict   
           `**kwargs` sammelt alle benannten (Keyword-)Argumente in einem Dictionary:

            ```python
            def zeige_info(**kwargs):
                print(type(kwargs))  # <class 'dict'>
                print(kwargs)
            
            zeige_info(name="Max", alter=30, stadt="Berlin")
            # Ausgabe: {'name': 'Max', 'alter': 30, 'stadt': 'Berlin'}
            ```

            Entpacken in Schleifen   
            Da `**kwargs` ein Dictionary ist, kann man es wie jedes `dict` durchlaufen:
            
            ```python
            def konfiguriere(**einstellungen):
                for schluessel in einstellungen:
                    print(f"{schluessel}: {einstellungen[schluessel]}")
            
                # Eleganter: .items()
                for k, v in einstellungen.items():
                    print(f"{k} = {v}")
            ```

            Entpacken beim Aufruf (Umkehrung)   
            `**kwargs` entsteht beim Sammeln von Argumenten in der Funktionsdefinition.
            
            Beim Aufruf kann man mit `**` ein `dict` entpacken und seine Schlüssel-Wert-Paare als benannte Argumente übergeben:
            
            ```python
            def verbinde(host, port, ssl=False):
                print(f"Verbinde zu {host}:{port} (SSL: {ssl})")
            
            config = {"host": "example.com", "port": 443, "ssl": True}
            
            # Entpacken beim Aufruf:
            verbinde(**config)
            # Verbinde zu example.com:port 443 (SSL: True)
            ```

