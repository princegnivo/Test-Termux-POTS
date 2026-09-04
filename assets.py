#!/data/data/com.termux/files/usr/bin/python3
"""
Toutes les paires de devises disponibles sur Pocket Option OTC
Avec leurs drapeaux respectifs
"""

PAIRS = {
    # ============ Paires Standard & Cross (Majors/Minors) ============
    "EURUSD_otc": {
        "name": "EUR/USD",
        "flag": "🇪🇺",
        "flag2": "🇺🇸",
        "display": "🇪🇺 EUR/USD 🇺🇸 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "USDJPY_otc": {
        "name": "USD/JPY",
        "flag": "🇺🇸",
        "flag2": "🇯🇵",
        "display": "🇺🇸 USD/JPY 🇯🇵 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "GBPUSD_otc": {
        "name": "GBP/USD",
        "flag": "🇬🇧",
        "flag2": "🇺🇸",
        "display": "🇬🇧 GBP/USD 🇺🇸 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "USDCAD_otc": {
        "name": "USD/CAD",
        "flag": "🇺🇸",
        "flag2": "🇨🇦",
        "display": "🇺🇸 USD/CAD 🇨🇦 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "USDCHF_otc": {
        "name": "USD/CHF",
        "flag": "🇺🇸",
        "flag2": "🇨🇭",
        "display": "🇺🇸 USD/CHF 🇨🇭 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "AUDUSD_otc": {
        "name": "AUD/USD",
        "flag": "🇦🇺",
        "flag2": "🇺🇸",
        "display": "🇦🇺 AUD/USD 🇺🇸 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "NZDUSD_otc": {
        "name": "NZD/USD",
        "flag": "🇳🇿",
        "flag2": "🇺🇸",
        "display": "🇳🇿 NZD/USD 🇺🇸 OTC",
        "type": "Major",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURGBP_otc": {
        "name": "EUR/GBP",
        "flag": "🇪🇺",
        "flag2": "🇬🇧",
        "display": "🇪🇺 EUR/GBP 🇬🇧 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURJPY_otc": {
        "name": "EUR/JPY",
        "flag": "🇪🇺",
        "flag2": "🇯🇵",
        "display": "🇪🇺 EUR/JPY 🇯🇵 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURCAD_otc": {
        "name": "EUR/CAD",
        "flag": "🇪🇺",
        "flag2": "🇨🇦",
        "display": "🇪🇺 EUR/CAD 🇨🇦 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURCHF_otc": {
        "name": "EUR/CHF",
        "flag": "🇪🇺",
        "flag2": "🇨🇭",
        "display": "🇪🇺 EUR/CHF 🇨🇭 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURNZD_otc": {
        "name": "EUR/NZD",
        "flag": "🇪🇺",
        "flag2": "🇳🇿",
        "display": "🇪🇺 EUR/NZD 🇳🇿 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURHUF_otc": {
        "name": "EUR/HUF",
        "flag": "🇪🇺",
        "flag2": "🇭🇺",
        "display": "🇪🇺 EUR/HUF 🇭🇺 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURTRY_otc": {
        "name": "EUR/TRY",
        "flag": "🇪🇺",
        "flag2": "🇹🇷",
        "display": "🇪🇺 EUR/TRY 🇹🇷 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "EURRUB_otc": {
        "name": "EUR/RUB",
        "flag": "🇪🇺",
        "flag2": "🇷🇺",
        "display": "🇪🇺 EUR/RUB 🇷🇺 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "GBPJPY_otc": {
        "name": "GBP/JPY",
        "flag": "🇬🇧",
        "flag2": "🇯🇵",
        "display": "🇬🇧 GBP/JPY 🇯🇵 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "GBPCAD_otc": {
        "name": "GBP/CAD",
        "flag": "🇬🇧",
        "flag2": "🇨🇦",
        "display": "🇬🇧 GBP/CAD 🇨🇦 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "GBPCHF_otc": {
        "name": "GBP/CHF",
        "flag": "🇬🇧",
        "flag2": "🇨🇭",
        "display": "🇬🇧 GBP/CHF 🇨🇭 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "GBPAUD_otc": {
        "name": "GBP/AUD",
        "flag": "🇬🇧",
        "flag2": "🇦🇺",
        "display": "🇬🇧 GBP/AUD 🇦🇺 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "AUDCAD_otc": {
        "name": "AUD/CAD",
        "flag": "🇦🇺",
        "flag2": "🇨🇦",
        "display": "🇦🇺 AUD/CAD 🇨🇦 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "AUDCHF_otc": {
        "name": "AUD/CHF",
        "flag": "🇦🇺",
        "flag2": "🇨🇭",
        "display": "🇦🇺 AUD/CHF 🇨🇭 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "AUDJPY_otc": {
        "name": "AUD/JPY",
        "flag": "🇦🇺",
        "flag2": "🇯🇵",
        "display": "🇦🇺 AUD/JPY 🇯🇵 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "AUDNZD_otc": {
        "name": "AUD/NZD",
        "flag": "🇦🇺",
        "flag2": "🇳🇿",
        "display": "🇦🇺 AUD/NZD 🇳🇿 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "CADCHF_otc": {
        "name": "CAD/CHF",
        "flag": "🇨🇦",
        "flag2": "🇨🇭",
        "display": "🇨🇦 CAD/CHF 🇨🇭 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "CADJPY_otc": {
        "name": "CAD/JPY",
        "flag": "🇨🇦",
        "flag2": "🇯🇵",
        "display": "🇨🇦 CAD/JPY 🇯🇵 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "CHFJPY_otc": {
        "name": "CHF/JPY",
        "flag": "🇨🇭",
        "flag2": "🇯🇵",
        "display": "🇨🇭 CHF/JPY 🇯🇵 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "CHFNOK_otc": {
        "name": "CHF/NOK",
        "flag": "🇨🇭",
        "flag2": "🇳🇴",
        "display": "🇨🇭 CHF/NOK 🇳🇴 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },
    "NZDJPY_otc": {
        "name": "NZD/JPY",
        "flag": "🇳🇿",
        "flag2": "🇯🇵",
        "display": "🇳🇿 NZD/JPY 🇯🇵 OTC",
        "type": "Cross",
        "payout": 87,
        "is_otc": True,
        "group": "standard"
    },

    # ============ Paires Exotiques (Base USD) ============
    "USDCNH_otc": {
        "name": "USD/CNH",
        "flag": "🇺🇸",
        "flag2": "🇨🇳",
        "display": "🇺🇸 USD/CNH 🇨🇳 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDINR_otc": {
        "name": "USD/INR",
        "flag": "🇺🇸",
        "flag2": "🇮🇳",
        "display": "🇺🇸 USD/INR 🇮🇳 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDBRL_otc": {
        "name": "USD/BRL",
        "flag": "🇺🇸",
        "flag2": "🇧🇷",
        "display": "🇺🇸 USD/BRL 🇧🇷 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDRUB_otc": {
        "name": "USD/RUB",
        "flag": "🇺🇸",
        "flag2": "🇷🇺",
        "display": "🇺🇸 USD/RUB 🇷🇺 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDTRY_otc": {
        "name": "USD/TRY",
        "flag": "🇺🇸",
        "flag2": "🇹🇷",
        "display": "🇺🇸 USD/TRY 🇹🇷 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDMXN_otc": {
        "name": "USD/MXN",
        "flag": "🇺🇸",
        "flag2": "🇲🇽",
        "display": "🇺🇸 USD/MXN 🇲🇽 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDEGP_otc": {
        "name": "USD/EGP",
        "flag": "🇺🇸",
        "flag2": "🇪🇬",
        "display": "🇺🇸 USD/EGP 🇪🇬 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDPHP_otc": {
        "name": "USD/PHP",
        "flag": "🇺🇸",
        "flag2": "🇵🇭",
        "display": "🇺🇸 USD/PHP 🇵🇭 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDPKR_otc": {
        "name": "USD/PKR",
        "flag": "🇺🇸",
        "flag2": "🇵🇰",
        "display": "🇺🇸 USD/PKR 🇵🇰 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDIDR_otc": {
        "name": "USD/IDR",
        "flag": "🇺🇸",
        "flag2": "🇮🇩",
        "display": "🇺🇸 USD/IDR 🇮🇩 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDMYR_otc": {
        "name": "USD/MYR",
        "flag": "🇺🇸",
        "flag2": "🇲🇾",
        "display": "🇺🇸 USD/MYR 🇲🇾 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDTHB_otc": {
        "name": "USD/THB",
        "flag": "🇺🇸",
        "flag2": "🇹🇭",
        "display": "🇺🇸 USD/THB 🇹🇭 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDZAR_otc": {
        "name": "USD/ZAR",
        "flag": "🇺🇸",
        "flag2": "🇿🇦",
        "display": "🇺🇸 USD/ZAR 🇿🇦 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDARS_otc": {
        "name": "USD/ARS",
        "flag": "🇺🇸",
        "flag2": "🇦🇷",
        "display": "🇺🇸 USD/ARS 🇦🇷 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDCOP_otc": {
        "name": "USD/COP",
        "flag": "🇺🇸",
        "flag2": "🇨🇴",
        "display": "🇺🇸 USD/COP 🇨🇴 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDCLP_otc": {
        "name": "USD/CLP",
        "flag": "🇺🇸",
        "flag2": "🇨🇱",
        "display": "🇺🇸 USD/CLP 🇨🇱 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDBDT_otc": {
        "name": "USD/BDT",
        "flag": "🇺🇸",
        "flag2": "🇧🇩",
        "display": "🇺🇸 USD/BDT 🇧🇩 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDVND_otc": {
        "name": "USD/VND",
        "flag": "🇺🇸",
        "flag2": "🇻🇳",
        "display": "🇺🇸 USD/VND 🇻🇳 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDDZD_otc": {
        "name": "USD/DZD",
        "flag": "🇺🇸",
        "flag2": "🇩🇿",
        "display": "🇺🇸 USD/DZD 🇩🇿 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },
    "USDSGD_otc": {
        "name": "USD/SGD",
        "flag": "🇺🇸",
        "flag2": "🇸🇬",
        "display": "🇺🇸 USD/SGD 🇸🇬 OTC",
        "type": "Exotic",
        "payout": 87,
        "is_otc": True,
        "group": "exotic"
    },

    # ============ Paires Inversées (Devises Locales / USD) ============
    "UAHUSD_otc": {
        "name": "UAH/USD",
        "flag": "🇺🇦",
        "flag2": "🇺🇸",
        "display": "🇺🇦 UAH/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "NGNUSD_otc": {
        "name": "NGN/USD",
        "flag": "🇳🇬",
        "flag2": "🇺🇸",
        "display": "🇳🇬 NGN/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "MADUSD_otc": {
        "name": "MAD/USD",
        "flag": "🇲🇦",
        "flag2": "🇺🇸",
        "display": "🇲🇦 MAD/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "ZARUSD_otc": {
        "name": "ZAR/USD",
        "flag": "🇿🇦",
        "flag2": "🇺🇸",
        "display": "🇿🇦 ZAR/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "YERUSD_otc": {
        "name": "YER/USD",
        "flag": "🇾🇪",
        "flag2": "🇺🇸",
        "display": "🇾🇪 YER/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "LBPUSD_otc": {
        "name": "LBP/USD",
        "flag": "🇱🇧",
        "flag2": "🇺🇸",
        "display": "🇱🇧 LBP/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "KESUSD_otc": {
        "name": "KES/USD",
        "flag": "🇰🇪",
        "flag2": "🇺🇸",
        "display": "🇰🇪 KES/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },
    "TNDUSD_otc": {
        "name": "TND/USD",
        "flag": "🇹🇳",
        "flag2": "🇺🇸",
        "display": "🇹🇳 TND/USD 🇺🇸 OTC",
        "type": "Inverse",
        "payout": 87,
        "is_otc": True,
        "group": "inverse"
    },

    # ============ Paires Asiatiques & Moyen-Orient (Cross CNY) ============
    "AEDCNY_otc": {
        "name": "AED/CNY",
        "flag": "🇦🇪",
        "flag2": "🇨🇳",
        "display": "🇦🇪 AED/CNY 🇨🇳 OTC",
        "type": "Asian",
        "payout": 87,
        "is_otc": True,
        "group": "asian"
    },
    "OMRCNY_otc": {
        "name": "OMR/CNY",
        "flag": "🇴🇲",
        "flag2": "🇨🇳",
        "display": "🇴🇲 OMR/CNY 🇨🇳 OTC",
        "type": "Asian",
        "payout": 87,
        "is_otc": True,
        "group": "asian"
    },
    "SARCNY_otc": {
        "name": "SAR/CNY",
        "flag": "🇸🇦",
        "flag2": "🇨🇳",
        "display": "🇸🇦 SAR/CNY 🇨🇳 OTC",
        "type": "Asian",
        "payout": 87,
        "is_otc": True,
        "group": "asian"
    },
    "QARCNY_otc": {
        "name": "QAR/CNY",
        "flag": "🇶🇦",
        "flag2": "🇨🇳",
        "display": "🇶🇦 QAR/CNY 🇨🇳 OTC",
        "type": "Asian",
        "payout": 87,
        "is_otc": True,
        "group": "asian"
    },
    "JODCNY_otc": {
        "name": "JOD/CNY",
        "flag": "🇯🇴",
        "flag2": "🇨🇳",
        "display": "🇯🇴 JOD/CNY 🇨🇳 OTC",
        "type": "Asian",
        "payout": 87,
        "is_otc": True,
        "group": "asian"
    },
    "BHDCNY_otc": {
        "name": "BHD/CNY",
        "flag": "🇧🇭",
        "flag2": "🇨🇳",
        "display": "🇧🇭 BHD/CNY 🇨🇳 OTC",
        "type": "Asian",
        "payout": 87,
        "is_otc": True,
        "group": "asian"
    }
}

# Groupes de paires
PAIR_GROUPS = {
    "standard": {
        "name": "📊 Paires Standard & Cross",
        "pairs": [k for k, v in PAIRS.items() if v["group"] == "standard"]
    },
    "exotic": {
        "name": "🌍 Paires Exotiques (Base USD)",
        "pairs": [k for k, v in PAIRS.items() if v["group"] == "exotic"]
    },
    "inverse": {
        "name": "🔄 Paires Inversées",
        "pairs": [k for k, v in PAIRS.items() if v["group"] == "inverse"]
    },
    "asian": {
        "name": "🌏 Paires Asiatiques & Moyen-Orient",
        "pairs": [k for k, v in PAIRS.items() if v["group"] == "asian"]
    }
}

def get_pair_display(pair_key: str) -> str:
    """Retourne l'affichage complet d'une paire avec drapeaux"""
    if pair_key in PAIRS:
        return PAIRS[pair_key]["display"]
    return pair_key

def get_all_pairs() -> list:
    """Retourne toutes les clés des paires"""
    return list(PAIRS.keys())

def get_pairs_by_group(group: str) -> list:
    """Retourne les paires d'un groupe spécifique"""
    if group in PAIR_GROUPS:
        return PAIR_GROUPS[group]["pairs"]
    return []

def get_pair_info(pair_key: str) -> dict:
    """Retourne les informations d'une paire"""
    return PAIRS.get(pair_key, {})
