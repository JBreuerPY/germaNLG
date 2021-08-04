#!/usr/bin/env python
# coding: utf-8

import os
import pkg_resources
import zipfile
import site
import pickle
import re    
from random import choice
import site

"############################################################################"
# Wortlisten laden
"############################################################################"

# get path of the zip file
archive = zipfile.ZipFile(site.getsitepackages()[-1]+"\\germaNLG\\data\\files.zip", 'r')

# adjectives.pickle öffnen und dict speichern
pickle_in = archive.open("adjectives.pickle", "r")
adjectives = pickle.load(pickle_in)
pickle_in.close()

# nouns.pickle öffnen und dict speichern
pickle_in = archive.open("nouns.pickle", "r")
nouns = pickle.load(pickle_in)
pickle_in.close()

# verbs.pickle öffnen und dict speichern
pickle_in = archive.open("verbs.pickle", "r")
verbs = pickle.load(pickle_in)
pickle_in.close()

# adpositions.pickle öffnen und dict speichern
pickle_in = archive.open("adpositions.pickle", "r")
adpositions = pickle.load(pickle_in)
pickle_in.close()

# pronouns.pickle öffnen und dict speichern
pickle_in = archive.open("pronouns.pickle", "r")
pronouns = pickle.load(pickle_in)
pickle_in.close()

##########################################################################################
##########################################################################################
"######################################### morphemes #####################################"
##########################################################################################
##########################################################################################

adjective_endings = {
    "en" : [
        ["null","dat","pl"],
        ["null","gen","m"],
        ["null","gen","n"],
        ["def","nom","pl"],
        ["acc","m"],
        ["def","acc","pl"],
        ["def","dat"],
        ["indef","dat"],
        ["def","gen"],
        ["indef","gen","m"],
        ["indef","gen","f"],
        ["indef","gen","n"]
            ],
    "er" : [
        ["null","nom","m"],
        ["null","dat","f"],
        ["null","gen","f"],
        ["null","gen","pl"],
        ["indef","nom","m"],
        ["indef","gen","pl"]
            ],
    "em" : [
        ["null","dat","m"],
        ["null","dat","n"]
            ],
    "es" : [
        ["null","nom","n"],
        ["null","acc","n"],
        ["indef","nom","n"],
        ["indef","acc","n"]
           ],
    "e" : [
        ["null","nom","f"],
        ["null","nom","pl"],
        ["null","acc","pl"],
        ["def","nom","m"],
        ["def","nom","f"],
        ["indef","nom","f"],
        ["def","nom","n"],
        ["indef","nom","pl"],
        ["acc","f"],
        ["def","acc","n"],
        ["indef","acc","pl"]
        ]
    
}

articles = {
    # definiert
    "der" : [
        ["def","nom","m"],
        ["def","gen","f"],
        ["def","gen","pl"],
        ["def","dat","f"],
            ],
    "die" : [
        ["def","nom","f"],
        ["def","nom","pl"],
        ["def","acc","pl"],
        ["def","acc","f"],
            ],
    "das" : [
        ["def","nom","n"],
        ["def","acc","n"],
            ],
    "des" : [
        ["def","gen","m"],
        ["def","gen","n"],
            ],
    "dem" : [
        ["def","dat","m"],
        ["def","dat","n"],
            ],
    "den" : [
        ["def","dat","pl"],
        ["def","acc","m"],
            ],
    # indefiniert
    "ein" : [
        ["indef","nom","m"],
        ["indef","nom","n"],
        ["indef","acc","n"],
            ],
    "eine" : [
        ["indef","nom","f"],
        ["indef","acc","f"],
            ],
    "eines" : [
        ["def","gen","m"],
        ["def","gen","n"],
            ],
    "einem" : [
        ["indef","dat","m"],
        ["indef","dat","n"],
            ],
    "einen" : [
        ["indef","acc","m"],
            ],
    "einer" : [
        ["indef","gen","f"],
        ["indef","dat","f"]
            ]
}

##########################################################################################
##########################################################################################
"######################################### lexicon #####################################"
##########################################################################################
##########################################################################################

articles = {
    # definiert
    "der" : [
        ["def","nom","m","sg"],
        ["def","gen","f","sg"],
        ["def","gen","pl"],
        ["def","dat","f","sg"],
            ],
    "die" : [
        ["def","nom","f","sg"],
        ["def","nom","pl"],
        ["def","acc","pl"],
        ["def","acc","f","sg"],
            ],
    "das" : [
        ["def","nom","n","sg"],
        ["def","acc","n","sg"],
            ],
    "des" : [
        ["def","gen","m","sg"],
        ["def","gen","n","sg"],
            ],
    "dem" : [
        ["def","dat","m","sg"],
        ["def","dat","n","sg"],
            ],
    "den" : [
        ["def","dat","pl"],
        ["def","acc","m","sg"],
            ],
    # indefiniert
    "ein" : [
        ["indef","nom","m","sg"],
        ["indef","nom","n","sg"],
        ["indef","acc","n","sg"],
            ],
    "eine" : [
        ["indef","nom","f","sg"],
        ["indef","acc","f","sg"],
            ],
    "eines" : [
        ["indef","gen","m","sg"],
        ["indef","gen","n","sg"],
            ],
    "einem" : [
        ["indef","dat","m","sg"],
        ["indef","dat","n","sg"],
            ],
    "einen" : [
        ["indef","acc","m","sg"],
            ],
    "einer" : [
        ["indef","gen","f","sg"],
        ["indef","dat","f","sg"]
            ],
    # Nullartikel
    str() : [
        ["null"],
        ["indef","pl"]
         ]
}

personalPronouns = {
    "ich_nom_sg" : "ich",
    "ich_acc_sg" : "mich",
    "ich_dat_sg" : "mir",
    "ich_gen_sg" : "mir",
    
    "du_nom_sg" : "du",
    "du_acc_sg" : "dich",
    "du_dat_sg" : "dir",
    "du_gen_sg" : "dir",
    
    "er_nom_sg" : "er",
    "er_acc_sg" : "ihn",
    "er_dat_sg" : "ihm",
    "er_gen_sg" : "ihm",
    
    "sie_nom_sg" : "sie",
    "sie_acc_sg" : "sie",
    "sie_dat_sg" : "ihr",
    "sie_gen_sg" : "ihr",
    
    "es_nom_sg" : "es",
    "es_acc_sg" : "es",
    "es_dat_sg" : "ihm",
    "es_gen_sg" : "ihm",
    
    "wir_nom_pl" : "wir",
    "wir_acc_pl" : "uns",
    "wir_dat_pl" : "uns",
    "wir_gen_pl" : "uns",
    
    "ihr_nom_pl" : "ihr",
    "ihr_acc_pl" : "euch",
    "ihr_dat_pl" : "euch",
    "ihr_gen_pl" : "euch",
    
    "sie_nom_pl" : "sie",
    "sie_acc_pl" : "sie",
    "sie_dat_pl" : "ihnen",
    "sie_gen_pl" : "ihnen",
}

