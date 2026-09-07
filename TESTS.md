# Taschenrechner – Testdokumentation

## Äquivalenzklassen und Grenzwerte

Für die Berechnungsfunktionen wurden Äquivalenzklassen und Grenzwerte definiert. Dabei werden insbesondere gültige Werte, Werte ausserhalb des erlaubten Bereichs, negative Werte und nicht-numerische Eingaben betrachtet.

Der erlaubte Wertebereich für Zahlen liegt zwischen:

- **−1'000'000'000'000**
- **+1'000'000'000'000**

Werte ausserhalb dieses Bereichs müssen mit einer Fehlermeldung abgelehnt werden.

---

## Funktionalität: `add`

| Klasse / Grenzwert / Negativfall | Testwerte (a, b)        | Erwartetes Ergebnis |
| -------------------------------- | ----------------------- | ------------------- |
| Ungültig (zu klein)              | (-1'000'000'000'001, 1) | Fehlermeldung       |
| Gültig                           | (-1'000'000'000'000, 1) | akzeptiert          |
| Ungültig (zu gross)              | (1'000'000'000'001, 1)  | Fehlermeldung       |
| Ungültig (keine Zahl)            | ("abc", "")             | Fehlermeldung       |

---

## Funktionalität: `subtract`

| Klasse / Grenzwert / Negativfall | Testwerte (a, b)        | Erwartetes Ergebnis |
| -------------------------------- | ----------------------- | ------------------- |
| Ungültig (zu klein)              | (-1'000'000'000'001, 1) | Fehlermeldung       |
| Gültig                           | (-1'000'000'000'000, 1) | akzeptiert          |
| Ungültig (zu gross)              | (1'000'000'000'001, 1)  | Fehlermeldung       |
| Ungültig (keine Zahl)            | ("abc", "")             | Fehlermeldung       |

---

## Funktionalität: `divide`

| Klasse / Grenzwert / Negativfall | Testwerte (a, b)        | Erwartetes Ergebnis |
| -------------------------------- | ----------------------- | ------------------- |
| Ungültig (zu klein)              | (-1'000'000'000'001, 1) | Fehlermeldung       |
| Gültig                           | (-1'000'000'000'000, 1) | akzeptiert          |
| Ungültig (zu gross)              | (1'000'000'000'001, 1)  | Fehlermeldung       |
| Ungültig (keine Zahl)            | ("abc", "")             | Fehlermeldung       |
| Ungültig (Division durch 0)      | (500, 0)                | Fehlermeldung       |

---

## Funktionalität: `multiply`

| Klasse / Grenzwert / Negativfall | Testwerte (a, b)        | Erwartetes Ergebnis |
| -------------------------------- | ----------------------- | ------------------- |
| Ungültig (zu klein)              | (-1'000'000'000'001, 1) | Fehlermeldung       |
| Gültig                           | (-1'000'000'000'000, 1) | akzeptiert          |
| Ungültig (zu gross)              | (1'000'000'000'001, 1)  | Fehlermeldung       |
| Ungültig (keine Zahl)            | ("abc", "")             | Fehlermeldung       |

---

## Funktionalität: `calculate`

| Klasse / Grenzwert / Negativfall | Testwerte       | Erwartetes Ergebnis |
| -------------------------------- | --------------- | ------------------- |
| Gültig (gültige Operation)       | ("add", 1, 0)   | akzeptiert          |
| Ungültig (ungültige Operation)   | ("sdaad", 1, 2) | Fehlermeldung       |

---

# Testfälle

## TF-01 – Division durch Null wird abgefangen

**ANF-ID:** ANF-03

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `10`
2. Zweite Zahl: `0`
3. Operation `÷` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Die Meldung

> „Division durch Null ist nicht definiert“

erscheint. Es wird kein Ergebniswert angezeigt.

---

## TF-02 – Zahlen unter −1'000'000'000'000 werden abgefangen

**ANF-ID:** ANF-04

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `-1'000'000'000'001`
2. Zweite Zahl: `1`
3. Operation `+` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Die Meldung

> „Zahlen müssen zwischen −1 000 000 000 000 und +1 000 000 000 000 liegen“

erscheint. Es wird kein Ergebniswert angezeigt.

---

## TF-03 – Zahlen über 1'000'000'000'000 werden abgefangen

**ANF-ID:** ANF-04

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `1'000'000'000'001`
2. Zweite Zahl: `1`
3. Operation `+` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Die Meldung

> „Zahlen müssen zwischen −1 000 000 000 000 und +1 000 000 000 000 liegen“

erscheint. Es wird kein Ergebniswert angezeigt.

---

## TF-04 – Korrekte Berechnung der Addition innerhalb der Range

**ANF-ID:** ANF-01

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `1'000'000'000'000`
2. Zweite Zahl: `1`
3. Operation `+` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Das Ergebnis ist:

```text
1'000'000'000'001
```

---

## TF-05 – Korrekte Berechnung der Subtraktion innerhalb der Range

**ANF-ID:** ANF-01

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `-1'000'000'000'000`
2. Zweite Zahl: `1`
3. Operation `-` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Das Ergebnis ist:

```text
-999999999999
```

---

## TF-06 – Multiplikation wird korrekt berechnet

**ANF-ID:** ANF-01

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `20`
2. Zweite Zahl: `10`
3. Operation `×` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Das Ergebnis ist:

```text
200
```

---

## TF-07 – Nicht-numerische Eingaben werden abgelehnt

**ANF-ID:** ANF-05

### Vorbedingung

Backend läuft, Oberfläche ist geöffnet.

### Testschritte

1. Erste Zahl: `"abc"`
2. Zweite Zahl: `""`
3. Operation `×` wählen
4. **Berechnen** klicken

### Erwartetes Ergebnis

Die Meldung

> „Operanden müssen numerische Werte haben“

erscheint. Es wird kein Ergebniswert angezeigt.

---

## TF-08 – Nicht implementierte Operationen werden abgelehnt

**ANF-ID:** ANF-01

### Vorbedingung

Backend läuft.

### Testschritte

Einen POST-Request an `/api/calculate` mit folgendem Body senden:

```json
{
  "operation": "safsafa",
  "a": 1,
  "b": 1
}
```

### Erwartetes Ergebnis

Die Response lautet:

```json
{
  "error": "Unbekannte Operation: safsafa"
}
```

---

# Zusammenfassung der Testfälle

| TF-ID | ANF-ID | Funktionalität                          |
| ----- | ------ | --------------------------------------- |
| TF-01 | ANF-03 | Division durch Null                     |
| TF-02 | ANF-04 | Zahlen unterhalb des erlaubten Bereichs |
| TF-03 | ANF-04 | Zahlen oberhalb des erlaubten Bereichs  |
| TF-04 | ANF-01 | Addition                                |
| TF-05 | ANF-01 | Subtraktion                             |
| TF-06 | ANF-01 | Multiplikation                          |
| TF-07 | ANF-05 | Nicht-numerische Eingaben               |
| TF-08 | ANF-01 | Ungültige Operation                     |
