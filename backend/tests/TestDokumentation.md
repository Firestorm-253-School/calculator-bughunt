# Test Dokumentation

## Tracebility Matrix

| ANF-ID | Anforderung | Test-IDs |
| - | - | - |
| ANF-01 | Die Applikation beherrscht genau vier Operationen: Addition, Subtraktion, Multiplikation und Division. Jede liefert das mathematisch korrekte Ergebnis. | TF-01, TF-04, TF-07, TF-11 |
| ANF-02 | Jede Rechnung nimmt genau zwei Operanden entgegen. | TF-14, TF-15 |
| ANF-03 | Eine Division durch Null wird abgefangen und mit einer verständlichen Meldung beantwortet. Die Applikation stürzt nicht ab. | TF-10 |
| ANF-04 | Operanden müssen zwischen −1 000 000 000 000 und +1 000 000 000 000 liegen, die Grenzen eingeschlossen. Werte ausserhalb werden mit einer Meldung abgelehnt. | TF-03, TF-06, TF-09, TF-13 |
| ANF-05 | Nicht-numerische Eingaben werden mit einer verständlichen Meldung abgelehnt. Die Applikation stürzt nicht ab. | TF-02, TF-05, TF-08, TF-12 |
| ANF-07 | Die API antwortet bei ungültigen Eingaben mit dem Statuscode 400 und einer JSON-Fehlermeldung, nicht mit 500. | TF-18 |
| ANF-08 | Liste mit Berechnungen: {operation, a, b} | TF-19 |

## Testprotokoll
| Durchlauf | TF-ID | Datum | Ergebnis | Tatsächliches Ergebnis |
| - | - | - | - | - |
| D1 | TF-16 | 08.09.26 | OK | - |
| D1 | TF-18 | 08.09.26 | OK | - |
| D1 | TF-19 | 08.09.26 | OK | - |
| D1 | TF-01 | 08.09.26 | OK | - |
| D1 | TF-02 | 08.09.26 | OK | - |
| D1 | TF-03 | 08.09.26 | OK | - |
| D1 | TF-04 | 08.09.26 | NotOK | -5 |
| D1 | TF-05 | 08.09.26 | OK | - |
| D1 | TF-06 | 08.09.26 | OK | - |
| D1 | TF-07 | 08.09.26 | OK | - |
| D1 | TF-08 | 08.09.26 | OK | - |
| D1 | TF-09 | 08.09.26 | OK | - |
| D1 | TF-10 | 08.09.26 | OK | - |
| D1 | TF-11 | 08.09.26 | OK | - |
| D1 | TF-12 | 08.09.26 | OK | - |
| D1 | TF-13 | 08.09.26 | OK | - |
| D1 | TF-14 | 08.09.26 | OK | - |
| D1 | TF-15 | 08.09.26 | OK | - |
| D1 | TF-16 | 08.09.26 | OK | - |
| D1 | TF-18 | 08.09.26 | OK | - |
| D1 | TF-19 | 08.09.26 | OK | - |

## Mängelliste
- Klasse 1: kritisch, System ist unbrauchbar, Datenverlust, Sicherheitslücke
- Klasse 2: schwer, Hauptfunktion gestört
- Klasse 3: leicht, stört, aber das Arbeiten ist möglich
- Klasse 4: kosmetisch, Schreibfehler oder Layout

| TF-ID | Klasse |
| - | - |
| TF-04 | 2 |