seperable_prefixes = ['auseinander', 'gegenüber', 'hinterher', 'hernieder', 'zusammen', 'herunter', 'hinunter', 'entgegen', 'herherab', 'vorüber', 'hinüber', 'zurecht', 'herüber', 'entlang', 'entzwei', 'voraus', 'herauf', 'hinein', 'nieder', 'hinaus', 'heraus', 'hervor', 'hinauf', 'vorbei', 'herbei', 'vorauf', 'zurück', 'herein', 'vorher', 'vorweg', 'hinweg', 'weiter', 'hinab', 'vorab', 'empor', 'hinan', 'heran', 'herzu', 'herum', 'voran', 'neben', 'hinzu', 'heim', 'nach', 'fehl', 'fern', 'fort', 'hoch', 'fest', 'los', 'vor', 'hin', 'bei', 'auf', 'mit', 'aus', 'rum', 'ein', 'weg', 'her', 'ab', 'an', 'da', 'zu']

##########################################################################################
##########################################################################################
"######################################### morphoNLG #####################################"
##########################################################################################
##########################################################################################

"########################################################################"
# Klasse: Adjective
"########################################################################"

class Adjective():
    def __init__(self,lemma):
        self.lemma = lemma
        self.case = "nom"
        self.article = "def"
        self.gender = "n"
        self.degree = "positive"
        self.position = "attributive"
        
    def setFEATURES(self,features):
        for feature in features:
            if feature in ["nom","dat","acc","gen"]:
                self.case = feature
            if feature in ["positive","comparative","superlative"]:
                self.degree = feature
            if feature in ["def","indef","null"]:
                self.article = feature
            if feature in ["m","f","n","pl"]:
                self.gender = feature
            if feature in ["attributive","predicative"]:
                self.position = feature
        
    def restem(self):
        # Attributiv
        if self.position == "attributive":
            # Komparativ
            if self.degree == "comparative":
                if self.lemma in adjectives:
                    return adjectives[self.lemma][0]
                else:
                    return self.lemma+"er"
            # Superlativ
            elif self.degree == "superlative":
                if self.lemma in adjectives:
                    return adjectives[self.lemma][1][:-2]
                else:
                    return self.lemma+"st"
            # Positiv
            else:
                if self.lemma[-2:] == "el":
                    return self.lemma[:-2]+"l"
                elif self.lemma[-2:] == "er" and self.lemma[-3] in "aeiou":
                    return self.lemma[:-2]+"r"
                elif self.lemma == "hoch":
                    return "hoh"
                else:
                    return self.lemma
        # Prädikativ
        else:
            # Komparativ
            if self.degree == "comparative":
                if self.lemma in adjectives:
                    return adjectives[self.lemma][0]
                else:
                    return self.lemma+"er"
            # Superlativ
            elif self.degree == "superlative":
                if self.lemma in adjectives:
                    return "am "+adjectives[self.lemma][1]
                else:
                    return "am "+self.lemma+"sten"
            # Positiv
            else:
                return self.lemma
            
    def decline(self):
        features = [self.article,self.case,self.gender]
        for ending in adjective_endings:
            for feats in adjective_endings[ending]:
                if all(element in features for element in feats) == True:
                    if self.position != "predicative":
                        if self.restem()[-1] == "e" and ending[0] == "e":
                            return self.restem()[:-1]+ending
                        else:
                            return self.restem()+ending
                    else:
                        return self.restem()
                
"########################################################################"
# Klasse: Noun
"########################################################################"

def create_noun_default_entry(lemma):
    word = ""
    rest = ""
    if lemma not in nouns:
        # Prüfe, ob es sich um eine Komposition handelt, deren letzte Komponente bekannt ist
        for num in range(len(lemma)):
            word = lemma[num:].capitalize()
            rest = lemma[:num]
            if len(word) > 1 and word in nouns:
                break
    # Eintrag erstellen
    default_entry = {}
    # Wenn es eine Komposition ist, wird der existierende Eintrag verwendet und erweitert
    if len(word) > 1 and word in nouns:
        for key in nouns[word]:
            if key == "gender":
                default_entry[key] = nouns[word][key]
            else:
                try:
                    default_entry[key] = rest.capitalize()+nouns[word][key].lower()
                except:
                    default_entry[key] = lemma
    # Default
    else:
        # Genus
        # Maskulin
        if "gender" not in default_entry:

            for suffix in ['ling', 'ich', 'us', 'er', 'ig']:
                if suffix in lemma and lemma[-len(suffix):] == suffix:
                    default_entry["gender"] = "m"
        # Feminin
        if "gender" not in default_entry:
            for suffix in ['schaft', 'keit', 'heit', 'enz', 'anz', 'tät', 'ion', 'ung', 'ie', 'ik']:
                if suffix in lemma and lemma[-len(suffix):] == suffix:
                    default_entry["gender"] = "f"
        # Neutral
        if "gender" not in default_entry:
            for suffix in ['ment', 'chen', 'lein', 'ing', 'en', 'ma', 'um']:
                if suffix in lemma and lemma[-len(suffix):] == suffix:
                    default_entry["gender"] = "n"
        # Default: Random
        if "gender" not in default_entry:
            default_entry["gender"] = choice(["n","f","m"])

        # Genitiv Singular
        if "gen_sg" not in default_entry:
            # n-Deklination
            if lemma[-1] == "e":
                default_entry["gen_sg"] = lemma+"n"
                default_entry["dat_sg"] = lemma+"n"
                default_entry["weak"] = True
            else:
                default_entry["gen_sg"] = lemma+"s"
        # Nominativ Plural
        # Endung -n/-en
        if "nom_pl" not in default_entry:
            for suffix in ['schaft', 'keit', 'heit', 'ung', 'tät', 'ion', 'ist', 
                           'ant', 'and', 'ent', 'us', 'um', 'ma', 'ik', 'in', 'or', 'e']:
                if suffix in lemma and lemma[-len(suffix):] == suffix:
                    if lemma[-1] in ["a","e"]:
                        default_entry["nom_pl"] = lemma[:-1]+"en"
                    elif lemma[-2] == "in":
                        default_entry["nom_pl"] = lemma[:-1]+"nen"
                    else:
                        default_entry["nom_pl"] = lemma+"en"
        if "nom_pl" not in default_entry:
            # Endung -e
            for suffix in ['ling', 'ier', 'ich', 'eur', 'ör', 'ig']:
                if suffix in lemma and lemma[-len(suffix):] == suffix:
                    default_entry["nom_pl"] = lemma+"e"
                    default_entry["dat_pl"] = lemma+"en"
        if "nom_pl" not in default_entry:
            # Endung -s
            for suffix in ['y', 'u', 'o', 'i', 'a']:
                if suffix in lemma and lemma[-len(suffix):] == suffix:
                    default_entry["nom_pl"] = lemma+"s"
        if "nom_pl" not in default_entry:
            # keine Endung
            default_entry["nom_pl"] = lemma
    return default_entry

