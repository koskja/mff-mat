# Vítejte v repozitáři mff-mat!

Tento repozitář slouží ke skladování úkolů z prvního ročníku Obecné matematiky. 
Najdete zde všechny úkoly, které se v tomto semestru probírají.
Zadání nových úloh budu (já, autor) osobně nahrávat, pokud si na to vzpomenu.

## Jak můžete přispět

Chcete-li se podílet na tomto projektu a přispět svými řešeními nebo materiály, postupujte podle následujících kroků:

1. **Forkněte tento repozitář**

   - Přejděte na stránku [koskja/mff-mat](https://github.com/koskja/mff-mat) a klikněte na tlačítko **Fork** vpravo nahoře.

2. **Naklonujte si svůj fork**

   - V terminálu spusťte:
     ```bash
     git clone https://github.com/VAŠE_UŽIVATELSKÉ_JMÉNO/mff-mat.git
     ```
     Nahraďte `VAŠE_UŽIVATELSKÉ_JMÉNO` svým uživatelským jménem na GitHubu.

3. **Přidejte původní repozitář jako upstream**

   - Abychom mohli synchronizovat změny z původního repozitáře, přidejte upstream:
     ```bash
     git remote add upstream https://github.com/koskja/mff-mat.git
     ```

4. **Aktualizujte svůj fork před prací**

   - Předtím, než začnete dělat změny, synchronizujte svůj fork:
     ```bash
     git fetch upstream
     git merge upstream/main
     ```

5. **Proveďte své změny**

   - Přidejte svá řešení nebo nové materiály.
   - Upravte existující soubory nebo přidejte nové.

6. **Commitujte své změny**
 Uložte své změny pomocí:
     ```bash
     git add .
     git commit -m "Přidal jsem své řešení úlohy XYZ"
     ```
, nebo ve VSCode otevřete Source Control panel (Ctrl+Shift+G; G) a klikněte na `+` pro všechny soubory, které chcete commitovat.

7. **Pushněte změny do svého forku**

   - Nahrajte své změny na GitHub:
     ```bash
     git push origin main
     ```

9. **Vytvořte Pull Request**

   - Přejděte na svůj fork na GitHubu.
   - Klikněte na tlačítko **Compare & Pull Request**.
   - Popište své změny a odešlete Pull Request.

## Důležité informace

- Tento projekt je určen k volnému sdílení. Nezapomínejte, že úkoly jsou od toho, aby vás něco naučily, a ne aby vám kazily pohodu a šanci na zápočet.
- Prosím, sdílejte pouze vlastní práci nebo práci, ke které máte oprávnění. Nechci, aby si pak ke mně někdo šel stěžovat.

## Kontakt

Máte-li jakékoli dotazy nebo potřebujete pomoc, neváhejte otevřít nový issue nebo mě kontaktovat přímo. 

---
