
### Install the module from github like this
```python
!pip install git+https://github.com/JBreuerPY/germaNLG
```

### 1. Importing the module
- import the Phrase class of the germaNLG module
- all the nessecary files will be loaded, this might take about one or two seconds. But right after the module is imported generating works fast.


```python
from germaNLG.germaNLG import Phrase
```

### 2. Creating simple sentences
- A verb, a subject and an object can be added by simple functions of the Phrase class
- After the settings are made, the sentence can be realised and it will be printed out


```python
# creating a new phrase
p = Phrase()
# setting a verb
p.VERB("suchen")
# setting a subject 
p.SUBJECT("Person")
# setting an object
p.OBJECT("Schlüssel")
# Satz realisieren
p.realise()
```




    'die Person sucht den Schlüssel'



### 2.1 Person, numer and pronouns
- Person and number can be set by using the methods setPERSON() and setNUMBER()
- Otherwise person and number are handled automaticly
- pronouns can be filled in as subjects or objects (pronouns need to be lowercased!)
- possessive pronouns can be put in front of a noun


```python
p = Phrase()
p.VERB("lieben")
# pronoun as subject 
p.SUBJECT("ich")
# setting an object with a possessive pronoun
p.OBJECT("mein Hund")
p.realise()
```




    'ich liebe meinen Hund'



### 3 Adding adjectives
- Adjectives can be added to components
- The degree of an adjective can be set by giving one of the following arguments: positive, comparative, superlative (Default: positive)
- more adjectives can be added, by multiple uses of the function addADJ()


```python
# adding an adjective to the object
p.object.addADJ("alt")
p.realise()
```




    'ich liebe meinen alten Hund'




```python
# setting adjective degreee to comparative
p.object.setADJdegree("comparative")
p.realise()
```




    'ich liebe meinen älteren Hund'




```python
# setting adjective degreee to superlative
p.object.setADJdegree("superlative")
p.realise()
```




    'ich liebe meinen ältesten Hund'



### 3.1 More complex adjectival constructions
- It's possible to add more than one word when setting an adjective
- In this case the last word of the string will be inflected


```python
p = Phrase()
p.VERB("lieben")
p.SUBJECT("ich")
p.OBJECT("mein Hund")
# adding an adjectival construction
p.object.addADJ("dermaßen alt")
p.realise()
```




    'ich liebe meinen dermaßen alten Hund'



### 4. Subjects and objects
- Gender, stem changes and irregularities are handled by the module automaticly
- Since german has a complex declination system and the fact, that different verbs need to be handled differently it might be useful to specify how Objects should be handled, to avoid mistakes
- To make sure there will be no mistake generated features can be set for the the Objects, also for subjects
- If there are no modifications made the system will handle declination by it self (which can lead to mistakes)
- the following features can be set:
    - cases: "nom","dat","acc","gen"
    - number: "sg","pl"
    - articles: "def","indef","null"
    - negated article (kein): "neg"
    - gender: "f","m","n"


```python
p = Phrase()
p.VERB("vergeben")
p.SUBJECT("Mädchen")
p.OBJECT("Junge")

# setting the features of the subject
p.subject.setFEATURES(["pl"])

# setting the features of the object
p.object.setFEATURES(["dat","indef"])

p.realise()
```




    'die Mädchen vergeben einem Jungen'



### 4.1 Specifiying gender
- There are some nouns in German which have the same form but may have different gender
- For this reason it's possible to set the gender features "m","f","n"
- For all other nouns gender is handled automaticly


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Beamte")
# set gender to feminin
p.object.setFEATURES(["f"])

p.realise()
```




    'der Arzt operiert die Beamte'




```python
# set gender to masculin
p.object.setFEATURES(["m"])

p.realise()
```




    'der Arzt operiert den Beamten'



### 4.2 Extending a subject or an object
- Subjects and objects can be extended to create PP's, complements with conjunctions or genetive complements
- if an extension is created and no other parameters are set, by default a conjunctional phrase will be realised with the conjunction "und"


```python
p = Phrase()
p.VERB("suchen")
p.SUBJECT("Frau")
p.OBJECT("Schlüssel")

# features: accusative and indefinite
p.object.setFEATURES(["acc","indef"])

# extending subject
p.subject.extend("Mann")
# add a conjunction
p.subject.addCONJUNCTION("und")

# extending object
p.object.extend("Kühlschrank")
# add a preposition (a prepositional phrase will be created)
p.object.addPREPOSITION("in","dat")

