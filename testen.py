import unittest
import konto
from liste_konten import Konto_Erweitert


class TestKontoErweitert(unittest.TestCase):
    def setUp(self):
        # globalen Klassenzustand zurücksetzen
        konto.Konto.WAEHRUNG = "EUR"

    # ------------------------------------------------------------
    # 5 Normalfälle
    # ------------------------------------------------------------

    def test_einzahlen_erhoeht_kontostand_und_speichert_transaktion(self):
        k = Konto_Erweitert("Eva", 100.0)

        k.einzahlen(50.0)

        self.assertEqual(k.kontostand, 150.0)
        self.assertEqual(k.transaktionen(), [50.0])

    def test_auszahlen_verringert_kontostand_und_speichert_negative_transaktion(self):
        k = Konto_Erweitert("Ben", 200.0)

        k.auszahlen(80.0)

        self.assertEqual(k.kontostand, 120.0)
        self.assertEqual(k.transaktionen(), [-80.0])

    def test_letzte_transaktionen_liefert_die_letzten_n_eintraege(self):
        k = Konto_Erweitert("Clara", 500.0)
        k.einzahlen(100.0)
        k.einzahlen(50.0)
        k.auszahlen(20.0)
        k.einzahlen(10.0)

        self.assertEqual(k.letzte_transaktionen(2), [-20.0, 10.0])

    def test_zusammenfassung_liefert_korrekte_statistik(self):
        k = Konto_Erweitert("David", 300.0)
        k.einzahlen(100.0)
        k.einzahlen(50.0)
        k.auszahlen(30.0)
        k.auszahlen(20.0)

        erwartet = {
            "anzahl_gesamt": 4,
            "summe_einzahlungen": 150.0,
            "summe_auszahlungen": -50.0,
            "groesste_einzahlung": 100.0,
            "groesste_auszahlung": -30.0,
        }

        self.assertEqual(k.zusammenfassung(), erwartet)

    def test_ueberweisen_bucht_auf_beiden_konten_korrekt(self):
        quelle = Konto_Erweitert("Eva", 500.0)
        ziel = Konto_Erweitert("Ben", 100.0)

        quelle.ueberweisen(ziel, 150.0)

        self.assertEqual(quelle.kontostand, 350.0)
        self.assertEqual(ziel.kontostand, 250.0)
        self.assertEqual(quelle.transaktionen(), [-150.0])
        self.assertEqual(ziel.transaktionen(), [150.0])

    # ------------------------------------------------------------
    # 5 Fehlerfälle
    # ------------------------------------------------------------

    def test_einzahlen_mit_null_wirft_value_error(self):
        k = Konto_Erweitert("Eva", 100.0)

        with self.assertRaises(ValueError):
            k.einzahlen(0)

    def test_auszahlen_mit_negativem_betrag_wirft_value_error(self):
        k = Konto_Erweitert("Ben", 100.0)

        with self.assertRaises(ValueError):
            k.auszahlen(-10)

    def test_auszahlen_ueber_kontostand_wirft_value_error(self):
        k = Konto_Erweitert("Clara", 50.0)

        with self.assertRaises(ValueError):
            k.auszahlen(60.0)

    def test_ueberweisen_auf_eigenes_konto_wirft_value_error(self):
        k = Konto_Erweitert("David", 200.0)

        with self.assertRaises(ValueError):
            k.ueberweisen(k, 50.0)

    def test_ueberweisen_auf_falschen_typ_wirft_type_error(self):
        quelle = Konto_Erweitert("Eva", 200.0)
        ziel = konto.Konto("Max", 100.0)

        with self.assertRaises(TypeError):
            quelle.ueberweisen(ziel, 50.0)

    # ------------------------------------------------------------
    # 3 Grenzfälle
    # ------------------------------------------------------------

    def test_letzte_transaktionen_mit_n_null_liefert_leere_liste(self):
        k = Konto_Erweitert("Eva", 100.0)
        k.einzahlen(20.0)

        self.assertEqual(k.letzte_transaktionen(0), [])

    def test_letzte_transaktionen_mit_n_groesser_als_anzahl_liefert_alle(self):
        k = Konto_Erweitert("Ben", 100.0)
        k.einzahlen(10.0)
        k.auszahlen(5.0)

        self.assertEqual(k.letzte_transaktionen(10), [10.0, -5.0])

    def test_zusammenfassung_ohne_transaktionen_liefert_default_werte(self):
        k = Konto_Erweitert("Clara", 100.0)

        erwartet = {
            "anzahl_gesamt": 0,
            "summe_einzahlungen": 0,
            "summe_auszahlungen": 0,
            "groesste_einzahlung": 0.0,
            "groesste_auszahlung": 0.0,
        }

        self.assertEqual(k.zusammenfassung(), erwartet)


if __name__ == "__main__":
    unittest.main()