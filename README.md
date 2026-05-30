
# Python für Java-Entwickler – Eine kurze Einführung
Ausgangspunkt: Mehrjährige Java-Erfahrung. Ziel: Python lesen, verstehen und schreiben können.

1. Grundlegendes Sprachkonzept


| Aspekt |	Java	| Python |
| ----------- | ----------- | ----------- |
| Paradigma	| Rein objektorientiert (mit Primitiven)	| Multi-Paradigma: OOP, funktional, prozedural| 
| Typsystem	| Statisch, explizit (String name = "Max")	| Dynamisch, implizit (name = "Max")| 
| Kompilation	| Compiler → Bytecode → JVM	| Interpretiert (Bytecode → Python-VM)| 
| Blöcke	| Geschweifte Klammern { ... }	| Einrückung definiert Blöcke | 

Wichtigster Unterschied: Keine geschweiften Klammern, kein Semikolon. Die Einrückung (standardmäßig 4 Leerzeichen) bestimmt die Blockstruktur – sie ist Teil der Syntax und nicht optional.

python
# Keine Klammern, kein Semikolon – Einrückung regelt alles
if x > 0:
    print("positiv")        # eingerückt = im if-Block
    print("weiter so")      # immer noch im if
else:
    print("nicht positiv")
print("hier bin ich draußen")
