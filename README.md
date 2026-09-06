# Taschenrechner – Auftrag

Diese Applikation wurde Ihnen **ohne Tests** übergeben.

## Starten

**Backend**

```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Läuft auf `http://localhost:5000`.

Zum Prüfen, ob das Backend läuft:

```bash
curl http://localhost:5000/api/operations
```

**Frontend**

```bash
cd frontend
python3 -m http.server 5173
```

Dann `http://localhost:5173` öffnen. Der Server muss **aus dem Ordner `frontend`**
gestartet werden, sonst wird die `index.html` nicht gefunden.

## Auftrag

Ihr habt 35 Minuten Zeit, die Applikation manuell zu prüfen und so viele Fehler wie
möglich zu finden. Haltet für jeden Fund fest: **Fundstelle** (Datei, Funktion oder
Endpunkt), **Symptom** (was passiert, was sollte passieren) und **wie lange** ihr
gesucht habt. Es ist nicht bekannt, wie viele Fehler es gibt.

Prüft sowohl über die Oberfläche als auch direkt gegen die API:

```
GET  /api/operations
POST /api/calculate     Body: {"operation": "add", "a": 2, "b": 3}
```