class Noun():
    def __init__(self,lemma):
        self.lemma = lemma
        self.case = "nom"
        self.number = "sg"
        # Wenn kein Eintrag für das Nomen existiert wird ein Defaulteintrag erstellt
        if lemma not in nouns:
            nouns[lemma] = create_noun_default_entry(lemma)
        
    # Features eingeben
    def setFEATURES(self,features):
        for feature in features:
            if feature in ["nom","dat","acc","gen"]:
                self.case = feature
            if feature in ["sg","pl"]:
                self.number = feature
              
    # Funktion, die das Genus wiedergibt
    def gender(self):
        try:
            return nouns[self.lemma]["gender"]
        except:
            for num in range(len(self.lemma)):
                known_word = self.lemma[num:-1].capitalize()
                if len(known_word) > 1 and known_word in nouns:
                    return Noun(known_word.capitalize()).gender()
            
            return "n"
                
    # Funktion, die die deklinierte Form ausgibt
    def decline(self):
        # Wenn Lemma in "nouns" vorhanden ist
        if self.lemma in nouns:
            if "weak" in nouns[self.lemma]:
                if nouns[self.lemma]["gender"] == "m":
                    nouns[self.lemma]["acc_sg"] = self.lemma+"n"
            # Wenn ein Eintrag der entsprechenden Featurekombinationen in "nouns" vorhanden ist
            if self.case+"_"+self.number in nouns[self.lemma]:
                return nouns[self.lemma][self.case+"_"+self.number]
            # Wenn kein Eintrag existiert
            else:
                # Singular
                if self.number == "sg":
                    return self.lemma
                # Plural
                else:
                    # Versuche
                    try:
                        # Pluralform des Nominativs wiedergeben
                        return nouns[self.lemma]["nom_pl"]
                    # Default
                    except:
                        # Lemma wiedergeben
                        return self.lemma
        # Wenn Lemma nicht in "nouns" vorhanden ist
        else:
            return self.lemma
        
        
"########################################################################"
# Klasse: Verb
"########################################################################"

def create_verb_default_entry(lemma,stem):
    # if there is no existing entry for the lemma
    if lemma not in verbs:
        # If there is a verb with a common combound stem
        known_lemmas = [verb for verb in verbs if verb in lemma and verb != '']
        if known_lemmas != []:
            shortest_lemma = min(known_lemmas,key=len)
            seperaple_prefix = lemma.replace(shortest_lemma,'')
            if seperaple_prefix != shortest_lemma and seperaple_prefix != '':
                default_entry = {}
                for key in verbs[shortest_lemma]:
                    if verbs[shortest_lemma][key] == None:
                        default_entry[key] = verbs[shortest_lemma][key]
                    elif key == 'partII':
                        default_entry[key] = seperaple_prefix+verbs[shortest_lemma][key]
                    elif key in ['auxiliary','usage']:
                        default_entry[key] = verbs[shortest_lemma][key]
                    else:
                        default_entry[key] = verbs[shortest_lemma][key]+' '+seperaple_prefix
                return default_entry
                
    seperable_prefix = ""
    # Präfix von trennbarem Verb bestimmen
    for prefix in seperable_prefixes:
        if len(lemma) >= len(prefix) and prefix == lemma[:len(prefix)]:
            seperable_prefix = prefix
    # Stamm
    unkSTEM = stem
    # 1P SG Stamm
    if lemma[-3:] == "eln":
        stem_1p = lemma[:-3]+"le"
    else:
        stem_1p = stem
    # Suffixe bestimmen
    try:
        # -t
        if unkSTEM[-1] in ["d","t"]:
            t = "et"
        else:
            t = "t"
        # -st
        if unkSTEM[-1] in ["d","t"]:
            st = "est"
        if unkSTEM[-1] in ["s","z","ß","x"]:
            st = "t"
        else:
            st = "st"
        # -te
        if unkSTEM[-1] in ["d","t"]:
            te = "ete"
        else:
            te = "te"
        # -e
        if lemma[-3:] == "eln":
            e = ""
        else:
            e = "e"
    # Default bei Verben mit Stammlänge < 3
    except:
        e = "e"
        t = "t"
        st = "st"
        te = "te"
    # Nicht trennbare Verben
    if seperable_prefix == "":
        default_entry = {'pres_1_sg': stem_1p+e,
                            'usage': {},
                            'pres_2_sg': unkSTEM+st,
                            'pres_3_sg': unkSTEM+t,
                            'past_1_sg': unkSTEM+te,
                            'partII': 'ge'+unkSTEM+t,
                            'subjunct_1_sg': unkSTEM+te,
                            'imp_sg': unkSTEM,
                            'imp_pl': unkSTEM+t,
                            'auxiliary': 'haben'}
    # Trennbare Verben
    else:
        rest = unkSTEM[len(seperable_prefix):]
        rest_1p = stem_1p[len(seperable_prefix):]
        default_entry = {'pres_1_sg': rest_1p+e+' '+seperable_prefix,
                            'usage': {},
                            'pres_2_sg': rest+st+' '+seperable_prefix,
                            'pres_3_sg': rest+t+' '+seperable_prefix,
                            'past_1_sg': rest+te+' '+seperable_prefix,
                            'partII': seperable_prefix+'ge'+rest+t,
                            'subjunct_1_sg': rest+te+' '+seperable_prefix,
                            'imp_sg': rest+" "+seperable_prefix,
                            'imp_pl': rest+t+' '+seperable_prefix,
                            'auxiliary': 'haben'}

    if lemma in verbs and None in [verbs[lemma][i] for i in verbs[lemma]]:
        for key in verbs[lemma]:
            if verbs[lemma][key] != None:
                default_entry[key] = verbs[lemma][key]

    return default_entry

