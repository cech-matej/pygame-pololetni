# Hádanka - hra v PyGame
*Multiplayer*

### Okruhy otázek
- Zeměpis (vyznačeno *žlutě*)
- Dějepis (vyznačeno *bíle*)
- Literatura (vyznačeno *modře*)

### Objekty hry
- 17 polí, která nesou náhodně zvolený okruh, viz. **Okruhy otázek**
- 2 hráči - modrý a červený

### Herní pravidla
Vždy začíná hráč s modrou barvou, kterému se (stejně jako červenému hráči) zobrazí pole s otázkou a 4 odpověďmi. V případě, že hráč klikl na správnou odpověď, vykreslí se odpověď zeleně (v opačném případě červeně) a zároveň se hráč posune o jedno pole dopředu (v opačném případě zůstává na aktuálním poli). 
Hráč, který dosáhne 17. pole a správně odpoví na poslední otázku daného okruhu, vyhrává.
