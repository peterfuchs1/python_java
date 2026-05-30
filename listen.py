# ─────────────────────────────────────────────
# 1. Einfache Listen erstellen
# ─────────────────────────────────────────────
def einfache_listen(zahlen: list[int]) -> None:
    namen = ["Anna", "Ben", "Clara", "David"]
    gemischt = [1, "Hallo", 3.14, True]

    print("=== Einfache Listen ===")
    print("Zahlen:", zahlen)
    print("Namen:", namen)
    print("Gemischt:", gemischt)

# ─────────────────────────────────────────────
# 2. Elemente hinzufügen
# ─────────────────────────────────────────────
def elemente_hinzufuegen():
    print("\n=== Elemente hinzufügen ===")

    zahlen.append(60)                  # ans Ende anhängen
    print("Nach append(60):", zahlen)

    zahlen.insert(0, 5)                # an bestimmter Position einfügen
    print("Nach insert(0, 5):", zahlen)

    zahlen.extend([70, 80, 90])        # mehrere Elemente anhängen
    print("Nach extend([70, 80, 90]):", zahlen)

# ─────────────────────────────────────────────
# 3. Elemente entfernen
# ─────────────────────────────────────────────
def elemente_entfernen():
    print("\n=== Elemente entfernen ===")

    zahlen.remove(5)                   # erstes Vorkommen eines Wertes entfernen
    print("Nach remove(5):", zahlen)

    entfernt = zahlen.pop()            # letztes Element entfernen und zurückgeben
    print(f"pop() → entfernt: {entfernt}, Liste: {zahlen}")

    entfernt_idx = zahlen.pop(0)       # Element an Index 0 entfernen
    print(f"pop(0) → entfernt: {entfernt_idx}, Liste: {zahlen}")

    del zahlen[1]                      # Element an Index 1 löschen
    print("Nach del zahlen[1]:", zahlen)

# ─────────────────────────────────────────────
# 4. Nützliche Listenoperationen
# ─────────────────────────────────────────────
def listenoperationen():

    print("\n=== Nützliche Operationen ===")

    print("Länge:", len(zahlen))
    print("Minimum:", min(zahlen))
    print("Maximum:", max(zahlen))
    print("Summe:", sum(zahlen))
    print("Sortiert (aufsteigend):", sorted(zahlen))
    print("Sortiert (absteigend):", sorted(zahlen, reverse=True))
    print("Index von 40:", zahlen.index(40))
    print("Anzahl von 30:", zahlen.count(30))

    zahlen_kopie = zahlen.copy()
    zahlen_kopie.sort()
    print("Sortierte Kopie:", zahlen_kopie)
    print("Original unverändert:", zahlen)

# ─────────────────────────────────────────────
# 5. List Comprehension
# ─────────────────────────────────────────────
def list_comprehension():
    print("\n=== List Comprehension ===")

    # Alle Zahlen verdoppeln
    verdoppelt = [x * 2 for x in zahlen]
    print("Verdoppelt:", verdoppelt)

    # Nur gerade Zahlen
    gerade = [x for x in zahlen if x % 2 == 0]
    print("Gerade Zahlen:", gerade)

    # Quadratzahlen von 1 bis 10
    quadrate = [x ** 2 for x in range(1, 11)]
    print("Quadratzahlen 1–10:", quadrate)

    # Namen in Großbuchstaben, die mit 'A' oder 'C' beginnen
    namen = ["Anna", "Ben", "Clara", "David"]
    gefilterte_namen = [name.upper() for name in namen if name.startswith(("A", "C"))]
    print("Gefilterte Namen (groß):", gefilterte_namen)

    # Verschachtelte List Comprehension: 3x3 Matrix
    matrix = [[zeile * spalte for spalte in range(1, 4)] for zeile in range(1, 4)]
    print("3x3-Multiplikationsmatrix:")
    for zeile in matrix:
        print(" ", zeile)

    # Alle Elemente einer verschachtelten Liste glätten (flatten)
    verschachtelt = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flach = [element for unterlist in verschachtelt for element in unterlist]
    print("Flache Liste:", flach)

# ─────────────────────────────────────────────
# 6. Slicing
# ─────────────────────────────────────────────
def list_slicing():
    print("\n=== Slicing ===")
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original:", s)
    print("s[2:6]   →", s[2:6])       # von Index 2 bis 5
    print("s[:4]    →", s[:4])        # erste 4 Elemente
    print("s[7:]    →", s[7:])        # ab Index 7
    print("s[::2]   →", s[::2])       # jedes zweite Element
    print("s[::-1]  →", s[::-1])      # umgekehrt

if __name__ == '__main__':
    print("\n=== Listen in Aktion ===")
    # Hier können weitere Tests oder Beispiele mit Listen eingefügt werden
    # z.B. das Kombinieren von Listen, das Verwenden von zip(), etc.
    zahlen = [10, 20, 30, 40, 50]
    einfache_listen(zahlen)

    elemente_hinzufuegen()
    elemente_entfernen()
    listenoperationen()
    list_comprehension()
    list_slicing()
