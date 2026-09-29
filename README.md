# Tic-Tac-Toe 🎮

Prosty projekt **kółko i krzyżyk** napisany w Pythonie z wykorzystaniem biblioteki **Tkinter**.

Projekt zrobiłem, żeby poćwiczyć tworzenie GUI oraz pisanie własnej logiki dla przeciwnika sterowanego przez komputer.

## 🕹️ Tryby gry

W projekcie znajdują się 3 wersje przeciwnika:

### `vs_random.py`

Komputer wybiera wolne pole losowo.

Jest to najprostsza wersja i można ją dość łatwo pokonać.

### `vs_defense.py`

Komputer potrafi:

* wygrać, jeśli ma taką możliwość,
* zablokować ruch gracza, jeśli gracz może wygrać,
* w pozostałych sytuacjach wybrać losowe pole.

### `vs_impossible.py`

Najbardziej zaawansowana wersja przeciwnika.

Komputer analizuje układ planszy i oprócz wygrywania oraz blokowania gracza stara się przewidywać kolejne ruchy.

Nie jest to klasyczny algorytm **Minimax** — logika przeciwnika została napisana przeze mnie na podstawie różnych możliwych układów na planszy.

## ✨ Funkcje

* plansza 3x3,
* gra gracz vs komputer,
* losowanie gracza rozpoczynającego,
* wykrywanie zwycięstwa,
* wykrywanie remisu,
* podświetlanie wygranej linii,
* przycisk restartu,
* 3 poziomy przeciwnika.

## 🛠️ Technologie

* **Python**
* **Tkinter**
* **Random**

## ▶️ Uruchomienie

Do uruchomienia projektu potrzebny jest Python 3.

Po pobraniu repozytorium można uruchomić wybraną wersję:

```bash
python vs_random.py
```

```bash
python vs_defense.py
```

```bash
python vs_impossible.py
```

## 📁 Struktura projektu

```text
tic-tac-toe/
│
├── README.md
│
├── vs_random.py
├── vs_defense.py
└── vs_impossible.py
```

## 📌 O projekcie

Projekt jest jednym z moich projektów do nauki Pythona.

Podczas tworzenia ćwiczyłem między innymi pracę z **Tkinterem**, funkcjami, tablicami 2D oraz tworzeniem logiki dla przeciwnika komputerowego.

Kolejne wersje przeciwnika powstawały stopniowo — od prostego losowania ruchów, przez blokowanie gracza, aż do bardziej rozbudowanej analizy planszy.