p.realise()
```




    'die Frau und der Mann suchen einen Schlüssel im Kühlschrank'




```python
# Example for a genitive complement
p = Phrase()
p.SUBJECT("Freund")
p.subject.extend("Junge")
p.subject.setGENITIVE()
p.realise()
```




    'der Freund des Jungen'



### 4.3 Modifying extensions
- The created extension is an object of the instance it was created for
- It can be modified like a subject or an object


```python
p = Phrase()
p.SUBJECT("Vater")
p.subject.addADJ("alt")
p.subject.extend("Junge")
# adding an adjective to the extension
# (by default the conjunction "und" is used)
p.subject.extension.addADJ("flink")
p.realise()
```




    'der alte Vater und der flinke Junge'



### 4.4 Adding an object
- A second object may be added and will be treated as an indirect object
- instance an object by using the method addOBJECT()
- the new created object can be modified, by corresponding to "object2"


```python
p = Phrase()
p.SUBJECT("Mutter")
p.VERB("schreiben")
p.OBJECT("Tochter")
# Adding another object
p.addOBJECT("Brief")
# Modifying the new object
p.object2.setFEATURES(["indef"])
p.realise()
```




    'die Mutter schreibt der Tochter einen Brief'



### 4.5 Reflexive
- The reflexive can be activated by using the method setREFLEXIVE()
- When reflexive was set to True the Object will refer to the subject, so a reflexive Pronoun is treated like the object and can be modified like it


```python
p = Phrase()
p.SUBJECT("Mutter")
p.VERB("schreiben")

p.setREFLEXIVE()

p.addOBJECT("Brief")
p.object2.setFEATURES(["indef"])

p.realise()
```




    'die Mutter schreibt sich einen Brief'



### 5. Adding an adverb
- An adverb can be set as well as the position, where the the adverb should be placed
- The positions are represented by numbers from 1-4 (default: 2)
- if position 1 is chosen the subject and finite verb form are changed


```python
p = Phrase()
p.VERB("suchen")
p.SUBJECT("Frau")
p.OBJECT("Schlüssel")
p.object.setFEATURES(["acc"])
# adding an adverb, choosing default position
p.addADVERB("verzweifelt")
p.realise()
```




    'die Frau sucht verzweifelt den Schlüssel'




```python
# adding an adverb, choosing position 1
p.addADVERB("verzweifelt","1")
p.realise()
```




    'verzweifelt sucht die Frau den Schlüssel'



### 6. Tense, Aspect and Mood
- Tense Aspect and Mood can be determined by setting boolean attributes of the Phrase to True
- To do that the following Methods can be used:
- setPRESENT(), setPAST(), setFUTURE1(), setFUTURE2(), setPRESENTPERFECT(), setPASTPERFECT(), setIMPERATIVE(), setSUBJUNCTIVE1(), setSUBJUNCTIVE2()
- Per default present tense, indicative and imperfect are chosen
- Aspect ist handled by setting the perfect tenses


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

# Past tense
p.setPAST()
p.realise()
```




    'der Arzt operierte den Patienten'




```python
# Future tense
p.setFUTURE1()
p.realise()
```




    'der Arzt wird den Patienten operieren'




```python
# Future II + Subjunctive II
p.setPASTPERFECT()
p.setSUBJUNCTIVE2()
p.realise()
```




    'der Arzt hätte den Patienten operiert'



### 7. Passive
- Passive can be set by using the method setPASSIVE()


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

# Future II + Subjunctive II + Passive
p.setPASTPERFECT()
p.setSUBJUNCTIVE2()
p.setPASSIVE()
p.realise()
```




    'der Patient wäre vom Arzt operiert worden'



### 8. Negation
- Negation can be set by using the method setNEGATED()


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

# Future II + Subjunctive II + Passive
p.setFUTURE2()
# Negated
p.setNEGATED()
p.realise()
```




    'der Arzt wird den Patienten nicht operiert haben'



### 9. Interrogative
- Negation can be set by using the method setNEGATED()
- A W-question can be formed by adding a question particle with the method addW()


```python
p.setINTERROGATIVE()
p.realise()
```




    'wird der Arzt den Patienten nicht operiert haben'




```python
p.addW("warum")
p.realise()
```




    'warum wird der Arzt den Patienten nicht operiert haben'



### 10. Modal verbs
- A modal verb can be added to the sentence by using the method addMODALVERB()


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

p.addMODALVERB("müssen")
p.realise()
```




    'der Arzt muss den Patienten operieren'



### 11. Conjuntional clauses
- Conjunctional clauses can be formed by using the method addCONJUNCTION() and feeding a conjunction to it


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

p.addCONJUNCTION("dass")
p.realise()
```




    'dass der Arzt den Patienten operiert'



### 12. Relative clauses
- Relative clauses are are formed by using the method setRELATIVE()


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

p.setRELATIVE()
p.realise()
```




    'der Arzt, der den Patienten operiert'



### 13. Layout
- By using the method setPUNCTUATION(), the sentence will be capitalized an punctuation will be set


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

p.setPUNCTUATION()
p.realise()
```




    'Der Arzt operiert den Patienten.'




```python
p.setINTERROGATIVE()
p.realise()
```




    'Operiert der Arzt den Patienten?'



### 13.1 Contractions
- There are some prepositions which can merge with articles
- this process is done automaticly by default
- auto contractions can be avoided by using the method noCONTRACTIONS()


```python
p = Phrase()
p.VERB("operieren")
p.SUBJECT("Arzt")
p.OBJECT("Patient")

p.object.extend("Herz")
p.object.addPREPOSITION("an","dat")

p.setPUNCTUATION()
p.realise()
```




    'Der Arzt operiert den Patienten am Herz.'




```python
# Disable auto contractions
p.noCONTRACTIONS()
p.realise()
```




    'Der Arzt operiert den Patienten an dem Herz.'