class Verb():
    def __init__(self,lemma):
        self.lemma = lemma
        self.person = "3"
        self.number = "sg"
        self.tense = "pres"
        self.aspect = "imperf"
        self.mood = "ind"
        self.voice = "active"
        try:
            # Trennbare Verben
            if lemma in verbs and len(verbs[lemma]["pres_1_sg"].split()) == 2:
                self.seperable = True
            else:
                self.seperable = False
        except:
            self.seperable = False
        # Kopulaverben
        if lemma in ["sein","werden","bleiben"]:
            self.copula = True
        else:
            self.copula = False
        # Stemming
        if self.lemma[-2:] == "en":
            self.stem = self.lemma[:-2]
        elif self.lemma[-1:] == "n": 
            self.stem = self.lemma[:-1]
        else:
            self.stem = self.lemma
        # Wenn kein Eintrag für das eingegebene Verb existiert, einen Defaulteintrag erstellen
        if self.lemma not in verbs or self.lemma in verbs and None in [verbs[self.lemma][i] for i in verbs[self.lemma]]:
            verbs[self.lemma] = create_verb_default_entry(self.lemma,self.stem)
                
    # Features setzen
    def setFEATURES(self,features):
        self.mood = "ind"
        self.number = "sg"
        self.aspect = "imperf"
        self.person = "3"
        self.tense = "pres"
        for feature in features:
            if feature in ["ind","imp","subjunct1","subjunct2"]:
                self.mood = feature
            if feature in ["sg","pl"]:
                self.number = feature
            if feature in ["perf","imperf"]:
                self.aspect = feature
            if feature in ["1","2","3"]:
                self.person = feature
            if feature in ["pres","past","fut"]:
                self.tense = feature
            if feature in ["active","passive"]:
                self.voice = feature
        if self.mood == "subjunct1" and self.tense == "past":
            self.tense = "pres"
        if self.mood == "subjunct2" and self.tense == "pres":
            self.tense = "past"
                
    # 1P SG wiedergeben, in einer Tupel
    # Index 0 enthält das Verb und Index 1 gff. ein das Präfix eines zusammengesetzten Verbs
    def form(self,spec):
        try:
            Form = verbs[self.lemma][spec+"_1_sg"]
            if len(Form.split()) == 2:
                return (Form.split()[0].strip()," "+Form.split()[1])
            else:
                return (Form,"")
        except:
            return (self.stem,"")
        
    # Hilfsverb
    def auxiliary(self):
        try:
            return verbs[self.lemma]["auxiliary"]
        except:
            return "haben"
        
    # Partizip II
    def participle(self):
        try:
            return verbs[self.lemma]["partII"]
        except:
            return "ge"+self.lemma
                
    # Ausführende Funktion, die das Verb konjugiert
    def conjugate(self):
        if self.lemma == "":
            return ""
        # ggf. Form trennen (bei trennbaren Verben)
        form = verbs[self.lemma]["pres_1_sg"].split()
        if len(form) == 1:
            form = [self.stem,""]
        else:
            form = [self.stem[len(form[1]):], " "+form[1]]
        # Aktiv
        if self.voice == "active":
            # Imperativ
            if self.mood == "imp":
                return verbs[self.lemma]["imp_"+self.number]
            # Kein Imperativ
            else:
                # Imperfekt
                if self.aspect == "imperf" and self.tense != "fut":
                    # Wenn das Wort im Lexikon vorhanden ist
                    if self.lemma in verbs:

                        # Subjunktiv 1
                        if self.mood == "subjunct1":
                            # Singular
                            if self.number == "sg":
                                # 1P + 3P
                                if self.person in ["1","3"]:
                                    if self.lemma == "sein":
                                        return "sei"
                                    # Endung -eln
                                    elif len(self.lemma) > 2 and self.lemma[-3:] == "eln":
                                        return form[0][:-2]+"le"+form[1]
                                    else:
                                        return form[0]+"e"+form[1]
                                # 2P
                                if self.person == "2":
                                    if self.lemma == "sein":
                                        return "seiest"
                                    else:
                                        # Endung mit -r oder -l
                                        if form[0][-1] in ["l","r"]:
                                            return form[0]+"st"+form[1]
                                        else:
                                            return form[0]+"est"+form[1]
                                        

                        # Wenn die Form im Eintrag vorhanden ist
                        if self.mood not in ["subjunct2","subjunct1"] and self.tense+"_"+self.person+"_"+self.number in verbs[self.lemma]:
                                # Form ausgeben
                                return verbs[self.lemma][self.tense+"_"+self.person+"_"+self.number]
                        elif self.mood == "subjunct2" and "subjunct_"+self.person+"_"+self.number in verbs[self.lemma]:
                                # Form ausgeben
                                return verbs[self.lemma]["subjunct_"+self.person+"_"+self.number]
                        # Wenn die Form nicht vorhanden ist
                        else:
                            # 2. Person
                            if self.person == "2":
                                # Singular
                                if self.number == "sg":
                                    # Subjunktiv 2
                                    if self.mood == "subjunct2":
                                        return self.form("subjunct")[0]+"st"+self.form("subjunct")[1]
                                    # Präteritum
                                    if self.mood != "subjunct2" and self.tense in ["past","pres"]:
                                        if verbs[self.lemma][self.tense+"_1_sg"][-1] in ["t","d"]:
                                            return self.form("past")[0]+"est"+self.form("past")[1]
                                        elif verbs[self.lemma][self.tense+"_1_sg"][-1] in ["s","ß","z"]:
                                            return self.form("past")[0]+"t"+self.form("past")[1]
                                        else:
                                            return self.form("past")[0]+"st"+self.form("past")[1]
                                # Plural
                                else:
                                    # Subjunktiv 2
                                    if self.mood == "subjunct2":
                                        return self.form("subjunct")[0]+"t"+self.form("subjunct")[1]
                                    # Präteritum
                                    if self.mood not in ["subjunct2","subjunct1"] and self.tense == "past":
                                        if self.form("past")[0][-1] in ["d","t"]:
                                            return self.form("past")[0]+"et"+self.form("past")[1]
                                        else:
                                            return self.form("past")[0]+"t"+self.form("past")[1]
                                    # Präsens (Plural)
                                    if "subjunct2" not in self.mood and self.tense == "pres":
                                        if self.mood != "subjunct1":
                                            if self.lemma == "sein":
                                                return "seid"
                                            # Endung -d/-t
                                            elif form[0][-1] in ["d","t","i"]:
                                                return form[0]+"et"+form[1]
                                            # Endung -ie
                                            elif self.stem[-3:] == "ien":
                                                return form[0]+"et"+form[1]
                                            # Default
                                            else:
                                                return form[0]+"t"+form[1]
                                        # Subjunktiv 1 2Pl
                                        else:
                                            if self.lemma == "sein":
                                                return "seiet"
                                            else:
                                                if form[0][-1] in ["r","l"]:
                                                    return form[0]+"t"+form[1]
                                                else:
                                                    return form[0]+"et"+form[1]

                            # 3. Person und 1. Person Plural
                            if self.person == "3" or self.person == "1" and self.number == "pl":
                                # Singular
                                if self.number == "sg":
                                    # Subjunktiv 2
                                    if self.mood == "subjunct2":
                                        return self.form("subjunct")[0]+self.form("subjunct")[1]
                                    # Präteritum
                                    if self.mood not in ["subjunct2","subjunct1"] and self.tense == "past":
                                        return self.form("past")[0]+self.form("past")[1]
                                # Plural
                                else:
                                    # Subjunktiv 2
                                    if self.mood == "subjunct2":
                                        if self.form("subjunct")[0][-1] == "e":
                                            return self.form("subjunct")[0]+"n"+self.form("subjunct")[1]
                                        else:
                                            return self.form("subjunct")[0]+"en"+self.form("subjunct")[1]
                                    # Präteritum
                                    if self.mood not in ["subjunct2","subjunct1"] and self.tense == "past":
                                        if self.form("past")[0][-1] == "e":
                                            return self.form("past")[0]+"n"+self.form("past")[1]
                                        else:
                                            return self.form("past")[0]+"en"+self.form("past")[1]
                                    # Präsens + Subjunktiv 1 (1+3P)
                                    if self.mood not in ["subjunct2"] and self.tense == "pres":
                                        if self.lemma == "sein":
                                            if self.mood == "subjunct1":
                                                return "seien"
                                            else:
                                                return "sind"
                                        # Default
                                        else:
                                            return self.lemma[len(form[1]):]+form[1]
                # Futur- und Perfektformen
                # Futur
                if self.tense == "fut":
                    aux = Verb("werden")
                    aux.setFEATURES([self.person,self.number,self.mood])
                    if self.aspect == "imperf":    
                        return aux.conjugate()+" "+self.lemma
                    else:
                        return aux.conjugate()+" "+self.participle()+" "+self.auxiliary()

                if self.aspect == "perf":
                    aux = Verb(self.auxiliary())
                    aux.setFEATURES([self.person,self.number,self.tense,self.mood])
                    return aux.conjugate()+" "+self.participle()
        # Passiv
        else:
            # Imperativ
            if self.mood == "imp":
                v = Verb("werden")
                v.setFEATURES(["2","imp",self.number])
                return v.conjugate()+" "+verbs[self.lemma]["partII"]
            # Kein Imperativ
            else:
                # Das Verb "werden" initialisieren
                werden = Verb("werden")
                werden.setFEATURES([self.person,self.number,self.tense,self.mood])
                # Imperfekt
                if self.aspect == "imperf":
                    # Präsens und Präteritum
                    if self.tense in ["pres","past"]:
                        return werden.conjugate()+" "+verbs[self.lemma]["partII"]
                    # Futur
                    else:
                        werden.setFEATURES([self.mood,self.person,self.number,"pres"])
                        return werden.conjugate()+" "+verbs[self.lemma]["partII"]+" werden"
                # Perfekt
                else:
                    # Hilfsverb "sein" initialisieren
                    aux = Verb("sein")
                    # Perfekt und Plusquamperfekt
                    if self.tense in ["pres","past"]:
                        aux.setFEATURES([self.person,self.number,self.tense,self.mood])
                        return aux.conjugate()+" "+verbs[self.lemma]["partII"]+" worden"
                    # Futur II
                    else:
                        werden.setFEATURES([self.person,self.number,"pres",self.mood])
                        return werden.conjugate()+" "+verbs[self.lemma]["partII"]+" worden sein"

