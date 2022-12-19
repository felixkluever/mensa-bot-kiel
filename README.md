# Mensa-Bot-Kiel
Ein Discord-Bot zum Ausgeben des Mensaspeiseplans in Kiel (Momentan nur Schwentinemensa Kiel)

## Bereits Gehostet

Unter dem folgenen Link ist der Bot bereits gehostet. Ich gehe davon aus, das er bis mindestens Sommer 2024 noch laufen sollte (sprich bis ich meinen Bachelor habe), garantiere aber für nichts.  

[Link zum Bot](https://discord.com/oauth2/authorize?client_id=1033814093364219965&scope=bot&permissions=3072)

## Selbst Hosten

### Vorraussetzungen

Falls der bot selbst gehostet werden soll werden folgene Dinge benötigt:

- Python (gestestet mit 3.10.6)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [python-discord](https://discordpy.readthedocs.io/en/stable/intro.html#installing)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [einen discord bot account](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)

### Anleitung

1. erfülle alle Vorraussetzungen
2. klone das repo
3. erstelle eine Datei namens `.env` im `src` Ordner mit folgenenm Inhalt:

``` 
DISCORD_KEY={YOUR KEY HERE}
```
Ersetz `YOUR KEY HERE` mit dem Key deines discord bot accounts

4. starte den Bot mit `Python3 start.py`
5. erstelle einen Bot-Join-Link [hier](https://discordapi.com/permissions.html) mit den Permissions:
  - view channels
  - send messages
6. lasse den Bot über deinen Bot-Link beitreten

## Zukünftige Entwicklung

Von meiner Seite aus gibt es gerade keine Pläne den Bot weiterzuentwickeln, außer es entstehen noch Wünsche nach neuen Features.
Allerdings wäre es theoretisch einfach möglich den Bot für alle andere Mensen des Studentenwerkes SH zu erweitern.

## Probleme
Bei Problemen könnt ihr mir gerne auf Discord schreiben oder einfach hier ein Issue erstellen oder sogar einen PR stellen wenn ihr das Problem selber beheben wollt.
