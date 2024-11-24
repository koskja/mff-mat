# P1M: Přesmyčky
Na vstupu je číslo N, pak N řádků s hesly (slova ve slovníku), pak číslo M a nakonec M řádků s dotazy (slova).

Pro každý dotaz najděte mezi hesly všechny jeho přesmyčky, tedy slova, která jsou složena ze stejných písmen ve stejných počtech, jen možná v jiném pořadí (každé slovo je svou vlastní přesmyčkou). Přesmyčky ke každému dotazu vypište na samostatný řádek v abecedním (lexikografickém) pořadí, oddělené mezerami. Pokud k dotazu není mezi hesly nalezena žádná přesmyčka, vypište prázdný řádek.

Příklad vstupu:

```
3
delta
datel
atlet
2
tadle
xyzzy
```

Odpovídající výstup:

```
datel delta
(prázdný řádek)
```