##########################################################################################
##########################################################################################
"######################################### germaNLG #####################################"
##########################################################################################
##########################################################################################

"############################################################################"
# Funktionen
"############################################################################"

# Artikel
def getArticle(features):
    for article in articles:
        for feats in articles[article]:
            if all(element in features for element in feats) == True:
                if article == None:
                    return ""
                return article
            
# Verschmelzung von Präpositionen und Artikeln            
def mergePREP(string):
    output = string.replace("an dem","am").replace("bei dem","beim").replace("in dem","im").replace("von dem","vom").replace("zu dem","zum").replace("zu der","zur").replace("an das","ans").replace("in das","ins").replace("auf das","aufs")
    return output   
        
"############################################################################"
# Klasse: NP
"############################################################################"

class NP():
    def __init__(self,lemma):
        if len(lemma.split()) == 2 and lemma.split()[0] in pronouns:
            self.lemma = lemma.split()[1]
            self.pronoun = lemma.split()[0]
        else:
            self.lemma = lemma
            self.pronoun = ""
        self.case = "nom"
        self.number = "sg"
        self.article = "def"
        self.adjectives = []
        self.preposition = []
        self.degree = "positive"
        self.negated = False
        self.modified = False
        self.person = "3"
        self.complement = ""
        
    def setFEATURES(self,features):
        for feature in features:
            if feature in ["nom","dat","acc","gen"]:
                self.case = feature
                self.modified = True
            if feature in ["sg","pl"]:
                self.number = feature
            if feature in ["def","indef","null"]:
                self.article = feature
            if feature == "neg":
                self.article = "indef"
                self.negated = True
            if feature in ["m","f","n"]:
                # ggf. Defaulteintrag löschen
                if self.lemma in nouns:
                    if "weak" in nouns[self.lemma]:
                        del nouns[self.lemma]
                # Eintrag modifizieren ggf. erstellen
                n = Noun(self.lemma)
                nouns[self.lemma]["gender"] = feature
                
    def checkPERSON(self):
        # Person anpassen
        if self.lemma in ["wir","ich"]:
            self.person = "1"
        if self.lemma in ["du","ihr"]:
            self.person = "2"
        if self.lemma in ["er","sie","es"]:
            self.person = "3"
                
    def addADJ(self,adj):
        self.adjectives.append(adj)
        
    def addPREP(self,prep,case=""):
        self.preposition.append(prep)
        if case != "":
            self.case = case
        
    def setADJdegree(self,degree):
        if degree in ["comp","comparative"]:
            self.degree = "comparative"
        elif degree in ["super","superlative"]:
            self.degree = "superlative"
        else:
            self.degree = "positive"
            
    def addCOMPLEMENT(self,complement):
        self.complement = complement
            
    def createNP(self):
        if self.lemma in pronouns:
            return self.lemma
        else:
            n = Noun(self.lemma)
            n.setFEATURES([self.case,self.number])
            gender = n.gender()
            # Artikel
            if self.pronoun == "":
                article = getArticle([self.article,self.case,self.number,gender])
            # Wenn ein Pronomen mitgeliefert wurde
            else:
                self.article = "indef"
                self.negated = False
                article = getArticle([self.article,self.case,self.number,gender])
                if article == "":
                    article = self.pronoun+"e"
                else:
                    article = self.pronoun+article.replace("ein","")
            # Adjektive
            adjs = []
            for adj in self.adjectives:
                rest = ""
                if len(adj.split()) == 2:
                    rest = adj.split()[0]+" "
                    adj = adj.split()[1]
                a = Adjective(adj)
                a.setFEATURES([self.article,self.case,self.number,self.degree,gender])
                adjs.append(rest+a.decline())
            np = ""
            if self.preposition != []:
                np += self.preposition[0]+" "
            if article != "":
                np += article+" "
            if adjs != []:
                np += ", ".join(adjs)+" "
            np += n.decline()
            if self.negated == True:
                np = "k"+np
            # Ergänzung
            if self.complement != "":
                np = self.complement+" "+np
            return np            
        
        
"##############################################################################"
# Klasse: Subject
"##############################################################################"

class Subject(NP):
    def __init__(self,lemma):
        if len(lemma.split()) == 2 and lemma.split()[0] in pronouns:
            self.lemma = lemma.split()[1]
            self.pronoun = lemma.split()[0]
        else:
            self.lemma = lemma
            self.pronoun = ""
        self.case = "nom"
        self.number = "sg"
        self.article = "def"
        self.adjectives = []
        self.preposition = []
        self.degree = "positive"
        self.extension = False
        self.negated = False
        self.connector = ""
        self.modified = False
        self.person = "3"
        self.complement = ""
        
    def gender(self):
        n = Noun(self.lemma)
        return n.gender()
    
    def extend(self, extension):
        self.extension = True
        self.connector = "conjunction"
        self.conjunction = "und"
        self.extension = NP(extension)
        
    def addPREPOSITION(self,prepositon,case="dat"):
        self.connector = "preposition"
        self.extension.addPREP(prepositon)
        self.extension.setFEATURES([case])
        
    def addCONJUNCTION(self,conjunction):
        self.connector = "conjunction"
        self.conjunction = conjunction
        
    def setGENITIVE(self):
        self.connector = "genitive"
        self.extension.setFEATURES(["gen"])
        
    def realiseSUBJECT(self, auto_nom = True):
        self.checkPERSON()
        # Personalpronomen
        if self.lemma in ["ich", "du","er","sie","es","wir","ihr"]:
            if self.lemma in ["wir","ihr"]:
                self.number = "pl"
            if self.lemma in ["er","sie","es"] and self.number == "pl":
                self.lemma = "sie"
            if self.lemma == "ich" and self.number == "pl":
                self.lemma = "wir"
            if self.lemma == "du" and self.number == "pl":
                self.lemma = "ihr"
            return personalPronouns[self.lemma+"_"+self.case+"_"+self.number]
        # Automatisch Subjekt Nominativ zuweisen (Außer beim Passiv)
        if auto_nom == True and self.modified == False:
            self.setFEATURES(["nom"])
        subject = self.createNP()
        if self.extension == False:
            return subject
        else:
            if self.connector == "conjunction":
                subject += " "+self.conjunction+" "+self.extension.createNP()
            else:
                subject += " "+self.extension.createNP()
        return subject
    
    
