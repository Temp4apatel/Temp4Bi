import sys
sys.path.append('../src')

from mast_stat import MastStat
import unittest

class TestMastStat(unittest.TestCase):
    def test_get_tenant_mast_count(self):
        maststat = MastStat()
        list_records = [
            ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7',
                'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', '20', '6600.00'],
            ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14',
             'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'],
            ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds',
                'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'],
            ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865',
                'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'],
            ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) - Block 2, WYK 0414',
             'Hutchinson3G Uk Ltd&Everything Everywhere Ltd', '21 Aug 2007', '20 Aug 2032', '25', '12750.00']
        ]

        stat = maststat.get_tenant_mast_count(list_records, 6)
        self.assertEqual(len(stat), 5)

    def test_get_tenant_mast_report(self):
        maststat = MastStat()
        list_records = [
            ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7',
                'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', '20', '6600.00'],
            ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14',
             'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'],
            ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds',
                'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'],
            ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865',
                'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'],
            ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) - Block 2, WYK 0414',
             'Hutchinson3G Uk Ltd&Everything Everywhere Ltd', '21 Aug 2007', '20 Aug 2032', '25', '12750.00']
        ]

        stat = maststat.get_tenant_mast_count(list_records, 6)
        self.assertEqual(stat, {'Arqiva Ltd': 1, 'Vodafone Ltd.': 1, 'Vodafone Ltd': 1, 'O2 (UK) Ltd': 1, 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd': 1})
    

if __name__ == '__main__':
    unittest.main()
