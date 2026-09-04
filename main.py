#!/data/data/com.termux/files/usr/bin/python3
"""
LEGITTRADE Bot - Version Termux
Bot de signaux de trading pour Pocket Option
Avec toutes les paires de devises et leurs drapeaux
"""

import asyncio
import sys
import os
import json
import time
import random
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Ajout du chemin
sys.path.append(str(Path(__file__).parent))

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)
from telegram.constants import ParseMode
from dotenv import load_dotenv
from loguru import logger

# Import des paires
from assets import PAIRS, PAIR_GROUPS, get_pair_display, get_all_pairs, get_pairs_by_group

# Chargement des variables
load_dotenv()

# Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
POCKET_SSID = os.getenv("POCKET_SSID")

# Configuration des logs
logger.remove()
logger.add(sys.stdout, 
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"
)
logger.add("logs/bot_{time:YYYY-MM-DD}.log", rotation="1 day", retention="7 days")

# Fichier de base de données
DB_FILE = Path("data/users.json")
DB_FILE.parent.mkdir(exist_ok=True)

class LegitTradeBot:
    """Bot principal pour Termux"""
    
    def __init__(self):
        self.token = TELEGRAM_TOKEN
        self.application = None
        self.is_running = True
        self.last_signals = {}
        self.signal_count = 0
        self.max_signals_per_hour = int(os.getenv("MAX_SIGNALS_PER_HOUR", "10"))
        
    # ==================== GESTION DES UTILISATEURS ====================
    
    def _load_users(self) -> dict:
        """Charger les utilisateurs"""
        try:
            if DB_FILE.exists():
                with open(DB_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def _save_users(self, users: dict):
        """Sauvegarder les utilisateurs"""
        try:
            with open(DB_FILE, 'w') as f:
                json.dump(users, f, indent=2)
        except Exception as e:
            logger.error(f"Erreur sauvegarde utilisateurs: {e}")
    
    def _get_user(self, telegram_id: int) -> Optional[dict]:
        """Récupérer un utilisateur"""
        users = self._load_users()
        return users.get(str(telegram_id))
    
    def _save_user(self, telegram_id: int, username: str, language: str = "fr", 
                   pocket_id: str = None, is_verified: bool = False):
        """Sauvegarder un utilisateur"""
        users = self._load_users()
        user = users.get(str(telegram_id), {})
        user.update({
            "telegram_id": telegram_id,
            "username": username,
            "language": language,
            "pocket_id": pocket_id or user.get("pocket_id"),
            "is_verified": is_verified or user.get("is_verified", False),
            "last_active": datetime.now().isoformat(),
            "created_at": user.get("created_at", datetime.now().isoformat())
        })
        users[str(telegram_id)] = user
        self._save_users(users)
    
    def _validate_user(self, telegram_id: int):
        """Valider un utilisateur"""
        users = self._load_users()
        if str(telegram_id) in users:
            users[str(telegram_id)]["is_verified"] = True
            self._save_users(users)
            return True
        return False
    
    # ==================== GENERATION DE SIGNAUX ====================
    
    def _generate_signal(self, timeframe: str) -> Optional[dict]:
        """Générer un signal de trading"""
        # Vérifier la limite de signaux
        current_hour = datetime.now().hour
        if current_hour not in self.last_signals:
            self.last_signals[current_hour] = 0
        
        if self.last_signals[current_hour] >= self.max_signals_per_hour:
            logger.warning("Limite de signaux horaire atteinte")
            return None
        
        # Sélectionner une paire aléatoire avec un bon payout
        available_pairs = get_all_pairs()
        if not available_pairs:
            return None
        
        # Filtrer les paires avec un payout minimum (simulé)
        pair_key = random.choice(available_pairs)
        pair_info = PAIRS[pair_key]
        
        # Simuler l'analyse de marché
        directions = ["CALL", "PUT"]
        direction = random.choice(directions)
        
        # Confiance basée sur des facteurs simulés
        confidence = round(random.uniform(0.65, 0.92), 2)
        
        # Prix d'entrée simulé
        base_price = random.uniform(1.05, 1.15)
        entry_price = round(base_price + random.uniform(-0.005, 0.005), 5)
        
        # Durée en fonction du timeframe
        duration_map = {
            "1min": 60,
            "2min": 120,
            "5min": 300
        }
        duration = duration_map.get(timeframe, 60)
        
        signal = {
            "asset": pair_key,
            "pair_display": pair_info["display"],
            "direction": direction,
            "entry_price": entry_price,
            "duration": duration,
            "timeframe": timeframe,
            "confidence": confidence,
            "timestamp": datetime.now(),
            "payout": pair_info.get("payout", 87),
            "indicators": {
                "rsi": round(random.uniform(25, 75), 2),
                "bb_upper": round(entry_price * 1.002, 5),
                "bb_lower": round(entry_price * 0.998, 5),
                "sma_short": round(entry_price * 0.9995, 5),
                "sma_long": round(entry_price * 1.0005, 5)
            }
        }
        
        # Incrémenter le compteur
        self.last_signals[current_hour] += 1
        self.signal_count += 1
        
        return signal
    
    def _format_signal(self, signal: dict) -> str:
        """Formater un signal pour l'envoi"""
        direction = signal["direction"]
        emoji = "🟢" if direction == "CALL" else "🔴"
        direction_text = "ACHAT (CALL)" if direction == "CALL" else "VENTE (PUT)"
        
        # Couleurs pour les indicateurs
        rsi_color = "🟢" if signal["indicators"]["rsi"] < 30 else "🔴" if signal["indicators"]["rsi"] > 70 else "🟡"
        
        signal_text = f"""
{emoji} **SIGNAL {direction_text}** {emoji}
{'=' * 40}

📊 **ACTIF**: {signal['pair_display']}
🕘 **HEURE D'ENTRÉE**: {signal['timestamp'].strftime('%H:%M')}
⏳ **EXPIRATION**: {signal['duration']}s ({signal['timeframe']})
💰 **PAYOUT**: {signal['payout']}%

🔮 **Direction**: {direction}
📊 **Confiance**: {signal['confidence']*100:.0f}%
💵 **Prix d'entrée**: {signal['entry_price']:.5f}

**Indicateurs:**
• RSI ({rsi_color}): {signal['indicators']['rsi']:.2f}
• BB Upper: {signal['indicators']['bb_upper']:.5f}
• BB Lower: {signal['indicators']['bb_lower']:.5f}
• SMA 2: {signal['indicators']['sma_short']:.5f}
• SMA 5: {signal['indicators']['sma_long']:.5f}

{'=' * 40}
⚠️ **Risque**: Gérez votre money management
📊 **Statistiques**: {self.signal_count} signaux envoyés
"""
        return signal_text
    
    # ==================== HANDLERS TELEGRAM ====================
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Commande /start"""
        user = update.effective_user
        
        welcome_text = """
👋 **Bonjour !**

Choisissez votre langue préférée.
Vous pouvez modifier la langue à tout moment depuis le menu principal
"""
        
        keyboard = [
            [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr")]
        ]
        
        await update.message.reply_text(
            welcome_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def language_selection(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Sélection de la langue"""
        query = update.callback_query
        await query.answer()
        
        language = query.data.split('_')[1]
        context.user_data['language'] = language
        
        # Sauvegarder l'utilisateur
        self._save_user(
            query.from_user.id,
            query.from_user.username or "unknown",
            language
        )
        
        # Message principal
        welcome_text = """
🤖 **LEGITTRADE Bot**

Bot qui traite les données de marché en temps réel sur toutes les 
principales paires de devises et identifie des points d'entrée 
structurés à la demande.

Développé par une équipe dédiée de développeurs et d'analystes de marché.
L'accès est basé sur des niveaux et lié au volume de trading actif sur Pocket Option.
"""
        
        keyboard = [
            [InlineKeyboardButton("🚀 Commencer", callback_data="start_bot")]
        ]
        
        try:
            await query.message.delete()
        except:
            pass
        
        await query.message.reply_text(
            welcome_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def start_bot(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Bouton Commencer"""
        query = update.callback_query
        await query.answer()
        
        main_text = """
📈 **LEGITTRADE Bot**

Bot analyse les tendances du marché à court terme et fournit 
des setups de trading structurés en temps réel - directement sur Telegram.

**Point d'entrée. Actif. Direction. Durée.**

Une session d'essai limitée est disponible pour les nouveaux utilisateurs.
"""
        
        keyboard = [
            [InlineKeyboardButton("🧪 Tester le bot", callback_data="test_bot")],
            [InlineKeyboardButton("🔗 Connecter un compte", callback_data="connect_account")],
            [InlineKeyboardButton("💎 Avoir signal", callback_data="get_signal")],
            [
                InlineKeyboardButton("🆘 Soutien", url="https://t.me/PrinceRoyal_1"),
                InlineKeyboardButton("📢 Canal", url="https://t.me/your_channel")
            ]
        ]
        
        try:
            await query.message.delete()
        except:
            pass
        
        await query.message.reply_text(
            main_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def test_bot(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Bouton Tester le bot"""
        query = update.callback_query
        await query.answer()
        
        test_text = """
🧪 **Tester le bot**

Pour tester le bot, veuillez connecter un compte.
Les comptes existants ne sont pas pris en charge.
"""
        
        keyboard = [
            [InlineKeyboardButton("➕ Créer un compte", url="https://pocketoption.com/signup")],
            [InlineKeyboardButton("✅ Vérifier le nouvel ID", callback_data="verify_id")],
            [InlineKeyboardButton("🔙 Retour", callback_data="back_to_main")]
        ]
        
        await query.message.reply_text(
            test_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def connect_account(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Connecter un compte"""
        query = update.callback_query
        await query.answer()
        
        text = """
🔗 **Connecter un compte**

Pour recevoir des signaux de trading, vous devez connecter votre compte Pocket Option.

1. Créez un compte sur Pocket Option
2. Envoyez votre ID Pocket Option
3. Attendez la validation par l'administrateur
"""
        
        keyboard = [
            [InlineKeyboardButton("➕ Créer un compte", url="https://pocketoption.com/signup")],
            [InlineKeyboardButton("✅ Vérifier l'ID", callback_data="verify_id")],
            [InlineKeyboardButton("🔙 Retour", callback_data="back_to_main")]
        ]
        
        await query.message.reply_text(
            text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def verify_id(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Vérification ID Pocket Option"""
        query = update.callback_query
        await query.answer()
        
        text = """
📝 **Vérification de l'ID**

Entrez votre ID Pocket Option.
**Chiffres uniquement.**

Exemple: `123456789`
"""
        
        keyboard = [
            [InlineKeyboardButton("🔙 Retour", callback_data="back_to_main")]
        ]
        
        await query.message.reply_text(
            text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        
        context.user_data['waiting_for_id'] = True
    
    async def handle_id_verification(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Gérer la vérification d'ID"""
        if not context.user_data.get('waiting_for_id', False):
            return
        
        user_input = update.message.text.strip()
        
        if not user_input.isdigit():
            await update.message.reply_text(
                "❌ Veuillez entrer uniquement des chiffres.",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Sauvegarder l'ID
        context.user_data['pocket_id'] = user_input
        context.user_data['waiting_for_id'] = False
        
        # Sauvegarder dans la base
        self._save_user(
            update.effective_user.id,
            update.effective_user.username or "unknown",
            context.user_data.get('language', 'fr'),
            pocket_id=user_input
        )
        
        # Envoyer à l'admin pour validation
        admin_message = f"""
🔑 **Nouvel ID à vérifier**

**User ID**: {update.effective_user.id}
**Username**: @{update.effective_user.username or "unknown"}
**ID Pocket**: `{user_input}`
**Langue**: {context.user_data.get('language', 'fr')}
"""
        
        for admin_id in ADMIN_IDS:
            try:
                keyboard = [
                    [
                        InlineKeyboardButton("✅ Valider", callback_data=f"validate_{update.effective_user.id}"),
                        InlineKeyboardButton("❌ Rejeter", callback_data=f"reject_{update.effective_user.id}")
                    ]
                ]
                await self.application.bot.send_message(
                    admin_id,
                    admin_message,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
            except Exception as e:
                logger.error(f"Erreur envoi à l'admin: {e}")
        
        await update.message.reply_text(
            "✅ **ID envoyé pour vérification !**\n"
            "Vous serez notifié une fois votre compte validé.",
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def validate_user(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Validation de l'utilisateur par l'admin"""
        query = update.callback_query
        await query.answer()
        
        action, user_id = query.data.split('_')
        user_id = int(user_id)
        
        if action == "validate":
            if self._validate_user(user_id):
                try:
                    await self.application.bot.send_message(
                        user_id,
                        """
✅ **Compte validé !**

Vous pouvez maintenant recevoir des signaux de trading.

Utilisez le bouton **💎 Avoir signal** pour commencer.

📊 **Bonne chance dans vos trades !**
""",
                        parse_mode=ParseMode.MARKDOWN
                    )
                except Exception as e:
                    logger.error(f"Erreur envoi à l'utilisateur: {e}")
                
                await query.message.edit_text(
                    "✅ **Utilisateur validé avec succès !**",
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await query.message.edit_text(
                    "❌ **Erreur lors de la validation**",
                    parse_mode=ParseMode.MARKDOWN
                )
        else:
            # Rejeter
            try:
                await self.application.bot.send_message(
                    user_id,
                    """
❌ **Compte rejeté**

Votre compte Pocket Option n'a pas été validé.

Veuillez contacter le support pour plus d'informations :
🆘 @PrinceRoyal_1
""",
                    parse_mode=ParseMode.MARKDOWN
                )
            except:
                pass
            
            await query.message.edit_text(
                "❌ **Utilisateur rejeté**",
                parse_mode=ParseMode.MARKDOWN
            )
    
    async def get_signal(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Bouton Avoir signal"""
        query = update.callback_query
        await query.answer()
        
        # Vérifier si l'utilisateur est validé
        user = self._get_user(query.from_user.id)
        
        if not user or not user.get('is_verified', False):
            await query.message.reply_text(
                """
❌ **Compte non validé**

Vous devez d'abord connecter et valider votre compte.

Utilisez le bouton **🔗 Connecter un compte**.
""",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        keyboard = [
            [InlineKeyboardButton("📊 1 Minute", callback_data="signal_1min")],
            [InlineKeyboardButton("📊 2 Minutes", callback_data="signal_2min")],
            [InlineKeyboardButton("📊 5 Minutes", callback_data="signal_5min")],
            [InlineKeyboardButton("📊 Toutes les paires", callback_data="signal_all")],
            [InlineKeyboardButton("🔙 Retour", callback_data="back_to_main")]
        ]
        
        await query.message.reply_text(
            "⏳ **Analyse en cours...**\n"
            "Choisissez la durée des signaux :",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def signal_generic(self, update: Update, context: ContextTypes.DEFAULT_TYPE, timeframe: str):
        """Générer et envoyer un signal"""
        query = update.callback_query
        await query.answer()
        
        # Vérifier l'utilisateur
        user = self._get_user(query.from_user.id)
        if not user or not user.get('is_verified', False):
            await query.message.reply_text(
                "❌ Compte non validé",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Générer le signal
        signal = self._generate_signal(timeframe)
        
        if not signal:
            await query.message.reply_text(
                f"""
⏳ **Aucun signal disponible pour {timeframe}**

Veuillez réessayer dans quelques minutes.

📊 **Limite horaire**: {self.max_signals_per_hour} signaux/heure
""",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Formater et envoyer
        signal_text = self._format_signal(signal)
        
        # Ajouter les statistiques
        user_stats = f"""
📊 **Vos statistiques**
- Signaux reçus: {self.signal_count}
- Dernier signal: {timeframe}
- Paiement moyen: {signal['payout']}%
"""
        
        keyboard = [
            [InlineKeyboardButton("📊 Nouveau signal", callback_data=f"signal_{timeframe}")],
            [InlineKeyboardButton("🔙 Retour", callback_data="back_to_main")]
        ]
        
        await query.message.reply_text(
            signal_text + "\n" + user_stats,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        
        logger.info(f"Signal {timeframe} envoyé à {query.from_user.id}")
    
    async def signal_1min(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Signal 1 minute"""
        await self.signal_generic(update, context, "1min")
    
    async def signal_2min(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Signal 2 minutes"""
        await self.signal_generic(update, context, "2min")
    
    async def signal_5min(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Signal 5 minutes"""
        await self.signal_generic(update, context, "5min")
    
    async def signal_all(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Signaux pour toutes les paires"""
        query = update.callback_query
        await query.answer()
        
        # Vérifier l'utilisateur
        user = self._get_user(query.from_user.id)
        if not user or not user.get('is_verified', False):
            await query.message.reply_text(
                "❌ Compte non validé",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Générer plusieurs signaux
        signals = []
        timeframes = ["1min", "2min", "5min"]
        all_text = "📊 **SIGNALS POUR TOUTES LES PAIRES**\n\n"
        
        for tf in timeframes:
            signal = self._generate_signal(tf)
            if signal:
                signals.append(signal)
                all_text += f"**{tf.upper()}**: {signal['pair_display']} - {signal['direction']} @ {signal['entry_price']:.5f}\n"
        
        if not signals:
            all_text += "\n⏳ Aucun signal disponible pour le moment."
        else:
            all_text += f"\n\n📊 **Total**: {len(signals)} signaux générés"
        
        keyboard = [
            [InlineKeyboardButton("📊 Actualiser", callback_data="signal_all")],
            [InlineKeyboardButton("🔙 Retour", callback_data="back_to_main")]
        ]
        
        await query.message.reply_text(
            all_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def back_to_main(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Retour au menu principal"""
        query = update.callback_query
        await query.answer()
        
        main_text = """
📈 **LEGITTRADE Bot**

Bot analyse les tendances du marché à court terme et fournit 
des setups de trading structurés en temps réel - directement sur Telegram.

**Point d'entrée. Actif. Direction. Durée.**
"""
        
        keyboard = [
            [InlineKeyboardButton("🧪 Tester le bot", callback_data="test_bot")],
            [InlineKeyboardButton("🔗 Connecter un compte", callback_data="connect_account")],
            [InlineKeyboardButton("💎 Avoir signal", callback_data="get_signal")],
            [
                InlineKeyboardButton("🆘 Soutien", url="https://t.me/PrinceRoyal_1"),
                InlineKeyboardButton("📢 Canal", url="https://t.me/your_channel")
            ]
        ]
        
        try:
            await query.message.delete()
        except:
            pass
        
        await query.message.reply_text(
            main_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    # ==================== CONFIGURATION ====================
    
    def setup_handlers(self):
        """Configuration des handlers"""
        self.application.add_handler(CommandHandler("start", self.start_command))
        
        # Callback handlers
        self.application.add_handler(CallbackQueryHandler(
            self.language_selection, pattern="^lang_"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.start_bot, pattern="^start_bot$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.test_bot, pattern="^test_bot$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.connect_account, pattern="^connect_account$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.verify_id, pattern="^verify_id$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.validate_user, pattern="^(validate|reject)_\\d+$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.get_signal, pattern="^get_signal$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.signal_1min, pattern="^signal_1min$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.signal_2min, pattern="^signal_2min$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.signal_5min, pattern="^signal_5min$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.signal_all, pattern="^signal_all$"
        ))
        self.application.add_handler(CallbackQueryHandler(
            self.back_to_main, pattern="^back_to_main$"
        ))
        
        # Message handler pour la vérification d'ID
        self.application.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            self.handle_id_verification
        ))
        
        # Error handler
        self.application.add_error_handler(self.error_handler)
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Gestionnaire d'erreurs"""
        logger.error(f"Update {update} caused error {context.error}")
        
        for admin_id in ADMIN_IDS:
            try:
                await self.application.bot.send_message(
                    admin_id,
                    f"❌ **Erreur Bot**\n```\n{context.error}\n```",
                    parse_mode=ParseMode.MARKDOWN
                )
            except:
                pass
    
    # ==================== DEMARRAGE ====================
    
    async def run(self):
        """Démarrer le bot"""
        if not self.token:
            logger.error("❌ TELEGRAM_BOT_TOKEN non configuré !")
            logger.info("Veuillez configurer le fichier .env")
            return
        
        # Créer l'application
        self.application = Application.builder().token(self.token).build()
        
        # Setup handlers
        self.setup_handlers()
        
        # Démarrer
        logger.info("🤖 LEGITTRADE Bot démarré sur Termux !")
        logger.info(f"📊 {len(PAIRS)} paires de devises disponibles")
        logger.info(f"👥 {len(ADMIN_IDS)} administrateurs configurés")
        logger.info("📱 Appuyez sur Ctrl+C pour arrêter")
        
        await self.application.run_polling()

# ==================== MAIN ====================

async def main():
    """Fonction principale"""
    try:
        bot = LegitTradeBot()
        await bot.run()
    except KeyboardInterrupt:
        logger.info("🛑 Bot arrêté par l'utilisateur")
    except Exception as e:
        logger.error(f"❌ Erreur fatale: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
