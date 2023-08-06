import math


class Data:
    alpha2List = [
        'AD',
        'AE',
        'AF',
        'AG',
        'AI',
        'AL',
        'AM',
        'AO',
        'AR',
        'AS',
        'AT',
        'AU',
        'AW',
        'AX',
        'AZ',
        'BA',
        'BB',
        'BD',
        'BE',
        'BF',
        'BG',
        'BH',
        'BI',
        'BJ',
        'BL',
        'BM',
        'BN',
        'BO',
        'BQ',
        'BR',
        'BS',
        'BT',
        'BW',
        'BY',
        'BZ',
        'CA',
        'CC',
        'CD',
        'CF',
        'CG',
        'CH',
        'CI',
        'CK',
        'CL',
        'CM',
        'CN',
        'CO',
        'CR',
        'CU',
        'CV',
        'CW',
        'CX',
        'CY',
        'CZ',
        'DE',
        'DJ',
        'DK',
        'DM',
        'DO',
        'DZ',
        'EC',
        'EE',
        'EG',
        'ER',
        'ES',
        'ET',
        'FI',
        'FJ',
        'FK',
        'FM',
        'FO',
        'FR',
        'GA',
        'GB',
        'GD',
        'GE',
        'GF',
        'GG',
        'GH',
        'GI',
        'GL',
        'GM',
        'GN',
        'GP',
        'GQ',
        'GR',
        'GS',
        'GT',
        'GU',
        'GW',
        'GY',
        'HK',
        'HM',
        'HN',
        'HR',
        'HT',
        'HU',
        'ID',
        'IE',
        'IL',
        'IM',
        'IN',
        'IO',
        'IQ',
        'IR',
        'IS',
        'IT',
        'JE',
        'JM',
        'JO',
        'JP',
        'KE',
        'KG',
        'KH',
        'KI',
        'KM',
        'KN',
        'KP',
        'KR',
        'KW',
        'KY',
        'KZ',
        'LA',
        'LB',
        'LC',
        'LI',
        'LK',
        'LR',
        'LS',
        'LT',
        'LU',
        'LV',
        'LY',
        'MA',
        'MC',
        'MD',
        'ME',
        'MF',
        'MG',
        'MH',
        'MK',
        'ML',
        'MM',
        'MN',
        'MO',
        'MP',
        'MQ',
        'MR',
        'MS',
        'MT',
        'MU',
        'MV',
        'MW',
        'MX',
        'MY',
        'MZ',
        'NA',
        'NC',
        'NE',
        'NF',
        'NG',
        'NI',
        'NL',
        'NO',
        'NP',
        'NR',
        'NU',
        'NZ',
        'OM',
        'PA',
        'PE',
        'PF',
        'PG',
        'PH',
        'PK',
        'PL',
        'PM',
        'PN',
        'PR',
        'PS',
        'PT',
        'PW',
        'PY',
        'QA',
        'RE',
        'RO',
        'RS',
        'RU',
        'RW',
        'SA',
        'SB',
        'SC',
        'SD',
        'SE',
        'SG',
        'SH',
        'SI',
        'SJ',
        'SK',
        'SL',
        'SM',
        'SN',
        'SO',
        'SR',
        'SS',
        'ST',
        'SV',
        'SX',
        'SY',
        'SZ',
        'TC',
        'TD',
        'TF',
        'TG',
        'TH',
        'TJ',
        'TK',
        'TL',
        'TM',
        'TN',
        'TO',
        'TR',
        'TT',
        'TV',
        'TW',
        'TZ',
        'UA',
        'UG',
        'UM',
        'US',
        'UY',
        'UZ',
        'VA',
        'VC',
        'VE',
        'VG',
        'VI',
        'VN',
        'VU',
        'WF',
        'WS',
        'YE',
        'YT',
        'ZA',
        'ZM',
        'ZW'
    ]
    alpha2ToAlpha3 = {'AD': 'AND',
                      'AE': 'ARE',
                      'AF': 'AFG',
                      'AG': 'ATG',
                      'AI': 'AIA',
                      'AL': 'ALB',
                      'AM': 'ARM',
                      'AO': 'AGO',
                      'AR': 'ARG',
                      'AS': 'ASM',
                      'AT': 'AUT',
                      'AU': 'AUS',
                      'AW': 'ABW',
                      'AX': 'ALA',
                      'AZ': 'AZE',
                      'BA': 'BIH',
                      'BB': 'BRB',
                      'BD': 'BGD',
                      'BE': 'BEL',
                      'BF': 'BFA',
                      'BG': 'BGR',
                      'BH': 'BHR',
                      'BI': 'BDI',
                      'BJ': 'BEN',
                      'BL': 'BLM',
                      'BM': 'BMU',
                      'BN': 'BRN',
                      'BO': 'BOL',
                      'BQ': 'BES',
                      'BR': 'BRA',
                      'BS': 'BHS',
                      'BT': 'BTN',
                      'BW': 'BWA',
                      'BY': 'BLR',
                      'BZ': 'BLZ',
                      'CA': 'CAN',
                      'CC': 'CCK',
                      'CD': 'COD',
                      'CF': 'CAF',
                      'CG': 'COG',
                      'CH': 'CHE',
                      'CI': 'CIV',
                      'CK': 'COK',
                      'CL': 'CHL',
                      'CM': 'CMR',
                      'CN': 'CHN',
                      'CO': 'COL',
                      'CR': 'CRI',
                      'CU': 'CUB',
                      'CV': 'CPV',
                      'CW': 'CUW',
                      'CX': 'CXR',
                      'CY': 'CYP',
                      'CZ': 'CZE',
                      'DE': 'DEU',
                      'DJ': 'DJI',
                      'DK': 'DNK',
                      'DM': 'DMA',
                      'DO': 'DOM',
                      'DZ': 'DZA',
                      'EC': 'ECU',
                      'EE': 'EST',
                      'EG': 'EGY',
                      'ER': 'ERI',
                      'ES': 'ESP',
                      'ET': 'ETH',
                      'FI': 'FIN',
                      'FJ': 'FJI',
                      'FK': 'FLK',
                      'FM': 'FSM',
                      'FO': 'FRO',
                      'FR': 'FRA',
                      'GA': 'GAB',
                      'GB': 'GBR',
                      'GD': 'GRD',
                      'GE': 'GEO',
                      'GF': 'GUF',
                      'GG': 'GGY',
                      'GH': 'GHA',
                      'GI': 'GIB',
                      'GL': 'GRL',
                      'GM': 'GMB',
                      'GN': 'GIN',
                      'GP': 'GLP',
                      'GQ': 'GNQ',
                      'GR': 'GRC',
                      'GS': 'SGS',
                      'GT': 'GTM',
                      'GU': 'GUM',
                      'GW': 'GNB',
                      'GY': 'GUY',
                      'HK': 'HKG',
                      'HM': 'HMD',
                      'HN': 'HND',
                      'HR': 'HRV',
                      'HT': 'HTI',
                      'HU': 'HUN',
                      'ID': 'IDN',
                      'IE': 'IRL',
                      'IL': 'ISR',
                      'IM': 'IMN',
                      'IN': 'IND',
                      'IO': 'IOT',
                      'IQ': 'IRQ',
                      'IR': 'IRN',
                      'IS': 'ISL',
                      'IT': 'ITA',
                      'JE': 'JEY',
                      'JM': 'JAM',
                      'JO': 'JOR',
                      'JP': 'JPN',
                      'KE': 'KEN',
                      'KG': 'KGZ',
                      'KH': 'KHM',
                      'KI': 'KIR',
                      'KM': 'COM',
                      'KN': 'KNA',
                      'KP': 'PRK',
                      'KR': 'KOR',
                      'KW': 'KWT',
                      'KY': 'CYM',
                      'KZ': 'KAZ',
                      'LA': 'LAO',
                      'LB': 'LBN',
                      'LC': 'LCA',
                      'LI': 'LIE',
                      'LK': 'LKA',
                      'LR': 'LBR',
                      'LS': 'LSO',
                      'LT': 'LTU',
                      'LU': 'LUX',
                      'LV': 'LVA',
                      'LY': 'LBY',
                      'MA': 'MAR',
                      'MC': 'MCO',
                      'MD': 'MDA',
                      'ME': 'MNE',
                      'MF': 'MAF',
                      'MG': 'MDG',
                      'MH': 'MHL',
                      'MK': 'MKD',
                      'ML': 'MLI',
                      'MM': 'MMR',
                      'MN': 'MNG',
                      'MO': 'MAC',
                      'MP': 'MNP',
                      'MQ': 'MTQ',
                      'MR': 'MRT',
                      'MS': 'MSR',
                      'MT': 'MLT',
                      'MU': 'MUS',
                      'MV': 'MDV',
                      'MW': 'MWI',
                      'MX': 'MEX',
                      'MY': 'MYS',
                      'MZ': 'MOZ',
                      'NA': 'NAM',
                      'NC': 'NCL',
                      'NE': 'NER',
                      'NF': 'NFK',
                      'NG': 'NGA',
                      'NI': 'NIC',
                      'NL': 'NLD',
                      'NO': 'NOR',
                      'NP': 'NPL',
                      'NR': 'NRU',
                      'NU': 'NIU',
                      'NZ': 'NZL',
                      'OM': 'OMN',
                      'PA': 'PAN',
                      'PE': 'PER',
                      'PF': 'PYF',
                      'PG': 'PNG',
                      'PH': 'PHL',
                      'PK': 'PAK',
                      'PL': 'POL',
                      'PM': 'SPM',
                      'PN': 'PCN',
                      'PR': 'PRI',
                      'PS': 'PSE',
                      'PT': 'PRT',
                      'PW': 'PLW',
                      'PY': 'PRY',
                      'QA': 'QAT',
                      'RE': 'REU',
                      'RO': 'ROU',
                      'RS': 'SRB',
                      'RU': 'RUS',
                      'RW': 'RWA',
                      'SA': 'SAU',
                      'SB': 'SLB',
                      'SC': 'SYC',
                      'SD': 'SDN',
                      'SE': 'SWE',
                      'SG': 'SGP',
                      'SH': 'SHN',
                      'SI': 'SVN',
                      'SJ': 'SJM',
                      'SK': 'SVK',
                      'SL': 'SLE',
                      'SM': 'SMR',
                      'SN': 'SEN',
                      'SO': 'SOM',
                      'SR': 'SUR',
                      'SS': 'SSD',
                      'ST': 'STP',
                      'SV': 'SLV',
                      'SX': 'SXM',
                      'SY': 'SYR',
                      'SZ': 'SWZ',
                      'TC': 'TCA',
                      'TD': 'TCD',
                      'TF': 'ATF',
                      'TG': 'TGO',
                      'TH': 'THA',
                      'TJ': 'TJK',
                      'TK': 'TKL',
                      'TL': 'TLS',
                      'TM': 'TKM',
                      'TN': 'TUN',
                      'TO': 'TON',
                      'TR': 'TUR',
                      'TT': 'TTO',
                      'TV': 'TUV',
                      'TW': 'TWN',
                      'TZ': 'TZA',
                      'UA': 'UKR',
                      'UG': 'UGA',
                      'UM': 'UMI',
                      'US': 'USA',
                      'UY': 'URY',
                      'UZ': 'UZB',
                      'VA': 'VAT',
                      'VC': 'VCT',
                      'VE': 'VEN',
                      'VG': 'VGB',
                      'VI': 'VIR',
                      'VN': 'VNM',
                      'VU': 'VUT',
                      'WF': 'WLF',
                      'WS': 'WSM',
                      'YE': 'YEM',
                      'YT': 'MYT',
                      'ZA': 'ZAF',
                      'ZM': 'ZMB',
                      'ZW': 'ZWE'
                      }
    alpha3List = [
        "ABW",
        "AFG",
        "AGO",
        "AIA",
        "ALA",
        "ALB",
        "AND",
        "ARE",
        "ARG",
        "ARM",
        "ASM",
        "ATF",
        "ATG",
        "AUS",
        "AUT",
        "AZE",
        "BDI",
        "BEL",
        "BEN",
        "BES",
        "BFA",
        "BGD",
        "BGR",
        "BHR",
        "BHS",
        "BIH",
        "BLM",
        "BLR",
        "BLZ",
        "BMU",
        "BOL",
        "BRA",
        "BRB",
        "BRN",
        "BTN",
        "BWA",
        "CAF",
        "CAN",
        "CCK",
        "CHE",
        "CHL",
        "CHN",
        "CIV",
        "CMR",
        "COD",
        "COG",
        "COK",
        "COL",
        "COM",
        "CPV",
        "CRI",
        "CUB",
        "CUW",
        "CXR",
        "CYM",
        "CYP",
        "CZE",
        "DEU",
        "DJI",
        "DMA",
        "DNK",
        "DOM",
        "DZA",
        "ECU",
        "EGY",
        "ERI",
        "ESP",
        "EST",
        "ETH",
        "FIN",
        "FJI",
        "FLK",
        "FRA",
        "FRO",
        "FSM",
        "GAB",
        "GBR",
        "GEO",
        "GGY",
        "GHA",
        "GIB",
        "GIN",
        "GLP",
        "GMB",
        "GNB",
        "GNQ",
        "GRC",
        "GRD",
        "GRL",
        "GTM",
        "GUF",
        "GUM",
        "GUY",
        "HKG",
        "HMD",
        "HND",
        "HRV",
        "HTI",
        "HUN",
        "IDN",
        "IMN",
        "IND",
        "IOT",
        "IRL",
        "IRN",
        "IRQ",
        "ISL",
        "ISR",
        "ITA",
        "JAM",
        "JEY",
        "JOR",
        "JPN",
        "KAZ",
        "KEN",
        "KGZ",
        "KHM",
        "KIR",
        "KNA",
        "KOR",
        "KWT",
        "LAO",
        "LBN",
        "LBR",
        "LBY",
        "LCA",
        "LIE",
        "LKA",
        "LSO",
        "LTU",
        "LUX",
        "LVA",
        "MAC",
        "MAF",
        "MAR",
        "MCO",
        "MDA",
        "MDG",
        "MDV",
        "MEX",
        "MHL",
        "MKD",
        "MLI",
        "MLT",
        "MMR",
        "MNE",
        "MNG",
        "MNP",
        "MOZ",
        "MRT",
        "MSR",
        "MTQ",
        "MUS",
        "MWI",
        "MYS",
        "MYT",
        "NAM",
        "NCL",
        "NER",
        "NFK",
        "NGA",
        "NIC",
        "NIU",
        "NLD",
        "NOR",
        "NPL",
        "NRU",
        "NZL",
        "OMN",
        "PAK",
        "PAN",
        "PCN",
        "PER",
        "PHL",
        "PLW",
        "PNG",
        "POL",
        "PRI",
        "PRK",
        "PRT",
        "PRY",
        "PSE",
        "PYF",
        "QAT",
        "REU",
        "ROU",
        "RUS",
        "RWA",
        "SAU",
        "SDN",
        "SEN",
        "SGP",
        "SGS",
        "SHN",
        "SJM",
        "SLB",
        "SLE",
        "SLV",
        "SMR",
        "SOM",
        "SPM",
        "SRB",
        "SSD",
        "STP",
        "SUR",
        "SVK",
        "SVN",
        "SWE",
        "SWZ",
        "SXM",
        "SYC",
        "SYR",
        "TCA",
        "TCD",
        "TGO",
        "THA",
        "TJK",
        "TKL",
        "TKM",
        "TLS",
        "TON",
        "TTO",
        "TUN",
        "TUR",
        "TUV",
        "TWN",
        "TZA",
        "UGA",
        "UKR",
        "UMI",
        "URY",
        "USA",
        "UZB",
        "VAT",
        "VCT",
        "VEN",
        "VGB",
        "VIR",
        "VNM",
        "VUT",
        "WLF",
        "WSM",
        "YEM",
        "ZAF",
        "ZMB",
        "ZWE"
    ]
    alpha3ToAlpha2 = {'ABW': 'AW',
                      'AFG': 'AF',
                      'AGO': 'AO',
                      'AIA': 'AI',
                      'ALA': 'AX',
                      'ALB': 'AL',
                      'AND': 'AD',
                      'ARE': 'AE',
                      'ARG': 'AR',
                      'ARM': 'AM',
                      'ASM': 'AS',
                      'ATF': 'TF',
                      'ATG': 'AG',
                      'AUS': 'AU',
                      'AUT': 'AT',
                      'AZE': 'AZ',
                      'BDI': 'BI',
                      'BEL': 'BE',
                      'BEN': 'BJ',
                      'BES': 'BQ',
                      'BFA': 'BF',
                      'BGD': 'BD',
                      'BGR': 'BG',
                      'BHR': 'BH',
                      'BHS': 'BS',
                      'BIH': 'BA',
                      'BLM': 'BL',
                      'BLR': 'BY',
                      'BLZ': 'BZ',
                      'BMU': 'BM',
                      'BOL': 'BO',
                      'BRA': 'BR',
                      'BRB': 'BB',
                      'BRN': 'BN',
                      'BTN': 'BT',
                      'BWA': 'BW',
                      'CAF': 'CF',
                      'CAN': 'CA',
                      'CCK': 'CC',
                      'CHE': 'CH',
                      'CHL': 'CL',
                      'CHN': 'CN',
                      'CIV': 'CI',
                      'CMR': 'CM',
                      'COD': 'CD',
                      'COG': 'CG',
                      'COK': 'CK',
                      'COL': 'CO',
                      'COM': 'KM',
                      'CPV': 'CV',
                      'CRI': 'CR',
                      'CUB': 'CU',
                      'CUW': 'CW',
                      'CXR': 'CX',
                      'CYM': 'KY',
                      'CYP': 'CY',
                      'CZE': 'CZ',
                      'DEU': 'DE',
                      'DJI': 'DJ',
                      'DMA': 'DM',
                      'DNK': 'DK',
                      'DOM': 'DO',
                      'DZA': 'DZ',
                      'ECU': 'EC',
                      'EGY': 'EG',
                      'ERI': 'ER',
                      'ESP': 'ES',
                      'EST': 'EE',
                      'ETH': 'ET',
                      'FIN': 'FI',
                      'FJI': 'FJ',
                      'FLK': 'FK',
                      'FRA': 'FR',
                      'FRO': 'FO',
                      'FSM': 'FM',
                      'GAB': 'GA',
                      'GBR': 'GB',
                      'GEO': 'GE',
                      'GGY': 'GG',
                      'GHA': 'GH',
                      'GIB': 'GI',
                      'GIN': 'GN',
                      'GLP': 'GP',
                      'GMB': 'GM',
                      'GNB': 'GW',
                      'GNQ': 'GQ',
                      'GRC': 'GR',
                      'GRD': 'GD',
                      'GRL': 'GL',
                      'GTM': 'GT',
                      'GUF': 'GF',
                      'GUM': 'GU',
                      'GUY': 'GY',
                      'HKG': 'HK',
                      'HMD': 'HM',
                      'HND': 'HN',
                      'HRV': 'HR',
                      'HTI': 'HT',
                      'HUN': 'HU',
                      'IDN': 'ID',
                      'IMN': 'IM',
                      'IND': 'IN',
                      'IOT': 'IO',
                      'IRL': 'IE',
                      'IRN': 'IR',
                      'IRQ': 'IQ',
                      'ISL': 'IS',
                      'ISR': 'IL',
                      'ITA': 'IT',
                      'JAM': 'JM',
                      'JEY': 'JE',
                      'JOR': 'JO',
                      'JPN': 'JP',
                      'KAZ': 'KZ',
                      'KEN': 'KE',
                      'KGZ': 'KG',
                      'KHM': 'KH',
                      'KIR': 'KI',
                      'KNA': 'KN',
                      'KOR': 'KR',
                      'KWT': 'KW',
                      'LAO': 'LA',
                      'LBN': 'LB',
                      'LBR': 'LR',
                      'LBY': 'LY',
                      'LCA': 'LC',
                      'LIE': 'LI',
                      'LKA': 'LK',
                      'LSO': 'LS',
                      'LTU': 'LT',
                      'LUX': 'LU',
                      'LVA': 'LV',
                      'MAC': 'MO',
                      'MAF': 'MF',
                      'MAR': 'MA',
                      'MCO': 'MC',
                      'MDA': 'MD',
                      'MDG': 'MG',
                      'MDV': 'MV',
                      'MEX': 'MX',
                      'MHL': 'MH',
                      'MKD': 'MK',
                      'MLI': 'ML',
                      'MLT': 'MT',
                      'MMR': 'MM',
                      'MNE': 'ME',
                      'MNG': 'MN',
                      'MNP': 'MP',
                      'MOZ': 'MZ',
                      'MRT': 'MR',
                      'MSR': 'MS',
                      'MTQ': 'MQ',
                      'MUS': 'MU',
                      'MWI': 'MW',
                      'MYS': 'MY',
                      'MYT': 'YT',
                      'NAM': 'NA',
                      'NCL': 'NC',
                      'NER': 'NE',
                      'NFK': 'NF',
                      'NGA': 'NG',
                      'NIC': 'NI',
                      'NIU': 'NU',
                      'NLD': 'NL',
                      'NOR': 'NO',
                      'NPL': 'NP',
                      'NRU': 'NR',
                      'NZL': 'NZ',
                      'OMN': 'OM',
                      'PAK': 'PK',
                      'PAN': 'PA',
                      'PCN': 'PN',
                      'PER': 'PE',
                      'PHL': 'PH',
                      'PLW': 'PW',
                      'PNG': 'PG',
                      'POL': 'PL',
                      'PRI': 'PR',
                      'PRK': 'KP',
                      'PRT': 'PT',
                      'PRY': 'PY',
                      'PSE': 'PS',
                      'PYF': 'PF',
                      'QAT': 'QA',
                      'REU': 'RE',
                      'ROU': 'RO',
                      'RUS': 'RU',
                      'RWA': 'RW',
                      'SAU': 'SA',
                      'SDN': 'SD',
                      'SEN': 'SN',
                      'SGP': 'SG',
                      'SGS': 'GS',
                      'SHN': 'SH',
                      'SJM': 'SJ',
                      'SLB': 'SB',
                      'SLE': 'SL',
                      'SLV': 'SV',
                      'SMR': 'SM',
                      'SOM': 'SO',
                      'SPM': 'PM',
                      'SRB': 'RS',
                      'SSD': 'SS',
                      'STP': 'ST',
                      'SUR': 'SR',
                      'SVK': 'SK',
                      'SVN': 'SI',
                      'SWE': 'SE',
                      'SWZ': 'SZ',
                      'SXM': 'SX',
                      'SYC': 'SC',
                      'SYR': 'SY',
                      'TCA': 'TC',
                      'TCD': 'TD',
                      'TGO': 'TG',
                      'THA': 'TH',
                      'TJK': 'TJ',
                      'TKL': 'TK',
                      'TKM': 'TM',
                      'TLS': 'TL',
                      'TON': 'TO',
                      'TTO': 'TT',
                      'TUN': 'TN',
                      'TUR': 'TR',
                      'TUV': 'TV',
                      'TWN': 'TW',
                      'TZA': 'TZ',
                      'UGA': 'UG',
                      'UKR': 'UA',
                      'UMI': 'UM',
                      'URY': 'UY',
                      'USA': 'US',
                      'UZB': 'UZ',
                      'VAT': 'VA',
                      'VCT': 'VC',
                      'VEN': 'VE',
                      'VGB': 'VG',
                      'VIR': 'VI',
                      'VNM': 'VN',
                      'VUT': 'VU',
                      'WLF': 'WF',
                      'WSM': 'WS',
                      'YEM': 'YE',
                      'ZAF': 'ZA',
                      'ZMB': 'ZM',
                      'ZWE': 'ZW'
                      }
    alpha3ToAreaKMm = {
        "ABW": 193,
        "AFG": 652230,
        "AGO": 1246700,
        "AIA": 91,
        "ALA": 1580,
        "ALB": 27398,
        "AND": 468,
        "ARE": 83600,
        "ARG": 2736690,
        "ARM": 28342,
        "ASM": 200,
        "ATG": 442,
        "AUS": 7633565,
        "AUT": 82445,
        "AZE": 86100,
        "BDI": 25680,
        "BEL": 30278,
        "BEN": 114305,
        "BES": 322,
        "BFA": 273602,
        "BGD": 130168,
        "BGR": 108612,
        "BHR": 778,
        "BHS": 10010,
        "BIH": 51187,
        "BLM": 25,
        "BLR": 202900,
        "BLZ": 22806,
        "BMU": 53,
        "BOL": 1083301,
        "BRA": 8460415,
        "BRB": 431,
        "BRN": 5265,
        "BTN": 38394,
        "BWA": 566730,
        "CAF": 622984,
        "CAN": 9093507,
        "CPV": 4033,
        "CHE": 39997,
        "CHL": 743812,
        "CHN": 9326410,
        "CIV": 318003,
        "CMR": 472710,
        "CCK": 14,
        "COD": 2267048,
        "COK": 237,
        "COL": 1038700,
        "COM": 1862,
        "CRI": 51060,
        "CUB": 109884,
        "CUW": 444,
        "CXR": 135,
        "CYM": 264,
        "CYP": 9241,
        "CZE": 77247,
        "DEU": 348672,
        "DJI": 23180,
        "DMA": 751,
        "DNK": 42434,
        "DOM": 48320,
        "DZA": 2381741,
        "ECU": 256369,
        "EGY": 995450,
        "ERI": 101000,
        "ESP": 498980,
        "EST": 42388,
        "SWZ": 17204,
        "ETH": 1000000,
        "FIN": 303815,
        "FJI": 18274,
        "FLK": 12173,
        "FRA": 543940,
        "ATF": 11249,
        "FRO": 1399,
        "FSM": 702,
        "GAB": 257667,
        "GBR": 242495,
        "GEO": 69700,
        "GGY": 65,
        "GHA": 227533,
        "GIB": 7,
        "GIN": 245717,
        "GMB": 10000,
        "GNQ": 28051,
        "GRC": 130647,
        "GRD": 344,
        "GRL": 2166086,
        "GTM": 107159,
        "GLP": 1628,
        "GUF": 83534,
        "GNB": 28120,
        "GUM": 540,
        "GUY": 196849,
        "HKG": 1106,
        "HMD": 368,
        "HND": 111890,
        "HRV": 55974,
        "HTI": 27560,
        "HUN": 89608,
        "IDN": 1811569,
        "IMN": 572,
        "IND": 2973190,
        "IOT": 54400,
        "IRL": 68883,
        "IRN": 1531595,
        "IRQ": 437367,
        "ISL": 100250,
        "ISR": 20330,
        "ITA": 294140,
        "JAM": 10831,
        "JEY": 118,
        "JOR": 88802,
        "JPN": 364546,
        "KAZ": 2699700,
        "KEN": 569140,
        "KGZ": 191801,
        "KHM": 176515,
        "KIR": 811,
        "KNA": 261,
        "KOR": 99909,
        "XKX": 10887,
        "KWT": 17818,
        "LAO": 230800,
        "LBN": 10230,
        "LBR": 96320,
        "LBY": 1759540,
        "LCA": 606,
        "LIE": 160,
        "LKA": 62732,
        "LSO": 30355,
        "LTU": 62680,
        "LUX": 2586,
        "LVA": 62249,
        "MAC": 115,
        "MAF": 25,
        "MAR": 446300,
        "MCO": 2,
        "MDA": 32891,
        "MDG": 581540,
        "MDV": 298,
        "MEX": 1943945,
        "MHL": 181,
        "MLI": 1220190,
        "MLT": 316,
        "MMR": 653508,
        "MNE": 13452,
        "MNG": 1553556,
        "MNP": 464,
        "MOZ": 786380,
        "MRT": 1025520,
        "MSR": 102,
        "MTQ": 1128,
        "MUS": 2030,
        "MWI": 94080,
        "MYS": 329613,
        "MYT": 374,
        "NAM": 823290,
        "NCL": 18576,
        "NER": 1266700,
        "NFK": 35,
        "NGA": 910768,
        "NIC": 119990,
        "NIU": 261,
        "NLD": 33893,
        "NOR": 365957,
        "MKD": 25433,
        "NPL": 143351,
        "NRU": 21,
        "NZL": 262443,
        "OMN": 309500,
        "PAK": 882623,
        "PAN": 74340,
        "PER": 1279996,
        "PHL": 298170,
        "PCN": 47,
        "PLW": 459,
        "PNG": 452860,
        "POL": 311888,
        "PRI": 9104,
        "PRK": 120538,
        "PRT": 91119,
        "PRY": 397302,
        "PSE": 6000,
        "PYF": 4167,
        "QAT": 11856,
        "COG": 342000,
        "REU": 2511,
        "ROU": 231291,
        "RUS": 16377742,
        "RWA": 24668,
        "SAU": 2149690,
        "SDN": 1731671,
        "SEN": 192530,
        "SGP": 716,
        "SGS": 3903,
        "SJM": 61022,
        "SLB": 27986,
        "SLE": 71620,
        "SLV": 20721,
        "SMR": 61,
        "SOM": 627337,
        "SPM": 242,
        "SRB": 88246,
        "SSD": 644329,
        "STP": 964,
        "SHN": 121,
        "SUR": 156000,
        "SVK": 48105,
        "SVN": 20151,
        "SWE": 410335,
        "SXM": 34,
        "SYC": 455,
        "SYR": 183630,
        "TCD": 1259200,
        "TGO": 54385,
        "THA": 510890,
        "TLS": 15007,
        "TJK": 141510,
        "TKL": 10,
        "TKM": 469930,
        "TON": 717,
        "TTO": 5128,
        "TUN": 155360,
        "TUR": 769632,
        "TCA": 616,
        "TUV": 26,
        "TWN": 32260,
        "TZA": 885800,
        "UGA": 197100,
        "UKR": 579300,
        "UMI": 34,
        "URY": 175015,
        "USA": 9147593,
        "UZB": 425400,
        "VAT": 1,
        "VCT": 389,
        "VEN": 882050,
        "VGB": 153,
        "VIR": 346,
        "VNM": 310070,
        "VUT": 12189,
        "WLF": 142,
        "WSM": 2821,
        "YEM": 527968,
        "ZAF": 1214470,
        "ZMB": 743398,
        "ZWE": 386847
    }
    alpha3ToCapital = {
        "ABW": "Oranjestad",
        "AFG": "Kabul",
        "AGO": "Luanda",
        "AIA": "The Valley",
        "ALA": "Mariehamn",
        "ALB": "Tirana",
        "AND": "Andorra la Vella",
        "ARE": "Abu Dhabi",
        "ARG": "Buenos Aires",
        "ARM": "Yerevan",
        "ASM": "Pago Pago",
        "ATF": "Port-aux-Français",
        "ATG": "Saint John's",
        "AUS": "Canberra",
        "AUT": "Vienna",
        "AZE": "Baku",
        "BDI": "Bujumbura",
        "BEL": "Brussels",
        "BEN": "Porto-Novo",
        "BES": "Kralendijk",
        "BFA": "Ouagadougou",
        "BGD": "Dhaka",
        "BGR": "Sofia",
        "BHR": "Manama",
        "BHS": "Nassau",
        "BIH": "Sarajevo",
        "BLM": "Gustavia",
        "BLR": "Minsk",
        "BLZ": "Belmopan",
        "BMU": "Hamilton",
        "BOL": "Sucre",
        "BRA": "Brasília",
        "BRB": "Bridgetown",
        "BRN": "Bandar Seri Begawan",
        "BTN": "Thimphu",
        "BVT": None,
        "BWA": "Gaborone",
        "CAF": "Bangui",
        "CAN": "Ottawa",
        "CCK": "West Island",
        "CHE": "Bern",
        "CHL": "Santiago",
        "CHN": "Beijing",
        "CIV": "Yamoussoukro",
        "CMR": "Yaoundé",
        "COD": "Kinshasa",
        "COG": "Brazzaville",
        "COK": "Avarua",
        "COL": "Bogotá",
        "COM": "Moroni",
        "CPV": "Praia",
        "CRI": "San José",
        "CUB": "Havana",
        "CUW": "Willemstad",
        "CXR": "Flying Fish Cove",
        "CYM": "George Town",
        "CYP": "Nicosia",
        "CZE": "Prague",
        "DEU": "Berlin",
        "DJI": "Djibouti",
        "DMA": "Roseau",
        "DNK": "Copenhagen",
        "DOM": "Santo Domingo",
        "DZA": "Algiers",
        "ECU": "Quito",
        "EGY": "Cairo",
        "ERI": "Asmara",
        "ESH": "El Aaiún",
        "ESP": "Madrid",
        "EST": "Tallinn",
        "ETH": "Addis Ababa",
        "FIN": "Helsinki",
        "FJI": "Suva",
        "FLK": "Stanley",
        "FRA": "Paris",
        "FRO": "Tórshavn",
        "FSM": "Palikir",
        "GAB": "Libreville",
        "GBR": "London",
        "GEO": "Tbilisi",
        "GGY": "St. Peter Port",
        "GHA": "Accra",
        "GIB": "Gibraltar",
        "GIN": "Malabo",
        "GLP": "Basse-Terre",
        "GMB": "Banjul",
        "GNB": "Bissau",
        "GNQ": "Malabo",
        "GRC": "Athens",
        "GRD": "St. George's",
        "GRL": "Nuuk",
        "GTM": "Guatemala City",
        "GUF": "Cayenne",
        "GUM": "Hagåtña",
        "GUY": "Georgetown",
        "HKG": "City of Victoria",
        "HMD": None,
        "HND": "Tegucigalpa",
        "HRV": "Zagreb",
        "HTI": "Port-au-Prince",
        "HUN": "Budapest",
        "IDN": "Jakarta",
        "IMN": "Douglas",
        "IND": "New Delhi",
        "IOT": "Diego Garcia",
        "IRL": "Dublin",
        "IRN": "Tehran",
        "IRQ": "Baghdad",
        "ISL": "Reykjavík",
        "ISR": "Jerusalem (Disputed)",
        "ITA": "Rome",
        "JAM": "Kingston",
        "JEY": "Saint Helier",
        "JOR": "Amman",
        "JPN": "Tokyo",
        "KAZ": "Astana",
        "KEN": "Nairobi",
        "KGZ": "Bishkek",
        "KHM": "Phnom Penh",
        "KIR": "South Tarawa",
        "KNA": "Basseterre",
        "KOR": "Seoul",
        "KWT": "Kuwait City",
        "LAO": "Vientiane",
        "LBN": "Beirut",
        "LBR": "Monrovia",
        "LBY": "Tripoli",
        "LCA": "Castries",
        "LIE": "Vaduz",
        "LKA": "Colombo",
        "LSO": "Maseru",
        "LTU": "Vilnius",
        "LUX": "Luxembourg City",
        "LVA": "Riga",
        "MAC": "Macao",
        "MAF": "Marigot",
        "MAR": "Rabat",
        "MCO": "Monte Carlo",
        "MDA": "Chișinău",
        "MDG": "Antananarivo",
        "MDV": "Malé",
        "MEX": "Mexico City",
        "MHL": "Majuro",
        "MKD": "Skopje",
        "MLI": "Bamako",
        "MLT": "Valletta",
        "MMR": "Naypyidaw",
        "MNE": "Podgorica",
        "MNG": "Ulaanbaatar",
        "MNP": "Saipan",
        "MOZ": "Maputo",
        "MRT": "Nouakchott",
        "MSR": "Plymouth",
        "MTQ": "Fort-de-France",
        "MUS": "Port Louis",
        "MWI": "Lilongwe",
        "MYS": "Kuala Lumpur",
        "MYT": "Mamoudzou",
        "NAM": "Windhoek",
        "NCL": "Nouméa",
        "NER": "Niamey",
        "NFK": "Kingston",
        "NGA": "Abuja",
        "NIC": "Managua",
        "NIU": "Alofi",
        "NLD": "Amsterdam",
        "NOR": "Oslo",
        "NPL": "Kathmandu",
        "NRU": "Yaren",
        "NZL": "Wellington",
        "OMN": "Muscat",
        "PAK": "Islamabad",
        "PAN": "Panama City",
        "PCN": "Adamstown",
        "PER": "Lima",
        "PHL": "Manila",
        "PLW": "Ngerulmud",
        "PNG": "Port Moresby",
        "POL": "Warsaw",
        "PRI": "San Juan",
        "PRK": "Pyongyang",
        "PRT": "Lisbon",
        "PRY": "Asunción",
        "PSE": "Jerusalem (Disputed)",
        "PYF": "Papeetē",
        "QAT": "Doha",
        "REU": "Saint-Denis",
        "ROU": "Bucharest",
        "RUS": "Moscow",
        "RWA": "Kigali",
        "SAU": "Riyadh",
        "SDN": "Juba",
        "SEN": "Dakar",
        "SGP": "Singapore",
        "SGS": "King Edward Point",
        "SHN": "Jamestown",
        "SJM": "Longyearbyen",
        "SLB": "Honiara",
        "SLE": "Freetown",
        "SLV": "San Salvador",
        "SMR": "City of San Marino",
        "SOM": "Mogadishu",
        "SPM": "Saint-Pierre",
        "SRB": "Belgrade",
        "SSD": "Juba",
        "STP": "São Tomé",
        "SUR": "Paramaribo",
        "SVK": "Bratislava",
        "SVN": "Ljubljana",
        "SWE": "Stockholm",
        "SWZ": "Lobamba",
        "SXM": "Philipsburg",
        "SYC": "Victoria",
        "SYR": "Damascus",
        "TCA": "Cockburn Town",
        "TCD": "N'Djamena",
        "TGO": "Lomé",
        "THA": "Bangkok",
        "TJK": "Dushanbe",
        "TKL": "Fakaofo",
        "TKM": "Ashgabat",
        "TLS": "Dili",
        "TON": "Nuku'alofa",
        "TTO": "Port of Spain",
        "TUN": "Tunis",
        "TUR": "Ankara",
        "TUV": "Funafuti",
        "TWN": "Taipei",
        "TZA": "Dodoma",
        "UGA": "Kampala",
        "UKR": "Kiev",
        "UMI": "Washington, D.C.",
        "URY": "Montevideo",
        "USA": "Washington, D.C.",
        "UZB": "Tashkent",
        "VAT": "Vatican City",
        "VCT": "Kingstown",
        "VEN": "Caracas",
        "VGB": "Road Town",
        "VIR": "Charlotte Amalie",
        "VNM": "Hanoi",
        "VUT": "Port Vila",
        "WLF": "Mata-Utu",
        "WSM": "Pago Pago",
        "YEM": "Sana'a",
        "ZAF": "Pretoria",
        "ZMB": "Lusaka",
        "ZWE": "Harare"
    }
    alpha3ToContinent = {
        "ABW": "SOUTH_AMERICA",
        "AFG": "ASIA",
        "AGO": "AFRICA",
        "AIA": "NORTH_AMERICA",
        "ALA": "EUROPE",
        "ALB": "EUROPE",
        "AND": "EUROPE",
        "ARE": "ASIA",
        "ARG": "SOUTH_AMERICA",
        "ARM": "ASIA",
        "ASM": "OCEANIA",
        "ATA": "ANTARCTICA",
        "ATF": "ANTARCTICA",
        "ATG": "NORTH_AMERICA",
        "AUS": "OCEANIA",
        "AUT": "EUROPE",
        "AZE": "ASIA",
        "BDI": "AFRICA",
        "BEL": "EUROPE",
        "BEN": "AFRICA",
        "BES": "NORTH_AMERICA",
        "BFA": "AFRICA",
        "BGD": "ASIA",
        "BGR": "EUROPE",
        "BHR": "ASIA",
        "BHS": "NORTH_AMERICA",
        "BIH": "EUROPE",
        "BLR": "EUROPE",
        "BLM": "NORTH_AMERICA",
        "BLZ": "NORTH_AMERICA",
        "BMU": "NORTH_AMERICA",
        "BOL": "SOUTH_AMERICA",
        "BRA": "SOUTH_AMERICA",
        "BRB": "NORTH_AMERICA",
        "BRN": "ASIA",
        "BTN": "ASIA",
        "BWA": "AFRICA",
        "CAF": "AFRICA",
        "CAN": "NORTH_AMERICA",
        "CCK": "VOID",
        "CHE": "EUROPE",
        "CHL": "SOUTH_AMERICA",
        "CHN": "ASIA",
        "CIV": "AFRICA",
        "CMR": "ASIA",
        "COD": "AFRICA",
        "COG": "AFRICA",
        "COK": "OCEANIA",
        "COL": "SOUTH_AMERICA",
        "COM": "AFRICA",
        "CPV": "AFRICA",
        "CRI": "NORTH_AMERICA",
        "CUB": "NORTH_AMERICA",
        "CUW": "SOUTH_AMERICA",
        "CXR": "OCEANIA",
        "CYM": "NORTH_AMERICA",
        "CYP": "ASIA",
        "CZE": "EUROPE",
        "DEU": "EUROPE",
        "DJI": "AFRICA",
        "DMA": "NORTH_AMERICA",
        "DNK": "EUROPE",
        "DOM": "NORTH_AMERICA",
        "DZA": "AFRICA",
        "ECU": "SOUTH_AMERICA",
        "EGY": "AFRICA",
        "ERI": "AFRICA",
        "ESP": "EUROPE",
        "EST": "EUROPE",
        "ETH": "AFRICA",
        "FIN": "EUROPE",
        "FJI": "OCEANIA",
        "FLK": "SOUTH_AMERICA",
        "FRA": "EUROPE",
        "FRO": "EUROPE",
        "FSM": "OCEANIA",
        "GAB": "AFRICA",
        "GBR": "EUROPE",
        "GEO": "ASIA",
        "GGY": "EUROPE",
        "GIN": "AFRICA",
        "GHA": "AFRICA",
        "GIB": "EUROPE",
        "GLP": "NORTH_AMERICA",
        "GMB": "AFRICA",
        "GNB": "AFRICA",
        "GNQ": "AFRICA",
        "GRC": "EUROPE",
        "GRD": "NORTH_AMERICA",
        "GRL": "NORTH_AMERICA",
        "GTM": "NORTH_AMERICA",
        "GUF": "SOUTH_AMERICA",
        "GUM": "OCEANIA",
        "GUY": "SOUTH_AMERICA",
        "HKG": "ASIA",
        "HMD": "ANTARCTICA",
        "HND": "NORTH_AMERICA",
        "HRV": "EUROPE",
        "HTI": "NORTH_AMERICA",
        "HUN": "EUROPE",
        "IDN": "OCEANIA",
        "IMN": "EUROPE",
        "IND": "ASIA",
        "IOT": "ASIA",
        "IRL": "EUROPE",
        "IRN": "ASIA",
        "IRQ": "ASIA",
        "ISL": "EUROPE",
        "ISR": "ASIA",
        "ITA": "EUROPE",
        "JAM": "NORTH_AMERICA",
        "JEY": "EUROPE",
        "JOR": "ASIA",
        "JPN": "ASIA",
        "KAZ": "ASIA",
        "KEN": "AFRICA",
        "KGZ": "ASIA",
        "KHM": "ASIA",
        "KIR": "OCEANIA",
        "KNA": "NORTH_AMERICA",
        "KOR": "VOID",
        "KOS": "EUROPE",
        "KWT": "ASIA",
        "LAO": "ASIA",
        "LBN": "ASIA",
        "LBR": "AFRICA",
        "LBY": "AFRICA",
        "LCA": "NORTH_AMERICA",
        "LIE": "EUROPE",
        "LKA": "ASIA",
        "LSO": "AFRICA",
        "LTU": "EUROPE",
        "LUX": "EUROPE",
        "LVA": "EUROPE",
        "MAC": "ASIA",
        "MAF": "NORTH_AMERICA",
        "MAR": "AFRICA",
        "MCO": "EUROPE",
        "MDA": "EUROPE",
        "MDG": "AFRICA",
        "MDV": "ASIA",
        "MEX": "NORTH_AMERICA",
        "MKD": "EUROPE",
        "MHL": "OCEANIA",
        "MLI": "AFRICA",
        "MLT": "EUROPE",
        "MMR": "ASIA",
        "MNE": "EUROPE",
        "MNG": "ASIA",
        "MNP": "OCEANIA",
        "MOZ": "AFRICA",
        "MRT": "AFRICA",
        "MSR": "NORTH_AMERICA",
        "MTQ": "NORTH_AMERICA",
        "MUS": "AFRICA",
        "MWI": "AFRICA",
        "MYS": "ASIA",
        "MYT": "AFRICA",
        "NAM": "AFRICA",
        "NCL": "OCEANIA",
        "NFK": "OCEANIA",
        "NER": "AFRICA",
        "NGA": "AFRICA",
        "NIC": "NORTH_AMERICA",
        "NIU": "OCEANIA",
        "NLD": "EUROPE",
        "NOR": "EUROPE",
        "NPL": "ASIA",
        "NRU": "OCEANIA",
        "NZL": "OCEANIA",
        "OMN": "ASIA",
        "PAK": "ASIA",
        "PAN": "NORTH_AMERICA",
        "PCN": "OCEANIA",
        "PER": "SOUTH_AMERICA",
        "PHL": "ASIA",
        "PLW": "OCEANIA",
        "PNG": "OCEANIA",
        "POL": "EUROPE",
        "PRI": "NORTH_AMERICA",
        "PRK": "ASIA",
        "PRT": "EUROPE",
        "PRY": "SOUTH_AMERICA",
        "PSE": "ASIA",
        "PYF": "OCEANIA",
        "QAT": "ASIA",
        "REU": "AFRICA",
        "ROU": "EUROPE",
        "RUS": "ASIA",
        "RWA": "AFRICA",
        "SAU": "ASIA",
        "SEN": "AFRICA",
        "SDN": "AFRICA",
        "SGP": "ASIA",
        "SGS": "ANTARCTICA",
        "SHN": "AFRICA",
        "SJM": "EUROPE",
        "SLB": "OCEANIA",
        "SLE": "AFRICA",
        "SLV": "NORTH_AMERICA",
        "SMR": "EUROPE",
        "SOM": "AFRICA",
        "SPM": "NORTH_AMERICA",
        "SRB": "EUROPE",
        "SSD": "AFRICA",
        "STP": "AFRICA",
        "SUR": "SOUTH_AMERICA",
        "SVK": "EUROPE",
        "SVN": "EUROPE",
        "SWE": "EUROPE",
        "SWZ": "AFRICA",
        "SXM": "NORTH_AMERICA",
        "SYC": "AFRICA",
        "SYR": "ASIA",
        "TCA": "NORTHERN_AMERICA",
        "TCD": "AFRICA",
        "TGO": "AFRICA",
        "THA": "ASIA",
        "TJK": "ASIA",
        "TKL": "OCEANIA",
        "TKM": "ASIA",
        "TLS": "OCEANIA",
        "TON": "OCEANIA",
        "TTO": "NORTH_AMERICA",
        "TUN": "AFRICA",
        "TUR": "EUROPE",
        "TUV": "OCEANIA",
        "TWN": "ASIA",
        "TZA": "AFRICA",
        "UGA": "AFRICA",
        "UKR": "EUROPE",
        "UMI": "OCEANIA",
        "URY": "SOUTH_AMERICA",
        "USA": "NORTH_AMERICA",
        "UZB": "ASIA",
        "VAT": "EUROPE",
        "VCT": "NORTH_AMERICA",
        "VEN": "SOUTH_AMERICA",
        "VGB": "NORTH_AMERICA",
        "VIR": "NORTH_AMERICA",
        "VNM": "ASIA",
        "VUT": "OCEANIA",
        "WLF": "OCEANIA",
        "WSM": "OCEANIA",
        "YEM": "ASIA",
        "ZAF": "AFRICA",
        "ZMB": "AFRICA",
        "ZWE": "AFRICA"
    }
    alpha3ToFlagURL = {
        "ABW": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag_of_Aruba.svg/1920px-Flag_of_Aruba.svg.png",
        "AFG": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_the_Taliban.svg/2560px-Flag_of_the_Taliban.svg.png",
        "AGO": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Angola.svg/1280px-Flag_of_Angola.svg.png",
        "AIA": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Anguilla.svg/2560px-Flag_of_Anguilla.svg.png",
        "ALA": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Flag_of_%C3%85land.svg/1920px-Flag_of_%C3%85land.svg.png",
        "ALB": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/1920px-Flag_of_Albania.svg.png",
        "AND": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Andorra.svg/1280px-Flag_of_Andorra.svg.png",
        "ARE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/1920px-Flag_of_the_United_Arab_Emirates.svg.png",
        "ARG": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/1280px-Flag_of_Argentina.svg.png",
        "ARM": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Flag_of_Armenia.svg/800px-Flag_of_Armenia.svg.png",
        "ASM": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag_of_American_Samoa.svg/2560px-Flag_of_American_Samoa.svg.png",
        "ATG": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag_of_Antigua_and_Barbuda.svg/1280px-Flag_of_Antigua_and_Barbuda.svg.png",
        "AUS": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia_%28converted%29.svg/800px-Flag_of_Australia_%28converted%29.svg.png",
        "AUT": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/800px-Flag_of_Austria.svg.png",
        "AZE": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Azerbaijan.svg/800px-Flag_of_Azerbaijan.svg.png",
        "BDI": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Burundi.svg/800px-Flag_of_Burundi.svg.png",
        "BEL": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Belgium.svg/800px-Flag_of_Belgium.svg.png",
        "BEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Benin.svg/800px-Flag_of_Benin.svg.png",
        "BES": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Flag_of_Bonaire.svg/1200px-Flag_of_Bonaire.svg.png",
        "BFA": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Burkina_Faso.svg/800px-Flag_of_Burkina_Faso.svg.png",
        "BGD": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/800px-Flag_of_Bangladesh.svg.png",
        "BGR": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Bulgaria.svg/800px-Flag_of_Bulgaria.svg.png",
        "BHR": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Bahrain.svg/800px-Flag_of_Bahrain.svg.png",
        "BHS": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_the_Bahamas.svg/800px-Flag_of_the_Bahamas.svg.png",
        "BIH": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag_of_Bosnia_and_Herzegovina.svg/800px-Flag_of_Bosnia_and_Herzegovina.svg.png",
        "BLM": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1920px-Flag_of_France.svg.png",
        "BLR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/800px-Flag_of_Belarus.svg.png",
        "BLZ": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Flag_of_Belize.svg/800px-Flag_of_Belize.svg.png",
        "BMU": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag_of_Bermuda.svg/2560px-Flag_of_Bermuda.svg.png",
        "BOL": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bandera_de_Bolivia_%28Estado%29.svg/800px-Bandera_de_Bolivia_%28Estado%29.svg.png",
        "BRA": "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/800px-Flag_of_Brazil.svg.png",
        "BRB": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Flag_of_Barbados.svg/800px-Flag_of_Barbados.svg.png",
        "BRN": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Brunei.svg/800px-Flag_of_Brunei.svg.png",
        "BTN": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flag_of_Bhutan.svg/800px-Flag_of_Bhutan.svg.png",
        "BWA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_Botswana.svg/800px-Flag_of_Botswana.svg.png",
        "CAE": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Central_African_Republic.svg/1024px-Flag_of_the_Central_African_Republic.svg.png",
        "CAF": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Central_African_Republic.svg/1024px-Flag_of_the_Central_African_Republic.svg.png",
        "CAN": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/2560px-Flag_of_Canada_%28Pantone%29.svg.png",
        "CPV": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Flag_of_Cape_Verde_%282-3_ratio%29.svg/800px-Flag_of_Cape_Verde_%282-3_ratio%29.svg.png",
        "CHE": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/1024px-Flag_of_Switzerland.svg.png",
        "CHL": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/1024px-Flag_of_Chile.svg.png",
        "CHN": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/1024px-Flag_of_the_People%27s_Republic_of_China.svg.png",
        "CIV": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_C%C3%B4te_d%27Ivoire.svg/800px-Flag_of_C%C3%B4te_d%27Ivoire.svg.png",
        "CMR": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Cameroon.svg/1024px-Flag_of_Cameroon.svg.png",
        "CCK": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Flag_of_the_Cocos_%28Keeling%29_Islands.svg/2560px-Flag_of_the_Cocos_%28Keeling%29_Islands.svg.png",
        "COD": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg/1024px-Flag_of_the_Democratic_Republic_of_the_Congo.svg.png",
        "COK": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Flag_of_the_Cook_Islands.svg/2560px-Flag_of_the_Cook_Islands.svg.png",
        "COL": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/1024px-Flag_of_Colombia.svg.png",
        "COM": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Flag_of_the_Comoros.svg/1024px-Flag_of_the_Comoros.svg.png",
        "CRI": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Costa_Rica_%28state%29.svg/1024px-Flag_of_Costa_Rica_%28state%29.svg.png",
        "CUB": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Flag_of_Cuba.svg/1024px-Flag_of_Cuba.svg.png",
        "CUW": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Flag_of_Cura%C3%A7ao.svg/1920px-Flag_of_Cura%C3%A7ao.svg.png",
        "CXR": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Flag_of_Christmas_Island.svg/2560px-Flag_of_Christmas_Island.svg.png",
        "CYM": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_the_Cayman_Islands.svg/2560px-Flag_of_the_Cayman_Islands.svg.png",
        "CYP": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Cyprus.svg/1024px-Flag_of_Cyprus.svg.png",
        "CZE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/1024px-Flag_of_the_Czech_Republic.svg.png",
        "DEU": "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1920px-Flag_of_Germany.svg.png",
        "DJI": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Flag_of_Djibouti.svg/1920px-Flag_of_Djibouti.svg.png",
        "DMA": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Flag_of_Dominica.svg/1920px-Flag_of_Dominica.svg.png",
        "DNK": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/1024px-Flag_of_Denmark.svg.png",
        "DOM": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_the_Dominican_Republic.svg/1920px-Flag_of_the_Dominican_Republic.svg.png",
        "DRC": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg/1024px-Flag_of_the_Democratic_Republic_of_the_Congo.svg.png",
        "DZA": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/1280px-Flag_of_Algeria.svg.png",
        "ECU": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/1920px-Flag_of_Ecuador.svg.png",
        "EGY": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Egypt.svg/1920px-Flag_of_Egypt.svg.png",
        "ERI": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Flag_of_Eritrea.svg/1920px-Flag_of_Eritrea.svg.png",
        "ESP": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1920px-Flag_of_Spain.svg.png",
        "EST": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Flag_of_Estonia.svg/1920px-Flag_of_Estonia.svg.png",
        "SWZ": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Flag_of_Eswatini.svg/1920px-Flag_of_Eswatini.svg.png",
        "ETH": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Flag_of_Ethiopia.svg/1280px-Flag_of_Ethiopia.svg.png",
        "FIN": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/1920px-Flag_of_Finland.svg.png",
        "FJI": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Fiji.svg/1920px-Flag_of_Fiji.svg.png",
        "FLK": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_Falkland_Islands.svg/2880px-Flag_of_the_Falkland_Islands.svg.png",
        "FRA": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1024px-Flag_of_France.svg.png",
        "ATF": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Flag_of_the_French_Southern_and_Antarctic_Lands.svg/1920px-Flag_of_the_French_Southern_and_Antarctic_Lands.svg.png",
        "FRO": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flag_of_the_Faroe_Islands.svg/1920px-Flag_of_the_Faroe_Islands.svg.png",
        "FSM": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Flag_of_the_Federated_States_of_Micronesia.svg/2560px-Flag_of_the_Federated_States_of_Micronesia.svg.png",
        "GAB": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Flag_of_Gabon.svg/1280px-Flag_of_Gabon.svg.png",
        "GBR": "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/2560px-Flag_of_the_United_Kingdom.svg.png",
        "GEO": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_Georgia.svg/1280px-Flag_of_Georgia.svg.png",
        "GGY": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_Guernsey.svg/1920px-Flag_of_Guernsey.svg.png",
        "GHA": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Ghana.svg/1280px-Flag_of_Ghana.svg.png",
        "GIB": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Flag_of_Gibraltar.svg/2560px-Flag_of_Gibraltar.svg.png",
        "GIN": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Flag_of_Guinea.svg/1280px-Flag_of_Guinea.svg.png",
        "GMB": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_The_Gambia.svg/1920px-Flag_of_The_Gambia.svg.png",
        "GNQ": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Equatorial_Guinea.svg/1280px-Flag_of_Equatorial_Guinea.svg.png",
        "GRC": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/1280px-Flag_of_Greece.svg.png",
        "GRD": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Grenada.svg/1920px-Flag_of_Grenada.svg.png",
        "GRL": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_Greenland.svg/1920px-Flag_of_Greenland.svg.png",
        "GTM": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Flag_of_Guatemala.svg/1920px-Flag_of_Guatemala.svg.png",
        "GLP": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1920px-Flag_of_France.svg.png",
        "GUF": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Flag_of_French_Guiana.svg/1280px-Flag_of_French_Guiana.svg.png",
        "GNB": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Guinea-Bissau.svg/1920px-Flag_of_Guinea-Bissau.svg.png",
        "GUM": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Flag_of_Guam.svg/2560px-Flag_of_Guam.svg.png",
        "GUY": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_Guyana.svg/1920px-Flag_of_Guyana.svg.png",
        "HKG": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/1920px-Flag_of_Hong_Kong.svg.png",
        "HMD": None,
        "HND": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Flag_of_Honduras.svg/1920px-Flag_of_Honduras.svg.png",
        "HRV": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Croatia.svg/1024px-Flag_of_Croatia.svg.png",
        "HTI": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Haiti.svg/1920px-Flag_of_Haiti.svg.png",
        "HUN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_Hungary.svg/1920px-Flag_of_Hungary.svg.png",
        "IDN": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/1920px-Flag_of_Indonesia.svg.png",
        "IMN": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_the_Isle_of_Man.svg/2560px-Flag_of_the_Isle_of_Man.svg.png",
        "IND": "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1280px-Flag_of_India.svg.png",
        "IOT": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_the_Commissioner_of_the_British_Indian_Ocean_Territory.svg/2560px-Flag_of_the_Commissioner_of_the_British_Indian_Ocean_Territory.svg.png",
        "IRL": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Flag_of_Ireland.svg/1920px-Flag_of_Ireland.svg.png",
        "IRN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Flag_of_Iran.svg/1920px-Flag_of_Iran.svg.png",
        "IRQ": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag_of_Iraq.svg/1280px-Flag_of_Iraq.svg.png",
        "ISL": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Iceland.svg/1280px-Flag_of_Iceland.svg.png",
        "ISR": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Israel.svg/1280px-Flag_of_Israel.svg.png",
        "ITA": "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/1280px-Flag_of_Italy.svg.png",
        "JAM": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Jamaica.svg/1920px-Flag_of_Jamaica.svg.png",
        "JEY": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Flag_of_Jersey.svg/2560px-Flag_of_Jersey.svg.png",
        "JOR": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Flag_of_Jordan.svg/1920px-Flag_of_Jordan.svg.png",
        "JPN": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/1920px-Flag_of_Japan.svg.png",
        "KAZ": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Flag_of_Kazakhstan.svg/1920px-Flag_of_Kazakhstan.svg.png",
        "KEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Kenya.svg/1920px-Flag_of_Kenya.svg.png",
        "KGZ": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Flag_of_Kyrgyzstan_%28official_standards%29.png/1920px-Flag_of_Kyrgyzstan_%28official_standards%29.png",
        "KHM": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_Cambodia.svg/1024px-Flag_of_Cambodia.svg.png",
        "KIR": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Flag_of_Kiribati.svg/1920px-Flag_of_Kiribati.svg.png",
        "KNA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Saint_Kitts_and_Nevis.svg/1920px-Flag_of_Saint_Kitts_and_Nevis.svg.png",
        "KOR": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/1280px-Flag_of_South_Korea.svg.png",
        "XKX": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Flag_of_Kosovo.svg/1920px-Flag_of_Kosovo.svg.png",
        "KWT": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Flag_of_Kuwait.svg/1920px-Flag_of_Kuwait.svg.png",
        "LAO": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Laos.svg/1920px-Flag_of_Laos.svg.png",
        "LBN": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Lebanon.svg/1920px-Flag_of_Lebanon.svg.png",
        "LBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Flag_of_Liberia.svg/1920px-Flag_of_Liberia.svg.png",
        "LBY": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Libya.svg/1920px-Flag_of_Libya.svg.png",
        "LCA": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Saint_Lucia.svg/1920px-Flag_of_Saint_Lucia.svg.png",
        "LIE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Flag_of_Liechtenstein.svg/1920px-Flag_of_Liechtenstein.svg.png",
        "LKA": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Flag_of_Sri_Lanka.svg/1920px-Flag_of_Sri_Lanka.svg.png",
        "LSO": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Flag_of_Lesotho.svg/1920px-Flag_of_Lesotho.svg.png",
        "LTU": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Flag_of_Lithuania.svg/1920px-Flag_of_Lithuania.svg.png",
        "LUX": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Flag_of_Luxembourg.svg/1920px-Flag_of_Luxembourg.svg.png",
        "MAC": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Flag_of_Macau.svg/1920px-Flag_of_Macau.svg.png",
        "LVA": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Flag_of_Latvia.svg/1920px-Flag_of_Latvia.svg.png",
        "MAF": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1920px-Flag_of_France.svg.png",
        "MAR": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Morocco.svg/1920px-Flag_of_Morocco.svg.png",
        "MCO": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Flag_of_Monaco.svg/1920px-Flag_of_Monaco.svg.png",
        "MDA": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Flag_of_Moldova.svg/2560px-Flag_of_Moldova.svg.png",
        "MDG": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Madagascar.svg/1920px-Flag_of_Madagascar.svg.png",
        "MDV": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_Maldives.svg/1920px-Flag_of_Maldives.svg.png",
        "MEX": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/2560px-Flag_of_Mexico.svg.png",
        "MHL": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Flag_of_the_Marshall_Islands.svg/1920px-Flag_of_the_Marshall_Islands.svg.png",
        "MLI": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Mali.svg/1920px-Flag_of_Mali.svg.png",
        "MLT": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Malta.svg/1920px-Flag_of_Malta.svg.png",
        "MMR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Flag_of_Myanmar.svg/1920px-Flag_of_Myanmar.svg.png",
        "MNE": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_Montenegro.svg/2560px-Flag_of_Montenegro.svg.png",
        "MNG": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Mongolia.svg/2560px-Flag_of_Mongolia.svg.png",
        "MNP": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Flag_of_the_Northern_Mariana_Islands.svg/2560px-Flag_of_the_Northern_Mariana_Islands.svg.png",
        "MOZ": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Flag_of_Mozambique.svg/1920px-Flag_of_Mozambique.svg.png",
        "MRT": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Flag_of_Mauritania.svg/1920px-Flag_of_Mauritania.svg.png",
        "MSR": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Flag_of_Montserrat.svg/2560px-Flag_of_Montserrat.svg.png",
        "MTQ": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Snake_Flag_of_Martinique.svg/1920px-Snake_Flag_of_Martinique.svg.png",
        "MUS": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Mauritius.svg/1920px-Flag_of_Mauritius.svg.png",
        "MWI": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Flag_of_Malawi.svg/1920px-Flag_of_Malawi.svg.png",
        "MYS": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/1920px-Flag_of_Malaysia.svg.png",
        "MYT": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1920px-Flag_of_France.svg.png",
        "NAM": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Namibia.svg/1920px-Flag_of_Namibia.svg.png",
        "NCL": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_FLNKS.svg/2560px-Flag_of_FLNKS.svg.png",
        "NER": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Flag_of_Niger.svg/1920px-Flag_of_Niger.svg.png",
        "NFK": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Norfolk_Island.svg/2560px-Flag_of_Norfolk_Island.svg.png",
        "NGA": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_Nigeria.svg/2560px-Flag_of_Nigeria.svg.png",
        "NIC": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Nicaragua.svg/2560px-Flag_of_Nicaragua.svg.png",
        "NIU": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Niue.svg/2560px-Flag_of_Niue.svg.png",
        "NLD": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/1920px-Flag_of_the_Netherlands.svg.png",
        "NOR": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/1920px-Flag_of_Norway.svg.png",
        "MKD": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_North_Macedonia.svg/2560px-Flag_of_North_Macedonia.svg.png",
        "NPL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Flag_of_Nepal.svg/1024px-Flag_of_Nepal.svg.png",
        "NRU": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Flag_of_Nauru.svg/2560px-Flag_of_Nauru.svg.png",
        "NZL": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Flag_of_New_Zealand.svg/1920px-Flag_of_New_Zealand.svg.png",
        "OMN": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Oman.svg/2560px-Flag_of_Oman.svg.png",
        "PAK": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Flag_of_Pakistan.svg/1920px-Flag_of_Pakistan.svg.png",
        "PAN": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Flag_of_Panama.svg/1920px-Flag_of_Panama.svg.png",
        "PER": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Flag_of_Peru.svg/1920px-Flag_of_Peru.svg.png",
        "PHL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_the_Philippines.svg/1920px-Flag_of_the_Philippines.svg.png",
        "PCN": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_the_Pitcairn_Islands.svg/2560px-Flag_of_the_Pitcairn_Islands.svg.png",
        "PLW": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Palau.svg/1920px-Flag_of_Palau.svg.png",
        "PNG": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Flag_of_Papua_New_Guinea.svg/1280px-Flag_of_Papua_New_Guinea.svg.png",
        "POL": "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Flag_of_Poland.svg/1920px-Flag_of_Poland.svg.png",
        "PRI": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Flag_of_Puerto_Rico.svg/1920px-Flag_of_Puerto_Rico.svg.png",
        "PRK": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Flag_of_North_Korea.svg/2560px-Flag_of_North_Korea.svg.png",
        "PRT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/1920px-Flag_of_Portugal.svg.png",
        "PRY": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Flag_of_Paraguay.svg/1920px-Flag_of_Paraguay.svg.png",
        "PSE": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Palestine.svg/1920px-Flag_of_Palestine.svg.png",
        "PYF": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Flag_of_French_Polynesia.svg/1920px-Flag_of_French_Polynesia.svg.png",
        "QAT": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Qatar.svg/1920px-Flag_of_Qatar.svg.png",
        "COG": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_the_Republic_of_the_Congo.svg/1024px-Flag_of_the_Republic_of_the_Congo.svg.png",
        "REU": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Flag_of_R%C3%A9union.svg/1920px-Flag_of_R%C3%A9union.svg.png",
        "ROU": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/1280px-Flag_of_Romania.svg.png",
        "RUS": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/1280px-Flag_of_Russia.svg.png",
        "RWA": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Rwanda.svg/1920px-Flag_of_Rwanda.svg.png",
        "SAU": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/1280px-Flag_of_Saudi_Arabia.svg.png",
        "SDN": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Sudan.svg/1920px-Flag_of_Sudan.svg.png",
        "SEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Flag_of_Senegal.svg/1280px-Flag_of_Senegal.svg.png",
        "SGP": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/1280px-Flag_of_Singapore.svg.png",
        "SGS": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Flag_of_South_Georgia_and_the_South_Sandwich_Islands.svg/2560px-Flag_of_South_Georgia_and_the_South_Sandwich_Islands.svg.png",
        "SJM": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/1920px-Flag_of_Norway.svg.png",
        "SLB": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Flag_of_the_Solomon_Islands.svg/1920px-Flag_of_the_Solomon_Islands.svg.png",
        "SLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Sierra_Leone.svg/1280px-Flag_of_Sierra_Leone.svg.png",
        "SLV": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Flag_of_El_Salvador.svg/1920px-Flag_of_El_Salvador.svg.png",
        "SMR": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Flag_of_San_Marino.svg/1280px-Flag_of_San_Marino.svg.png",
        "SOM": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Flag_of_Somalia.svg/1280px-Flag_of_Somalia.svg.png",
        "SPM": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1920px-Flag_of_France.svg.png",
        "SRB": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/1280px-Flag_of_Serbia.svg.png",
        "SSD": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Flag_of_South_Sudan.svg/1920px-Flag_of_South_Sudan.svg.png",
        "STP": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Sao_Tome_and_Principe.svg/1920px-Flag_of_Sao_Tome_and_Principe.svg.png",
        "SHN": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Saint_Helena.svg/2560px-Flag_of_Saint_Helena.svg.png",
        "SUR": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Flag_of_Suriname.svg/1280px-Flag_of_Suriname.svg.png",
        "SXM": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Flag_of_Sint_Maarten.svg/1920px-Flag_of_Sint_Maarten.svg.png",
        "SVK": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/1280px-Flag_of_Slovakia.svg.png",
        "SVN": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/1920px-Flag_of_Slovenia.svg.png",
        "SWE": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Flag_of_Sweden.svg/1920px-Flag_of_Sweden.svg.png",
        "SYC": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Seychelles.svg/1920px-Flag_of_Seychelles.svg.png",
        "SYR": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Flag_of_Syria.svg/1920px-Flag_of_Syria.svg.png",
        "TCD": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag_of_Chad.svg/1024px-Flag_of_Chad.svg.png",
        "TGO": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Flag_of_Togo.svg/1920px-Flag_of_Togo.svg.png",
        "THA": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Thailand.svg/1280px-Flag_of_Thailand.svg.png",
        "TLS": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Flag_of_East_Timor.svg/1920px-Flag_of_East_Timor.svg.png",
        "TJK": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Flag_of_Tajikistan.svg/1920px-Flag_of_Tajikistan.svg.png",
        "TKL": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Flag_of_Tokelau.svg/2560px-Flag_of_Tokelau.svg.png",
        "TKM": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Turkmenistan.svg/1280px-Flag_of_Turkmenistan.svg.png",
        "TON": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Tonga.svg/2560px-Flag_of_Tonga.svg.png",
        "TTO": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_Trinidad_and_Tobago.svg/1920px-Flag_of_Trinidad_and_Tobago.svg.png",
        "TUN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Tunisia.svg/1280px-Flag_of_Tunisia.svg.png",
        "TUR": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/1280px-Flag_of_Turkey.svg.png",
        "TCA": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Flag_of_the_Turks_and_Caicos_Islands.svg/2560px-Flag_of_the_Turks_and_Caicos_Islands.svg.png",
        "TUV": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tuvalu.svg/1920px-Flag_of_Tuvalu.svg.png",
        "TWN": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/1920px-Flag_of_the_Republic_of_China.svg.png",
        "TZA": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tanzania.svg/1280px-Flag_of_Tanzania.svg.png",
        "UGA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Flag_of_Uganda.svg/1280px-Flag_of_Uganda.svg.png",
        "UKR": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/1280px-Flag_of_Ukraine.svg.png",
        "UMI": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/1920px-Flag_of_the_United_States.svg.png",
        "URY": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Uruguay.svg/1280px-Flag_of_Uruguay.svg.png",
        "USA": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/1920px-Flag_of_the_United_States.svg.png",
        "UZB": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Flag_of_Uzbekistan.svg/1920px-Flag_of_Uzbekistan.svg.png",
        "VAT": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_the_Vatican_City.svg/1280px-Flag_of_the_Vatican_City.svg.png",
        "VCT": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Flag_of_Saint_Vincent_and_the_Grenadines.svg/1920px-Flag_of_Saint_Vincent_and_the_Grenadines.svg.png",
        "VEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Flag_of_Venezuela_%28state%29.svg/1280px-Flag_of_Venezuela_%28state%29.svg.png",
        "VGB": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_the_British_Virgin_Islands.svg/2560px-Flag_of_the_British_Virgin_Islands.svg.png",
        "VIR": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Flag_of_the_United_States_Virgin_Islands.svg/1920px-Flag_of_the_United_States_Virgin_Islands.svg.png",
        "VNM": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/1280px-Flag_of_Vietnam.svg.png",
        "VUT": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Flag_of_Vanuatu_%28official%29.svg/1920px-Flag_of_Vanuatu_%28official%29.svg.png",
        "WLF": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Flag_of_Wallis_and_Futuna.svg/1920px-Flag_of_Wallis_and_Futuna.svg.png",
        "WSM": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Samoa.svg/1920px-Flag_of_Samoa.svg.png",
        "YEM": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag_of_Yemen.svg/1280px-Flag_of_Yemen.svg.png",
        "ZAF": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/1280px-Flag_of_South_Africa.svg.png",
        "ZMB": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Zambia.svg/1280px-Flag_of_Zambia.svg.png",
        "ZWE": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Flag_of_Zimbabwe.svg/1920px-Flag_of_Zimbabwe.svg.png"
    }
    alpha3ToGDP = {
        "ABW": 3293000000,
        "AFG": 17876000000,
        "AGO": 85000000000,
        "AIA": 379000000,
        "ALA": 1503000000,
        "ALB": 15278000000,
        "AND": 3154000000,
        "ARE": 421142000000,
        "ARG": 449663000000,
        "ARM": 13672000000,
        "ASM": 636000000,
        "ATF": 0,
        "ATG": 1661000000,
        "AUS": 1380207000000,
        "AUT": 445075000000,
        "AZE": 48047000000,
        "BDI": 3002000000,
        "BEL": 533097000000,
        "BEN": 14403000000,
        "BES": 583000000,
        "BFA": 15990000000,
        "BGD": 317465000000,
        "BGR": 67925000000,
        "BHR": 38574000000,
        "BHS": 13578000000,
        "BIH": 20164000000,
        "BLM": 191000000,
        "BLR": 63080000000,
        "BLZ": 1906000000,
        "BMU": 7361000000,
        "BOL": 40895000000,
        "BRA": 1847795000000,
        "BRB": 5209000000,
        "BRN": 13469000000,
        "BTN": 2564000000,
        "BWA": 18340000000,
        "CAF": 2220000000,
        "CAN": 1741496000000,
        "CCK": 11012550,
        "CHE": 731425000000,
        "CHL": 282318000000,
        "CHN": 14342933000000,
        "CIV": 58539000000,
        "CMR": 38861000000,
        "COD": 47319000000,
        "COG": 12397000000,
        "COK": 379000000,
        "COL": 323802000000,
        "COM": 1165000000,
        "CPV": 1981000000,
        "CRI": 61773000000,
        "CUB": 105354000000,
        "CUW": 3101000000,
        "CXR": 52177900,
        "CYM": 6020000000,
        "CYP": 24565000000,
        "CZE": 250680000000,
        "DEU": 3861123000000,
        "DJI": 3166000000,
        "DMA": 582000000,
        "DNK": 350104000000,
        "DOM": 88941000000,
        "DZA": 171157000000,
        "ECU": 107435000000,
        "EGY": 317359000000,
        "ERI": 1981000000,
        "ESP": 1393490000000,
        "EST": 31471000000,
        "ETH": 92750000000,
        "FIN": 269296000000,
        "FJI": 5504000000,
        "FLK": 193280000,
        "FRA": 2715518000000,
        "FRO": 3126000000,
        "FSM": 414000000,
        "GAB": 16887000000,
        "GBR": 2826441000000,
        "GEO": 17742000000,
        "GGY": 4469000000,
        "GHA": 66999000000,
        "GIB": 3221550302,
        "GIN": 12354000000,
        "GLP": 10000000000,
        "GMB": 1822000000,
        "GNB": 1322000000,
        "GNQ": 11024000000,
        "GRC": 205326000000,
        "GRD": 1211000000,
        "GRL": 3023000000,
        "GTM": 76710000000,
        "GUF": 4870000000,
        "GUY": 5173000000,
        "GUM": 6311000000,
        "HKG": 365710000000,
        "HMD": 0,
        "HND": 25095000000,
        "HRV": 60415000000,
        "HTI": 8051000000,
        "HUN": 163469000000,
        "IDN": 1119190000000,
        "IMN": 7492000000,
        "IND": 2891582000000,
        "IOT": 0,
        "IRL": 398590000000,
        "IRN": 603779000000,
        "IRQ": 225232000000,
        "ISL": 24188000000,
        "ISR": 395098000000,
        "ITA": 2003576000000,
        "JAM": 15830000000,
        "JEY": 6630000000,
        "JOR": 44502000000,
        "JPN": 5082465000000,
        "KAZ": 181667000000,
        "KEN": 95501000000,
        "KGZ": 8454000000,
        "KHM": 27097000000,
        "KIR": 194000000,
        "KNA": 1050000000,
        "KOR": 1646539000000,
        "KWT": 134623000000,
        "LAO": 18822000000,
        "LBN": 56409000000,
        "LBR": 2582000000,
        "LBY": 32600000000,
        "LCA": 2122000000,
        "LIE": 6797000000,
        "LKA": 84008000000,
        "LSO": 2460000000,
        "LTU": 54627000000,
        "LUX": 71104000000,
        "LVA": 34102000000,
        "MAC": 53859000000,
        "MAF": 599000000,
        "MAR": 119700000000,
        "MCO": 7423000000,
        "MDA": 11955000000,
        "MDG": 14104000000,
        "MDV": 5642000000,
        "MEX": 1256440000000,
        "MHL": 237000000,
        "MKD": 12694000000,
        "MLI": 17432000000,
        "MLT": 14863000000,
        "MMR": 76784000000,
        "MNE": 5542000000,
        "MNG": 13852000000,
        "MNP": 1182000000,
        "MOZ": 15296000000,
        "MRT": 7593000000,
        "MTQ": 11314000000,
        "MSR": 67000000,
        "MUS": 14180000000,
        "MWI": 8099000000,
        "MYS": 364684000000,
        "MYT": 3049992000,
        "NAM": 12366000000,
        "NCL": 9879000000,
        "NER": 12927000000,
        "NFK": 60200000,
        "NGA": 474516000000,
        "NIC": 12520000000,
        "NIU": 10000000,
        "NLD": 907050000000,
        "NOR": 403336000000,
        "NPL": 30714000000,
        "NRU": 132000000,
        "NZL": 206936000000,
        "OMN": 76331000000,
        "PAK": 263000000000,
        "PAN": 66787000000,
        "PCN": 154352,
        "PER": 226850000000,
        "PHL": 359354000000,
        "PLW": 280000000,
        "PNG": 24796900000,
        "POL": 595862000000,
        "PRI": 104988000000,
        "PRK": 16331000000,
        "PRT": 238785000000,
        "PRY": 38086000000,
        "PSE": 17058000000,
        "PYF": 6023000000,
        "QAT": 183466000000,
        "REU": 22000000000,
        "ROU": 250075000000,
        "RUS": 1692930000000,
        "RWA": 10355000000,
        "SAU": 792966000000,
        "SDN": 34895000000,
        "SEN": 23664000000,
        "SGP": 372073000000,
        "SGS": 0,
        "SHN": 51900000,
        "SJM": 277300000,
        "SLB": 1302000000,
        "SLE": 4121000000,
        "SLV": 27022000000,
        "SMR": 1602000000,
        "SOM": 1626000000,
        "SRB": 51475000000,
        "SSD": 4959000000,
        "SPM": 261300000,
        "STP": 421000000,
        "SUR": 3697000000,
        "SVK": 105079000000,
        "SVN": 54174000000,
        "SWE": 530883000000,
        "SWZ": 4594000000,
        "SXM": 1009000000,
        "SYC": 1698000000,
        "SYR": 20379000000,
        "TCA": 1197000000,
        "TCD": 11271000000,
        "TGO": 7270000000,
        "THA": 542016000000,
        "TJK": 8333000000,
        "TKL": 9400000,
        "TKM": 48276000000,
        "TLS": 2017000000,
        "TON": 508000000,
        "TTO": 23208000000,
        "TUN": 38797000000,
        "TUR": 761425000000,
        "TUV": 47000000,
        "TWN": 315020000000,
        "TZA": 61136000000,
        "UGA": 32609000000,
        "UKR": 153781000000,
        "UMI": 13000000,
        "URY": 56045000000,
        "USA": 21433226000000,
        "UZB": 57921000000,
        "VAT": 21200000,
        "VCT": 825000000,
        "VIR": 3984000000,
        "VEN": 134960000000,
        "VGB": 1296000000,
        "VNM": 261921000000,
        "VUT": 906000000,
        "WSM": 844000000,
        "WLF": 188000000,
        "YEM": 24935000000,
        "ZAF": 351430000000,
        "ZMB": 23085000000,
        "ZWE": 21440000000
    }
    alpha3ToLargestCity = {
        "ABW": "Oranjestad",
        "AFG": "Kabul",
        "AGO": "Luanda",
        "AIA": "The Valley",
        "ALA": "Mariehamn",
        "ALB": "Tirana",
        "AND": "Andorra la Vella",
        "ARE": "Dubai",
        "ARG": "Buenos Aires",
        "ARM": "Yerevan",
        "ASM": "Tāfuna",
        "ATA": "McMurdo Station",
        "ATF": "Port-aux-Français",
        "ATG": "St. John's",
        "AUS": "Sydney",
        "AUT": "Vienna",
        "AZE": "Baku",
        "BDI": "Bujumbura",
        "BEL": "Brussels",
        "BEN": "Cotonou",
        "BES": "Kralendijk",
        "BFA": "Ouagadougou",
        "BGD": "Dhaka",
        "BGR": "Sofia",
        "BHR": "Manama",
        "BHS": "Nassaug",
        "BIH": "Sarajevo",
        "BLM": "Gustavia",
        "BLR": "Minsk",
        "BLZ": "Belize City",
        "BMU": "Hamilton",
        "BOL": "Santa Cruz de la Sierra",
        "BRA": "São Paulo",
        "BRB": "Bridgetown",
        "BRN": "Bandar Seri Begawan",
        "BTN": "Thimphu",
        "BVT": None,
        "BWA": "Gaborone",
        "CAF": "Bangui",
        "CAN": "Toronto",
        "CCK": "Bantam",
        "CHE": "Zürich",
        "CHL": "Santiago",
        "CHN": "Shanghai",
        "CIV": "Abidjan",
        "CMR": "Yaoundé",
        "COD": "Kinshasa",
        "COG": "Brazzaville",
        "COK": "Avarua",
        "COL": "Bogotá",
        "COM": "Moroni",
        "CPV": "Praia",
        "CRI": "San José",
        "CUB": "Havana",
        "CUW": "Willemstad",
        "CXR": "Flying Fish Cove",
        "CYM": "George Town",
        "CYP": "Nicosia",
        "CZE": "Prague",
        "DEU": "Berlin",
        "DJI": "Djibouti",
        "DMA": "Roseau",
        "DNK": "Copenhagen",
        "DOM": "Santo Domingo",
        "DZA": "Algiers",
        "ECU": "Quito",
        "EGY": "Cairo",
        "ERI": "Asmara",
        "ESP": "Madrid",
        "EST": "Tallinn",
        "ETH": "Addis Ababa",
        "FIN": "Helsinki",
        "FJI": "Suva",
        "FLK": "Stanley",
        "FRA": "Paris",
        "FRO": "Tórshavn",
        "FSM": "Weno",
        "GAB": "Libreville",
        "GBR": "London",
        "GEO": "Tbilisi",
        "GGY": "Saint Peter Port",
        "GHA": "Accra",
        "GIB": "Westside",
        "GIN": "Conakry",
        "GLP": "Pointe-à-Pitre",
        "GMB": "Banjul",
        "GNB": "Bissau",
        "GNQ": "Bata",
        "GRC": "Athens",
        "GRD": "St. George's",
        "GRL": "Nuuk",
        "GTM": "Guatemala City",
        "GUF": "Cayenne",
        "GUM": "Dededo",
        "GUY": "Georgetown",
        "HKG": "Hong Kong",
        "HMD": None,
        "HND": "Tegucigalpa",
        "HRV": "Zagreb",
        "HTI": "Port-au-Prince",
        "HUN": "Budapest",
        "IDN": "Jakarta",
        "IMN": "Douglas",
        "IND": "Mumbai",
        "IOT": "Diego Garcia",
        "IRL": "Dublin",
        "IRN": "Tehran",
        "IRQ": "Baghdad",
        "ISL": "Reykjavík",
        "ISR": "Jerusalem (Disputed)",
        "ITA": "Rome",
        "JAM": "Kingston",
        "JEY": "Saint Helier",
        "JOR": "Amman",
        "JPN": "Tokyo",
        "KAZ": "Almaty",
        "KEN": "Nairobi",
        "KGZ": "Bishkek",
        "KHM": "Phnom Penh",
        "KIR": "South Tarawa",
        "KNA": "Basseterre",
        "KOR": "Seoul",
        "KWT": "Kuwait City",
        "LAO": "Vientiane",
        "LBN": "Beirut",
        "LBR": "Monrovia",
        "LBY": "Tripoli",
        "LCA": "Castries",
        "LIE": "Schaan",
        "LKA": "Colombo",
        "LSO": "Maseru",
        "LTU": "Vilnius",
        "LUX": "Luxembourg City",
        "LVA": "Riga",
        "MAC": "Macao",
        "MAF": "Marigot",
        "MAR": "Casablanca",
        "MCO": "Larvotto",
        "MDA": "Chișinău",
        "MDG": "Antananarivo",
        "MDV": "Malé",
        "MEX": "Mexico City",
        "MHL": "Majuro",
        "MKD": "Skopje",
        "MLI": "Bamako",
        "MLT": "St. Paul's Bay",
        "MMR": "Yangon",
        "MNE": "Podgorica",
        "MNG": "Ulaanbaatar",
        "MNP": "Saipan",
        "MOZ": "Maputo",
        "MRT": "Nouakchott",
        "MSR": "Brades",
        "MTQ": "Fort-de-France",
        "MUS": "Port Louis",
        "MWI": "Lilongwe",
        "MYS": "Kuala Lumpur",
        "MYT": "Mamoudzou",
        "NAM": "Ho Chi Minh City",
        "NCL": "Nouméa",
        "NER": "Niamey",
        "NFK": "Burnt Pine",
        "NGA": "Lagos",
        "NIC": "Managua",
        "NIU": "Alofi",
        "NLD": "Amsterdam",
        "NOR": "Oslo",
        "NPL": "Kathmandu",
        "NRU": "Denigomodu District",
        "NZL": "Auckland",
        "OMN": "Muscat",
        "PAK": "Karachi",
        "PAN": "Panama City",
        "PCN": "Adamstown",
        "PER": "Lima",
        "PHL": "Quezon City",
        "PLW": "Koror",
        "PNG": "Port Moresby",
        "POL": "Warsaw",
        "PRI": "San Juan",
        "PRK": "Pyongyang",
        "PRT": "Lisbon",
        "PRY": "Asunción",
        "PSE": "Gaza City",
        "PYF": "Fa'a'ā",
        "QAT": "Doha",
        "REU": "Saint-Denis",
        "ROU": "Bucharest",
        "RUS": "Moscow",
        "RWA": "Kigali",
        "SAU": "Riyadh",
        "SDN": "Omdurman",
        "SEN": "Dakar",
        "SGP": "Singapore",
        "SGS": "King Edward Point",
        "SHN": "Half Tree Hollow",
        "SJM": "Longyearbyen",
        "SLB": "Honiara",
        "SLE": "Freetown",
        "SLV": "San Salvador",
        "SMR": "Dogana",
        "SOM": "Mogadishu",
        "SPM": "Saint-Pierre",
        "SRB": "Belgrade",
        "SSD": "Juba",
        "STP": "São Tomé",
        "SUR": "Paramaribo",
        "SVK": "Bratislava",
        "SVN": "Ljubljana",
        "SWE": "Stockholm",
        "SWZ": "Manzini",
        "SXM": "Lower Prince's Quarter",
        "SYC": "Victoria",
        "SYR": "Damascus",
        "TCA": "Providenciales",
        "TCD": "N'Djamena",
        "TGO": "Lomé",
        "THA": "Bangkok",
        "TJK": "Dushanbe",
        "TKL": "Atafu",
        "TKM": "Ashgabat",
        "TLS": "Dili",
        "TON": "Nukuʻalofa",
        "TTO": "San Fernando",
        "TUN": "Tunis",
        "TUR": "Istanbul",
        "TUV": "Funafuti",
        "TWN": "New Taipei",
        "TZA": "Dar es Salaam",
        "UGA": "Kampala",
        "UKR": "Kyiv",
        "UMI": "New York City",
        "URY": "Montevideo",
        "USA": "New York City",
        "UZB": "Tashkent",
        "VAT": "Vatican City",
        "VCT": "Kingstown",
        "VEN": "Caracas",
        "VGB": "Road Town",
        "VIR": "Charlotte Amalie",
        "VNM": "Ho Chi Minh City",
        "VUT": "Port Vila",
        "WLF": "Matā'Utu",
        "WSM": "Apia",
        "YEM": "Sana'a",
        "ZAF": "Johannesburg",
        "ZMB": "Lusaka",
        "ZWE": "Harare"
    }
    alpha3ToName = {
        "ABW": "Aruba",
        "AFG": "Afghanistan",
        "AGO": "Angola",
        "AIA": "Anguilla",
        "ALA": "Åland Islands",
        "ALB": "Albania",
        "AND": "Andorra",
        "ARE": "United Arab Emirates",
        "ARG": "Argentina",
        "ARM": "Armenia",
        "ASM": "American Samoa",
        "ATA": "Antarctica",
        "ATF": "French Southern Territories",
        "ATG": "Antigua and Barbuda",
        "AUS": "Australia",
        "AUT": "Austria",
        "AZE": "Azerbaijan",
        "BDI": "Burundi",
        "BEL": "Belgium",
        "BEN": "Benin",
        "BES": "Caribbean Netherlands",
        "BFA": "Burkina Faso",
        "BGD": "Bangladesh",
        "BGR": "Bulgaria",
        "BHR": "Bahrain",
        "BHS": "Bahamas",
        "BIH": "Bosnia and Herzegovina",
        "BLM": "Saint Barthélemy",
        "BLR": "Belarus",
        "BLZ": "Belize",
        "BMU": "Bermuda",
        "BOL": "Bolivia",
        "BRA": "Brazil",
        "BRB": "Barbados",
        "BRN": "Brunei",
        "BTN": "Bhutan",
        "BWA": "Botswana",
        "CAF": "Central African Republic",
        "CAN": "Canada",
        "CCK": "Cocos (Keeling) Islands",
        "CHE": "Switzerland",
        "CHL": "Chile",
        "CHN": "China",
        "CIV": "Côte d'Ivoire",
        "CMR": "Cameroon",
        "COD": "Democratic Republic of the Congo",
        "COG": "Republic of the Congo",
        "COK": "Cook Islands",
        "COL": "Colombia",
        "COM": "Comoros",
        "CPV": "Cabo Verde",
        "CRI": "Costa Rica",
        "CUB": "Cuba",
        "CUW": "Curaçao",
        "CXR": "Christmas Island",
        "CYM": "Cayman Islands",
        "CYP": "Cyprus",
        "CZE": "Czech Republic",
        "DEU": "Germany",
        "DJI": "Djibouti",
        "DMA": "Dominica",
        "DNK": "Denmark",
        "DOM": "Dominican Republic",
        "DZA": "Algeria",
        "ECU": "Ecuador",
        "EGY": "Egypt",
        "ERI": "Eritrea",
        "ESP": "Spain",
        "EST": "Estonia",
        "ETH": "Ethiopia",
        "FIN": "Finland",
        "FJI": "Fiji",
        "FLK": "Falkland Islands",
        "FRA": "France",
        "FRO": "Faroe Islands",
        "FSM": "Micronesia",
        "GAB": "Gabon",
        "GBR": "United Kingdom",
        "GEO": "Georgia",
        "GGY": "Guernsey",
        "GHA": "Ghana",
        "GIB": "Gibraltar",
        "GIN": "Guinea",
        "GLP": "Guadeloupe",
        "GMB": "Gambia",
        "GNB": "Guinea-Bissau",
        "GNQ": "Equatorial Guinea",
        "GRC": "Greece",
        "GRD": "Grenada",
        "GRL": "Greenland",
        "GTM": "Guatemala",
        "GUF": "French Guiana",
        "GUM": "Guam",
        "GUY": "Guyana",
        "HKG": "Hong Kong",
        "HMD": "Heard Island and McDonald Islands",
        "HND": "Honduras",
        "HRV": "Croatia",
        "HTI": "Haiti",
        "HUN": "Hungary",
        "IDN": "Indonesia",
        "IMN": "Isle of Man",
        "IND": "India",
        "IOT": "British Indian Ocean Territory",
        "IRL": "Ireland",
        "IRN": "Iran",
        "IRQ": "Iraq",
        "ISL": "Iceland",
        "ISR": "Israel",
        "ITA": "Italy",
        "JAM": "Jamaica",
        "JEY": "Jersey",
        "JOR": "Jordan",
        "JPN": "Japan",
        "KAZ": "Kazakhstan",
        "KEN": "Kenya",
        "KGZ": "Kyrgyzstan",
        "KHM": "Cambodia",
        "KIR": "Kiribati",
        "KNA": "Saint Kitts and Nevis",
        "KOR": "South Korea",
        "KWT": "Kuwait",
        "LAO": "Laos",
        "LBN": "Lebanon",
        "LBR": "Liberia",
        "LBY": "Libya",
        "LCA": "Saint Lucia",
        "LIE": "Liechtenstein",
        "LKA": "Sri Lanka",
        "LSO": "Lesotho",
        "LTU": "Lithuania",
        "LUX": "Luxembourg",
        "LVA": "Latvia",
        "MAC": "Macao",
        "MAF": "Saint Martin",
        "MAR": "Morocco",
        "MCO": "Monaco",
        "MDA": "Moldova",
        "MDG": "Madagascar",
        "MDV": "Maldives",
        "MEX": "Mexico",
        "MHL": "Marshall Islands",
        "MKD": "North Macedonia",
        "MLI": "Mali",
        "MLT": "Malta",
        "MMR": "Myanmar",
        "MNE": "Montenegro",
        "MNG": "Mongolia",
        "MNP": "Northern Mariana Islands",
        "MOZ": "Mozambique",
        "MRT": "Mauritania",
        "MSR": "Montserrat",
        "MTQ": "Martinique",
        "MUS": "Mauritius",
        "MWI": "Malawi",
        "MYS": "Malaysia",
        "MYT": "Mayotte",
        "NAM": "Namibia",
        "NCL": "New Caledonia",
        "NER": "Niger",
        "NFK": "Norfolk Island",
        "NGA": "Nigeria",
        "NIC": "Nicaragua",
        "NIU": "Niue",
        "NLD": "Netherlands",
        "NOR": "Norway",
        "NPL": "Nepal",
        "NRU": "Nauru",
        "NZL": "New Zealand",
        "OMN": "Oman",
        "PAK": "Pakistan",
        "PAN": "Panama",
        "PCN": "Pitcairn",
        "PER": "Peru",
        "PHL": "Philippines",
        "PLW": "Palau",
        "PNG": "Papua New Guinea",
        "POL": "Poland",
        "PRI": "Puerto Rico",
        "PRK": "North Korea",
        "PRT": "Portugal",
        "PRY": "Paraguay",
        "PSE": "Palestine",
        "PYF": "French Polynesia",
        "QAT": "Qatar",
        "REU": "Réunion",
        "ROU": "Romania",
        "RUS": "Russia",
        "RWA": "Rwanda",
        "SAU": "Saudi Arabia",
        "SDN": "Sudan",
        "SEN": "Senegal",
        "SGP": "Singapore",
        "SGS": "South Georgia and the South Sandwich Islands",
        "SHN": "Saint Helena, Ascension and Tristan da Cunha",
        "SJM": "Svalbard and Jan Mayen",
        "SLB": "Solomon Islands",
        "SLE": "Sierra Leone",
        "SLV": "El Salvador",
        "SMR": "San Marino",
        "SOM": "Somalia",
        "SPM": "Saint Pierre and Miquelon",
        "SRB": "Serbia",
        "SSD": "South Sudan",
        "STP": "Sao Tome and Principe",
        "SUR": "Suriname",
        "SVK": "Slovakia",
        "SVN": "Slovenia",
        "SWE": "Sweden",
        "SWZ": "Eswatini",
        "SXM": "Sint Maarten",
        "SYC": "Seychelles",
        "SYR": "Syria",
        "TCA": "Turks and Caicos Islands",
        "TCD": "Chad",
        "TGO": "Togo",
        "THA": "Thailand",
        "TJK": "Tajikistan",
        "TKL": "Tokelau",
        "TKM": "Turkmenistan",
        "TLS": "Timor-Leste",
        "TON": "Tonga",
        "TTO": "Trinidad and Tobago",
        "TUN": "Tunisia",
        "TUR": "Turkey",
        "TUV": "Tuvalu",
        "TWN": "Taiwan",
        "TZA": "Tanzania",
        "UGA": "Uganda",
        "UKR": "Ukraine",
        "UMI": "United States Minor Outlying Islands",
        "URY": "Uruguay",
        "USA": "United States",
        "UZB": "Uzbekistan",
        "VAT": "Vatican City",
        "VCT": "Saint Vincent and the Grenadines",
        "VEN": "Venezuela",
        "VGB": "British Virgin Islands",
        "VIR": "U.S. Virgin Islands",
        "VNM": "Vietnam",
        "VUT": "Vanuatu",
        "WLF": "Wallis and Futuna",
        "WSM": "Samoa",
        "XKX": "Kosovo",
        "YEM": "Yemen",
        "ZAF": "South Africa",
        "ZMB": "Zambia",
        "ZWE": "Zimbabwe"
    }
    alpha3ToPopulation = {
        "ABW": 107394,
        "AFG": 27657145,
        "AGO": 25868000,
        "AIA": 13452,
        "ALA": 28875,
        "ALB": 2886026,
        "AND": 78014,
        "ARE": 9856000,
        "ARG": 43590400,
        "ARM": 2994400,
        "ASM": 57100,
        "ATA": 1000,
        "ATF": 140,
        "ATG": 86295,
        "AUS": 24117360,
        "AUT": 8725931,
        "AZE": 9730500,
        "BDI": 10114505,
        "BEL": 11319511,
        "BEN": 10653654,
        "BES": 17408,
        "BFA": 19034397,
        "BGD": 161006790,
        "BGR": 7153784,
        "BHR": 1404900,
        "BHS": 378040,
        "BIH": 3531159,
        "BLM": 9417,
        "BLR": 9498700,
        "BLZ": 370300,
        "BMU": 61954,
        "BOL": 10985059,
        "BRA": 206135893,
        "BRB": 285000,
        "BRN": 411900,
        "BTN": 775620,
        "BWA": 2141206,
        "CAF": 4998000,
        "CAN": 36155487,
        "CCK": 550,
        "CHE": 8341600,
        "CHL": 18191900,
        "CHN": 1377422166,
        "CIV": 22671331,
        "CMR": 22709892,
        "COD": 85026000,
        "COG": 4741000,
        "COK": 18100,
        "COL": 48759958,
        "COM": 806153,
        "CPV": 531239,
        "CRI": 4890379,
        "CUB": 11239004,
        "CUW": 154843,
        "CXR": 2072,
        "CYM": 58238,
        "CYP": 847000,
        "CZE": 10558524,
        "DEU": 81770900,
        "DJI": 900000,
        "DMA": 71293,
        "DNK": 5717014,
        "DOM": 10075045,
        "DZA": 40400000,
        "ECU": 16545799,
        "EGY": 91290000,
        "ERI": 5352000,
        "ESH": 510713,
        "ESP": 46438422,
        "EST": 1315944,
        "ETH": 92206005,
        "FIN": 5491817,
        "FJI": 867000,
        "FLK": 2563,
        "FRA": 66710000,
        "FRO": 49376,
        "FSM": 102800,
        "GAB": 1802278,
        "GBR": 65110000,
        "GEO": 3720400,
        "GGY": 62999,
        "GHA": 27670174,
        "GIB": 33140,
        "GIN": 1222442,
        "GLP": 400132,
        "GMB": 1882450,
        "GNB": 1547777,
        "GNQ": 1222442,
        "GRC": 10858018,
        "GRD": 103328,
        "GRL": 55847,
        "GTM": 16176133,
        "GUF": 254541,
        "GUM": 184200,
        "GUY": 746900,
        "HKG": 7324300,
        "HMD": 0,
        "HND": 8576532,
        "HRV": 4190669,
        "HTI": 11078033,
        "HUN": 9823000,
        "IDN": 258705000,
        "IMN": 84497,
        "IND": 1366000000,
        "IOT": 3000,
        "IRL": 6378000,
        "IRN": 79369900,
        "IRQ": 37883543,
        "ISL": 334300,
        "ISR": 8527400,
        "ITA": 60665551,
        "JAM": 2723246,
        "JEY": 100800,
        "JOR": 9531712,
        "JPN": 126960000,
        "KAZ": 17753200,
        "KEN": 47251000,
        "KGZ": 6047800,
        "KHM": 15626444,
        "KIR": 113400,
        "KNA": 46204,
        "KOR": 50801405,
        "KWT": 4183658,
        "LAO": 6492400,
        "LBN": 5988000,
        "LBR": 4615000,
        "LBY": 6385000,
        "LCA": 186000,
        "LIE": 37623,
        "LKA": 20966000,
        "LSO": 1894194,
        "LTU": 2872294,
        "LUX": 576200,
        "LVA": 1961600,
        "MAC": 649100,
        "MAF": 36979,
        "MAR": 33337529,
        "MCO": 38400,
        "MDA": 3553100,
        "MDG": 22434363,
        "MDV": 344023,
        "MEX": 122273473,
        "MHL": 54880,
        "MKD": 2058539,
        "MLI": 18135000,
        "MLT": 425384,
        "MMR": 51419420,
        "MNE": 621810,
        "MNG": 3093100,
        "MNP": 56940,
        "MOZ": 26423700,
        "MRT": 3718678,
        "MSR": 4922,
        "MTQ": 378243,
        "MUS": 1262879,
        "MWI": 16832910,
        "MYS": 31405416,
        "MYT": 226915,
        "NAM": 2324388,
        "NCL": 268767,
        "NER": 20715000,
        "NFK": 2302,
        "NGA": 186988000,
        "NIC": 6262703,
        "NIU": 1470,
        "NLD": 17019800,
        "NOR": 5223256,
        "NPL": 28431500,
        "NRU": 10084,
        "NZL": 4697854,
        "OMN": 4420133,
        "PAK": 194125062,
        "PAN": 3814672,
        "PCN": 56,
        "PER": 31488700,
        "PHL": 103279800,
        "PLW": 17950,
        "PNG": 8083700,
        "POL": 38437239,
        "PRI": 3474182,
        "PRK": 25281000,
        "PRT": 10374822,
        "PRY": 6854536,
        "PSE": 4682467,
        "PYF": 271800,
        "QAT": 2587564,
        "REU": 840974,
        "ROU": 19861408,
        "RUS": 146599183,
        "RWA": 11553188,
        "SAU": 32248200,
        "SDN": 12131000,
        "SEN": 14799859,
        "SGP": 5535000,
        "SGS": 30,
        "SHN": 4255,
        "SJM": 2562,
        "SLB": 642000,
        "SLE": 7075641,
        "SLV": 6520675,
        "SMR": 33005,
        "SOM": 11079000,
        "SPM": 6069,
        "SRB": 7076372,
        "SSD": 12131000,
        "STP": 187356,
        "SUR": 541638,
        "SVK": 5426252,
        "SVN": 2064188,
        "SWE": 9894888,
        "SWZ": 1132657,
        "SXM": 38247,
        "SYC": 91400,
        "SYR": 18564000,
        "TCA": 31458,
        "TCD": 14497000,
        "TGO": 7143000,
        "THA": 65327652,
        "TJK": 8593600,
        "TKL": 1411,
        "TKM": 4751120,
        "TLS": 1167242,
        "TON": 103252,
        "TTO": 1349667,
        "TUN": 11154400,
        "TUR": 78741053,
        "TUV": 10640,
        "TWN": 23503349,
        "TZA": 55155000,
        "UGA": 33860700,
        "UKR": 42692393,
        "UMI": 300,
        "URY": 3480222,
        "USA": 323947000,
        "UZB": 31576400,
        "VAT": 451,
        "VCT": 109991,
        "VEN": 31028700,
        "VGB": 28514,
        "VIR": 114743,
        "VNM": 92700000,
        "VUT": 277500,
        "WLF": 11750,
        "WSM": 57100,
        "YEM": 27478000,
        "ZAF": 55653654,
        "ZMB": 15933883,
        "ZWE": 14240168
    }
    australianStateAlphaList = [
        "AU-ACT",
        "AU-AQ",
        "AU-CC",
        "AU-CX",
        "AU-HM",
        "AU-JBT",
        "AU-NF",
        "AU-NSW",
        "AU-NT",
        "AU-QLD",
        "AU-SA",
        "AU-TAS",
        "AU-VIC",
        "AU-WA"
    ]
    australianStateAlphaToAreaKM = {
        "AU-ACT": 2358,
        "AU-AQ": 5896500,
        "AU-CC": 14,
        "AU-CX": 135,
        "AU-HM": 372,
        "AU-JBT": 67,
        "AU-NF": 35,
        "AU-NSW": 809952,
        "AU-NT": 1419630,
        "AU-QLD": 1851736,
        "AU-SA": 1044353,
        "AU-TAS": 90758,
        "AU-VIC": 237657,
        "AU-WA": 2642753
    }
    australianStateAlphaToCapital = {
        "AU-ACT": "Canberra",
        "AU-AQ": None,
        "AU-CC": "West Island",
        "AU-CX": "Flying Fish Cove",
        "AU-HM": None,
        "AU-JBT": None,
        "AU-NF": "Kingston",
        "AU-NSW": "Sydney",
        "AU-NT": "Darwin",
        "AU-QLD": "Bribane",
        "AU-SA": "Adelaide",
        "AU-TAS": "Hobart",
        "AU-VIC": "Melbourne",
        "AU-WA": "Perth"
    }
    australianStateAlphaToLargestCity = {
        "AU-ACT": "Canberra",
        "AU-AQ": None,
        "AU-CC": "Bantam",
        "AU-CX": "Flying Fish Cove",
        "AU-HM": None,
        "AU-JBT": None,
        "AU-NF": "Burnt Pine",
        "AU-NSW": "Sydney",
        "AU-NT": "Darwin",
        "AU-QLD": "Brisbane",
        "AU-SA": "Adelaide",
        "AU-TAS": "Hobart",
        "AU-VIC": "Melbourne",
        "AU-WA": "Perth"
    }
    australianStateAlphaToFlagURL = {
        "AU-ACT": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Flag_of_the_Australian_Capital_Territory.svg/2560px-Flag_of_the_Australian_Capital_Territory.svg.png",
        "AU-AQ": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Australia_%28converted%29.svg/2560px-Flag_of_Australia_%28converted%29.svg.png",
        "AU-CC": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Flag_of_the_Cocos_%28Keeling%29_Islands.svg/2560px-Flag_of_the_Cocos_%28Keeling%29_Islands.svg.png",
        "AU-CX": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Flag_of_Christmas_Island.svg/2560px-Flag_of_Christmas_Island.svg.png",
        "AU-HM": None,
        "AU-JBT": None,
        "AU-NF": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Norfolk_Island.svg/2560px-Flag_of_Norfolk_Island.svg.png",
        "AU-NSW": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_New_South_Wales.svg/2560px-Flag_of_New_South_Wales.svg.png",
        "AU-NT": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_the_Northern_Territory.svg/2560px-Flag_of_the_Northern_Territory.svg.png",
        "AU-QLD": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Flag_of_Queensland.svg/2560px-Flag_of_Queensland.svg.png",
        "AU-SA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Flag_of_South_Australia.svg/2560px-Flag_of_South_Australia.svg.png",
        "AU-TAS": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Flag_of_Tasmania.svg/2560px-Flag_of_Tasmania.svg.png",
        "AU-VIC": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Flag_of_Victoria_%28Australia%29.svg/2560px-Flag_of_Victoria_%28Australia%29.svg.png",
        "AU-WA": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Flag_of_Western_Australia.svg/2560px-Flag_of_Western_Australia.svg.png"
    }
    australianStateAlphaToGDP = {
        "AU-ACT": 30071150400,
        "AU-AQ": 0,
        "AU-CC": 11012550,
        "AU-CX": 52177900,
        "AU-HM": 0,
        "AU-JBT": 0,
        "AU-NF": 60209320,
        "AU-NSW": 459505881900,
        "AU-NT": 19227685600,
        "AU-QLD": 267262844800,
        "AU-SA": 79647156800,
        "AU-TAS": 23601390400,
        "AU-VIC": 337379604000,
        "AU-WA": 214887196800
    }
    australianStateNameToAlpha = {
        "AUSTRALIAN_CAPITAL_TERRITORY": "AU-ACT",
        "CAPITAL_TERRITORY": "AU-ACT",
        "AUSTRALIAN_ANTARCTIC_TERRITORY": "AU-AQ",
        "ANTARCTIC_TERRITORY": "AU-AQ",
        "COCOS_(KEELING)_ISLANDS": "AU-CC",
        "COCOS_KEELING_ISLANDS": "AU-CC",
        "KEELING_ISLANDS": "AU-CC",
        "COCOS_ISLANDS": "AU-CC",
        "CHRISTMAS_ISLAND": "AU-CX",
        "HEARD_ISLAND_AND_MCDONALD_ISLANDS": "AU-HM",
        "HEARD_ISLAND": "AU-HM",
        "MCDONALD_ISLAND": "AU-HM",
        "MCDONALD_ISLANDS": "AU-HM",
        "JERVIS_BAY_TERRITORY": "AU-JBT",
        "JERVIS_BAY": "AU-JBT",
        "NORFOLK_ISLAND": "AU-NF",
        "NEW_SOUTH_WALES": "AU-NSW",
        "NSW": "AU-NSW",
        "NORTHERN_TERRITORY": "AU-NT",
        "QUEENSLAND": "AU-QLD",
        "SOUTH_AUSTRALIA": "AU-SA",
        "TASMANIA": "AU-TAS",
        "WESTERN_AUSTRALIA": "AU-WA"
    }
    australianStateAlphaToName = {
        "AU-ACT": "Australian Capital Territory",
        "AU-AQ": "Australian Antarctic Territory",
        "AU-CC": "Cocos (Keeling) Islands",
        "AU-CX": "Christmas Island",
        "AU-HM": "Heard Island and McDonald Islands",
        "AU-JBT": "Jervis Bay Territory",
        "AU-NF": "Norfolk Island",
        "AU-NSW": "New South Wales",
        "AU-NT": "Northern Territory",
        "AU-QLD": "Queensland",
        "AU-SA": "South Australia",
        "AU-TAS": "Tasmania",
        "AU-VIC": "Victoria",
        "AU-WA": "Western Australia"
    }
    australianStateNameList = [
        "AUSTRALIAN_CAPITAL_TERRITORY",
        "CAPITAL_TERRITORY",
        "AUSTRALIAN_ANTARCTIC_TERRITORY",
        "ANTARCTIC_TERRITORY",
        "COCOS_(KEELING)_ISLANDS",
        "COCOS_KEELING_ISLANDS",
        "KEELING_ISLANDS",
        "COCOS_ISLANDS",
        "CHRISTMAS_ISLAND",
        "HEARD_ISLAND_AND_MCDONALD_ISLANDS",
        "HEARD_ISLAND",
        "MCDONALD_ISLAND",
        "MCDONALD_ISLANDS",
        "JERVIS_BAY_TERRITORY",
        "JERVIS_BAY",
        "NORFOLK_ISLAND",
        "NEW_SOUTH_WALES",
        "NSW",
        "NORTHERN_TERRITORY",
        "QUEENSLAND",
        "SOUTH_AUSTRALIA",
        "TASMANIA",
        "WESTERN_AUSTRALIA"
    ]
    australianStateAlphaToPopulation = {
        "AU-ACT": 431826,
        "AU-AQ": 60,
        "AU-CC": 547,
        "AU-CX": 1938,
        "AU-HM": 0,
        "AU-JBT": 405,
        "AU-NF": 1758,
        "AU-NSW": 8176368,
        "AU-NT": 247023,
        "AU-QLD": 5206400,
        "AU-SA": 1771703,
        "AU-TAS": 541965,
        "AU-VIC": 6648564,
        "AU-WA": 2675797
    }
    australianStateAlphaToType = {
        "AU-ACT": "INTERNAL_TERRITORY",
        "AU-AQ": "EXTERNAL_TERRITORY",
        "AU-CC": "EXTERNAL_TERRITORY",
        "AU-CX": "EXTERNAL_TERRITORY",
        "AU-HM": "EXTERNAL_TERRITORY",
        "AU-JBT": "INTERNAL_TERRITORY",
        "AU-NF": "EXTERNAL_TERRITORY",
        "AU-NSW": "STATE",
        "AU-NT": "INTERNAL_TERRITORY",
        "AU-QLD": "STATE",
        "AU-SA": "STATE",
        "AU-TAS": "STATE",
        "AU-VIC": "STATE",
        "AU-WA": "STATE"
    }
    canadianProvinceAlphaList = [
        "CA-AB",
        "CA-BC",
        "CA-MB",
        "CA-NB",
        "CA-NL",
        "CA-NS",
        "CA-NT",
        "CA-NU",
        "CA-ON",
        "CA-PE",
        "CA-QC",
        "CA-SK",
        "CA-YT"
    ]
    canadianProvinceAlphaToAreaKM = {
        "CA-AB": 661848,
        "CA-BC": 944735,
        "CA-MB": 647797,
        "CA-NB": 72908,
        "CA-NL": 405212,
        "CA-NS": 55284,
        "CA-NT": 1346106,
        "CA-NU": 2093190,
        "CA-ON": 1076395,
        "CA-PE": 5660,
        "CA-QC": 1542056,
        "CA-SK": 651036,
        "CA-YT": 482443
    }
    canadianProvinceAlphaToCapital = {
        "CA-AB": "Edmonton",
        "CA-BC": "Victoria",
        "CA-MB": "Winnipeg",
        "CA-NB": "Fredericton",
        "CA-NL": "St. John's",
        "CA-NS": "Halifax",
        "CA-NT": "Yellowknife",
        "CA-NU": "Iqaluit",
        "CA-ON": "Toronto",
        "CA-PE": "Charlottetown",
        "CA-QC": "Quebec City",
        "CA-SK": "Regina",
        "CA-YT": "Whitehorse"
    }
    canadianProvinceAlphaToLargestCity = {
        "CA-AB": "Calgary",
        "CA-BC": "Vancouver",
        "CA-MB": "Winnipeg",
        "CA-NB": "Moncton",
        "CA-NL": "St. John's",
        "CA-NS": "Halifax",
        "CA-NT": "Yellowknife",
        "CA-NU": "Iqaluit",
        "CA-ON": "Toronto",
        "CA-PE": "Charlottetown",
        "CA-QC": "Montreal",
        "CA-SK": "Saskatoon",
        "CA-YT": "Whitehorse"
    }
    canadianProvinceAlphaToFlagURL = {
        "CA-AB": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Flag_of_Alberta.svg/2560px-Flag_of_Alberta.svg.png",
        "CA-BC": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Flag_of_British_Columbia.svg/1920px-Flag_of_British_Columbia.svg.png",
        "CA-MB": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Flag_of_Manitoba.svg/2560px-Flag_of_Manitoba.svg.png",
        "CA-NB": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Flag_of_New_Brunswick.svg/1920px-Flag_of_New_Brunswick.svg.png",
        "CA-NL": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Newfoundland_and_Labrador.svg/2560px-Flag_of_Newfoundland_and_Labrador.svg.png",
        "CA-NS": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Flag_of_Nova_Scotia.svg/2560px-Flag_of_Nova_Scotia.svg.png",
        "CA-NT": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_the_Northwest_Territories.svg/2560px-Flag_of_the_Northwest_Territories.svg.png",
        "CA-NU": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Flag_of_Nunavut.svg/2560px-Flag_of_Nunavut.svg.png",
        "CA-ON": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Ontario.svg/2560px-Flag_of_Ontario.svg.png",
        "CA-PE": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Flag_of_Prince_Edward_Island.svg/1920px-Flag_of_Prince_Edward_Island.svg.png",
        "CA-QC": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/1920px-Flag_of_Quebec.svg.png",
        "CA-SK": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Flag_of_Saskatchewan.svg/2560px-Flag_of_Saskatchewan.svg.png",
        "CA-YT": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Flag_of_Yukon.svg/2560px-Flag_of_Yukon.svg.png"
    }
    canadianProvinceAlphaToGDP = {
        "CA-AB": 282060000000,
        "CA-BC": 247030000000,
        "CA-MB": 58984000000,
        "CA-NB": 30554000000,
        "CA-NL": 28247000000,
        "CA-NS": 37236000000,
        "CA-NT": 3630000000,
        "CA-NU": 2948000000,
        "CA-ON": 712556000000,
        "CA-PE": 6010000000,
        "CA-QC": 367733000000,
        "CA-SK": 66234000000,
        "CA-YT": 2521000000
    }
    canadianProvinceNameToAlpha = {
        "ALBERTA": "CA-AB",
        "BRITISH_COLUMBIA": "CA-AB",
        "MANITOBA": "CA-MB",
        "NEWFOUNDLAND_AND_LABRADOR": "CA-NL",
        "NEW_BRUNSWICK": "CA-NB",
        "NORTHWEST_TERRITORIES": "CA-NT",
        "NOVA_SCOTIA": "CA-NS",
        "NUNAVUT": "CA-NU",
        "ONTARIO": "CA-ON",
        "PRINCE_EDWARD_ISLAND": "CA-PE",
        "PEI": "CA-PE",
        "QUEBEC": "CA-QC",
        "SASKATCHEWAN": "CA-SK",
        "YUKON_TERRITORIES": "CA-YT",
        "YUKON": "CA-YT"
    }
    canadianProvinceAlphaToName = {
        "CA-AB": "Alberta",
        "CA-BC": "British Columbia",
        "CA-MB": "Manitoba",
        "CA-NB": "New Brunswick",
        "CA-NL": "Newfoundland and Labrador",
        "CA-NS": "Nova Scotia",
        "CA-NT": "Northwest Territories",
        "CA-NU": "Nunavut",
        "CA-ON": "Ontario",
        "CA-PE": "Prince Edward Island",
        "CA-QC": "Quebec",
        "CA-SK": "Saskatchewan",
        "CA-YT": "Yukon Territories"
    }
    canadianProvinceNameList = [
        "ALBERTA",
        "BRITISH_COLUMBIA",
        "MANITOBA",
        "NEWFOUNDLAND_AND_LABRADOR",
        "NEW_BRUNSWICK",
        "NORTHWEST_TERRITORIES",
        "NOVA_SCOTIA",
        "NUNAVUT",
        "ONTARIO",
        "PRINCE_EDWARD_ISLAND",
        "PEI",
        "QUEBEC",
        "SASKATCHEWAN",
        "YUKON_TERRITORIES",
        "YUKON"
    ]
    canadianProvinceAlphaToPopulation = {
        "CA-AB": 4067175,
        "CA-BC": 4648055,
        "CA-MB": 1278365,
        "CA-NB": 747101,
        "CA-NL": 519716,
        "CA-NS": 923598,
        "CA-NT": 41786,
        "CA-NU": 35944,
        "CA-ON": 13448494,
        "CA-PE": 142907,
        "CA-QC": 8164361,
        "CA-SK": 1098352,
        "CA-YT": 35874
    }
    canadianProvinceAlphaToType = {
        "CA-AB": "PROVINCE",
        "CA-BC": "PROVINCE",
        "CA-MB": "PROVINCE",
        "CA-NB": "PROVINCE",
        "CA-NL": "PROVINCE",
        "CA-NS": "PROVINCE",
        "CA-NT": "TERRITORY",
        "CA-NU": "TERRITORY",
        "CA-ON": "PROVINCE",
        "CA-PE": "PROVINCE",
        "CA-QC": "PROVINCE",
        "CA-SK": "PROVINCE",
        "CA-YT": "TERRITORY"
    }
    continents = ["NORTH_AMERICA", "SOUTH_AMERICA", "EUROPE", "AFRICA", "ASIA", "OCEANIA", "ANTARCTICA"]
    continentToAlpha = {
        'AFRICA': ['AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'COD', 'COG', 'COM', 'CPV', 'DJI', 'DZA', 'EGY',
                   'ERI', 'ETH', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG',
                   'MLI', 'MOZ', 'MRT', 'MUS', 'MWI', 'MYT', 'NAM', 'NER', 'NGA', 'REU', 'RWA', 'SDN', 'SEN', 'SHN',
                   'SLE', 'SOM', 'SSD', 'STP', 'SWZ', 'SYC', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'ZAF', 'ZMB', 'ZWE'],
        'ANTARCTICA': ['ATF', 'HMD', 'SGS'],
        'ASIA': ['AFG', 'ARE', 'ARM', 'AZE', 'BGD', 'BHR', 'BRN', 'BTN', 'CHN', 'CMR', 'CYP', 'GEO', 'HKG', 'IND',
                 'IOT', 'IRN', 'IRQ', 'ISR', 'JOR', 'JPN', 'KAZ', 'KGZ', 'KHM', 'KWT', 'LAO', 'LBN', 'LKA', 'MAC',
                 'MDV', 'MMR', 'MNG', 'MYS', 'NPL', 'OMN', 'PAK', 'PHL', 'PRK', 'PSE', 'QAT', 'RUS', 'SAU', 'SGP',
                 'SYR', 'THA', 'TJK', 'TKM', 'TWN', 'UZB', 'VNM', 'YEM'],
        'EUROPE': ['ALA', 'ALB', 'AND', 'AUT', 'BEL', 'BGR', 'BIH', 'BLR', 'CHE', 'CZE', 'DEU', 'DNK', 'ESP', 'EST',
                   'FIN', 'FRA', 'FRO', 'GBR', 'GGY', 'GIB', 'GRC', 'HRV', 'HUN', 'IMN', 'IRL', 'ISL', 'ITA', 'JEY',
                   'LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MDA', 'MKD', 'MLT', 'MNE', 'NLD', 'NOR', 'POL', 'PRT', 'ROU',
                   'SJM', 'SMR', 'SRB', 'SVK', 'SVN', 'SWE', 'TUR', 'UKR', 'VAT'],
        'NORTH_AMERICA': ['AIA', 'ATG', 'BES', 'BHS', 'BLM', 'BLZ', 'BMU', 'BRB', 'CAN', 'CRI', 'CUB', 'CYM', 'DMA',
                          'DOM', 'GLP', 'GRD', 'GRL', 'GTM', 'HND', 'HTI', 'JAM', 'KNA', 'LCA', 'MAF', 'MEX', 'MSR',
                          'MTQ', 'NIC', 'PAN', 'PRI', 'SLV', 'SPM', 'SXM', 'TTO', 'USA', 'VCT', 'VGB', 'VIR'],
        'OCEANIA': ['ASM', 'AUS', 'COK', 'CXR', 'FJI', 'FSM', 'GUM', 'IDN', 'KIR', 'MHL', 'MNP', 'NCL', 'NFK', 'NIU',
                    'NRU', 'NZL', 'PCN', 'PLW', 'PNG', 'PYF', 'SLB', 'TKL', 'TLS', 'TON', 'TUV', 'UMI', 'VUT', 'WLF',
                    'WSM'],
        'SOUTH_AMERICA': ['ABW', 'ARG', 'BOL', 'BRA', 'CHL', 'COL', 'CUW', 'ECU', 'FLK', 'GUF', 'GUY', 'PER', 'PRY',
                          'SUR', 'URY', 'VEN']}
    continentToLargestCity = {
        "NORTH_AMERICA": {"CITY": "Mexico City", "COUNTRY": "MEX"},
        "SOUTH_AMERICA": {"CITY": "Sao Paulo", "COUNTRY": "BRA"},
        "EUROPE": {"CITY": "Istanbul", "COUNTRY": "TUR"},
        "AFRICA": {"CITY": "Kinhasa", "COUNTRY": "COD"},
        "ASIA": {"CITY": "Tokyo", "COUNTRY": "JPN"},
        "OCEANIA": {"CITY": "Jakarta", "COUNTRY": "IDN"},
        "ANTARCTICA": {"CITY": "McMurdo Station", "COUNTRY": "ATA"}
    }
    countryNameList = [
        "Aruba",
        "Afghanistan",
        "Angola",
        "Anguilla",
        "Åland Islands",
        "Albania",
        "Andorra",
        "United Arab Emirates",
        "Argentina",
        "Armenia",
        "American Samoa",
        "Antarctica",
        "French Southern Territories",
        "Antigua and Barbuda",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Burundi",
        "Belgium",
        "Benin",
        "Bonaire, Sint Eustatius and Saba",
        "Burkina Faso",
        "Bangladesh",
        "Bulgaria",
        "Bahrain",
        "Bahamas",
        "Bosnia and Herzegovina",
        "Saint Barthélemy",
        "Belarus",
        "Belize",
        "Bermuda",
        "Bolivia (Plurinational State of)",
        "Brazil",
        "Barbados",
        "Brunei Darussalam",
        "Bhutan",
        "Bouvet Island",
        "Botswana",
        "Central African Republic",
        "Canada",
        "Cocos (Keeling) Islands",
        "Switzerland",
        "Chile",
        "China",
        "Côte d'Ivoire",
        "Cameroon",
        "Congo (Democratic Republic of the)",
        "Congo",
        "Cook Islands",
        "Colombia",
        "Comoros",
        "Cabo Verde",
        "Costa Rica",
        "Cuba",
        "Curaçao",
        "Christmas Island",
        "Cayman Islands",
        "Cyprus",
        "Czech Republic",
        "Germany",
        "Djibouti",
        "Dominica",
        "Denmark",
        "Dominican Republic",
        "Algeria",
        "Ecuador",
        "Egypt",
        "Eritrea",
        "Western Sahara",
        "Spain",
        "Estonia",
        "Ethiopia",
        "Finland",
        "Fiji",
        "Falkland Islands (Malvinas)",
        "France",
        "Faroe Islands",
        "Micronesia (Federated States of)",
        "Gabon",
        "United Kingdom of Great Britain and Northern Ireland",
        "Georgia",
        "Guernsey",
        "Ghana",
        "Gibraltar",
        "Guinea",
        "Guadeloupe",
        "Gambia",
        "Guinea-Bissau",
        "Equatorial Guinea",
        "Greece",
        "Grenada",
        "Greenland",
        "Guatemala",
        "French Guiana",
        "Guam",
        "Guyana",
        "Hong Kong",
        "Heard Island and McDonald Islands",
        "Honduras",
        "Croatia",
        "Haiti",
        "Hungary",
        "Indonesia",
        "Isle of Man",
        "India",
        "British Indian Ocean Territory",
        "Ireland",
        "Iran (Islamic Republic of)",
        "Iraq",
        "Iceland",
        "Israel",
        "Italy",
        "Jamaica",
        "Jersey",
        "Jordan",
        "Japan",
        "Kazakhstan",
        "Kenya",
        "Kyrgyzstan",
        "Cambodia",
        "Kiribati",
        "Saint Kitts and Nevis",
        "Korea (Republic of)",
        "Kuwait",
        "Lao People's Democratic Republic",
        "Lebanon",
        "Liberia",
        "Libya",
        "Saint Lucia",
        "Liechtenstein",
        "Sri Lanka",
        "Lesotho",
        "Lithuania",
        "Luxembourg",
        "Latvia",
        "Macao",
        "Saint Martin (French part)",
        "Morocco",
        "Monaco",
        "Moldova (Republic of)",
        "Madagascar",
        "Maldives",
        "Mexico",
        "Marshall Islands",
        "Macedonia (the former Yugoslav Republic of)",
        "Mali",
        "Malta",
        "Myanmar",
        "Montenegro",
        "Mongolia",
        "Northern Mariana Islands",
        "Mozambique",
        "Mauritania",
        "Montserrat",
        "Martinique",
        "Mauritius",
        "Malawi",
        "Malaysia",
        "Mayotte",
        "Namibia",
        "New Caledonia",
        "Niger",
        "Norfolk Island",
        "Nigeria",
        "Nicaragua",
        "Niue",
        "Netherlands",
        "Norway",
        "Nepal",
        "Nauru",
        "New Zealand",
        "Oman",
        "Pakistan",
        "Panama",
        "Pitcairn",
        "Peru",
        "Philippines",
        "Palau",
        "Papua New Guinea",
        "Poland",
        "Puerto Rico",
        "Korea (Democratic People's Republic of)",
        "Portugal",
        "Paraguay",
        "Palestine",
        "Palestine, State of",
        "French Polynesia",
        "Qatar",
        "Réunion",
        "Romania",
        "Russian Federation",
        "Rwanda",
        "Saudi Arabia",
        "Sudan",
        "Senegal",
        "Singapore",
        "South Georgia and the South Sandwich Islands",
        "Saint Helena, Ascension and Tristan da Cunha",
        "Svalbard and Jan Mayen",
        "Solomon Islands",
        "Sierra Leone",
        "El Salvador",
        "San Marino",
        "Somalia",
        "Saint Pierre and Miquelon",
        "Serbia",
        "South Sudan",
        "Sao Tome and Principe",
        "Suriname",
        "Slovakia",
        "Slovenia",
        "Sweden",
        "Swaziland",
        "Sint Maarten (Dutch part)",
        "Seychelles",
        "Syrian Arab Republic",
        "Turks and Caicos Islands",
        "Chad",
        "Togo",
        "Thailand",
        "Tajikistan",
        "Tokelau",
        "Turkmenistan",
        "Timor-Leste",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Tuvalu",
        "Taiwan",
        "Tanzania, United Republic of",
        "Uganda",
        "Ukraine",
        "United States Minor Outlying Islands",
        "Uruguay",
        "United States Of America",
        "United States",
        "Uzbekistan",
        "Holy See",
        "Saint Vincent and the Grenadines",
        "Venezuela (Bolivarian Republic of)",
        "Virgin Islands (British)",
        "Virgin Islands (U.S.)",
        "Viet Nam",
        "Vanuatu",
        "Wallis and Futuna",
        "Samoa",
        "Yemen",
        "South Africa",
        "Zambia",
        "Zimbabwe"
    ]
    nameToAlpha3 = {
        "AFGHANISTAN": "AFG",
        "ALAND_ISLANDS": "ALA",
        "ALBANIA": "ALB",
        "ALGERIA": "DZA",
        "AMERICAN_SAMOA": "ASM",
        "ANDORRA": "AND",
        "ANGOLA": "AGO",
        "ANGUILLA": "AIA",
        "ANTARCTICA": "ATA",
        "ANTIGUA_AND_BARBUDA": "ATG",
        "ARGENTINA": "ARG",
        "ARMENIA": "ARM",
        "ARUBA": "ABW",
        "AUSTRALIA": "AUS",
        "AUSTRIA": "AUT",
        "AZERBAIJAN": "AZE",
        "BAHAMAS": "BHS",
        "BAHRAIN": "BHR",
        "BANGLADESH": "BGD",
        "BARBADOS": "BRB",
        "BELARUS": "BLR",
        "BELGIUM": "BEL",
        "BELIZE": "BLZ",
        "BENIN": "BEN",
        "BERMUDA": "BMU",
        "BHUTAN": "BTN",
        "BOLIVARIAN_REPUBLIC_OF_VENEZUELA": "VEN",
        "BOLIVIA": "BOL",
        "BONAIRE,_SINT_EUSTATIUS_AND_SABA": "BES",
        "BONAIRE_SINT_EUSTATIUS_AND_SABA": "BES",
        "BONAIRE": "BES",
        "BOSNIA_AND_HERZEGOVINA": "BIH",
        "BOTSWANA": "BWA",
        "BRAZIL": "BRA",
        "BRITISH_INDIAN_OCEAN_TERRITORY": "IOT",
        "BRITISH_VIRGIN_ISLANDS": "VGB",
        "BRUNEI": "BRN",
        "BULGARIA": "BGR",
        "BURKINA_FASO": "BFA",
        "BURUNDI": "BDI",
        "CABO_VERDE": "CPV",
        "CAMBODIA": "KHM",
        "CAMEROON": "CMR",
        "CANADA": "CAN",
        "CAYMAN_ISLANDS": "CYM",
        "CENTRAL_AFRICAN_REPUBLIC": "CAF",
        "CHAD": "TCD",
        "CHILE": "CHL",
        "CHINA": "CHN",
        "CHRISTMAS_ISLAND": "CXR",
        "COCOS_(KEELING)_ISLANDS": "CCK",
        "COLOMBIA": "COL",
        "COMOROS": "COM",
        "CONGO": "COG",
        "CONGO_(DEMOCRATIC_REPUBLIC_OF_THE)": "COD",
        "COOK_ISLANDS": "COK",
        "COSTA_RICA": "CRI",
        "CROATIA": "HRV",
        "CUBA": "CUB",
        "CURACAO": "CUW",
        "CYPRUS": "CYP",
        "CZECH_REPUBLIC": "CZE",
        "CÔTE_D'IVOIRE": "CIV",
        "DEMOCRATIC_PEOPLE'S_REPUBLIC_OF_KOREA": "PRK",
        "DEMOCRATIC_REPUBLIC_OF_THE_CONGO": "COD",
        "DRC": "COD",
        "DENMARK": "DNK",
        "DJIBOUTI": "DJI",
        "DOMINICA": "DMA",
        "DOMINICAN_REPUBLIC": "DOM",
        "ECUADOR": "ECU",
        "EGYPT": "EGY",
        "EL_SALVADOR": "SLV",
        "EQUATORIAL_GUINEA": "GNQ",
        "ERITREA": "ERI",
        "ESTONIA": "EST",
        "ETHIOPIA": "ETH",
        "FALKLAND_ISLANDS": "FLK",
        "FALKLAND_ISLANDS_(MALVINAS)": "FLK",
        "FAROE_ISLANDS": "FRO",
        "FEDERATED_STATES_OF_MICRONESIA": "FSM",
        "FIJI": "FJI",
        "FINLAND": "FIN",
        "FRANCE": "FRA",
        "FRENCH_GUIANA": "GUF",
        "FRENCH_POLYNESIA": "PYF",
        "FRENCH_SOUTHERN_TERRITORIES": "ATF",
        "GABON": "GAB",
        "GAMBIA": "GMB",
        "GAZA": "PSE",
        "GAZA_STRIP": "PSE",
        "GEORGIA": "GEO",
        "GERMANY": "DEU",
        "GHANA": "GHA",
        "GIBRALTAR": "GIB",
        "GREECE": "GRC",
        "GREENLAND": "GRL",
        "GRENADA": "GRD",
        "GUADELOUPE": "GLP",
        "GUAM": "GUM",
        "GUATEMALA": "GTM",
        "GUERNSEY": "GGY",
        "GUINEA": "GIN",
        "GUINEA-BISSAU": "GNB",
        "GUYANA": "GUY",
        "HAITI": "HTI",
        "HEARD_ISLAND_AND_MCDONALD_ISLANDS": "HMD",
        "HOLY_SEE": "VAT",
        "HONDURAS": "HND",
        "HONG_KONG": "HKG",
        "HUNGARY": "HUN",
        "ICELAND": "ISL",
        "INDIA": "IND",
        "INDONESIA": "IDN",
        "IRAN": "IRN",
        "IRAN_(ISLAMIC_REPUBLIC_OF)": "IRN",
        "IRAQ": "IRQ",
        "IRELAND": "IRL",
        "ISLAMIC_REPUBLIC_OF_IRAN": "IRN",
        "ISLE_OF_MAN": "IMN",
        "ISRAEL": "ISR",
        "ITALY": "ITA",
        "IVORY_COAST": "CIV",
        "JAMAICA": "JAM",
        "JAPAN": "JPN",
        "JERSEY": "JEY",
        "JORDAN": "JOR",
        "KAZAKHSTAN": "KAZ",
        "KENYA": "KEN",
        "KIRIBATI": "KIR",
        "KOREA_(DEMOCRATIC_PEOPLE'S_REPUBLIC_OF)": "PRK",
        "KOREA_(REPUBLIC_OF)": "KOR",
        "KUWAIT": "KWT",
        "KYRGYZSTAN": "KGZ",
        "LAOS": "LAO",
        "LAO_PEOPLE'S_DEMOCRATIC_REPUBLIC": "LAO",
        "LAS_MALVINAS": "FLK",
        "LATVIA": "LVA",
        "LEBANON": "LBN",
        "LESOTHO": "LSO",
        "LIBERIA": "LBR",
        "LIBYA": "LBY",
        "LIECHTENSTEIN": "LIE",
        "LITHUANIA": "LTU",
        "LUXEMBOURG": "LUX",
        "MACAO": "MAC",
        "MACEDONIA": "MKD",
        "MACEDONIA_(THE_FORMER_YUGOSLAV_REPUBLIC_OF)": "MKD",
        "MADAGASCAR": "MDG",
        "MALAWI": "MWI",
        "MALAYSIA": "MYS",
        "MALDIVES": "MDV",
        "MALI": "MLI",
        "MALTA": "MLT",
        "MALVINAS": "FLK",
        "MARSHALL_ISLANDS": "MHL",
        "MARTINIQUE": "MTQ",
        "MAURITANIA": "MRT",
        "MAURITIUS": "MUS",
        "MAYOTTE": "MYT",
        "MEXICO": "MEX",
        "MICRONESIA": "FSM",
        "MICRONESIA_(FEDERATED_STATES_OF)": "FSM",
        "MOLDOVA": "MDA",
        "MOLDOVA_(REPUBLIC_OF)": "MDA",
        "MONACO": "MCO",
        "MONGOLIA": "MNG",
        "MONTENEGRO": "MNE",
        "MONTSERRAT": "MSR",
        "MOROCCO": "MAR",
        "MOZAMBIQUE": "MOZ",
        "MYANMAR": "MMR",
        "NAMIBIA": "NAM",
        "NAURU": "NRU",
        "NEPAL": "NPL",
        "NETHERLANDS": "NLD",
        "NEW_CALEDONIA": "NCL",
        "NEW_ZEALAND": "NZL",
        "NICARAGUA": "NIC",
        "NIGER": "NER",
        "NIGERIA": "NGA",
        "NIUE": "NIU",
        "NORFOLK_ISLAND": "NFK",
        "NORTHERN_MARIANA_ISLANDS": "MNP",
        "NORTH_KOREA": "PRK",
        "NORWAY": "NOR",
        "OMAN": "OMN",
        "PAKISTAN": "PAK",
        "PALAU": "PLW",
        "PALESTINE": "PSE",
        "PALESTINE,_STATE_OF": "PSE",
        "PANAMA": "PAN",
        "PAPUA_NEW_GUINEA": "PNG",
        "PARAGUAY": "PRY",
        "PERU": "PER",
        "PHILIPPINES": "PHL",
        "PITCAIRN": "PCN",
        "POLAND": "POL",
        "PORTUGAL": "PRT",
        "PUERTO_RICO": "PRI",
        "QATAR": "QAT",
        "REPUBLIC_OF_KOREA": "KOR",
        "REPUBLIC_OF_MOLDOVA": "MDA",
        "REUNION": "REU",
        "ROMANIA": "ROU",
        "RUSSIA": "RUS",
        "RUSSIAN_FEDERATION": "RUS",
        "RWANDA": "RWA",
        "RÃ©UNION": "REU",
        "SAINT_BARTHELEMY": "BLM",
        "SAINT_BARTHÃ©LEMY": "BLM",
        "SAINT_HELENA,_ASCENSION_AND_TRISTAN_DA_CUNHA": "SHN",
        "SAINT_KITTS_AND_NEVIS": "KNA",
        "SAINT_LUCIA": "LCA",
        "SAINT_MARTIN": "MAF",
        "SAINT_MARTIN_(FRENCH_PART)": "MAF",
        "SAINT_PIERRE_AND_MIQUELON": "SPM",
        "SAINT_VINCENT_AND_THE_GRENADINES": "VCT",
        "SAMOA": "WSM",
        "SAN_MARINO": "SMR",
        "SAO_TOME_AND_PRINCIPE": "STP",
        "SAUDI_ARABIA": "SAU",
        "SENEGAL": "SEN",
        "SERBIA": "SRB",
        "SEYCHELLES": "SYC",
        "SIERRA_LEONE": "SLE",
        "SINGAPORE": "SGP",
        "SINT_MAARTEN": "SXM",
        "SINT_MAARTEN_(DUTCH_PART)": "SXM",
        "SLOVAKIA": "SVK",
        "SLOVENIA": "SVN",
        "SOLOMON_ISLANDS": "SLB",
        "SOMALIA": "SOM",
        "SOUTH_AFRICA": "ZAF",
        "SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS": "SGS",
        "SOUTH_KOREA": "KOR",
        "SOUTH_SUDAN": "SSD",
        "SPAIN": "ESP",
        "SRI_LANKA": "LKA",
        "STATE_OF_PALESTINE": "PSE",
        "SUDAN": "SDN",
        "SURINAME": "SUR",
        "SVALBARD_AND_JAN_MAYEN": "SJM",
        "SWAZILAND": "SWZ",
        "SWEDEN": "SWE",
        "SWITZERLAND": "CHE",
        "SYRIA": "SYR",
        "SYRIAN_ARAB_REPUBLIC": "SYR",
        "TAIWAN": "TWN",
        "TAJIKISTAN": "TJK",
        "TANZANIA": "TZA",
        "TANZANIA,_UNITED_REPUBLIC_OF": "TZA",
        "THAILAND": "THA",
        "THE_FORMER_YUGOSLAV_REPUBLIC_OF_MACEDONIA": "MKD",
        "THE_VATICAN": "VAT",
        "TIMOR-LESTE": "TLS",
        "TOGO": "TGO",
        "TOKELAU": "TKL",
        "TONGA": "TON",
        "TRINIDAD_AND_TOBAGO": "TTO",
        "TUNISIA": "TUN",
        "TURKEY": "TUR",
        "TURKMENISTAN": "TKM",
        "TURKS_AND_CAICOS_ISLANDS": "TCA",
        "TUVALU": "TUV",
        "U.S._VIRGIN_ISLANDS": "VIR",
        "UGANDA": "UGA",
        "UKRAINE": "UKR",
        "UNITED_ARAB_EMIRATES": "ARE",
        "UNITED_KINGDOM": "GBR",
        "UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND": "GBR",
        "UNITED_REPUBLIC_OF_TANZANIA": "TZA",
        "UNITED_STATES": "USA",
        "UNITED_STATES_MINOR_OUTLYING_ISLANDS": "UMI",
        "UNITED_STATES_OF_AMERICA": "USA",
        "UNITED_STATES_VIRGIN_ISLANDS": "VIR",
        "URUGUAY": "URY",
        "US_VIRGIN_ISLANDS": "VIR",
        "UZBEKISTAN": "UZB",
        "VANUATU": "VUT",
        "VATICAN": "VAT",
        "VATICAN_CITY": "VAT",
        "VENEZUELA": "VEN",
        "VENEZUELA_(BOLIVARIAN_REPUBLIC_OF)": "VEN",
        "VIETNAM": "VNM",
        "VIET_NAM": "VNM",
        "VIRGIN_ISLANDS_(BRITISH)": "VGB",
        "VIRGIN_ISLANDS_(U.S.)": "VIR",
        "WALLIS_AND_FUTUNA": "WLF",
        "WESTERN_SAHARA": "ESH",
        "WEST_BANK": "PSE",
        "YEMEN": "YEM",
        "ZAMBIA": "ZMB",
        "ZIMBABWE": "ZWE",
        "Ã…LAND_ISLANDS": "ALA"
    }
    southAfricanProvinceAlphaList = [
        "ZA-EC",
        "ZA-FS",
        "ZA-GP",
        "ZA-KZN",
        "ZA-LP",
        "ZA-MP",
        "ZA-NC",
        "ZA-NW",
        "ZA-WC"
    ]
    southAfricanProvinceAlphaToAreaKM = {
        "ZA-EC": 168966,
        "ZA-FS": 129825,
        "ZA-GP": 18178,
        "ZA-KZN": 94361,
        "ZA-LP": 125754,
        "ZA-MP": 76495,
        "ZA-NC": 372889,
        "ZA-NW": 104882,
        "ZA-WC": 129462
    }
    southAfricanProvinceAlphaToCapital = {
        "ZA-EC": "Bhisho",
        "ZA-FS": "Bloemfontein",
        "ZA-GP": "Johannesburg",
        "ZA-KZN": "Pietermaritzburg",
        "ZA-LP": "Polokwane",
        "ZA-MP": "Mbombela",
        "ZA-NC": "Kimberley",
        "ZA-NW": "Mahikeng",
        "ZA-WC": "Cape Town"
    }
    southAfricanProvinceAlphaToLargestCity = {
        "ZA-EC": "Gqeberha",
        "ZA-FS": "Bloemfontein",
        "ZA-GP": "Johannesburg",
        "ZA-KZN": "Durban",
        "ZA-LP": "Polokwane",
        "ZA-MP": "Mbombela",
        "ZA-NC": "Kimberley",
        "ZA-NW": "Rustenburg",
        "ZA-WC": "Cape Town"
    }
    southAfricanProvinceAlphaToFlagURL = {
        "ZA-EC": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1a/Eastern_Cape_arms.svg/1920px-Eastern_Cape_arms.svg.png",
        "ZA-FS": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/Coat_of_arms_of_the_Free_State.svg/1920px-Coat_of_arms_of_the_Free_State.svg.png",
        "ZA-GP": "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Gauteng_arms.svg/1920px-Gauteng_arms.svg.png",
        "ZA-KZN": "https://upload.wikimedia.org/wikipedia/en/thumb/7/79/KwaZulu-Natal_coat_of_arms.svg/1280px-KwaZulu-Natal_coat_of_arms.svg.png",
        "ZA-LP": "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Limpopo_arms.svg/1280px-Limpopo_arms.svg.png",
        "ZA-MP": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_Mpumalanga_Province.svg/1920px-Flag_of_Mpumalanga_Province.svg.png",
        "ZA-NC": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Northern_Cape_coat_of_arms.svg/1920px-Northern_Cape_coat_of_arms.svg.png",
        "ZA-NW": "https://upload.wikimedia.org/wikipedia/en/thumb/4/49/North_West_arms.svg/1280px-North_West_arms.svg.png",
        "ZA-WC": "https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/Coat_of_arms_of_the_Western_Cape.svg/1920px-Coat_of_arms_of_the_Western_Cape.svg.png"
    }
    southAfricanProvinceAlphaToGDP = {
        "ZA-EC": 17944581200,
        "ZA-FS": 11829260800,
        "ZA-GP": 78574412000,
        "ZA-KZN": 37191870800,
        "ZA-LP": 16903756800,
        "ZA-MP": 17756985400,
        "ZA-NC": 4681143600,
        "ZA-NW": 15727516000,
        "ZA-WC": 31948861000
    }
    southAfricanProvinceNameToAlpha = {
        "EASTERN_CAPE": "ZA-EC",
        "FREE_STATE": "ZA-FS",
        "GAUTENG": "ZA-GP",
        "KWAZULU-NATAL": "ZA-KZN",
        "KWAZULU_NATAL": "ZA-KZN",
        "LIMPOPO": "ZA-LP",
        "MPUMALANGA": "ZA-MP",
        "NORTH_WEST": "ZA-NW",
        "NORTHWEST": "ZA-NW",
        "NORTHERN_CAPE": "ZA-NC",
        "WESTERN_CAPE": "ZA-WC"
    }
    southAfricanProvinceAlphaToName = {
        "ZA-EC": "Eastern Cape",
        "ZA-FS": "Free State",
        "ZA-GP": "Gauteng",
        "ZA-KZN": "KwaZulu-Natal",
        "ZA-LP": "Limpopo",
        "ZA-MP": "Mpumalanga",
        "ZA-NC": "Northern Cape",
        "ZA-NW": "North West",
        "ZA-WC": "Western Cape"
    }
    southAfricanProvinceNameList = [
        "EASTERN_CAPE",
        "FREE_STATE",
        "GAUTENG",
        "KWAZULU-NATAL",
        "KWAZULU_NATAL",
        "LIMPOPO",
        "MPUMALANGA",
        "NORTH_WEST",
        "NORTHWEST",
        "NORTHERN_CAPE",
        "WESTERN_CAPE"
    ]
    southAfricanProvinceAlphaToPopulation = {
        "ZA-EC": 6562053,
        "ZA-FS": 2745590,
        "ZA-GP": 12272263,
        "ZA-KZN": 10267300,
        "ZA-LP": 5404868,
        "ZA-MP": 4039939,
        "ZA-NC": 1145861,
        "ZA-NW": 3509953,
        "ZA-WC": 5822734
    }
    southAfricanProvinceAlphaToType = {
        "ZA-EC": "PROVINCE",
        "ZA-FS": "PROVINCE",
        "ZA-GP": "PROVINCE",
        "ZA-KZN": "PROVINCE",
        "ZA-LP": "PROVINCE",
        "ZA-MP": "PROVINCE",
        "ZA-NC": "PROVINCE",
        "ZA-NW": "PROVINCE",
        "ZA-WC": "PROVINCE"
    }
    usaStateAlphaList = [
        "US-AL",
        "US-AK",
        "US-AZ",
        "US-AR",
        "US-AS",
        "US-CA",
        "US-CO",
        "US-CT",
        "US-DC",
        "US-DE",
        "US-FL",
        "US-GA",
        "US-GU",
        "US-HI",
        "US-ID",
        "US-IL",
        "US-IN",
        "US-IA",
        "US-KS",
        "US-KY",
        "US-LA",
        "US-ME",
        "US-MD",
        "US-MA",
        "US-MI",
        "US-MN",
        "US-MS",
        "US-MO",
        "US-MT",
        "US-MP",
        "US-NE",
        "US-NV",
        "US-NH",
        "US-NJ",
        "US-NM",
        "US-NY",
        "US-NC",
        "US-ND",
        "US-OH",
        "US-OK",
        "US-OR",
        "US-PA",
        "US-PR",
        "US-RI",
        "US-SC",
        "US-SD",
        "US-TN",
        "US-TX",
        "US-UT",
        "US-VT",
        "US-VA",
        "US-VI",
        "US-WA",
        "US-WV",
        "US-WI",
        "US-WY"
    ]
    usaStateAlphaToAreaKM = {
        "US-AL": 135767,
        "US-AK": 1723337,
        "US-AZ": 295234,
        "US-AR": 137732,
        "US-AS": 1505,
        "US-CA": 423967,
        "US-CO": 269601,
        "US-CT": 14357,
        "US-DC": 177,
        "US-DE": 6446,
        "US-FL": 170312,
        "US-GA": 153910,
        "US-GU": 1478,
        "US-HI": 28313,
        "US-ID": 216443,
        "US-IL": 149995,
        "US-IN": 94326,
        "US-IA": 145746,
        "US-KS": 213100,
        "US-KY": 104656,
        "US-LA": 135659,
        "US-ME": 91633,
        "US-MD": 32131,
        "US-MA": 27336,
        "US-MI": 250487,
        "US-MN": 225163,
        "US-MS": 125438,
        "US-MO": 180540,
        "US-MT": 380831,
        "US-MP": 5117,
        "US-NE": 200330,
        "US-NV": 286380,
        "US-NH": 24214,
        "US-NJ": 22591,
        "US-NM": 314917,
        "US-NY": 141297,
        "US-NC": 139391,
        "US-ND": 183108,
        "US-OH": 116098,
        "US-OK": 181037,
        "US-OR": 254799,
        "US-PA": 119280,
        "US-PR": 13791,
        "US-RI": 4001,
        "US-SC": 82933,
        "US-SD": 199729,
        "US-TN": 109153,
        "US-TX": 695662,
        "US-UT": 219882,
        "US-VT": 24906,
        "US-VA": 110787,
        "US-VI": 1898,
        "US-WA": 184661,
        "US-WV": 62756,
        "US-WI": 169635,
        "US-WY": 253335
    }
    usaStateAlphaToCapital = {
        "US-AL": "Montgomery",
        "US-AK": "Juneau",
        "US-AZ": "Phoenix",
        "US-AR": "Little Rock",
        "US-AS": "Pago Pago",
        "US-CA": "Sacramento",
        "US-CO": "Denver",
        "US-CT": "Hartford",
        "US-DC": "Washington",
        "US-DE": "Dover",
        "US-FL": "Tallahassee",
        "US-GA": "Atlanta",
        "US-GU": "Hagatna",
        "US-HI": "Honolulu",
        "US-ID": "Boise",
        "US-IL": "Springfield",
        "US-IN": "Indianapolis",
        "US-IA": "Des Moines",
        "US-KS": "Topeka",
        "US-KY": "Frankfort",
        "US-LA": "Baton Rogue",
        "US-ME": "Augusta",
        "US-MD": "Annapolis",
        "US-MA": "Boston",
        "US-MI": "Lansing",
        "US-MN": "St. Paul",
        "US-MS": "Jackson",
        "US-MO": "Jefferson City",
        "US-MT": "Helena",
        "US-MP": "Saipan",
        "US-NE": "Lincoln",
        "US-NV": "Carson City",
        "US-NH": "Concord",
        "US-NJ": "Trenton",
        "US-NM": "Santa Fe",
        "US-NY": "Albany",
        "US-NC": "Raleigh",
        "US-ND": "Bismarck",
        "US-OH": "Columbus",
        "US-OK": "Oklahoma City",
        "US-OR": "Salem",
        "US-PA": "Harrisburg",
        "US-PR": "San Juan",
        "US-RI": "Providence",
        "US-SC": "Columbia",
        "US-SD": "Pierre",
        "US-TN": "Nashville",
        "US-TX": "Austin",
        "US-UT": "Salt Lake City",
        "US-VT": "Montpelier",
        "US-VA": "Richmond",
        "US-VI": "Charlotte Amalie",
        "US-WA": "Olympia",
        "US-WV": "Charleston",
        "US-WI": "Madison",
        "US-WY": "Cheyenne"
    }
    usaStateAlphaToLargestCity = {
        "US-AL": "Huntsville",
        "US-AK": "Anchorage",
        "US-AZ": "Phoenix",
        "US-AR": "Little Rock",
        "US-AS": "Tafuna",
        "US-CA": "Los Angeles",
        "US-CO": "Denver",
        "US-CT": "Bridgeport",
        "US-DC": "Washington",
        "US-DE": "Wilmington",
        "US-FL": "Jacksonville",
        "US-GA": "Atlanta",
        "US-GU": "Dededo",
        "US-HI": "Honolulu",
        "US-ID": "Boise",
        "US-IL": "Chicago",
        "US-IN": "Indianapolis",
        "US-IA": "Des Moines",
        "US-KS": "Wichita",
        "US-KY": "Louisville",
        "US-LA": "New Orleans",
        "US-ME": "Portland",
        "US-MD": "Baltimore",
        "US-MA": "Boston",
        "US-MI": "Detroit",
        "US-MN": "Minneapolis",
        "US-MS": "Jackson",
        "US-MO": "Kansas City",
        "US-MT": "Billings",
        "US-MP": "Saipan",
        "US-NE": "Omaha",
        "US-NV": "Las Vegas",
        "US-NH": "Manchester",
        "US-NJ": "Newark",
        "US-NM": "Albuquerque",
        "US-NY": "New York City",
        "US-NC": "Charlotte",
        "US-ND": "Fargo",
        "US-OH": "Columbus",
        "US-OK": "Oklahoma City",
        "US-OR": "Portland",
        "US-PA": "Philadelphia",
        "US-PR": "San Juan",
        "US-RI": "Providence",
        "US-SC": "Charleston",
        "US-SD": "Sioux Falls",
        "US-TN": "Nashville",
        "US-TX": "Houston",
        "US-UT": "Salt Lake City",
        "US-VT": "Burlington",
        "US-VA": "Virginia Beach",
        "US-VI": "Charlotte Amalie",
        "US-WA": "Seattle",
        "US-WV": "Charleston",
        "US-WI": "Milwaukee",
        "US-WY": "Cheyenne"
    }
    usaStateAlphaToFlagURL = {
        "US-AL": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Alabama.svg/1920px-Flag_of_Alabama.svg.png",
        "US-AK": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Alaska.svg/1920px-Flag_of_Alaska.svg.png",
        "US-AZ": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Arizona.svg/1920px-Flag_of_Arizona.svg.png",
        "US-AR": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Arkansas.svg/1920px-Flag_of_Arkansas.svg.png",
        "US-AS": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag_of_American_Samoa.svg/2560px-Flag_of_American_Samoa.svg.png",
        "US-CA": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_California.svg/1920px-Flag_of_California.svg.png",
        "US-CO": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Flag_of_Colorado.svg/1920px-Flag_of_Colorado.svg.png",
        "US-CT": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Flag_of_Connecticut.svg/1920px-Flag_of_Connecticut.svg.png",
        "US-DC": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_the_District_of_Columbia.svg/2560px-Flag_of_the_District_of_Columbia.svg.png",
        "US-DE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Flag_of_Delaware.svg/1920px-Flag_of_Delaware.svg.png",
        "US-FL": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Flag_of_Florida.svg/1920px-Flag_of_Florida.svg.png",
        "US-GA": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Flag_of_Georgia_%28U.S._state%29.svg/1920px-Flag_of_Georgia_%28U.S._state%29.svg.png",
        "US-GU": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Flag_of_Guam.svg/2560px-Flag_of_Guam.svg.png",
        "US-HI": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Flag_of_Hawaii.svg/2560px-Flag_of_Hawaii.svg.png",
        "US-ID": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_Idaho.svg/1920px-Flag_of_Idaho.svg.png",
        "US-IL": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Illinois.svg/1920px-Flag_of_Illinois.svg.png",
        "US-IN": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Flag_of_Indiana.svg/1920px-Flag_of_Indiana.svg.png",
        "US-IA": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Flag_of_Iowa.svg/1920px-Flag_of_Iowa.svg.png",
        "US-KS": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Flag_of_Kansas.svg/1920px-Flag_of_Kansas.svg.png",
        "US-KY": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Flag_of_Kentucky.svg/2560px-Flag_of_Kentucky.svg.png",
        "US-LA": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Flag_of_Louisiana.svg/1920px-Flag_of_Louisiana.svg.png",
        "US-ME": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Flag_of_Maine.svg/1920px-Flag_of_Maine.svg.png",
        "US-MD": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Flag_of_Maryland.svg/1920px-Flag_of_Maryland.svg.png",
        "US-MA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Flag_of_Massachusetts.svg/1920px-Flag_of_Massachusetts.svg.png",
        "US-MI": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Flag_of_Michigan.svg/1920px-Flag_of_Michigan.svg.png",
        "US-MN": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Minnesota.svg/1920px-Flag_of_Minnesota.svg.png",
        "US-MS": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_Mississippi.svg/1920px-Flag_of_Mississippi.svg.png",
        "US-MO": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Flag_of_Missouri.svg/2560px-Flag_of_Missouri.svg.png",
        "US-MT": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_Montana.svg/1920px-Flag_of_Montana.svg.png",
        "US-MP": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Flag_of_the_Northern_Mariana_Islands.svg/2560px-Flag_of_the_Northern_Mariana_Islands.svg.png",
        "US-NE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Flag_of_Nebraska.svg/1920px-Flag_of_Nebraska.svg.png",
        "US-NV": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Flag_of_Nevada.svg/1920px-Flag_of_Nevada.svg.png",
        "US-NH": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Flag_of_New_Hampshire.svg/1920px-Flag_of_New_Hampshire.svg.png",
        "US-NJ": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_New_Jersey.svg/1920px-Flag_of_New_Jersey.svg.png",
        "US-NM": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_New_Mexico.svg/1920px-Flag_of_New_Mexico.svg.png",
        "US-NY": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_New_York.svg/2560px-Flag_of_New_York.svg.png",
        "US-NC": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Flag_of_North_Carolina.svg/1920px-Flag_of_North_Carolina.svg.png",
        "US-ND": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Flag_of_North_Dakota.svg/1920px-Flag_of_North_Dakota.svg.png",
        "US-OH": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Ohio.svg/1920px-Flag_of_Ohio.svg.png",
        "US-OK": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Flag_of_Oklahoma.svg/1920px-Flag_of_Oklahoma.svg.png",
        "US-OR": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Oregon.svg/1920px-Flag_of_Oregon.svg.png",
        "US-PA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Flag_of_Pennsylvania.svg/1920px-Flag_of_Pennsylvania.svg.png",
        "US-PR": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Flag_of_Puerto_Rico.svg/1920px-Flag_of_Puerto_Rico.svg.png",
        "US-RI": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Rhode_Island.svg/1920px-Flag_of_Rhode_Island.svg.png",
        "US-SC": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Flag_of_South_Carolina.svg/1920px-Flag_of_South_Carolina.svg.png",
        "US-SD": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_South_Dakota.svg/1920px-Flag_of_South_Dakota.svg.png",
        "US-TN": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Tennessee.svg/1920px-Flag_of_Tennessee.svg.png",
        "US-TX": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Flag_of_Texas.svg/1920px-Flag_of_Texas.svg.png",
        "US-UT": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag_of_Utah.svg/1920px-Flag_of_Utah.svg.png",
        "US-VT": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Vermont.svg/1920px-Flag_of_Vermont.svg.png",
        "US-VA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Flag_of_Virginia.svg/1920px-Flag_of_Virginia.svg.png",
        "US-VI": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Flag_of_the_United_States_Virgin_Islands.svg/1920px-Flag_of_the_United_States_Virgin_Islands.svg.png",
        "US-WA": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Flag_of_Washington.svg/1920px-Flag_of_Washington.svg.png",
        "US-WV": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Flag_of_West_Virginia.svg/2560px-Flag_of_West_Virginia.svg.png",
        "US-WI": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Flag_of_Wisconsin.svg/1920px-Flag_of_Wisconsin.svg.png",
        "US-WY": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Wyoming.svg/1920px-Flag_of_Wyoming.svg.png"
    }
    usaStateAlphaToGDP = {
        "US-AL": 243555000000,
        "US-AK": 54020000000,
        "US-AZ": 400156000000,
        "US-AR": 143438000000,
        "US-AS": 638000000,
        "US-CA": 3290170000000,
        "US-CO": 416937000000,
        "US-CT": 294649000000,
        "US-DC": 151390000000,
        "US-DE": 79282000000,
        "US-FL": 1198913000000,
        "US-GA": 673072000000,
        "US-GU": 6311000000,
        "US-HI": 89661000000,
        "US-ID": 92300000000,
        "US-IL": 938216000000,
        "US-IN": 415344000000,
        "US-IA": 220929000000,
        "US-KS": 193139000000,
        "US-KY": 234311000000,
        "US-LA": 253315000000,
        "US-ME": 74604000000,
        "US-MD": 443729000000,
        "US-MA": 625113000000,
        "US-MI": 559479000000,
        "US-MN": 407395000000,
        "US-MS": 123781000000,
        "US-MO": 359034000000,
        "US-MT": 57919000000,
        "US-MP": 1182000000,
        "US-NE": 150507000000,
        "US-NV": 187394000000,
        "US-NH": 93891000000,
        "US-NJ": 671483000000,
        "US-NM": 108241000000,
        "US-NY": 1868224000000,
        "US-NC": 646207000000,
        "US-ND": 64978000000,
        "US-OH": 732117000000,
        "US-OK": 205559000000,
        "US-OR": 264113000000,
        "US-PA": 832704000000,
        "US-PR": 103138000000,
        "US-RI": 64170000000,
        "US-SC": 266079000000,
        "US-SD": 60810000000,
        "US-TN": 411689000000,
        "US-TX": 1950359000000,
        "US-UT": 212855000000,
        "US-VT": 36089000000,
        "US-VA": 586250000000,
        "US-VI": 4068000000,
        "US-WA": 661520000000,
        "US-WV": 85799000000,
        "US-WI": 363586000000,
        "US-WY": 41199000000
    }
    usaStateNameToAlpha = {
        "ALABAMA": "US-AL",
        "ALASKA": "US-AK",
        "ARIZONA": "US-AZ",
        "ARKANSAS": "US-AR",
        "AMERICAN_SAMOA": "US-AS",
        "CALIFORNIA": "US-CA",
        "COLORADO": "US-CO",
        "CONNECTICUT": "US-CT",
        "DISTRICT_OF_COLUMBIA": "US-DC",
        "DC": "US-DC",
        "WASHINGTON_DC": "US-DC",
        "DELAWARE": "US-DE",
        "FLORIDA": "US-FL",
        "GEORGIA": "US-GA",
        "GUAM": "US-GU",
        "HAWAII": "US-HI",
        "IDAHO": "US-ID",
        "ILLINOIS": "US-IL",
        "INDIANA": "US-IN",
        "IOWA": "US-IA",
        "KANSAS": "US-KS",
        "KENTUCKY": "US-KY",
        "LOUISIANA": "US-LA",
        "MAINE": "US-ME",
        "MARYLAND": "US-MD",
        "MASSACHUSETTS": "US-MA",
        "MICHIGAN": "US-MI",
        "MINNESOTA": "US-MN",
        "MISSISSIPPI": "US-MS",
        "MISSOURI": "US-MO",
        "MONTANA": "US-MT",
        "NORTHERN_MARIANA_ISLANDS": "US-MP",
        "NEBRASKA": "US-NE",
        "NEVADA": "US-NV",
        "NEW_HAMPSHIRE": "US-NH",
        "NEW_JERSEY": "US-NJ",
        "NEW_MEXICO": "US-NM",
        "NEW_YORK": "US-NY",
        "NORTH_CAROLINA": "US-NC",
        "NORTH_DAKOTA": "US-ND",
        "OHIO": "US-OH",
        "OKLAHOMA": "US-OK",
        "OREGON": "US-OR",
        "PENNSYLVANIA": "US-PA",
        "PUERTO_RICO": "US-PR",
        "RHODE_ISLAND": "US-RI",
        "SOUTH_CAROLINA": "US-SC",
        "SOUTH_DAKOTA": "US-SD",
        "TENNESSEE": "US-TN",
        "TEXAS": "US-TX",
        "UTAH": "US-UT",
        "VERMONT": "US-VT",
        "VIRGINIA": "US-VA",
        "US_VIRGIN_ISLANDS": "US-VI",
        "U.S._VIRGIN_ISLANDS": "US-VI",
        "VIRGIN_ISLANDS": "US-VI",
        "WASHINGTON": "US-WA",
        "WEST_VIRGINIA": "US-WV",
        "WISCONSIN": "US-WI",
        "WYOMING": "US-WY"
    }
    usaStateAlphaToName = {
        "US-AL": "Alabama",
        "US-AK": "Alaska",
        "US-AZ": "Arizona",
        "US-AR": "Arkansas",
        "US-AS": "American Samoa",
        "US-CA": "California",
        "US-CO": "Colorado",
        "US-CT": "Connecticut",
        "US-DC": "District of Columbia",
        "US-DE": "Delaware",
        "US-FL": "Florida",
        "US-GA": "Georgia",
        "US-GU": "Guam",
        "US-HI": "Hawaii",
        "US-ID": "Idaho",
        "US-IL": "Illinois",
        "US-IN": "Indiana",
        "US-IA": "Iowa",
        "US-KS": "Kansas",
        "US-KY": "Kentucky",
        "US-LA": "Louisiana",
        "US-ME": "Maine",
        "US-MD": "Maryland",
        "US-MA": "Massachusetts",
        "US-MI": "Michigan",
        "US-MN": "Minnesota",
        "US-MS": "Mississippi",
        "US-MO": "Missouri",
        "US-MT": "Montana",
        "US-MP": "Northern Mariana Islands",
        "US-NE": "Nebraska",
        "US-NV": "Nevada",
        "US-NH": "New Hampshire",
        "US-NJ": "New Jersey",
        "US-NM": "New Mexico",
        "US-NY": "New York",
        "US-NC": "North Carolina",
        "US-ND": "North Dakota",
        "US-OH": "Ohio",
        "US-OK": "Oklahoma",
        "US-OR": "Oregon",
        "US-PA": "Pennsylvania",
        "US-PR": "Puerto Rico",
        "US-RI": "Rhode Island",
        "US-SC": "South Carolina",
        "US-SD": "South Dakota",
        "US-TN": "Tennessee",
        "US-TX": "Texas",
        "US-UT": "Utah",
        "US-VT": "Vermont",
        "US-VA": "Virginia",
        "US-VI": "US Virgin Islands",
        "US-WA": "Washington",
        "US-WV": "West Virginia",
        "US-WI": "Wisconsin",
        "US-WY": "Wyoming"
    }
    usaStateNameList = [
        "ALABAMA",
        "ALASKA",
        "ARIZONA",
        "ARKANSAS",
        "AMERICAN_SAMOA",
        "CALIFORNIA",
        "COLORADO",
        "CONNECTICUT",
        "DISTRICT_OF_COLUMBIA",
        "DC",
        "WASHINGTON_DC",
        "DELAWARE",
        "FLORIDA",
        "GEORGIA",
        "GUAM",
        "HAWAII",
        "IDAHO",
        "ILLINOIS",
        "INDIANA",
        "IOWA",
        "KANSAS",
        "KENTUCKY",
        "LOUISIANA",
        "MAINE",
        "MARYLAND",
        "MASSACHUSETTS",
        "MICHIGAN",
        "MINNESOTA",
        "MISSISSIPPI",
        "MISSOURI",
        "MONTANA",
        "NORTHERN_MARIANA_ISLANDS",
        "NEBRASKA",
        "NEVADA",
        "NEW_HAMPSHIRE",
        "NEW_JERSEY",
        "NEW_MEXICO",
        "NEW_YORK",
        "NORTH_CAROLINA",
        "NORTH_DAKOTA",
        "OHIO",
        "OKLAHOMA",
        "OREGON",
        "PENNSYLVANIA",
        "PUERTO_RICO",
        "RHODE_ISLAND",
        "SOUTH_CAROLINA",
        "SOUTH_DAKOTA",
        "TENNESSEE",
        "TEXAS",
        "UTAH",
        "VERMONT",
        "VIRGINIA",
        "US_VIRGIN_ISLANDS",
        "U.S._VIRGIN_ISLANDS",
        "VIRGIN_ISLANDS",
        "WASHINGTON",
        "WEST_VIRGINIA",
        "WISCONSIN",
        "WYOMING"
    ]
    usaStateAlphaToPopulation = {
        "US-AL": 5024279,
        "US-AK": 733391,
        "US-AZ": 7151502,
        "US-AR": 3011524,
        "US-AS": 49437,
        "US-CA": 39538223,
        "US-CO": 5773714,
        "US-CT": 3605944,
        "US-DC": 689545,
        "US-DE": 989948,
        "US-FL": 21538187,
        "US-GA": 10711908,
        "US-GU": 168485,
        "US-HI": 1455271,
        "US-ID": 1839106,
        "US-IL": 12812508,
        "US-IN": 6785528,
        "US-IA": 3190369,
        "US-KS": 2937880,
        "US-KY": 4505836,
        "US-LA": 4657757,
        "US-ME": 1362359,
        "US-MD": 6177224,
        "US-MA": 7029917,
        "US-MI": 10077331,
        "US-MN": 5706494,
        "US-MS": 2961279,
        "US-MO": 6154913,
        "US-MT": 1084225,
        "US-MP": 51433,
        "US-NE": 1961504,
        "US-NV": 3104614,
        "US-NH": 1377529,
        "US-NJ": 9288994,
        "US-NM": 2117552,
        "US-NY": 20201249,
        "US-NC": 10439388,
        "US-ND": 779094,
        "US-OH": 11799448,
        "US-OK": 3959353,
        "US-OR": 4237256,
        "US-PA": 13002700,
        "US-PR": 3285874,
        "US-RI": 1097379,
        "US-SC": 5118425,
        "US-SD": 886667,
        "US-TN": 6910840,
        "US-TX": 29145505,
        "US-UT": 3271616,
        "US-VT": 643077,
        "US-VA": 8631393,
        "US-VI": 106235,
        "US-WA": 7705281,
        "US-WV": 1793716,
        "US-WI": 5893718,
        "US-WY": 576851
    }
    usaStateAlphaToRegion = {
        "US-AL": "South East",
        "US-AK": "Alaska",
        "US-AZ": "South West",
        "US-AR": "South East",
        "US-AS": "Pacific Islands",
        "US-CA": "West",
        "US-CO": "South West",
        "US-CT": "North East",
        "US-DC": "Mid Atlantic",
        "US-DE": "Mid Atlantic",
        "US-FL": "South East",
        "US-GA": "South East",
        "US-GU": "Pacific Islands",
        "US-HI": "Pacific Islands",
        "US-ID": "North West",
        "US-IL": "Mid-West",
        "US-IN": "Mid-West",
        "US-IA": "Mid-West",
        "US-KS": "Mid-West",
        "US-KY": "Mid-West",
        "US-LA": "South East",
        "US-ME": "North East",
        "US-MD": "Mid Atlantic",
        "US-MA": "North East",
        "US-MI": "Mid-West",
        "US-MN": "Mid-West",
        "US-MS": "South East",
        "US-MO": "Mid-West",
        "US-MT": "North West",
        "US-MP": "Pacific Islands",
        "US-NE": "Mid-West",
        "US-NV": "West",
        "US-NH": "North East",
        "US-NJ": "Mid Atlantic",
        "US-NM": "South West",
        "US-NY": "Mid Atlantic",
        "US-NC": "South East",
        "US-ND": "Mid-West",
        "US-OH": "Mid-West",
        "US-OK": "South West",
        "US-OR": "North West",
        "US-PA": "Mid Atlantic",
        "US-PR": "Caribbean Islands",
        "US-RI": "North East",
        "US-SC": "South East",
        "US-SD": "Mid-West",
        "US-TN": "South East",
        "US-TX": "South West",
        "US-UT": "South West",
        "US-VT": "North East",
        "US-VA": "Mid Atlantic",
        "US-VI": "Caribbean Islands",
        "US-WA": "North West",
        "US-WV": "Mid Atlantic",
        "US-WI": "Mid-West",
        "US-WY": "North West"
    }
    usaStateRegionToAlpha = {
        "ALASKA": ["US-AK"],
        "CARIBBEAN_ISLANDS": ["US-PR", "US-VI"],
        "MID_ATLANTIC": ["US-DC", "US-DE", "US-MD", "US-NJ", "US-NY", "US-PA", "US-VA", "US-WV"],
        "MID-WEST": ["US-IL", "US-IN", "US-IA", "US-KS", "US-KY", "US-MI", "US-MN", "US-MO", "US-NE", "US-ND", "US-OH",
                     "US-SD", "US-WI"],
        "NORTH_EAST": ["US-CT", "US-ME", "US-MA", "US-NH", "US-RI", "US-VT"],
        "NORTH_WEST": ["US-ID", "US-MT", "US-OR", "US-WA", "US-WY"],
        "PACIFIC_ISLANDS": ["US-AS", "US-GU", "US-HI", "US-MP"],
        "SOUTH_EAST": ["US-AL", "US-AR", "US-FL", "US-GA", "US-LA", "US-MS", "US-NC", "US-SC", "US-TN"],
        "SOUTH_WEST": ["US-AZ", "US-CO", "US-NM", "US-OK", "US-TX", "US-UT"],
        "WEST": ["US-CA", "US-NV"]
    }
    usaRegionToLargestCity = {
        "ALASKA": {"CITY": "Anchorage", "STATE": "US-AK"},
        "CARIBBEAN_ISLANDS": {"CITY": "San Juan", "STATE": "US-PR"},
        "MID_ATLANTIC": {"CITY": "New York City", "STATE": "US-NY"},
        "MID-WEST": {"CITY": "Chicago", "STATE": "US-IL"},
        "NORTH_EAST": {"CITY": "Boston", "STATE": "US-MA"},
        "NORTH_WEST": {"CITY": "Seattle", "STATE": "US-WA"},
        "PACIFIC_ISLANDS": {"CITY": "Honolulu", "STATE": "US-HI"},
        "SOUTH_EAST": {"CITY": "Jacksonville", "STATE": "US-FL"},
        "SOUTH_WEST": {"CITY": "Houston", "STATE": "US-TX"},
        "WEST": {"CITY": "Los Angeles", "STATE": "US-CA"}
    }
    usaStateType = {
        "US-AL": "STATE",
        "US-AK": "STATE",
        "US-AZ": "STATE",
        "US-AR": "STATE",
        "US-AS": "TERRITORY",
        "US-CA": "STATE",
        "US-CO": "STATE",
        "US-CT": "STATE",
        "US-DC": "FEDERAL_DISTRICT",
        "US-DE": "STATE",
        "US-FL": "STATE",
        "US-GA": "STATE",
        "US-GU": "TERRITORY",
        "US-HI": "STATE",
        "US-ID": "STATE",
        "US-IL": "STATE",
        "US-IN": "STATE",
        "US-IA": "STATE",
        "US-KS": "STATE",
        "US-KY": "COMMONWEALTH",
        "US-LA": "STATE",
        "US-ME": "STATE",
        "US-MD": "STATE",
        "US-MA": "COMMONWEALTH",
        "US-MI": "STATE",
        "US-MN": "STATE",
        "US-MS": "STATE",
        "US-MO": "STATE",
        "US-MT": "STATE",
        "US-MP": "TERRITORY",
        "US-NE": "STATE",
        "US-NV": "STATE",
        "US-NH": "STATE",
        "US-NJ": "STATE",
        "US-NM": "STATE",
        "US-NY": "STATE",
        "US-NC": "STATE",
        "US-ND": "STATE",
        "US-OH": "STATE",
        "US-OK": "STATE",
        "US-OR": "STATE",
        "US-PA": "COMMONWEALTH",
        "US-PR": "TERRITORY",
        "US-RI": "STATE",
        "US-SC": "STATE",
        "US-SD": "STATE",
        "US-TN": "STATE",
        "US-TX": "STATE",
        "US-UT": "STATE",
        "US-VT": "STATE",
        "US-VA": "COMMONWEALTH",
        "US-VI": "TERRITORY",
        "US-WA": "STATE",
        "US-WV": "STATE",
        "US-WI": "STATE",
        "US-WY": "STATE"
    }


