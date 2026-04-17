# Jak nastavit vlastní doménu (technologie-bez-vrasek.com)

Aplikace aktuálně běží na adrese **https://t-b-v.onrender.com**.
Jako asistent s přístupem pouze přes API nemohu přímo ovládat nastavení tvého registrátora domény.

Pro připojení tvé domény `technologie-bez-vrasek.com` musíš udělat následující kroky:

1. **Jdi do administrace na Renderu**: Otevři si [dashboard.render.com](https://dashboard.render.com/) a přihlas se.
2. Vyber projekt **t-b-v** (Static Site).
3. V levém menu klikni na **Settings** a sjeď dolů do sekce **Custom Domains**.
4. Klikni na **Add Custom Domain** a napiš `technologie-bez-vrasek.com` a `www.technologie-bez-vrasek.com`.
5. **Nastav DNS záznamy u svého registrátora domény** (např. Wedos, Forpsi, Active24):
   - Budeš muset přidat **CNAME záznam** nebo **A záznam** tak, jak ti Render přesně ukáže na obrazovce (většinou CNAME pro `www` směřující na `t-b-v.onrender.com` a `A` záznam(y) pro hlavní doménu).
6. Render ti následně automaticky vygeneruje bezplatný SSL (HTTPS) certifikát. Může to trvat několik minut po změně DNS.
