
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
| Blöcke	| Geschweifte Klammern { ... }	| Einrückung definiert Blöcke | 

**Wichtigster Unterschied:** Keine geschweiften Klammern, kein Semikolon. Die **Einrückung** (standardmäßig 4 Leerzeichen) bestimmt die Blockstruktur – sie ist Teil der Syntax und nicht optional.

```python
# Keine Klammern, kein Semikolon – Einrückung regelt alles
if x > 0:
    print("positiv")        # eingerückt = im if-Block
    print("weiter so")      # immer noch im if
else:
    print("nicht positiv")
print("hier bin ich draußen")
```

2. Variablen und Datentypen
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

3. Grundstruktur einer Klasse
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

4. Klassenmethoden vs. Objektmethoden (statische vs. Instanzmethoden)
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

5. Sondermethoden: __methoden__ (Dunder-Methoden)   
*Dunder* = **D**ouble **Under**score.
Diese Methoden haben fixe Namen, die Python intern aufruft. Sie sind das Gegenstück zu überschriebenen Methoden von `Object` oder implementierten Interfaces in Java.