"##############################################################################"
# Klasse: Object
"##############################################################################"    

class Object(Subject):
    def __init__(self,lemma):
        if len(lemma.split()) == 2 and lemma.split()[0] in pronouns:
            self.lemma = lemma.split()[1]
            self.pronoun = lemma.split()[0]
        else:
            self.lemma = lemma
            self.pronoun = ""
        self.case = "nom"
        self.number = "sg"
        self.article = "def"
        self.adjectives = []
        self.preposition = []
        self.degree = "positive"
        self.extension = False
        self.negated = False
        self.connector = ""
        self.modified = False
        self.person = "3"
        self.complement = ""
    
    def extend(self, extension,features=[]):
        self.extension = True
        self.connector = "conjunction"
        self.conjunction = "und"
        self.extension = NP(extension)
        self.extension.setFEATURES(features)
        
    def realiseOBJECT(self):
        self.checkPERSON()
        # Personalpronomen
        if self.lemma in ["ich", "du","er","sie","es","wir","ihr"]:
            if self.lemma in ["wir","ihr"]:
                self.number = "pl"
            if self.lemma in ["er","sie","es"] and self.number == "pl":
                self.lemma = "sie"
            if self.lemma == "ich" and self.number == "pl":
                self.lemma = "wir"
            if self.lemma == "du" and self.number == "pl":
                self.lemma = "ihr"
            return personalPronouns[self.lemma+"_"+self.case+"_"+self.number]
        # Reflexivpronomen
        if self.lemma == "REFL":
            if self.case in ["gen","nom"]:
                self.case = "acc"
            if self.person == "1":
                if self.subNumber == "sg":
                    if self.case == "dat":
                        return "mir"
                    else:
                        return "mich"
                else:
                    return "uns"
            elif self.person == "2":
                if self.subNumber == "sg":
                    if self.case == "dat":
                        return "dir"
                    else:
                        return "dich"
                else:
                    return "euch"
            else:
                return "sich"   
        # NP erstellen
        obj = self.createNP()
        if self.extension == False:
            return obj
        else:
            if self.connector == "conjunction":
                obj += " "+self.conjunction+" "+self.extension.createNP()
            else:
                obj += " "+self.extension.createNP()
        return obj
    
"##############################################################################"
# Klasse: VP
"##############################################################################"      
    
