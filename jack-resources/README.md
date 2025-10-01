# Einarbeitung in JACK

Was ihr in den folgenden Ordnern findet:

- `Beispielaufgaben`: Eine von uns erstelle Beispielaufgaben. Diese zeigen Beispielhaft wie man (detailliertes) Feedback gibt, wie man mit generierten Variablen arbeitet und folgt unseren Konventionen und Standards. Diese Aufgabe könnt ihr als .zip-Datei in Jack importieren.
- `Codebloecke_in_Aufgaben_hinzufuegen`: Beinhaltet das Python Skript mit Erklärung wie ihr die aufklappbaren Codeblöcke erstellen und in JACK einfügen könnt.
- `JACK-Wiki`: Ein paar Worte bezüglich des Wikis. Dort haben wir ein paar relevante Links des Wiki gesammelt.
- `Aufgabenvariablen_generieren`: Enthält alle von uns bisher dazu erarbeiteten Skripte und ein Beispiel zur Aufgabenvariablengenerierung.
- `Standards`: Eine Beispielaufgabe ist enthalten, die keine Tatsächliche Aufgabe implementiert, sondern lediglich unsere Standards aufzeigt. Diese Aufgabe könnt ihr ebenfalls als .zip-Datei in Jack importieren. Außerdem gibt es noch eine README-Datei, die weitere Standards enthält, sodass wir konsistente Kurse erstellen.

# Tipps

- Solltet ihr unter MacOS arbeiten, könnt ihr zum Komprimieren von Aufgaben vor dem Importieren in Jack nicht die hauseigene Komprimierfunktion nutzen, da diese weitere Dateien in die zip-Datei einfügt. Damit kann Jack nicht umgehen und wird diese zip-Datei nicht akzeptieren. Verwendet stattdessen eine CLI-Tool (z. B. ditto) zum Komprimieren.
- Falls ihr euch mit dynamischer Bildeinbettung beschäftigt meldet euch bei Edward Späth (edward.spaeth@stud.fra-uas.de).

# Getting Started with JACK (english version)

## Folder Overview

- **`Beispielaufgaben` (Example Tasks)**
  Contains an example task created by us. It demonstrates how to provide (detailed) feedback, how to work with generated variables, and follows our conventions and standards.
  👉 You can import this task into JACK as a `.zip` file.

- **`Codebloecke_in_Aufgaben_hinzufuegen` (Adding Code Blocks to Tasks)**
  Includes the Python script and explanation on how to create expandable code blocks and insert them into JACK.

- **`JACK-Wiki`**
  A short note on the wiki, where we’ve collected some relevant JACK Wiki links.

- **`Aufgabenvariablen_generieren` (Generating Task Variables)**
  Contains all scripts developed so far for generating task variables, along with an example.

- **`Standards`**
  Contains an example task that doesn’t implement an actual task but showcases our formatting and content standards.
  👉 This task can also be imported into JACK as a `.zip` file.
  Additionally, there’s a `README` file with further standards to ensure consistency across all courses.

---

## Tips

- **macOS Users:**
  When compressing tasks for JACK import, do **not** use the built-in compression function. It includes extra files that JACK can't handle and will cause import errors.
  ✅ Use a CLI tool like `ditto` instead:
  ```bash
  ditto -c -k --sequesterRsrc --keepParent your-folder your-folder.zip
  ```
