# 🤖 LEGITTRADE Bot for Termux

Bot Telegram de signaux de trading pour Pocket Option, optimisé pour Termux.

## 📱 Caractéristiques

- ✅ **60+ paires de devises** avec drapeaux
- ✅ Signaux 1min, 2min, 5min
- ✅ Interface Telegram interactive
- ✅ Gestion des utilisateurs
- ✅ Validation des comptes
- ✅ Statistiques en temps réel
- ✅ Optimisé pour Termux
- ✅ Léger et rapide

## 📊 Paires disponibles

### Paires Standard & Cross (Majors/Minors)
🇪🇺 EUR/USD 🇺🇸 • 🇺🇸 USD/JPY 🇯🇵 • 🇬🇧 GBP/USD 🇺🇸 • 🇺🇸 USD/CAD 🇨🇦 • 🇺🇸 USD/CHF 🇨🇭 • 🇦🇺 AUD/USD 🇺🇸 • 🇳🇿 NZD/USD 🇺🇸 • 🇪🇺 EUR/GBP 🇬🇧 • 🇪🇺 EUR/JPY 🇯🇵 • 🇪🇺 EUR/CAD 🇨🇦 • 🇪🇺 EUR/CHF 🇨🇭 • 🇪🇺 EUR/NZD 🇳🇿 • 🇪🇺 EUR/HUF 🇭🇺 • 🇪🇺 EUR/TRY 🇹🇷 • 🇪🇺 EUR/RUB 🇷🇺 • 🇬🇧 GBP/JPY 🇯🇵 • 🇬🇧 GBP/CAD 🇨🇦 • 🇬🇧 GBP/CHF 🇨🇭 • 🇬🇧 GBP/AUD 🇦🇺 • 🇦🇺 AUD/CAD 🇨🇦 • 🇦🇺 AUD/CHF 🇨🇭 • 🇦🇺 AUD/JPY 🇯🇵 • 🇦🇺 AUD/NZD 🇳🇿 • 🇨🇦 CAD/CHF 🇨🇭 • 🇨🇦 CAD/JPY 🇯🇵 • 🇨🇭 CHF/JPY 🇯🇵 • 🇨🇭 CHF/NOK 🇳🇴 • 🇳🇿 NZD/JPY 🇯🇵

### Paires Exotiques (Base USD)
🇺🇸 USD/CNH 🇨🇳 • 🇺🇸 USD/INR 🇮🇳 • 🇺🇸 USD/BRL 🇧🇷 • 🇺🇸 USD/RUB 🇷🇺 • 🇺🇸 USD/TRY 🇹🇷 • 🇺🇸 USD/MXN 🇲🇽 • 🇺🇸 USD/EGP 🇪🇬 • 🇺🇸 USD/PHP 🇵🇭 • 🇺🇸 USD/PKR 🇵🇰 • 🇺🇸 USD/IDR 🇮🇩 • 🇺🇸 USD/MYR 🇲🇾 • 🇺🇸 USD/THB 🇹🇭 • 🇺🇸 USD/ZAR 🇿🇦 • 🇺🇸 USD/ARS 🇦🇷 • 🇺🇸 USD/COP 🇨🇴 • 🇺🇸 USD/CLP 🇨🇱 • 🇺🇸 USD/BDT 🇧🇩 • 🇺🇸 USD/VND 🇻🇳 • 🇺🇸 USD/DZD 🇩🇿 • 🇺🇸 USD/SGD 🇸🇬

### Paires Inversées
🇺🇦 UAH/USD 🇺🇸 • 🇳🇬 NGN/USD 🇳🇬 • 🇲🇦 MAD/USD 🇺🇸 • 🇿🇦 ZAR/USD 🇺🇸 • 🇾🇪 YER/USD 🇺🇸 • 🇱🇧 LBP/USD 🇺🇸 • 🇰🇪 KES/USD 🇺🇸 • 🇹🇳 TND/USD 🇺🇸

### Paires Asiatiques & Moyen-Orient
🇦🇪 AED/CNY 🇨🇳 • 🇴🇲 OMR/CNY 🇨🇳 • 🇸🇦 SAR/CNY 🇨🇳 • 🇶🇦 QAR/CNY 🇨🇳 • 🇯🇴 JOD/CNY 🇨🇳 • 🇧🇭 BHD/CNY 🇨🇳

## 🚀 Installation rapide

```bash
# 1. Installer Termux (depuis F-Droid)

# 2. Cloner et installer
git clone https://github.com/yourusername/legittrade-bot-termux.git
cd legittrade-bot-termux
bash install.sh

# 3. Configurer
nano .env
# Ajouter TELEGRAM_BOT_TOKEN et ADMIN_IDS

# 4. Démarrer
python main.py

# Démarrer en arrière-plan
tmux new -s bot
python main.py
# Ctrl+B, D pour détacher

# Revenir
tmux attach -t bot

# Arrêter
tmux kill-session -t bot

