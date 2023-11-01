import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(4) #2->4 to break test

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

#omat testit

    def test_negatiivinen_alkutilavuus_nollaantuu(self):
        self.neg_t = Varasto(-1)

        self.assertAlmostEqual(self.neg_t.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollaantuu(self):
        self.neg_as = Varasto(10, -1)

        self.assertAlmostEqual(self.neg_as.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_ei_voi_lisata_yli_tilavuuden(self):
        tilaa = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(tilaa+1)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_maaran_otto_ei_vahenna_saldoa(self):
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_ei_voi_ottaa_enempaa_kuin_saldo(self):
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(saldo+1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str(self):
        self.assertAlmostEqual(str(self.varasto), str(Varasto(10)))
