# Beispielaufgaben

## Beispielaufgaben

Hier sind ein paar Beispielaufgaben, die wir erstellt haben. Damit soll gezeigt werden wie erstellte Aufgaben und Variablen aussehen.
Ihr könnt in JACK Aufgaben von eurem "Workspace" aus importieren und exportieren. Die Aufgaben werden dann in einer ZIP Datei heruntergeladen.
Ihr könnt Aufgaben importieren, indem ihr in eurem Workspace einen Rechtsclick auf euren Benutzernamen macht und die Option "Import content" nutzt. Exportieren könnt ihr wenn ihr im Workspace Rechtsclick auf eine Aufgabe macht und die Option "Export Exercise" nutzt.

## Evaluatorausdrücke

Beim Überprüfen ob eine Eingabe in einem FillIn-Feld (https://wiki.uni-due.de/jack/index.php?title=Fill-In_(JACK3)), braucht man einen mathematischen Ausdruck mit welchem das Ergebnis überprüft wird. Man kann z.B. einen direkten Vergleich mit dem Operator `equals()` oder einen RegEx-Vergleich mit dem Operator `matches()` machen. Negierung kann mit `not()` erfolgen.

Ein paar Evaluator Beispiele. Wir nehmen an, dass wir ein Eingabefeld (FillIn) mit der Bezeichnung "a" haben. Die Bezeichnung kann bei Erstellen des Eingabefeldes gewählt werden.
Beispiele:
Es wird überprüft ob der Wert im Eingabefeld "a" dem Wert "42" (Integer) enspricht.

> equals([input=a], 42)

Es wird überprüft ob der Wert im Eingabefeld "a" dem Wert der Variable "var1" enspricht.

> equals([input=a], [var=var1])

Angenommen die Studierenden müssen für die Aufgaben in ein Textfeld den durch Komma getrennten Wert "1,2" angeben.
Damit Studierene z.B. eine beliebige Anzahl von Lehrzeichen zwischen den Kommas und Zahlen eingeben können, wäre es gut einen regulären Ausdruck zu nutzen.
**ABER** in diesem Fall wäre es besser einfach zwei Abgabefelder zu machen. Allgemein solltet ihr mehrere Eingaben in einem Textfeld mit Kommas getrennt vermeiden, da den Studierenden erstmal nicht klar ist wie sie Werte eingeben können. Es wäre besser, mehrere FillIn-Felder zu machen. Dieses Beispiel ist nur der Vollständigkeit halber:
Es wird überprüft ob der Wert im Eingabefeld "a" dem regulären Ausdruck "\s*1\s*,\s*2\s*" enspricht.

> matches([input=a], "\s*1\s*,\s*2\s*")

Es wird überprüft ob der Wert im Eingabefeld "a" dem regulären Ausdruck in der Variable "var1" enspricht.

> matches([input=a], [var=var1])

Es wird überprüft, dass der Wert im Eingabefeld "a" **NICHT** dem Wert "42" (Integer) enspricht.

> not(equals([input=a], 42))

# Sample Tasks (english version)

## Sample Tasks

Here are a few sample tasks we’ve created to demonstrate what tasks and variables look like.
In JACK, you can import and export tasks from your **Workspace**. The tasks are downloaded as a ZIP file.

You can import tasks by right-clicking your username in the Workspace and selecting **"Import content"**.
To export a task, right-click on the task in the Workspace and select **"Export Exercise"**.

## Evaluator Expressions

When checking if an input in a FillIn field (https://wiki.uni-due.de/jack/index.php?title=Fill-In_(JACK3)) is correct, you use a mathematical expression to evaluate the result.
You can, for example, use a direct comparison with the `equals()` operator, or a RegEx match with the `matches()` operator.
Negation can be applied using the `not()` function.

Here are a few evaluator examples.
Let’s assume we have an input field (FillIn) labeled `"a"`. The label can be defined when creating the FillIn field.

### Examples

**Check whether the value in input field "a" is equal to the integer value `42`:**

```text
equals([input=a], 42)
```

**Check whether the value in input field "a" is equal to the value of the variable `var1`:**

```text
equals([input=a], [var=var1])
```

Suppose students are required to enter the comma-separated value `"1,2"` into a text field.
To allow for any number of spaces between the commas and the numbers, using a regular expression would be helpful.

**HOWEVER**, in this case, it would be better to simply use two separate input fields.
In general, you should avoid asking students to enter multiple values separated by commas in a single text field, as it may not be immediately clear to them how the input should be formatted.
It’s better to use multiple FillIn fields instead.

This example is provided for completeness only:

**Check whether the value in input field "a" matches the regular expression `"\s*1\s*,\s*2\s*"`:**

```text
matches([input=a], "\s*1\s*,\s*2\s*")
```

**Check whether the value in input field "a" matches the regular expression stored in the variable `var1`:**

```text
matches([input=a], [var=var1])
```

Check that the value in input field "a" is NOT equal to the integer value 42:

```text
not(equals([input=a], 42))
```