class VP():
    def __init__(self,verb):
        if len(verb.split()) == 1:
            self.verb = verb
            self.verbrest = ""
            self.secondverb = ""
        elif len(verb.split()) == 3 and verb.split()[0][-1] == "n" and verb.split()[1] == "und":
            self.verb = verb.split()[-1]
            self.secondverb = verb.split()[0]
            self.verbrest = ""
        else:
            self.verb = verb.split()[-1]
            self.verbrest = " ".join(verb.split()[:-1])
        self.person = "3"
        self.number = "sg"
        self.tense = "pres"
        self.mood = "ind"
        self.aspect = "imperf"
        self.modalverb = ""
        self.adverb = ""
        self.adverbPosition = ""
        self.negated = False
        self.interrogative = False
        self.w = ""
        self.relative = False
        self.subjunctional = False
        self.autodeclination = False
        self.reflexive = False
        self.objects = 0
        self.voice = "active"
        self.punctuation = False
        self.contractions = True
        
    def setPERSON(self,person):
        self.person = person
        
    def setNUMBER(self,number):
        self.number = number
        
    def setPASSIVE(self):
        self.voice = "passive"
        
    def setPRESENT(self):
        self.tense = "pres"
        
    def setPAST(self):
        self.tense = "past"
        
    def setFUTURE1(self):
        self.tense = "fut"
        
    def setFUTURE2(self):
        self.tense = "fut"
        self.aspect = "perf"
        
    def setPRESENTPERFECT(self):
        self.tense = "pres"
        self.aspect = "perf"
        
    def setPASTPERFECT(self):
        self.tense = "past"
        self.aspect = "perf"
        
    def setSUBJUNCTIVE1(self):
        self.mood = "subjunct1"
        
    def setSUBJUNCTIVE2(self):
        self.mood = "subjunct2"
        
    def setIMPERATIVE(self):
        self.mood = "imp"
        
    def setNEGATED(self):
        self.negated = True
        
    def setINTERROGATIVE(self):
        self.interrogative = True
        
    def addW(self,w="was"):
        self.interrogative = True
        self.w = w
        
    def addMODALVERB(self,modalverb):
        self.modalverb = modalverb
        
    def setRELATIVE(self):
        self.relative = True
    
    def addCONJUNCTION(self,subjunction="dass"):
        self.subjunctional = True
        self.subjunction = subjunction
        
    def SUBJECT(self,subject):
        self.subject = Subject(subject)
        
    def OBJECT(self,obj):
        self.object = Object(obj)
        self.objects = 1
        
    def addOBJECT(self,obj):
        self.object2 = Object(obj)
        self.objects = 2
        
    def addADVERB(self,adverb, position="2"):
        self.adverb = adverb
        if position in ["1","2","3","4"]:
            self.adverbPosition = position
            
    def addADJUNCT(self,adjunct):
        self.adjunct = NP(adjunct)
        
    def setREFLEXIVE(self):
        # Subjekt realisieren
        subject = self.subject.realiseSUBJECT()
        # Person und Numerus ggf. an Subjekt anpassen
        # Numerus
        if subject in ["er","es","du","ich"]:
            self.subject.number = "sg"
        if subject in ["ihr","wir"]:
            self.subject.number = "pl"
        # Person
        if subject in ["ich","wir"]:
            self.person = "1"
        if subject in ["du","ihr"]:
            self.person = "2"
        if subject in ["er","sie","es"]:
            self.person = "3"
        self.OBJECT("REFL")
        self.object.person = self.person
        self.object.subNumber = self.subject.number
        
    def setAUTO(self):
        self.autodeclination = True
        
    # Interpunktion und Satzgroßschreibung aktivieren
    def setPUNCTUATION(self):
        self.punctuation = True
        
    # Kontraktionen vermeiden
    def noCONTRACTIONS(self):
        self.contractions = False
        
    def info(self):
        return verbs[self.verb]["usage"]
        
    # Verbform erstellen
    # Gibt ein dict wieder, das die verschiedenen Bestandtteile der gesamten Verbform enthält
    def form(self,second=False):
        if second == False:
            verb = Verb(self.verb)
        else:
            verb = Verb(self.secondverb)
        parts = {}
        if self.verb == "":
            return {"finite_verb":"","rest":"","infinitive":""}
        # Kein Imperativ
        if self.mood != "imp":
            # Aktiv
            if self.voice == "active":
                # Numerus an Subjekt anpassen
                self.number = self.subject.number
                # Bei einer Subjekerweiterung Numerus anpassen
                try:
                    if self.subject.connector == "conjunction":
                        self.number = "pl"
                except:
                    pass
            # Passiv
            else:
                # Numerus an Subjekt anpassen
                try:
                    self.number = self.object.number
                except:
                    pass
                # Bei einer Subjekerweiterung Numerus anpassen
                try:
                    if self.object.connector == "conjunction":
                        self.number = "pl"
                except:
                    pass
            verb.setFEATURES([self.person,self.number,self.tense,self.mood,self.aspect,self.voice])
            modalverb = Verb(self.modalverb)
            modalverb.setFEATURES([self.person,self.number,self.tense,self.mood,self.aspect,self.voice])
            # Mit Modalverb
            if self.modalverb != "":
                # Aktiv
                if self.voice == "active":
                    parts["finite_verb"] = modalverb.conjugate().split()[0]
                    if len(modalverb.conjugate().split()) >= 2:
                        if self.tense != "fut" and self.aspect == "perf":
                            parts["rest"] = self.modalverb
                        else:
                            parts["rest"] = " ".join(modalverb.conjugate().split()[1:])
                    else:
                        parts["rest"] = ""
                    parts["infinitive"] = self.verb
                # Passiv
                else:
                    if self.tense in ["past","pres"] and self.aspect != "perf":
                        modalverb.setFEATURES([self.person,self.number,self.tense,self.mood,self.aspect,"active"])
                        parts["finite_verb"] = modalverb.conjugate().split()[0]
                        parts["rest"] = verbs[self.verb]["partII"]+" werden"
                        parts["infinitive"] = ""
                    else:
                        parts["finite_verb"] = verb.conjugate().split()[0]
                        if len(verb.conjugate().split()) >= 2:
                            parts["rest"] = " ".join(verb.conjugate().split()[1:])+" "+self.modalverb
                        else:
                            parts["rest"] = ""
                        parts["infinitive"] = ""
            # Ohne Modalverb
            else:
                parts["finite_verb"] = verb.conjugate().split()[0]
                if len(verb.conjugate().split()) >= 2:
                    parts["rest"] = " ".join(verb.conjugate().split()[1:])
                else:
                    parts["rest"] = ""
                parts["infinitive"] = ""
            return parts
        # Imperativ
        else:
            verb.setFEATURES([self.number,"2","imp"])
            if len(verb.conjugate().split()) == 2:
                parts["finite_verb"] = verb.conjugate().split()[0]
                parts["rest"] = " ".join(verb.conjugate().split()[1])
            else:
                parts["finite_verb"] = verb.conjugate()
                parts["rest"] = ""
            return parts
        
    def realise(self):
        # Wenn das Verb kein Kopulaverb ist und keine Spezifikation bezüglich des Kasus vorgenommen wurde
        try:
            if self.object.modified == False:
                self.autodeclination = True
        except:
            pass
        # Automatische Deklination
        if self.autodeclination == True:
            # 1 Objekt
            if self.objects == 1:
                for entry in verbs[self.verb]["usage"]:
                    if entry[1] == [] and len(entry[0]) == 1:
                        self.object.setFEATURES(entry[0])
                        break
                if self.object.case == "nom":
                    self.object.case = "acc"
            # 2 Objekte
            if self.objects == 2:
                for entry in verbs[self.verb]["usage"]:
                    if entry[1] == [] and len(entry[0]) == 2:
                        self.object.setFEATURES([entry[0][0]])
                        self.object2.setFEATURES([entry[0][1]])
                        break
                if self.object.case == "nom":
                    self.object.case = "dat"
                    self.object2.case = "acc"
                    
        # Kopulaverben
        if self.verb in ["sein","bleiben","werden"]:
            try:
                self.object.case = "nom"
            except:
                pass
            
        # Wenn Modus nicht Imperativ ist
        if self.mood != "imp":
            # Subjekt realisieren
            try:
                subject = self.subject.realiseSUBJECT()
            except:
                self.subject = Subject("es")
                subject = self.subject.realiseSUBJECT()
            
            # Person und Numerus ggf. an Subjekt anpassen
            # Aktiv
            if self.voice == "active":
                # Numerus
                if subject in ["er","es","du","ich"]:
                    self.subject.number = "sg"
                if subject in ["ihr","wir"]:
                    self.subject.number = "pl"
                # Person
                if subject in ["ich","wir"]:
                    self.person = "1"
                if subject in ["du","ihr"]:
                    self.person = "2"
                if subject in ["er","sie","es"]:
                    self.person = "3"
            # Passiv
            else:
                try:
                    # Numerus
                    if self.object.lemma in ["er","es","du","ich"]:
                        self.object.number = "sg"
                    if self.object.lemma in ["ihr","wir"]:
                        self.object.number = "pl"
                    # Person
                    if self.object.lemma in ["ich","wir"]:
                        self.person = "1"
                    if self.object.lemma in ["du","ihr"]:
                        self.person = "2"
                    if self.object.lemma in ["er","sie","es"]:
                        self.person = "3"
                except:
                    pass
                
        # Verbform-dict erstellen
        form = self.form()
        if self.secondverb != "":
            form2 = self.form(second=True)
            for key in form:
                if form2[key] != form[key]:
                    form[key] += " und "+form2[key]
            
        VF = ""
        LK = ""
        MF = ""
        RK = ""
        NF = ""
        
        # Imperativ
        if self.mood == "imp":
            LK += form["finite_verb"]
            if self.negated == True:
                MF += "nicht "
            # Objekt 1 und 2 ins Mittelfeld
            try:
                MF += self.object.realiseOBJECT()
            except:
                pass
            try:
                MF += " "+self.object2.realiseOBJECT()
            except:
                pass
            # Adverb ins Mittelfeld
            if self.adverb != "":
                MF += " "+self.adverb
            # Rest ins Mittelfeld
            MF += " "+form["rest"]
            
        # Kein Imperativ
        else:
            # Aktiv
            if self.voice == "active":
                # kein Relativsatz oder Subjunktional
                if self.relative == False and self.subjunctional == False:
                    # Aussage
                    if self.interrogative == False:
                        # Adverb nicht auf Position 1
                        if self.adverbPosition != "1":
                            VF += subject
                            LK += self.w+" "+form["finite_verb"]
                        # Position 1
                        else:
                            VF += self.w+" "+form["finite_verb"]
                            LK += subject
                    # Frage
                    else:
                        # W-Fragewort
                        VF += self.w+" "+form["finite_verb"]
                        LK += subject
                    # Objekt 1 und 2 ins Mittelfeld
                    try:
                        MF += self.object.realiseOBJECT()
                    except:
                        pass
                    try:
                        MF += " "+self.object2.realiseOBJECT()
                    except:
                        pass
                    # Adverb
                    if self.adverb != "":
                        # Position 1
                        if self.adverbPosition == "1":
                            VF = self.adverb+" "+VF
                        # Position 2
                        if self.adverbPosition == "2":
                            MF = self.adverb+" "+MF
                        # Position 3
                        if self.adverbPosition == "3":
                            MF += " "+self.adverb
                        # Position 4
                        if self.adverbPosition == "4":
                            NF = self.adverb
                        
                    # Übrige Verbformen
                    RK += form["infinitive"]+" "+form["rest"]
                    
                # Relativsatz oder Subjunktional
                else:
                    # Subjunktional
                    if self.subjunctional == True:
                        LK += self.subjunction+" "
                    # Relativsatz
                    if self.relative == True:
                        LK += subject+", "+getArticle([self.subject.gender(),self.subject.number,self.subject.case,"def"])
                    # Subjekt im Mittelfeld
                    if self.subjunctional == True and self.relative == False:
                        MF += subject+" "
                    # Objekt 1 und 2 ins Mittelfeld
                    try:
                        MF += self.object.realiseOBJECT()
                    except:
                        pass
                    # Adverb ins Mittelfeld
                    if self.adverb != "":
                        MF += " "+self.adverb
                    RK += form["infinitive"]+" "+form["rest"]+" "+form["finite_verb"]
                    try:
                        MF += " "+self.object2.realiseOBJECT()
                    except:
                        pass
                # Negation
                if self.negated == True:
                    MF += " nicht"
            # Passiv
            else:
                # kein Relativsatz oder Subjunktional
                if self.relative == False and self.subjunctional == False:
                    
                    # Verb: Frage
                    if self.interrogative == True:
                        # W-Fragewort
                        VF += self.w+" "+form["finite_verb"]+" "
                        
                    # Objekte
                    # Objekt 1 ins Vorfeldfeld
                    object_used = False
                    try:
                        self.object2.setFEATURES(["nom"])
                        VF += self.object2.realiseOBJECT()+" "
                        # Verb
                        if self.interrogative == False:
                            if self.adverbPosition != "1":
                                LK += form["finite_verb"]+" "
                            else:
                                VF = form["finite_verb"]+" "+VF+" "
                    except:
                        try:
                            self.object.setFEATURES(["nom"])
                            VF += self.object.realiseOBJECT()+" "
                            if self.interrogative == False:
                                if self.adverbPosition != "1":
                                    LK += form["finite_verb"]+" "
                                else:
                                    VF = form["finite_verb"]+" "+VF+" "
                            object_used = True
                        except:
                            object_used = True
                    # Objekt 2 ins Mittelfeld
                    if object_used == False:
                        try:
                            self.object.setFEATURES(["dat"])
                            MF += " "+self.object.realiseOBJECT()
                        except:
                            pass
                    
                    # Subjekt in Mittelfeld
                    self.subject.setFEATURES(["dat"])
                    try:
                        self.subject.extension.setFEATURES(["dat"])
                    except:
                        pass
                    MF += " von "+self.subject.realiseSUBJECT(auto_nom=False)
                    
                    # Adverb
                    if self.adverb != "":
                        # Position 1
                        if self.adverbPosition == "1":
                            VF = self.adverb+" "+VF
                        # Position 2
                        if self.adverbPosition == "2":
                            MF = self.adverb+" "+MF
                        # Position 3
                        if self.adverbPosition == "3":
                            MF += " "+self.adverb
                        # Position 4
                        if self.adverbPosition == "4":
                            NF = self.adverb
                    
                    # Restliche Verbformen
                    RK += form["infinitive"]+" "+form["rest"]
                    
                
                else:
                    # Subjunktional
                    if self.subjunctional == True:
                        VF += self.subjunction+" "
                         
                    # Objekte
                    # Objekt 1 ins Vorfeldfeld
                    object_used = False
                    try:
                        if self.w == "":
                            self.object2.setFEATURES(["nom"])
                            VF += self.object2.realiseOBJECT()+" "
                            if self.relative == True:
                                VF +=", "+getArticle([self.object2.gender(),self.object2.number,self.object2.case,"def"])+" "
                    except:
                        if self.w == "":
                            self.object.setFEATURES(["nom"])
                            VF += self.object.realiseOBJECT()+" "
                            if self.relative == True:
                                VF +=", "+getArticle([self.object.gender(),self.object.number,self.object.case,"def"])+" "
                        object_used = True
                    # Objekt 2 ins Mittelfeld
                    if object_used == False:
                        try:
                            self.object.setFEATURES(["dat"])
                            MF += " "+self.object.realiseOBJECT()
                        except:
                            pass
                    
                    # Subjekt in Mittelfeld
                    self.subject.setFEATURES(["dat"])
                    MF += " von "+self.subject.realiseSUBJECT(auto_nom=False)
                    
                    # Adverb ins Mittelfeld
                    if self.adverb != "":
                        MF += " "+self.adverb
                    
                    # Restliche Verbformen
                    RK += form["infinitive"]+" "+form["rest"]+" "+form["finite_verb"]
                    
                # Negation
                if self.negated == True:
                    MF += " nicht"
                    
        # Verbrest, bei komplexen Verben
        if self.verbrest != "":
            MF += " "+self.verbrest+" "
                    
        # Ausgabe
        output = re.sub(r"\s+"," ", " ".join([VF, LK, MF, RK, NF]).strip()).replace(" ,",",")
        # ggf. ein Adjunkt hinzufügen
        try:
            output += " "+self.adjunct.createNP()
        except:
            pass
        # Großschreibung und Interpunktion
        if self.punctuation == True:
            if self.subjunctional == False:
                output = output[0].upper()+output[1:]
            if self.interrogative == True:
                output += "?"
            else:
                output += "."
        # Kontraktionen von Präposition und Artikel
        if self.contractions == True:
            output = mergePREP(output)
        return output
    
    
