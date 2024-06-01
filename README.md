## Entwicklungsumgebung einrichten

1. Poetry installieren `pip install poetry`
2. Abhängigkeiten herunterladen `poetry install`
3. `OPENAI_API_KEY` als Umgebungsvariable einrichten, siehe https://platform.openai.com/api-keys
4. Test von OPENAI starten `poetry run python test.py`

## Docker Image bauen und ausführen
Hinweis: Um das Docker Image zu ändern, bitte `Dockerfile` bearbeiten.
1. `docker build -t faktencheck:latest .`
1. `docker run faktencheck:latest`

## Ziel des Projektes

1. Epic: Als politisch interessierter Mensch führe ich politische Gespräche im Netz und real. Ich möchte dabei eine Hilfe haben um Fakten zu überprüfen und pro/contra Belege für Aussagen zu finden. Dazu brauche ich eine "App", wo ich Fragen oder Aussagen eingeben kann und verifizierte Belege erhalten kann.
    1. Feature: Projekt aufsetzen mit Poetry, Git/GitHub und Jupyter
        1. US: Projekt wird dockerisiert
        1. US: CICD pipeline aufsetzen in GitHub um das Docker Image zu bauen
        1. US: Jupyter funktioniert bei Julia und Christian
    1. Feature: OpenAI/ChatGPT auswerten, ob es für das Projekt verwendet werden kann 
        1. US: Als User möchte eine Frage an OpenAI über API senden und eine Antwort erhalten.
        1. US: Wir erhalten beim Aufruf der API eine Quota Meldung und OpenAI kann nicht verwendet werden.

## Projekt Logbuch

### 25.05.2024
- Embeddings in die Tiefe und ausprobieren

### 06.05.2024
- Prompting + Fine tuning
- Embeddings Tutorials https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

### 01.06.2024
1. OPENAI / Python
    - Social Media Bot (Mastodon, BluSky?, LinkedIn?, Reddit?, Facebook?, Instagram?, TikTok? - https://developers.tiktok.com/: Frage/Antwort Bot
    - Embeddings (Hypothese: Eine Frage/mehrere Antworten, Frage mit Antworten mit Hilfe von Embeddings)
    - Retrain (Ziel: wie erreicht? oder warum nicht erreicht?)
2. Kurs zu dem Thema
    - OpenAI API Einführung
    - Wie funktioniert Embeddings
    - Retrain
    - Wie baut man ein Bot

**Was wollen wir machen: Wir wollen ein Produkt, das in Produktion geht und echte Kunden hat.**

1 Iteration (3 Monaten = 12 Termine = Anfang Oktober): Bot in Social Media, User gibt eine Frage ein, Bot antwortet.
- Welche Platform klären (mit Beispiel)
- Wo läuft unser Bot (auf welchem Server)
- Welche Daten des Bots wollen wir analysieren? KPI, die wir messen
- OPENAI API, wie verwenden, Kosten klären

Infrastruktur, wo läuft unser Docker Container: Azure, AWS, Google, Telekom
- 1 virtuelle Maschine 1 CPU, 1 GB RAM, 25 GB Disk
    - Google 25 EUR
    - Digital Ocean 6 USD = 6,5 EUR
    - AWS 9,6 USD = 10 EUR 
    - Azure 6,5 EUR
  [Entscheidung: wir nehmen das **nicht**]
- AWS Lamda sind die ersten 1 Mio. Aufrufe kostenlos und für uns genau das richtige
  [Entscheidung: wir nehmen das]
- zuerst lokal, dann remote

### 08.06.2024
- eine Dummy AWS Lamda Function schreiben und zum laufen bringen in AWS

### 15.06.2024
- Tiktok, Instagram, LinkedIn, Facebook, BluSky, Mastodon, X (letzte Bastion)
- Bot Tutorial durchspielen
- Outcome: Entscheidung welche SM Plattform

### 22.06.2024
- Starten der Entwicklung: Klasse, Methoden
