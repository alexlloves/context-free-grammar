import nltk

# -------------------------------------------
# Este programa usa NLTK para identificar 
# la estructura gramatical de una oración en español.
#
# Las variables no cambian:
# - S: Sentence (oración completa)
# - NP: Noun Phrase (sintagma nominal)
# - VP: Verb Phrase (sintagma verbal)
# - AP: Adjective Phrase (grupo de adjetivos)
# - PP: Prepositional Phrase (preposición + NP)
#
# Pero el vocabulario (palabras) está en español.
# -------------------------------------------

grammar = nltk.CFG.fromstring("""
    S -> NP VP

    AP -> A | A AP
    NP -> N | D NP | AP NP | N PP
    PP -> P NP
    VP -> V | V NP | V NP PP

    A -> "grande" | "azul" | "pequeno" | "seco" | "ancho"
    D -> "o" | "a" | "un" | "unha"
    N -> "ela" | "cidade" | "coche" | "calle" | "perro" | "binoculares"
    P -> "sobre" | "antes" | "debajo" | "con"
    V -> "viu" | "caminó"
""")

parser = nltk.ChartParser(grammar)

# Entrada del usuario
sentence = input("Introduza unha oración en galego: ").lower().split()

try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()  # Mostrar árbol gráfico (opcional)
        break
except ValueError:
    print("❌ Non se pode xerar unha árbore de análisis.")


"""Frases de ejemplo que sí funcionan:

    ela caminó

    o perro viu a cidade

    ela viu o coche con binoculares
 """
