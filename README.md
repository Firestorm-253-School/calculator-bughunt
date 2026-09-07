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

Dann `http://localhost:5173` öffnen. Der Server muss **aus dem Ordner** `frontend`
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


| ANF-ID | Anforderung                                                                                                                                                  | Priorität |      |                                                                                                                                                             |                                                                                                                                                                                                |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ANF-01 | Die Applikation beherrscht genau vier Operationen: Addition, Subtraktion, Multiplikation und Division. Jede liefert das mathematisch korrekte Ergebnis.      | hoch      | 5min | Multiplikation ist quadriren und nicht multiplizieren 3x3=27                                                                                                | calculator.py Line 16,17                                                                                                                                                                       |
| ANF-02 | Jede Rechnung nimmt genau zwei Operanden entgegen.                                                                                                           | hoch      | 2min | Er nimmt mehr entgegen als 3 verwirft einfach die 3 weg wo nicht a oder b ist wirft aber keinen fehler                                                      |                                                                                                                                                                                                |
| ANF-03 | Eine Division durch Null wird abgefangen und mit einer verständlichen Meldung beantwortet. Die Applikation stürzt nicht ab.                                  | hoch      | 5min | Keine verständliche fehlermeldung nur Backend nicht erreichbar bei einer null nur wenn beide null ist funktioniert die fehermeldung anstat and or verwenden | calculator.py line 20-23                                                                                                                                                                       |
| ANF-04 | Operanden müssen zwischen −1 000 000 000 000 und +1 000 000 000 000 liegen, die Grenzen eingeschlossen. Werte ausserhalb werden mit einer Meldung abgelehnt. | mittel    |      |                                                                                                                                                             |                                                                                                                                                                                                |
| ANF-05 | Nicht-numerische Eingaben werden mit einer verständlichen Meldung abgelehnt. Die Applikation stürzt nicht ab.                                                | hoch      | 4min | API gibt ValueError: could not convert string to float: 'a' zurück wenn ich buchstaben eingebe                                                              | api.py 38-42 er versucht den wert zuerste zu einem float zu convertieren bevor er ihn bearbeitet dadurch bevor fehlermeldung zurück geworfen werden kann status code 500 Internal server error |
| ANF-06 | Sobald eine Fehlermeldung erscheint, wird kein Ergebnis mehr angezeigt. Es darf nie gleichzeitig ein Ergebnis und eine Fehlermeldung sichtbar sein.          | mittel    | 1min | Alte ergebnise werden nicht gelöscht wenn ein fehler auftrat                                                                                                |                                                                                                                                                                                                |
| ANF-07 | Die API antwortet bei ungültigen Eingaben mit dem Statuscode 400 und einer JSON-Fehlermeldung, nicht mit 500.                                                | hoch      | 1min | gibt bei string eingaben statuscode 500 zurück                                                                                                              |                                                                                                                                                                                                |




## Addieren


| Äquivalenz Klassen | Bereich    | Vertreter       | Erwartung     |
| ------------------ | ---------- | --------------- | ------------- |
| gültig             | Zahlen     | 10/10           | 20            |
| ungültig           | Buchstaben | a/10, 10/a, a/a | Fehlermeldung |



| Wert                              | Warum     |
| --------------------------------- | --------- |
| 10e10000000000000000000000000000  | Overflow  |
| -10e10000000000000000000000000000 | Underflow |



| TF-ID | ANF-ID | Titel               | Testschritte                                  | Erw. Ergebnis |
| ----- | ------ | ------------------- | --------------------------------------------- | ------------- |
| TF-01 | ANF-01 | Zahlen Addieren     | add(10,10)                                    | 20            |
| TF-02 | ANF-05 | Buchstaben Addieren | add(a,10)                                     | Err           |
| TF-03 | ANF-04 | Over-/Underflow     | add(10e1000, 10e1000) add(-10e1000, -10e1000) | Err           |




## Subtrahieren


| Äquivalenz Klassen | Bereich    | Vertreter       | Erwartung     |
| ------------------ | ---------- | --------------- | ------------- |
| gültig             | Zahlen     | 10/10, -10/-10  | 0             |
| ungültig           | Buchstaben | a/10, 10/a, a/a | Fehlermeldung |