"########################################################################"    
# Klasse: Phrase
"########################################################################"    

class Phrase(VP):
    def __init__(self):
        self.verb = ""
        self.verbrest = ""
        self.secondverb = ""
        self.person = "3"
        self.number = "sg"
        self.tense = "pres"
        self.mood = "ind"
        self.aspect = "imperf"
        self.modalverb = ""
        self.adverb = ""
        self.adverbPosition = ""
        self.negated = False
        self.interrogative = False
        self.w = ""
        self.subjunctive = "2"
        self.relative = False
        self.subjunctional = False
        self.autodeclination = False
        self.reflexive = False
        self.objects = 0
        self.voice = "active"
        self.punctuation = False
        self.contractions = True
        
    def VERB(self,verb):
        if len(verb.split()) == 1:
            self.verb = verb
            self.verbrest = ""
            self.secondverb = ""
        elif len(verb.split()) == 3 and verb.split()[0][-1] == "n" and verb.split()[1] == "und":
            self.verb = verb.split()[-1]
            self.secondverb = verb.split()[0]
            self.verbrest = ""
        else:
            self.verb = verb.split()[-1]
            self.verbrest = " ".join(verb.split()[:-1]) 

            
# Functions for faster use of sentence parts

# NP
def np(noun,features=[],adjs=[],prep=''):
    np = NP(noun)
    np.setFEATURES(features)
    [np.setADJdegree(feature) for feature in features]
    [np.addADJ(adj) for adj in adjs]
    np.addPREP(prep)
    return np.createNP().strip()

# Single adjective
def single_adj(adj,features=[]):
    a = Adjective(adj)
    a.setFEATURES(features)
    return a.decline()

# Single verb
def single_verb(verb,features=[]):
    v = Verb(verb)
    v.setFEATURES(features)
    return v.conjugate()