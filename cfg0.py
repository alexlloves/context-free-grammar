import nltk

# -------------------------------------------
# Este programa usa NLTK para analizar frases en español
# según una gramática libre de contexto (CFG).
#
# - S: oración completa (Sentence)
# - NP: sintagma nominal (Noun Phrase), es el sujeto o complemento. Ej: "el perro", "la niña"
# - VP: sintagma verbal (Verb Phrase), contiene el verbo y puede tener complemento. Ej: "ve un gato"
# - Det: determinante (el, la, un, una)
# - N: sustantivo (niño, perro, gato...)
# - V: verbo (juega, ve, persigue)

# Definir la gramática en español
grammar = nltk.CFG.fromstring("""
    S -> NP VP

    NP -> Det N | N
    VP -> V | V NP

    Det -> "o" | "a" | "un" | "unha"
    N -> "rapaz" | "rapaza" | "perro" | "gato" | "pelota"
    V -> "xoga" | "ve" | "persigue"
""")

# Crear el parser
parser = nltk.ChartParser(grammar)

# Solicitar entrada
sentence = input("Frase en español: ").lower().split()

# Intentar analizar la frase
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()  # Opcional: muestra el árbol gráficamente
except ValueError:
    print("❌ No se pudo generar un árbol de análisis para esa frase.")
