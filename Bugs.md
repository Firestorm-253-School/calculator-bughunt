# Bugs

1. Subtract
   - Time: 30s
   - Bug: Erste Zahl wird von der Zweiten subtrahiert
   - Erwartet: Zweite zahl wird von der Ersten subtrahiert
   - Ort: API - /api/calculate - subtract

2. Division durch 0
   - Time: 8min
   - Bug: Bei division durch 0 -> Backend nicht erreichbar.
   - Erwartet: Saubere Fehlermeldung (ANF-03)
   - Ort: API - /api/calculate - division

3. Multiply liefert falsches ergebnis
   - Time: 11min
   - Bug: Potenz statt multiplikation
   - Erwartet: Multiplikation
   - Ort: API - /api/calculate - multiply

4. Zahlen grösser und kleiner als 1 000 000 000 000 / -1 000 000 000 000 akzeptiert
   - Time: 15min
   - Bug: Zahlen über 1 000 000 000 000 und unter -1 000 000 000 000 werden nicht abgelehnt
   - Erwartet: (ANF-04) werte sollten mit einer meldung abgelehnt werden
   - Ort: Api - /api/calculate

5. Kein sauberer Error bei ungültiger Eingabe
   - Time: 18min
   - Bug: Wenn bei a oder b ein sting mitgegeben wird, bekommt man einen unsauberen 500 error
   - Ort: API - /api/calculate
   - Erwartet: Sauberer error (JSON / Status 400) - ANF-07

6. Bei einem Error wird immernoch das letzte Resultat angezeigt
   - Time: 23min
   - Bug: Resultat wird bei Error angezeigt
   - Erwartet: Resultat wird bei ungültiger eingabe / error nicht angezeigt - ANF-06
   - Ort: Frontend / UI

7. Overflow wird nicht sauber gehandled
   - Time: 30min
   - Bug: Wenn das ergebnis zu gross ist wird der error nicht sauber gehandled
   - Erwartet: Error wird sauber gehandled und angezeigt
   - Ort: API - /api/calculate