| Wert                              | Warum     |
| --------------------------------- | --------- |
| 10e10000000000000000000000000000  | Overflow  |
| -10e10000000000000000000000000000 | Underflow |



| TF-ID | ANF-ID | Titel                   | Testschritte                                 | Erw. Ergebnis |
| ----- | ------ | ----------------------- | -------------------------------------------- | ------------- |
| TF-04 | ANF-01 | Zahlen Subtrahieren     | sub(10, 5)                                   | 5             |
| TF-05 | ANF-05 | Buchstaben Subtrahieren | sub(a,10)                                    | Err           |
| TF-06 | ANF-04 | Over-/Underflow         | sub(10e1000, 10e1000) sub(-10e1000, 10e1000) | Err           |




## Dividieren


| Äquivalenz Klassen | Bereich          | Vertreter       | Erwartung     |
| ------------------ | ---------------- | --------------- | ------------- |
| gültig             | Zahlen           | 10/10, -10/-10  | 1             |
| ungültig           | Buchstaben       | a/10, 10/a, a/a | Fehlermeldung |
| ungültig           | Division durch 0 | 10/0            | Fehlermeldung |



| Wert                              | Warum                |
| --------------------------------- | -------------------- |
| 0                                 | Division mit 0 = NaN |
| 10e10000000000000000000000000000  | Overflow             |
| -10e10000000000000000000000000000 | Underflow            |



| TF-ID | ANF-ID | Titel                 | Testschritte                                    | Erw. Ergebnis |
| ----- | ------ | --------------------- | ----------------------------------------------- | ------------- |
| TF-07 | ANF-01 | Zahlen Dividieren     | div(10,10)                                      | 1             |
| TF-08 | ANF-05 | Buchstaben Dividieren | div(a,10)                                       | Err           |
| TF-09 | ANF-04 | Over-/Underflow       | div(10e1000, 10e-1000) div(-10e-1000, 10e-1000) | Err           |
| TF-10 | ANF-03 | Division mit 0        | div(10, 0)                                      | Err           |




## Multiplizieren


| Äquivalenz Klassen | Bereich        | Vertreter       | Erwartung     |
| ------------------ | -------------- | --------------- | ------------- |
| gültig             | Zahlen         | 10/10, -10/-10  | 100           |
| ungültig           | Buchstaben     | a/10, 10/a, a/a | Fehlermeldung |
| gültig             | Multiplikation | 10/0, 0/10      | 0             |



| Wert                              | Warum     |
| --------------------------------- | --------- |
| 10e10000000000000000000000000000  | Overflow  |
| -10e10000000000000000000000000000 | Underflow |



| TF-ID | ANF-ID | Titel           | Testschritte                                   | Erw. Ergebnis |
| ----- | ------ | --------------- | ---------------------------------------------- | ------------- |
| TF-11 | ANF-01 | Zahlen Mult     | mult(10,10)                                    | 100           |
| TF-12 | ANF-05 | Buchstaben Mult | mult(a,10)                                     | Err           |
| TF-13 | ANF-04 | Over-/Underflow | mult(10e1000, 10e1000) mult(-10e1000, 10e1000) | Err           |




## Weiteres


| TF-ID | ANF-ID | Titel                                  | Testschritte                               | Erw. Ergebnis    |
| ----- | ------ | -------------------------------------- | ------------------------------------------ | ---------------- |
| TF-14 | ANF-02 | Anzahl Operatoren 3                    | add(10,10,10)                              | Err              |
| TF-15 | ANF-02 | Anzahl Operatoren 2                    | add(10,10)                                 | 20               |
| TF-16 | ANF-02 | Anzahl Operatoren 1                    | add(10)                                    | Err              |
| TF-17 | ANF-06 | If Err → result empty                  | Err                                        | result = ""      |
| TF-18 | ANF-07 | If API-Input invalid → Status 400 +msg | `{ "operation": "add", "a": 2, "b": "a" }` | Status 400 + msg |
 
