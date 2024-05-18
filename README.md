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

### 16.04.2024
- Prompting + Fine tuning
- Embeddings Tutorials https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
