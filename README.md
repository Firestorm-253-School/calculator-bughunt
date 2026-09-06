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

Sie haben 35 Minuten Zeit, die Applikation manuell zu prüfen und so viele Fehler wie
möglich zu finden. Halten Sie für jeden Fund fest: **Fundstelle** (Datei, Funktion oder
Endpunkt), **Symptom** (was passiert, was sollte passieren) und **wie lange** ihr
gesucht habt. Es ist nicht bekannt, wie viele Fehler es gibt.

Prüft sowohl über die Oberfläche als auch direkt gegen die API:

```
GET  /api/operations
POST /api/calculate     Body: {"operation": "add", "a": 2, "b": 3}
```

## Anfoderungen

|      ANF-ID     |      Anforderung                                                                                                                                                    |      Priorität     |   |   |   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|---|---|---|
|     ANF-01      |     Die Applikation beherrscht genau vier Operationen: Addition, Subtraktion, Multiplikation und Division. Jede liefert das mathematisch korrekte Ergebnis.         |     hoch           |   |   |   |
|     ANF-02      |     Jede Rechnung nimmt genau zwei Operanden entgegen.                                                                                                              |     hoch           |   |   |   |
|     ANF-03      |     Eine Division durch Null wird abgefangen und mit einer verständlichen Meldung beantwortet. Die Applikation stürzt nicht ab.                                     |     hoch           |   |   |   |
|     ANF-04      |     Operanden müssen zwischen −1 000 000 000 000 und +1 000 000 000 000 liegen, die Grenzen eingeschlossen. Werte ausserhalb werden mit einer Meldung abgelehnt.    |     mittel         |   |   |   |
|     ANF-05      |     Nicht-numerische Eingaben werden mit einer verständlichen Meldung abgelehnt. Die Applikation stürzt nicht ab.                                                   |     hoch           |   |   |   |
|     ANF-06      |     Sobald eine Fehlermeldung erscheint, wird kein Ergebnis mehr angezeigt. Es darf nie gleichzeitig ein Ergebnis und eine Fehlermeldung sichtbar sein.             |     mittel         |   |   |   |
|     ANF-07      |     Die API antwortet bei ungültigen Eingaben mit dem Statuscode 400 und einer JSON-Fehlermeldung, nicht mit 500.                                                   |     hoch           |   |   |   |
