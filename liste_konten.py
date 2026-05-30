import konto
class Konto_Erweitert(konto.Konto):
    """
     Erweiterung der Basisklasse Konto um Listenfunktionalität:
     - Transaktionsverlauf speichern
     - Auswertungen per List Comprehension
     """

    def __init__(self, inhaber: str, kontostand: float = 0.0):
        super().__init__(inhaber, kontostand)
        self._transaktionen: list[float] = []

    def einzahlen(self, betrag: float) -> None:
        """
        Überschreibt einzahlen(), um zusätzlich die Transaktion zu speichern.
        :param betrag:
        """
        super().einzahlen(betrag)
        self._transaktionen.append(float(betrag))

    def auszahlen(self, betrag: float) -> None:
        """
        Überschreibt auszahlen(), um zusätzlich die Transaktion zu speichern.
        Auszahlung wird als negativer Wert gespeichert.
        :param betrag:
        """
        super().auszahlen(betrag)
        self._transaktionen.append(-float(betrag))

    def transaktionen(self) -> list[float]:
        """
        Gibt eine Kopie der Transaktionsliste zurück.
        :return: Liste der Transaktionen (positive Werte für Einzahlungen, negative Werte für Auszahlungen)
        """
        return self._transaktionen.copy()

    def letzte_transaktionen(self, n: int = 5) -> list[float]:
        """
        Gibt die letzten n Transaktionen zurück.
        :param n: Anzahl der letzten Transaktionen
        :return: Liste der Transaktionen (positive Werte für Einzahlungen, negative Werte für Auszahlungen)
        """
        if n <= 0:
            return []
        return self._transaktionen[-n:]

    def einzahlungen(self) -> list[float]:
        """
        List Comprehension: nur positive Transaktionen.
        :return Liste aller Einzahlungen
        """
        return [t for t in self._transaktionen if t > 0]

    def auszahlungen(self) -> list[float]:
        """
        List Comprehension: nur negative Transaktionen.
        :return Liste aller Auszahlungen
        """
        return [t for t in self._transaktionen if t < 0]

    def transaktionen_ueber(self, grenze: float) -> list[float]:
        """
        List Comprehension: alle Transaktionen, deren Betrag (absolut) über der Grenze liegt.
        """
        return [t for t in self._transaktionen if abs(t) > grenze]

    def zusammenfassung(self) -> dict:
        """
        Liefert eine kleine Statistik zur Transaktionsliste.
        """
        einz = self.einzahlungen()
        ausz = self.auszahlungen()
        return {
            "anzahl_gesamt": len(self._transaktionen),
            "summe_einzahlungen": sum(einz),
            "summe_auszahlungen": sum(ausz),
            "groesste_einzahlung": max(einz, default=0.0),
            "groesste_auszahlung": min(ausz, default=0.0),
        }

    def ueberweisen(self, zielkonto: 'Konto_Erweitert', betrag: float) -> None:
        """
        Überweist einen Betrag von diesem Konto auf ein Zielkonto.

        :param zielkonto: Das Empfängerkonto (Konto_Erweitert)
        :param betrag: Der zu überweisende Betrag (muss positiv sein)
        :raises ValueError: Wenn Betrag ungültig oder nicht genug Guthaben vorhanden
        :raises TypeError: Wenn zielkonto kein Konto_Erweitert ist
        """
        if not isinstance(zielkonto, Konto_Erweitert):
            raise TypeError("Zielkonto muss vom Typ Konto_Erweitert sein.")

        if self == zielkonto:
            raise ValueError("Überweisung auf das eigene Konto ist nicht möglich.")

        if betrag <= 0:
            raise ValueError("Überweisungsbetrag muss positiv sein.")

        if betrag > self.kontostand:
            raise ValueError(f"Nicht genug Guthaben. Available: {self.kontostand:.2f}, benötigt: {betrag:.2f}")

        # Auszahlung auf Quellkonto
        self.auszahlen(betrag)
        # Einzahlung auf Zielkonto
        zielkonto.einzahlen(betrag)

        print(f"✓ Überweisung: {self.inhaber} → {zielkonto.inhaber}: {betrag:.2f} {self.WAEHRUNG}")

if __name__ == "__main__":
    print("=== Test Konto_Erweitert ===")

    # Instanz erzeugen
    k = Konto_Erweitert("Eva", 500.0)
    print(f"Konto von {k.inhaber} angelegt")
    print("Start:", k)

    # Buchungen
    a,b,c = 200,50,100
    print(f"Es werden Einzahlung in der Summe von {sum([a,b,c])} durchgeführt")
    k.einzahlen(a)
    k.einzahlen(b)
    k.einzahlen(c)
    c,d = 30,80
    print(f"Es werden Auszahlungen in der Summe von {c+d} durchgeführt")
    k.auszahlen(c)
    k.auszahlen(d)

    print("Nach den Buchungen:", k)
    print("Alle Transaktionen:", k.transaktionen())
    print("Letzte 3 Transaktionen:", k.letzte_transaktionen(3))
    print("Einzahlungen:", k.einzahlungen())
    print("Auszahlungen:", k.auszahlungen())
    print("Transaktionen über |60|:", k.transaktionen_ueber(60))
    print("Zusammenfassung:", k.zusammenfassung())

    # Vererbung + Klassenmethoden aus Basis testen
    k2 = Konto_Erweitert.von_string("Clara;350.75")
    print("Mit Klassenmethode 'von_string' erzeugt:", k2)
    # Währung für alle Konten ändern (statische Methode)
    # konto.Konto.setze_waehrung("USD")
    # Diese Codezeile ist gleichwertig
    # Konto_Erweitert.setze_waehrung("USD")

    print("Neue Währung:", konto.Konto.WAEHRUNG)
    print("k in neuer Währung:", k)
    print(f"k2 in neuer Währung: {k2}")

    # ─────────────────────────────────────────────────────────────
    # Überweisungen testen
    # ─────────────────────────────────────────────────────────────
    print("\n=== Test Überweisungen ===\n")

    k3 = Konto_Erweitert("Ben", 200.0)
    print(f"Konten vor der Überweisung \n  Eva: {k} \n  Ben: {k3}")

    k.ueberweisen(k3, 150.0)
    print(f"Nach Überweisung:")
    print(f"  Eva: {k}")
    print(f"  Ben: {k3}")

    print(f"\nTransaktionen Eva: {k.transaktionen()}")
    print(f"Transaktionen Ben: {k3.transaktionen()}")

    # Fehlerfälle
    print("\n=== Fehlerfälle ===")
    try:
        k.ueberweisen(k, 50)  # Auf eigenes Konto
    except ValueError as e:
        print(f"Fehler: {e}")

    try:
        k.ueberweisen(k2, 10000)  # Zu wenig Guthaben
    except ValueError as e:
        print(f"Fehler: {e}")

    try:
        k.ueberweisen(k3, -50)  # Negativer Betrag
    except ValueError as e:
        print(f"Fehler: {e}")