class AustralianStates:

    @classmethod
    def doesStateExist(cls, australianStateAlpha: str):
        if AustralianStates.getRedirectedNameToAlpha(australianStateAlpha) in Data.australianStateAlphaList:
            return True
        else:
            return False

    @classmethod
    def getAreaKM(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToAreaKM[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]

    @classmethod
    def getAreaMiles(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return math.ceil(int(Data.australianStateAlphaToAreaKM[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]) / 2.59)

    @classmethod
    def getAreaRanking(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            areaDict = {}
            for item in Data.australianStateAlphaList:
                if AustralianStates.getAreaKM(item) is None:
                    areaDict[item] = 0
                else:
                    areaDict[item] = AustralianStates.getAreaKM(item)
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == AustralianStates.getRedirectedNameToAlpha(australianStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        return dict(sorted(Data.australianStateAlphaToAreaKM.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCapital(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToCapital[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]

    @classmethod
    def getFlagURL(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToFlagURL[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]

    @classmethod
    def getGDP(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return int(Data.australianStateAlphaToGDP[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)])

    @classmethod
    def getGDPRanking(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            gdpDict = {}
            for count, item in enumerate(Data.australianStateAlphaList):
                if AustralianStates.getGDP(item) is None:
                    pass
                else:
                    gdpDict[item] = AustralianStates.getGDP(item)
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == AustralianStates.getRedirectedNameToAlpha(australianStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        return dict(sorted(Data.australianStateAlphaToGDP.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGdpPerCapita(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            if AustralianStates.getGDP(AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)) == 0:
                return 0
            elif AustralianStates.getPopulation(AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)) == 0:
                return 0
            else:
                return int(AustralianStates.getGDP(AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)) / AustralianStates.getPopulation(
                AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)))

    @classmethod
    def getGdpPerCapitaRanking(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for count, item in enumerate(Data.australianStateAlphaList):
                if AustralianStates.getGdpPerCapita(item) is None:
                    pass
                else:
                    gdpPerCapitaDict[item] = AustralianStates.getGdpPerCapita(item)
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == AustralianStates.getRedirectedNameToAlpha(australianStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.australianStateAlphaList):
            if AustralianStates.getGdpPerCapita(item) is None:
                pass
            else:
                gdpPerCapitaDict[item] = AustralianStates.getGdpPerCapita(item)
        return dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getLargestCity(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToLargestCity[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]

    @classmethod
    def getName(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToName[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]

    @classmethod
    def getPopulation(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToPopulation[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]

    @classmethod
    def getPopulationRanking(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            newSorted = dict(sorted(Data.australianStateAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == AustralianStates.getRedirectedNameToAlpha(australianStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        return dict(sorted(Data.australianStateAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            population = AustralianStates.getPopulation(australianStateAlpha)
            areaKM = AustralianStates.getAreaKM(australianStateAlpha)
            return float(round(population / areaKM ,2))

    @classmethod
    def getPopulationDensityInMiles(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            population = AustralianStates.getPopulation(australianStateAlpha)
            areaMiles = AustralianStates.getAreaMiles(australianStateAlpha)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.australianStateAlphaList):
                if AustralianStates.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = AustralianStates.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == AustralianStates.getRedirectedNameToAlpha(australianStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.australianStateAlphaList):
            if AustralianStates.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = AustralianStates.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getRedirectedNameToAlpha(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.australianStateAlphaList:
            return name.upper()
        elif name.upper().replace(" ", "_") in Data.australianStateNameList:
            return Data.australianStateNameToAlpha[name.upper().replace(" ", "_")]
        else:
            return None

    @classmethod
    def getStateType(cls, australianStateAlpha: str):
        if AustralianStates.doesStateExist(australianStateAlpha) is False:
            return None
        else:
            return Data.australianStateAlphaToType[AustralianStates.getRedirectedNameToAlpha(australianStateAlpha)]


class CanadianProvinces:

    @classmethod
    def doesProvinceExist(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha) in Data.canadianProvinceAlphaList:
            return True
        else:
            return False

    @classmethod
    def getAreaKM(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToAreaKM[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]

    @classmethod
    def getAreaMiles(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return math.ceil(int(Data.canadianProvinceAlphaToAreaKM[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]) / 2.59)

    @classmethod
    def getAreaRanking(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            areaDict = {}
            for item in Data.canadianProvinceAlphaList:
                if CanadianProvinces.getAreaKM(item) is None:
                    areaDict[item] = 0
                else:
                    areaDict[item] = CanadianProvinces.getAreaKM(item)
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        return dict(sorted(Data.canadianProvinceAlphaToAreaKM.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCapital(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToCapital[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]

    @classmethod
    def getFlagURL(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToFlagURL[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]

    @classmethod
    def getGDP(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return int(Data.canadianProvinceAlphaToGDP[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)])

    @classmethod
    def getGDPRanking(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            gdpDict = {}
            for count, item in enumerate(Data.canadianProvinceAlphaList):
                if CanadianProvinces.getGDP(item) is None:
                    pass
                else:
                    gdpDict[item] = CanadianProvinces.getGDP(item)
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        return dict(sorted(Data.canadianProvinceAlphaToGDP.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGdpPerCapita(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return int(CanadianProvinces.getGDP(CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)) / CanadianProvinces.getPopulation(
                CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)))

    @classmethod
    def getGdpPerCapitaRanking(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for count, item in enumerate(Data.canadianProvinceAlphaList):
                if CanadianProvinces.getGdpPerCapita(item) is None:
                    pass
                else:
                    gdpPerCapitaDict[item] = CanadianProvinces.getGdpPerCapita(item)
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.canadianProvinceAlphaList):
            if CanadianProvinces.getGdpPerCapita(item) is None:
                pass
            else:
                gdpPerCapitaDict[item] = CanadianProvinces.getGdpPerCapita(item)
        return dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getLargestCity(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToLargestCity[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]

    @classmethod
    def getName(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToName[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]

    @classmethod
    def getPopulation(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToPopulation[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]

    @classmethod
    def getPopulationRanking(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            newSorted = dict(sorted(Data.canadianProvinceAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        return dict(sorted(Data.canadianProvinceAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            population = CanadianProvinces.getPopulation(canadianProvinceAlpha)
            areaKM = CanadianProvinces.getAreaKM(canadianProvinceAlpha)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            population = CanadianProvinces.getPopulation(canadianProvinceAlpha)
            areaMiles = CanadianProvinces.getAreaMiles(canadianProvinceAlpha)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.canadianProvinceAlphaList):
                if CanadianProvinces.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = CanadianProvinces.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.canadianProvinceAlphaList):
            if CanadianProvinces.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = CanadianProvinces.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getRedirectedNameToAlpha(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.canadianProvinceAlphaList:
            return name.upper()
        elif name.upper().replace(" ", "_") in Data.canadianProvinceNameList:
            return Data.canadianProvinceNameToAlpha[name.upper().replace(" ", "_")]
        else:
            return None

    @classmethod
    def getProvinceType(cls, canadianProvinceAlpha: str):
        if CanadianProvinces.doesProvinceExist(canadianProvinceAlpha) is False:
            return None
        else:
            return Data.canadianProvinceAlphaToType[CanadianProvinces.getRedirectedNameToAlpha(canadianProvinceAlpha)]


class Continents:

    @classmethod
    def doesContinentExist(cls, continent: str):
        if continent.upper().replace(" ", "_") in Data.continents:
            return True
        else:
            return False

    @classmethod
    def getAreaInKM(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            areaTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                areaTotal += Countries.getAreaInKM(country)
            return areaTotal

    @classmethod
    def getAreaInMiles(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            areaTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                areaTotal += Countries.getAreaInKM(country)
            return math.ceil(int(areaTotal) / 2.59)

    @classmethod
    def getAreaRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            areaDict = {}
            for continent2 in Data.continents:
                areaTotal = 0
                for country in Data.continentToAlpha[continent2]:
                    areaTotal += Countries.getAreaInKM(country)
                areaDict[continent2] = areaTotal
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        areaDict = {}
        for continent2 in Data.continents:
            areaTotal = 0
            for country in Data.continentToAlpha[continent2]:
                if Countries.getAreaInKM(country) == 0:
                    pass
                else:
                    areaTotal += Countries.getAreaInKM(country)
            areaDict[continent2] = areaTotal
        return dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGDP(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            gdpTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                if Countries.getGDP(country) is None:
                    pass
                else:
                    gdpTotal += Countries.getGDP(country)
            return gdpTotal

    @classmethod
    def getGDPRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            gdpDict = {}
            for region in Data.continents:
                gdpTotal = 0
                for country in Data.continentToAlpha[region]:
                    if Countries.getGDP(country) is None:
                        pass
                    else:
                        gdpTotal += Countries.getGDP(country)
                gdpDict[region] = gdpTotal
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        gdpDict = {}
        for continent in Data.continents:
            if Continents.getGDP(continent) is None:
                pass
            elif Continents.getGDP(continent) == 0:
                pass
            else:
                gdpDict[continent] = Continents.getGDP(continent)
        newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
        rank = 0
        rankingDict = {}
        for count, item in enumerate(newSorted):
            rankingDict[count + 1] = item
        return rankingDict

    @classmethod
    def getGdpPerCapita(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            return int(Continents.getGDP(continent) / Continents.getPopulation(continent))

    @classmethod
    def getGdpPerCapitaRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for continent2 in Data.continents:
                if Continents.getGdpPerCapita(continent2) == 0:
                    pass
                else:
                    gdpPerCapitaDict[continent2] = Continents.getGdpPerCapita(continent2)
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.continents):
            if Continents.getGdpPerCapita(item) is None:
                pass
            elif Continents.getGdpPerCapita(item) == 0:
                pass
            else:
                gdpPerCapitaDict[item] = Continents.getGdpPerCapita(item)
        newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
        rank = 0
        rankingDict = {}
        for count, item in enumerate(newSorted):
            rankingDict[count + 1] = item
        return rankingDict

    @classmethod
    def getLargestCity(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            return Data.continentToLargestCity[continent.upper().replace(" ", "_")]

    @classmethod
    def getPopulation(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            populationTotal = 0
            for country in Data.continentToAlpha[continent.upper().replace(" ", "_")]:
                if Countries.getPopulation(country) is None:
                    pass
                else:
                    populationTotal += Countries.getPopulation(country)
            return populationTotal

    @classmethod
    def getPopulationRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            populationDict = {}
            for continent2 in Data.continents:
                populationTotal = 0
                for continent3 in Data.continentToAlpha[continent2]:
                    if Continents.getPopulation(continent3) is None:
                        pass
                    else:
                        populationTotal += Continents.getPopulation(continent3)
                populationDict[continent2] = populationTotal
            newSorted = dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        populationDict = {}
        for continent2 in Data.continents:
            populationTotal = 0
            for country in Data.continentToAlpha[continent2]:
                if Countries.getPopulation(country) is None:
                    pass
                else:
                    populationTotal += Countries.getPopulation(country)
            populationDict[continent2] = populationTotal
        return dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            population = Continents.getPopulation(continent)
            areaKM = Continents.getAreaInKM(continent)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            population = Continents.getPopulation(continent)
            areaMiles = Continents.getAreaInMiles(continent)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.continents):
                if Continents.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = Continents.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == continent.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.continents):
            if Continents.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = Continents.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCountries(cls, continent: str):
        if Continents.doesContinentExist(continent) is False:
            return None
        else:
            return Data.continentToAlpha[continent.upper().replace(" ", "_")]


class Countries:

    @classmethod
    def doesCountryExist(cls, alpha3: str):
        if Countries.getRedirectedNameToAlpha3(alpha3) in Data.alpha3List:
            return True
        else:
            return False

    @classmethod
    def getAreaInKM(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToAreaKMm[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getAreaInMiles(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return math.ceil(int(Data.alpha3ToAreaKMm[Countries.getRedirectedNameToAlpha3(alpha3)]) / 2.59)

    @classmethod
    def getAreaRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            areaDict = {}
            for count, item in enumerate(Data.alpha3List):
                if Countries.getAreaInKM(item) is None:
                    pass
                else:
                    areaDict[item] = Countries.getAreaInKM(item)
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        areaDict = {}
        for country in Data.alpha3List:
            if Countries.getAreaInKM(country) is None:
                pass
            else:
                areaDict[country] = Countries.getAreaInKM(country)
        return dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCapital(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToCapital[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getContinent(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToContinent[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getFlagURL(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToFlagURL[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getGDP(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToGDP[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getGDPRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            gdpDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getGDP(item) is None:
                        pass
                    else:
                        gdpDict[item] = Countries.getGDP(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        return dict(sorted(Data.alpha3ToGDP.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGdpPerCapita(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            try:
                return int(Data.alpha3ToGDP[Countries.getRedirectedNameToAlpha3(alpha3)] / Data.alpha3ToPopulation[
                    Countries.getRedirectedNameToAlpha3(alpha3)])
            except ZeroDivisionError:
                return 0
            except TypeError:
                return None

    @classmethod
    def getGdpPerCapitaRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for count, item in enumerate(Data.alpha3List):
                try:
                    if Countries.getGdpPerCapita(item) is None:
                        pass
                    else:
                        gdpPerCapitaDict[item] = Countries.getGdpPerCapita(item)
                except KeyError:
                    pass
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.alpha3List):
            try:
                if Countries.getGdpPerCapita(item) is None:
                    pass
                else:
                    gdpPerCapitaDict[item] = Countries.getGdpPerCapita(item)
            except KeyError:
                pass
        newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
        return newSorted

    @classmethod
    def getLargestCity(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToLargestCity[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getName(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            return Data.alpha3ToName[Countries.getRedirectedNameToAlpha3(alpha3)]

    @classmethod
    def getPopulation(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            try:
                return Data.alpha3ToPopulation[Countries.getRedirectedNameToAlpha3(alpha3)]
            except KeyError:
                return None

    @classmethod
    def getPopulationRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            newSorted = dict(sorted(Data.alpha3ToPopulation.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        return dict(sorted(Data.alpha3ToPopulation.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            population = Countries.getPopulation(alpha3)
            areaKM = Countries.getAreaInKM(alpha3)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            population = Countries.getPopulation(alpha3)
            areaMiles = Countries.getAreaInMiles(alpha3)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, alpha3: str):
        if Countries.doesCountryExist(alpha3) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.alpha3List):
                if Countries.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = Countries.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == Countries.getRedirectedNameToAlpha3(alpha3):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.alpha3List):
            if Countries.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = Countries.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getRedirectedNameToAlpha3(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.alpha3List:
            return name.upper()
        elif name.upper() in Data.alpha2List:
            return Data.alpha2ToAlpha3[name.upper()]
        elif name.title().replace("_", " ") in Data.countryNameList:
            return Data.nameToAlpha3[name.upper().replace(" ", "_")]
        else:
            return None

    @classmethod
    def getRedirectedNameToAlpha2(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.alpha3List:
            return Data.alpha3ToAlpha2[name.upper()]
        elif name.upper() in Data.alpha2List:
            return name.upper()
        elif name.title().replace("_", " ") in Data.countryNameList:
            alpha3 = Data.nameToAlpha3[name.upper().replace(" ", "_")]
            return Data.alpha3ToAlpha2[alpha3]
        else:
            return None


class SouthAfricanProvinces:

    @classmethod
    def doesProvinceExist(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha) in Data.southAfricanProvinceAlphaList:
            return True
        else:
            return False

    @classmethod
    def getAreaKM(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToAreaKM[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]

    @classmethod
    def getAreaMiles(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return math.ceil(int(Data.southAfricanProvinceAlphaToAreaKM[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]) / 2.59)

    @classmethod
    def getAreaRanking(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            areaDict = {}
            for item in Data.southAfricanProvinceAlphaList:
                if SouthAfricanProvinces.getAreaKM(item) is None:
                    areaDict[item] = 0
                else:
                    areaDict[item] = SouthAfricanProvinces.getAreaKM(item)
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        return dict(sorted(Data.southAfricanProvinceAlphaToAreaKM.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCapital(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToCapital[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]

    @classmethod
    def getFlagURL(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToFlagURL[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]

    @classmethod
    def getGDP(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return int(Data.southAfricanProvinceAlphaToGDP[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)])

    @classmethod
    def getGDPRanking(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            gdpDict = {}
            for count, item in enumerate(Data.southAfricanProvinceAlphaList):
                if SouthAfricanProvinces.getGDP(item) is None:
                    pass
                else:
                    gdpDict[item] = SouthAfricanProvinces.getGDP(item)
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        return dict(sorted(Data.southAfricanProvinceAlphaToGDP.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGdpPerCapita(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return int(SouthAfricanProvinces.getGDP(SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)) / SouthAfricanProvinces.getPopulation(
                SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)))

    @classmethod
    def getGdpPerCapitaRanking(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for count, item in enumerate(Data.southAfricanProvinceAlphaList):
                if SouthAfricanProvinces.getGdpPerCapita(item) is None:
                    pass
                else:
                    gdpPerCapitaDict[item] = SouthAfricanProvinces.getGdpPerCapita(item)
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.southAfricanProvinceAlphaList):
            if SouthAfricanProvinces.getGdpPerCapita(item) is None:
                pass
            else:
                gdpPerCapitaDict[item] = SouthAfricanProvinces.getGdpPerCapita(item)
        return dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getLargestCity(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToLargestCity[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]

    @classmethod
    def getName(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToName[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]

    @classmethod
    def getPopulation(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToPopulation[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]

    @classmethod
    def getPopulationRanking(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            newSorted = dict(sorted(Data.southAfricanProvinceAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        return dict(sorted(Data.southAfricanProvinceAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            population = SouthAfricanProvinces.getPopulation(southAfricanProvinceAlpha)
            areaKM = SouthAfricanProvinces.getAreaKM(southAfricanProvinceAlpha)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            population = SouthAfricanProvinces.getPopulation(southAfricanProvinceAlpha)
            areaMiles = SouthAfricanProvinces.getAreaMiles(southAfricanProvinceAlpha)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.southAfricanProvinceAlphaList):
                if SouthAfricanProvinces.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = SouthAfricanProvinces.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.southAfricanProvinceAlphaList):
            if SouthAfricanProvinces.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = SouthAfricanProvinces.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getRedirectedNameToAlpha(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.southAfricanProvinceAlphaList:
            return name.upper()
        elif name.upper().replace(" ", "_") in Data.southAfricanProvinceNameList:
            return Data.southAfricanProvinceNameToAlpha[name.upper().replace(" ", "_")]
        else:
            return None

    @classmethod
    def getProvinceType(cls, southAfricanProvinceAlpha: str):
        if SouthAfricanProvinces.doesProvinceExist(southAfricanProvinceAlpha) is False:
            return None
        else:
            return Data.southAfricanProvinceAlphaToType[SouthAfricanProvinces.getRedirectedNameToAlpha(southAfricanProvinceAlpha)]


class UsaStates:

    @classmethod
    def doesStateExist(cls, usStateAlpha: str):
        if UsaStates.getRedirectedNameToAlpha(usStateAlpha) in Data.usaStateAlphaList:
            return True
        else:
            return False

    @classmethod
    def getAreaKM(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToAreaKM[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getAreaMiles(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return math.ceil(int(Data.usaStateAlphaToAreaKM[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]) / 2.59)

    @classmethod
    def getAreaRanking(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            areaDict = {}
            for item in Data.usaStateAlphaList:
                if UsaStates.getAreaKM(item) is None:
                    areaDict[item] = 0
                else:
                    areaDict[item] = UsaStates.getAreaKM(item)
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == UsaStates.getRedirectedNameToAlpha(usStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        return dict(sorted(Data.usaStateAlphaToAreaKM.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getCapital(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToCapital[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getFlagURL(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToFlagURL[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getGDP(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return int(Data.usaStateAlphaToGDP[UsaStates.getRedirectedNameToAlpha(usStateAlpha)])

    @classmethod
    def getGDPRanking(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            gdpDict = {}
            for count, item in enumerate(Data.usaStateAlphaList):
                if UsaStates.getGDP(item) is None:
                    pass
                else:
                    gdpDict[item] = UsaStates.getGDP(item)
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == UsaStates.getRedirectedNameToAlpha(usStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        return dict(sorted(Data.usaStateAlphaToGDP.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGdpPerCapita(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return int(UsaStates.getGDP(UsaStates.getRedirectedNameToAlpha(usStateAlpha)) / UsaStates.getPopulation(
                UsaStates.getRedirectedNameToAlpha(usStateAlpha)))

    @classmethod
    def getGdpPerCapitaRanking(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for count, item in enumerate(Data.usaStateAlphaList):
                if UsaStates.getGdpPerCapita(item) is None:
                    pass
                else:
                    gdpPerCapitaDict[item] = UsaStates.getGdpPerCapita(item)
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == UsaStates.getRedirectedNameToAlpha(usStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.usaStateAlphaList):
            if UsaStates.getGdpPerCapita(item) is None:
                pass
            else:
                gdpPerCapitaDict[item] = UsaStates.getGdpPerCapita(item)
        return dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getLargestCity(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToLargestCity[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getName(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToName[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getPopulation(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToPopulation[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getPopulationRanking(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            newSorted = dict(sorted(Data.usaStateAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == UsaStates.getRedirectedNameToAlpha(usStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        return dict(sorted(Data.usaStateAlphaToPopulation.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, usaStateAlpha: str):
        if UsaStates.doesStateExist(usaStateAlpha) is False:
            return None
        else:
            population = UsaStates.getPopulation(usaStateAlpha)
            areaKM = UsaStates.getAreaKM(usaStateAlpha)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, usaStateAlpha: str):
        if UsaStates.doesStateExist(usaStateAlpha) is False:
            return None
        else:
            population = UsaStates.getPopulation(usaStateAlpha)
            areaMiles = UsaStates.getAreaMiles(usaStateAlpha)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, usaStateAlpha: str):
        if UsaStates.doesStateExist(usaStateAlpha) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.usaStateAlphaList):
                if UsaStates.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = UsaStates.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == UsaStates.getRedirectedNameToAlpha(usaStateAlpha):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.usaStateAlphaList):
            if UsaStates.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = UsaStates.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getRedirectedNameToAlpha(cls, name: str):
        if name is None:
            return None
        elif name.upper() in Data.usaStateAlphaList:
            return name.upper()
        elif name.upper().replace(" ", "_") in Data.usaStateNameList:
            return Data.usaStateNameToAlpha[name.upper().replace(" ", "_")]
        else:
            return None

    @classmethod
    def getRegion(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateAlphaToRegion[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]

    @classmethod
    def getStateType(cls, usStateAlpha: str):
        if UsaStates.doesStateExist(usStateAlpha) is False:
            return None
        else:
            return Data.usaStateType[UsaStates.getRedirectedNameToAlpha(usStateAlpha)]


class UsaRegions:

    @classmethod
    def doesRegionExist(cls, usRegion: str):
        if usRegion.upper().replace(" ", "_") in Data.usaStateRegionToAlpha.keys():
            return True
        else:
            return False

    @classmethod
    def getAreaInKM(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            areaTotal = 0
            for state in Data.usaStateRegionToAlpha[usRegion.upper().replace(" ", "_")]:
                areaTotal += UsaStates.getAreaKM(state)
            return areaTotal

    @classmethod
    def getAreaInMiles(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            areaTotal = 0
            for state in Data.usaStateRegionToAlpha[usRegion.upper().replace(" ", "_")]:
                areaTotal += UsaStates.getAreaKM(state)
            return math.ceil(int(areaTotal) / 2.59)

    @classmethod
    def getAreaRanking(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            areaDict = {}
            for region in Data.usaStateRegionToAlpha.keys():
                areaTotal = 0
                for state in Data.usaStateRegionToAlpha[region]:
                    areaTotal += UsaStates.getAreaKM(state)
                areaDict[region] = areaTotal
            newSorted = dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == usRegion.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getAreaRankingDict(cls):
        areaDict = {}
        for region in Data.usaStateRegionToAlpha.keys():
            areaTotal = 0
            for state in Data.usaStateRegionToAlpha[region]:
                areaTotal += UsaStates.getAreaKM(state)
            areaDict[region] = areaTotal
        return dict(sorted(areaDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGDP(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            gdpTotal = 0
            for state in Data.usaStateRegionToAlpha[usRegion.upper().replace(" ", "_")]:
                gdpTotal += UsaStates.getGDP(state)
            return gdpTotal

    @classmethod
    def getGDPRanking(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            gdpDict = {}
            for region in Data.usaStateRegionToAlpha.keys():
                gdpTotal = 0
                for state in Data.usaStateRegionToAlpha[region]:
                    gdpTotal += UsaStates.getGDP(state)
                gdpDict[region] = gdpTotal
            newSorted = dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == usRegion.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGDPRankingDict(cls):
        gdpDict = {}
        for region in Data.usaStateRegionToAlpha.keys():
            gdpTotal = 0
            for state in Data.usaStateRegionToAlpha[region]:
                gdpTotal += UsaStates.getGDP(state)
            gdpDict[region] = gdpTotal
        return dict(sorted(gdpDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getGdpPerCapita(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            return int(UsaRegions.getGDP(usRegion) / UsaRegions.getPopulation(usRegion))

    @classmethod
    def getGdpPerCapitaRanking(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            gdpPerCapitaDict = {}
            for region in Data.usaStateRegionToAlpha.keys():
                gdpPerCapitaDict[region] = float(UsaRegions.getGDP(region) / UsaRegions.getPopulation(region))
            newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == usRegion.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getGdpPerCapitaRankingDict(cls):
        gdpPerCapitaDict = {}
        for count, item in enumerate(Data.usaStateRegionToAlpha.keys()):
            if UsaRegions.getGdpPerCapita(item) is None:
                pass
            else:
                gdpPerCapitaDict[item] = UsaRegions.getGdpPerCapita(item)
        newSorted = dict(sorted(gdpPerCapitaDict.items(), key=lambda kv: kv[1], reverse=True))
        rank = 0
        rankingDict = {}
        for count, item in enumerate(newSorted):
            rankingDict[count + 1] = item
        return rankingDict

    @classmethod
    def getLargestCity(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            return Data.usaRegionToLargestCity[usRegion.upper().replace(" ", "_")]

    @classmethod
    def getPopulation(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            populationTotal = 0
            for state in Data.usaStateRegionToAlpha[usRegion.upper().replace(" ", "_")]:
                populationTotal += UsaStates.getPopulation(state)
            return populationTotal

    @classmethod
    def getPopulationRanking(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            populationDict = {}
            for region in Data.usaStateRegionToAlpha.keys():
                populationTotal = 0
                for state in Data.usaStateRegionToAlpha[region]:
                    populationTotal += UsaStates.getPopulation(state)
                populationDict[region] = populationTotal
            newSorted = dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == usRegion.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationRankingDict(cls):
        populationDict = {}
        for region in Data.usaStateRegionToAlpha.keys():
            populationTotal = 0
            for state in Data.usaStateRegionToAlpha[region]:
                populationTotal += UsaStates.getPopulation(state)
            populationDict[region] = populationTotal
        return dict(sorted(populationDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getPopulationDensityInKM(cls, usaRegion: str):
        if UsaRegions.doesRegionExist(usaRegion) is False:
            return None
        else:
            population = UsaRegions.getPopulation(usaRegion)
            areaKM = UsaRegions.getAreaInKM(usaRegion)
            return float(round(population / areaKM, 2))

    @classmethod
    def getPopulationDensityInMiles(cls, usaRegion: str):
        if UsaRegions.doesRegionExist(usaRegion) is False:
            return None
        else:
            population = UsaRegions.getPopulation(usaRegion)
            areaMiles = UsaRegions.getAreaInMiles(usaRegion)
            return float(round(population / areaMiles, 2))

    @classmethod
    def getPopulationDensityRanking(cls, usaRegion: str):
        if UsaRegions.doesRegionExist(usaRegion) is False:
            return None
        else:
            populationDensityDict = {}
            for count, item in enumerate(Data.usaStateRegionToAlpha.keys()):
                if UsaRegions.getPopulationDensityInKM(item) is None:
                    pass
                else:
                    populationDensityDict[item] = UsaRegions.getPopulationDensityInKM(item)
            newSorted = dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))
            rank = 0
            for count, item in enumerate(newSorted):
                if str(item) == usaRegion.upper().replace(" ", "_"):
                    rank = count + 1
                    break
            return rank

    @classmethod
    def getPopulationDensityRankingDict(cls):
        populationDensityDict = {}
        for count, item in enumerate(Data.usaStateRegionToAlpha.keys()):
            if UsaRegions.getPopulationDensityInKM(item) is None:
                pass
            else:
                populationDensityDict[item] = UsaRegions.getPopulationDensityInKM(item)
        return dict(sorted(populationDensityDict.items(), key=lambda kv: kv[1], reverse=True))

    @classmethod
    def getStates(cls, usRegion: str):
        if UsaRegions.doesRegionExist(usRegion) is False:
            return None
        else:
            return Data.usaStateRegionToAlpha[usRegion.upper().replace(" ", "_")]
