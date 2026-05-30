class Konto:
    # Klassenvariable (gemeinsam für alle Instanzen)
    ANZAHL_KONTEN = 0
    WAEHRUNG = "EUR"

    def __init__(self, inhaber: str, kontostand: float = 0.0):
        """
        Kontruktor

        :param inhaber:
        :param kontostand:
        """
        # Instanzvariablen (pro Objekt)
        self.inhaber = inhaber
        self._kontostand = 0.0
        self.kontostand = kontostand  # nutzt den Setter für Validierung
        Konto.ANZAHL_KONTEN += 1

    # Dunder-Methode: offizielle String-Repräsentation (für Entwickler)
    def __repr__(self) -> str:
        """

        :return:
        """
        return f"Konto(inhaber={self.inhaber!r}, kontostand={self.kontostand:.2f}, waehrung={Konto.WAEHRUNG!r})"

    # Dunder-Methode: benutzerfreundliche Ausgabe (für Benutzer)
    def __str__(self) -> str:
        return f"Konto von {self.inhaber}: {self.kontostand:.2f} {Konto.WAEHRUNG}"

    # Dunder-Methode: Vergleich zweier Objekte
    def __eq__(self, other) -> bool:
        if not isinstance(other, Konto):
            return NotImplemented
        return self.inhaber == other.inhaber and self.kontostand == other.kontostand

    # Dunder-Methode: Aufrufbar wie eine Funktion
    def __call__(self, betrag: float) -> None:
        # Einzahlen über Funktionsaufruf: konto(100)
        self.einzahlen(betrag)

    # Dunder-Methode: Wird beim Löschen der Instanz aufgerufen (nicht immer garantiert!)
    def __del__(self):
        Konto.ANZAHL_KONTEN -= 1

    # Property-Decorator: Getter
    @property
    def kontostand(self) -> float:
        return self._kontostand

    # Property-Decorator: Setter mit Validierung
    @kontostand.setter
    def kontostand(self, wert: float) -> None:
        if wert < 0:
            raise ValueError("Kontostand darf nicht negativ sein.")
        self._kontostand = float(wert)

    def einzahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError("Einzahlungsbetrag muss positiv sein.")
        self._kontostand += betrag

    def auszahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError("Auszahlungsbetrag muss positiv sein.")
        if betrag > self._kontostand:
            raise ValueError("Nicht genug Guthaben.")
        self._kontostand -= betrag

    # Statische Methode: benötigt weder cls noch self
    @staticmethod
    def ist_gueltiger_betrag(betrag: float) -> bool:
        return isinstance(betrag, (int, float)) and betrag > 0

    @classmethod
    def von_string(cls, daten: str):
        """
        Alternativer Konstruktor.
        Erwartetes Format: 'Inhaber;Kontostand', z. B. 'Clara;350.75'
        """
        teile = daten.split(";")
        if len(teile) != 2:
            raise ValueError("Format muss 'Inhaber;Kontostand' sein.")

        inhaber = teile[0].strip()
        try:
            kontostand = float(teile[1].strip())
        except ValueError as exc:
            raise ValueError("Kontostand muss eine Zahl sein.") from exc

        return cls(inhaber, kontostand)

    @staticmethod
    def setze_waehrung( neue_waehrung: str) -> None:
        """
        Setzt die Waehrung fuer alle Konten (Klassenvariable).
        Beispiel: Konto.setze_waehrung("USD")
        """
        neue_waehrung = neue_waehrung.strip().upper()
        if not neue_waehrung:
            raise ValueError("Waehrung darf nicht leer sein.")
        Konto.WAEHRUNG = neue_waehrung


if __name__ == "__main__":
    print("=== Test der Klasse Konto ===")

    k1 = Konto("Anna", 100.0)
    k2 = Konto("Ben", 50.0)

    print(k1)           # __str__
    print(repr(k2))     # __repr__

    k1.einzahlen(25)
    k1.auszahlen(40)
    print("Nach Buchungen:", k1)

    # Property (Getter/Setter)
    print("Kontostand ueber Getter:", k1.kontostand)
    k1.kontostand = 200.0
    print("Kontostand nach Setter:", k1.kontostand)

    # __call__
    k1(30)  # entspricht einzahlen(30)
    print("Nach __call__:", k1)

    # __eq__
    k3 = Konto("Anna", 230.0)
    print("k1 == k3 ?", k1 == k3)

    # Klassenvariable
    print("Anzahl Konten:", Konto.ANZAHL_KONTEN)
    print("Waehrung:", Konto.WAEHRUNG)

    # Statische Methode
    print("Ist 15.5 gueltig?", Konto.ist_gueltiger_betrag(15.5))
    print("Ist -2 gueltig?", Konto.ist_gueltiger_betrag(-2))

    # Klassenmethode: alternativer Konstruktor
    k4 = Konto.von_string("Clara;350.75")
    print("Aus Klassenmethode erzeugt:", k4)

    # Zusätzliche Klassenmethode: Waehrung setzen
    Konto.setze_waehrung("usd")
    print("Neue Waehrung:", Konto.WAEHRUNG)
    print("k1 nach Waehrungswechsel:", k1)
    print("k4 nach Waehrungswechsel:", k4)

    try:
        Konto.von_string("FalschesFormat")
    except ValueError as e:
        print("Fehler bei von_string:", e)

    try:
        Konto.setze_waehrung("   ")
    except ValueError as e:
        print("Fehler bei setze_waehrung:", e)