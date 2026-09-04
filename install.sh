#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 Installation de LEGITTRADE Bot pour Termux"
echo "============================================="
echo ""

# Mise à jour
echo "📦 Mise à jour des paquets..."
pkg update -y && pkg upgrade -y

# Installation des dépendances
echo "📦 Installation des dépendances..."
pkg install -y python python-pip git

# Installation des paquets Python
echo "🐍 Installation des paquets Python..."
pip install --upgrade pip
pip install python-telegram-bot==20.6
pip install loguru python-dotenv

# Création des dossiers
mkdir -p logs data

# Création du fichier .env
if [ ! -f ".env" ]; then
    echo "📝 Création du fichier .env..."
    cat > .env << EOL
# Telegram Bot
TELEGRAM_BOT_TOKEN=your_bot_token_here
ADMIN_IDS=123456789

# Pocket Option
POCKET_SSID=your_ssid_here

# Trading
MAX_SIGNALS_PER_HOUR=10
DEFAULT_AMOUNT=1.0

# Langue par défaut
DEFAULT_LANGUAGE=fr
EOL
fi

echo ""
echo "✅ Installation terminée !"
echo ""
echo "📝 Éditez le fichier .env avec vos identifiants :"
echo "   nano .env"
echo ""
echo "🚀 Pour démarrer le bot :"
echo "   python main.py"
echo ""
echo "📊 Pour l'exécuter en arrière-plan avec tmux :"
echo "   tmux new -s bot"
echo "   python main.py"
echo "   (Ctrl+B, D pour détacher)"
echo ""
echo "📱 Pour revenir au bot :"
echo "   tmux attach -t bot"
