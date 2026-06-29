#!/usr/bin/env python3
"""Generate word-connections table tbody (run once, paste into word-connections.html)."""
from pathlib import Path

groups = [
    ("Nature", [
        ("root", ["Sun", "Sol", "Soleil", "Sole", "Sol", "Sonne"], "en-break"),
        ("derived", ["solar", "solar", "solaire", "solare", "solar", "solar"], "en-aligned"),
    ]),
    ("Nature", [
        ("root", ["Sea", "Mar", "Mer", "Mare", "Mar", "Meer"], "en-break"),
        ("derived", ["marine", "marino", "marin", "marino", "marinho", "marin"], "en-borrowed"),
        ("derived", ["maritime", "marítimo", "maritime", "marittimo", "marítimo", "maritim"], "en-borrowed"),
    ]),
    ("Work", [
        ("root", ["Work", "Trabajo", "Travail", "Lavoro", "Trabalho", "Arbeit"], "en-break"),
        ("derived", ["worker", "trabajador", "travailleur", "lavoratore", "trabalhador", "Arbeiter"], None),
        ("derived", ["labor", "trabajar", "travailler", "lavorare", "trabalhar", "arbeiten"], "en-borrowed"),
    ]),
    ("Food", [
        ("root", ["Eat", "Comer", "Manger", "Mangiare", "Comer", "Essen"], "en-break"),
        ("derived", ["food", "comida", "nourriture", "cibo", "comida", "Essen"], "en-break"),
        ("derived", ["dining room", "comedor", "salle à manger", "sala da pranzo", "refeitório", "Speiseraum"], None),
    ]),
    ("Body", [
        ("root", ["Tongue", "Lengua", "Langue", "Lingua", "Língua", "Zunge"], None),
        ("derived", ["language", "lenguaje", "langage", "linguaggio", "linguagem", "Sprache"], "en-break"),
        ("derived", ["linguist", "lingüista", "linguiste", "linguista", "linguista", "Linguist"], "en-aligned"),
        ("derived", ["sublingual", "sublingual", "sublingual", "sublinguale", "sublingual", "sublingual"], "en-aligned"),
        ("derived", ["cunnilingus", "cunnilingus", "cunnilingus", "cunnilingus", "cunnilingus", "cunnilingus"], "en-aligned"),
    ]),
    ("Body", [
        ("root", ["Heart", "Corazón", "Cœur", "Cuore", "Coração", "Herz"], "en-break"),
        ("derived", ["cardiac", "cardíaco", "cardiaque", "cardiaco", "cardíaco", "kardial"], "en-borrowed"),
        ("derived", ["courage", "alentar", "courage", "coraggio", "coragem", "Mut"], None),
    ]),
    ("Body", [
        ("root", ["Eye", "Ojo", "Œil", "Occhio", "Olho", "Auge"], "en-break"),
        ("derived", ["ocular", "ocular", "oculaire", "oculare", "ocular", "okular"], "en-borrowed"),
        ("derived", ["ophthalmologist", "oculista", "oculiste", "oculista", "oculista", "Augenarzt"], None),
    ]),
    ("Body", [
        ("root", ["Ear", "Oído", "Oreille", "Orecchio", "Orelha", "Ohr"], "en-break"),
        ("derived", ["auditory", "auditivo", "auditif", "uditivo", "auditivo", "auditiv"], "en-borrowed"),
        ("derived", ["hearing", "oír", "ouïr", "udire", "ouvir", "hören"], None),
    ]),
    ("Body", [
        ("root", ["Foot", "Pie", "Pied", "Piede", "Pé", "Fuß"], "en-break"),
        ("derived", ["pedal", "pedigrí", "piéton", "pedonale", "pedestre", "Pedal"], "en-borrowed"),
        ("derived", ["pedestrian", "peatón", "piéton", "pedone", "pedestre", "Fußgänger"], None),
    ]),
    ("Body", [
        ("root", ["Tooth", "Diente", "Dent", "Dente", "Dente", "Zahn"], "en-break"),
        ("derived", ["dental", "dental", "dentaire", "dentale", "dental", "dental"], "en-borrowed"),
        ("derived", ["dentist", "dentista", "dentiste", "dentista", "dentista", "Zahnarzt"], None),
    ]),
    ("Body", [
        ("root", ["Head", "Cabeza", "Tête", "Testa", "Cabeça", "Kopf"], "en-break"),
        ("derived", ["capital", "cabecera", "capitale", "capitale", "capital", "Hauptstadt"], "en-borrowed"),
        ("derived", ["decapitate", "descabezar", "décapiter", "decapitare", "decapitar", "enthaupten"], "en-borrowed"),
    ]),
    ("Body", [
        ("root", ["Hand", "Mano", "Main", "Mano", "Mão", "Hand"], None),
        ("derived", ["manual", "manual", "manuel", "manuale", "manual", "manuell"], "en-aligned"),
        ("derived", ["manipulate", "manejar", "manier", "maneggiare", "manejar", "manipulieren"], "en-borrowed"),
        ("derived", ["manufacture", "manufactura", "manufacture", "manifattura", "manufatura", "Manufaktur"], "en-borrowed"),
    ]),
    ("Food", [
        ("root", ["Meat", "Carne", "Chair", "Carne", "Carne", "Fleisch"], "en-break"),
        ("derived", ["carnivore", "carnívoro", "carnivore", "carnivoro", "carnívoro", "Fleischfresser"], "en-borrowed"),
        ("derived", ["butcher", "carnicero", "boucher", "macellaio", "carniceiro", "Metzger"], None),
    ]),
    ("Home", [
        ("root", ["House", "Casa", "Maison", "Casa", "Casa", "Haus"], "en-break"),
        ("derived", ["homemade", "casero", "maison", "casalingo", "caseiro", "hausgemacht"], None),
        ("derived", ["little house", "casita", "maisonnette", "casetta", "casinha", "Häuschen"], None),
    ]),
    ("Time", [
        ("root", ["Day", "Día", "Jour", "Giorno", "Dia", "Tag"], "en-break"),
        ("derived", ["daily", "diario", "journalier", "giornaliero", "diário", "täglich"], "en-borrowed"),
    ]),
    ("Time", [
        ("root", ["Year", "Año", "An", "Anno", "Ano", "Jahr"], "en-break"),
        ("derived", ["annual", "anual", "annuel", "annuale", "anual", "jährlich"], "en-borrowed"),
    ]),
    ("Morality", [
        ("root", ["Bad", "Malo", "Mal", "Male", "Mau", "Schlecht"], "en-break"),
        ("derived", ["malice", "malicia", "malice", "malizia", "malícia", "Bosheit"], "en-borrowed"),
        ("derived", ["wicked", "malvado", "méchant", "malvagio", "malvado", "böse"], None),
    ]),
    ("Opposition", [
        ("root", ["Against", "Contra", "Contre", "Contro", "Contra", "Gegen"], "en-break"),
        ("derived", ["contrast", "contraste", "contraste", "contrasto", "contraste", "Kontrast"], "en-borrowed"),
        ("derived", ["contradict", "contradecir", "contredire", "contraddire", "contradizer", "widersprechen"], "en-borrowed"),
    ]),
    ("Sleep", [
        ("root", ["Sleep", "Dormir", "Dormir", "Dormire", "Dormir", "Schlaf"], "en-break"),
        ("derived", ["dormitory", "dormitorio", "dortoir", "dormitorio", "dormitório", "Schlafsaal"], "en-borrowed"),
    ]),
    ("Health", [
        ("root", ["Sick", "Enfermo", "Malade", "Malato", "Doente", "Krank"], "en-break"),
        ("derived", ["infirmary", "enfermería", "infirmerie", "infermeria", "enfermaria", "Krankenstation"], "en-borrowed"),
        ("derived", ["nurse", "enfermero", "infirmier", "infermiere", "enfermeiro", "Krankenpfleger"], None),
    ]),
    ("Life", [
        ("root", ["Life", "Vida", "Vie", "Vita", "Vida", "Leben"], "en-break"),
        ("derived", ["vital", "vital", "vital", "vitale", "vital", "vital"], "en-aligned"),
        ("derived", ["live", "vivir", "vivre", "vivere", "viver", "leben"], None),
    ]),
    ("Life", [
        ("root", ["Death", "Muerte", "Mort", "Morte", "Morte", "Tod"], "en-break"),
        ("derived", ["mortal", "mortal", "mortel", "mortale", "mortal", "sterblich"], "en-borrowed"),
        ("derived", ["die", "morir", "mourir", "morire", "morrer", "sterben"], None),
    ]),
    ("Nature", [
        ("root", ["Moon", "Luna", "Lune", "Luna", "Lua", "Mond"], "en-break"),
        ("derived", ["lunatic", "lunático", "lunatique", "lunatico", "lunático", "verrückt"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Light", "Luz", "Lumière", "Luce", "Luz", "Licht"], "en-break"),
        ("derived", ["illuminate", "iluminar", "illuminer", "illuminare", "iluminar", "illuminieren"], "en-borrowed"),
        ("derived", ["lucid", "lúcido", "lucide", "lucido", "lúcido", "luzid"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Water", "Agua", "Eau", "Acqua", "Água", "Wasser"], "en-break"),
        ("derived", ["aquatic", "acuático", "aquatique", "acquatico", "aquático", "aquatisch"], "en-borrowed"),
        ("derived", ["aquarium", "acuario", "aquarium", "acquario", "aquário", "Aquarium"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Fire", "Fuego", "Feu", "Fuoco", "Fogo", "Feuer"], "en-break"),
        ("derived", ["bonfire", "hogera", "feu de camp", "falò", "fogueira", "Lagerfeuer"], None),
        ("derived", ["blaze", "incendio", "incendie", "incendio", "incêndio", "Brand"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Earth", "Tierra", "Terre", "Terra", "Terra", "Erde"], "en-break"),
        ("derived", ["terrestrial", "terrestre", "terrestre", "terrestre", "terrestre", "irdisch"], "en-borrowed"),
        ("derived", ["terrain", "terreno", "terrain", "terreno", "terreno", "Terrain"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Star", "Estrella", "Étoile", "Stella", "Estrela", "Stern"], "en-break"),
        ("derived", ["astronomy", "astronomía", "astronomie", "astronomia", "astronomia", "Astronomie"], "en-borrowed"),
        ("derived", ["stellar", "estelar", "stellaire", "stellare", "estelar", "stellar"], "en-borrowed"),
    ]),
    ("Emotions", [
        ("root", ["Love", "Amor", "Amour", "Amore", "Amor", "Liebe"], "en-break"),
        ("derived", ["loving", "amoroso", "amoureux", "amoroso", "amoroso", "liebevoll"], None),
        ("derived", ["in love", "enamorado", "amoureux", "innamorato", "apaixonado", "verliebt"], None),
    ]),
    ("War", [
        ("root", ["War", "Guerra", "Guerre", "Guerra", "Guerra", "Krieg"], "en-break"),
        ("derived", ["warrior", "guerrero", "guerrier", "guerriero", "guerreiro", "Krieger"], None),
    ]),
    ("Peace", [
        ("root", ["Peace", "Paz", "Paix", "Pace", "Paz", "Frieden"], "en-break"),
        ("derived", ["peaceful", "pacífico", "pacifique", "pacifico", "pacífico", "friedlich"], "en-borrowed"),
    ]),
    ("Knowledge", [
        ("root", ["Book", "Libro", "Livre", "Libro", "Livro", "Buch"], "en-break"),
        ("derived", ["bookstore", "librería", "librairie", "libreria", "livraria", "Buchhandlung"], "en-borrowed"),
        ("derived", ["free", "libre", "libre", "libero", "livre", "frei"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Flower", "Flor", "Fleur", "Fiore", "Flor", "Blume"], "en-break"),
        ("derived", ["flourish", "florecer", "fleurir", "fiorire", "florescer", "gedeihen"], "en-borrowed"),
    ]),
    ("Nature", [
        ("root", ["Tree", "Árbol", "Arbre", "Albero", "Árvore", "Baum"], "en-break"),
        ("derived", ["arbor", "arbóreo", "arboricole", "arboreo", "arbóreo", "Arboretum"], "en-borrowed"),
        ("derived", ["arboretum", "arbolado", "arboretum", "albereto", "arvoredo", "Bäumchen"], "en-borrowed"),
    ]),
    ("Power", [
        ("root", ["King", "Rey", "Roi", "Re", "Rei", "König"], "en-break"),
        ("derived", ["queen", "reina", "reine", "regina", "rainha", "Königin"], None),
        ("derived", ["reign", "reinado", "règne", "regno", "reinado", "Herrschaft"], "en-borrowed"),
    ]),
    ("Time", [
        ("root", ["Night", "Noche", "Nuit", "Notte", "Noite", "Nacht"], "en-break"),
        ("derived", ["nocturnal", "nocturno", "nocturne", "notturno", "noturno", "nächtlich"], "en-borrowed"),
    ]),
    ("Body", [
        ("root", ["Blood", "Sangre", "Sang", "Sangue", "Sangue", "Blut"], "en-break"),
        ("derived", ["bleed", "sangrar", "saigner", "sanguinare", "sangrar", "bluten"], None),
        ("derived", ["sanguine", "sanguíneo", "sanguin", "sanguigno", "sanguíneo", "sanguinisch"], "en-borrowed"),
    ]),
    ("Animals", [
        ("root", ["Dog", "Perro", "Chien", "Cane", "Cão", "Hund"], "en-break"),
        ("derived", ["canine", "canino", "canin", "canino", "canino", "caninisch"], "en-borrowed"),
        ("derived", ["kennel", "perrera", "chenil", "canile", "canil", "Zwinger"], None),
    ]),
    ("Morality", [
        ("root", ["Good", "Bueno", "Bon", "Buono", "Bom", "Gut"], "en-break"),
        ("derived", ["benevolent", "benevolente", "bienveillant", "benevolo", "benevolente", "wohlwollend"], "en-borrowed"),
        ("derived", ["benefit", "beneficio", "bénéfice", "beneficio", "benefício", "Nutzen"], "en-borrowed"),
    ]),
    ("Speech", [
        ("root", ["Say", "Decir", "Dire", "Dire", "Dizer", "Sagen"], "en-break"),
        ("derived", ["dictionary", "diccionario", "dictionnaire", "dizionario", "dicionário", "Wörterbuch"], "en-borrowed"),
        ("derived", ["verdict", "veredicto", "verdict", "verdetto", "veredicto", "Urteil"], "en-borrowed"),
    ]),
    ("Writing", [
        ("root", ["Write", "Escribir", "Écrire", "Scrivere", "Escrever", "Schreiben"], "en-break"),
        ("derived", ["inscription", "inscripción", "inscription", "iscrizione", "inscrição", "Inschrift"], "en-borrowed"),
        ("derived", ["describe", "describir", "décrire", "descrivere", "descrever", "beschreiben"], "en-borrowed"),
        ("derived", ["scribe", "escriba", "scribe", "scriba", "escrivão", "Schreiber"], "en-aligned"),
    ]),
    ("Senses", [
        ("root", ["See", "Ver", "Voir", "Vedere", "Ver", "Sehen"], "en-break"),
        ("derived", ["vision", "visión", "vision", "visione", "visão", "Vision"], "en-borrowed"),
        ("derived", ["television", "televisión", "télévision", "televisione", "televisão", "Fernsehen"], "en-borrowed"),
    ]),
    ("Nation", [
        ("root", ["Nation", "Nación", "Nation", "Nazione", "Nação", "Nation"], None),
        ("derived", ["born", "nacido", "né", "nato", "nascido", "geboren"], None),
        ("derived", ["native", "nativo", "natif", "nativo", "nativo", "eingeboren"], None),
    ]),
    ("Food", [
        ("root", ["Try / taste", "Probar", "Prouver", "Provare", "Provar", "Prüfen"], "en-break"),
        ("derived", ["proof / test", "prueba", "preuve", "prova", "prova", "Prüfung"], "en-borrowed"),
        ("derived", ["approval", "aprobación", "approbation", "approvazione", "aprovação", "Genehmigung"], "en-borrowed"),
    ]),
    ("Food", [
        ("root", ["Bread", "Pan", "Pain", "Pane", "Pão", "Brot"], "en-break"),
        ("derived", ["bakery", "panadería", "boulangerie", "panetteria", "padaria", "Bäckerei"], None),
        ("derived", ["baker", "panadero", "boulanger", "panettiere", "padeiro", "Bäcker"], None),
    ]),
    ("Commerce", [
        ("root", ["Sell", "Vender", "Vendre", "Vendere", "Vender", "Verkaufen"], "en-break"),
        ("derived", ["vendor", "vendedor", "vendeur", "venditore", "vendedor", "Verkäufer"], None),
    ]),
    ("Travel", [
        ("root", ["Boat", "Barco", "Barque", "Barca", "Barco", "Boot"], "en-break"),
        ("derived", ["embark", "embarcar", "embarquer", "imbarcare", "embarcar", "einschiffen"], "en-borrowed"),
        ("derived", ["disembark", "desembarcar", "débarquer", "disimbarcare", "desembarcar", "ausschiffen"], "en-borrowed"),
    ]),
    ("Travel", [
        ("root", ["Airplane", "Avión", "Avion", "Aereo", "Avião", "Flugzeug"], "en-break"),
        ("derived", ["aviation", "aviación", "aviation", "aviazione", "aviação", "Aviation"], "en-borrowed"),
        ("derived", ["aviator", "aviador", "aviateur", "aviatore", "aviador", "Flieger"], "en-borrowed"),
    ]),
    ("Body", [
        ("root", ["Beard", "Barba", "Barbe", "Barba", "Barba", "Bart"], None),
        ("derived", ["barber", "barbero", "barbier", "barbiere", "barbeiro", "Barbier"], None),
    ]),
    ("Time", [
        ("root", ["Twelve", "Doce", "Douze", "Dodici", "Doze", "Zwölf"], "en-break"),
        ("derived", ["dozen", "docena", "douzaine", "dozzina", "dúzia", "Dutzend"], "en-borrowed"),
    ]),
    ("Confinement", [
        ("root", ["Jail", "Cárcel", "Prison", "Carcere", "Prisão", "Gefängnis"], "en-break"),
        ("derived", ["incarcerated", "encarcelado", "incarcéré", "incarcerato", "encarcerado", "inhaftiert"], "en-borrowed"),
        ("derived", ["cell", "celda", "cellule", "cella", "cela", "Zelle"], None),
    ]),
]


# Column order after English: German, Spanish, Portuguese, Italian, French
LANG_ORDER = ("de", "es", "pt", "it", "fr")


def lang_cells(words: list[str]) -> list[str]:
    """words: [en, es, fr, it, pt, de] -> output de, es, pt, it, fr"""
    en, es, fr, it, pt, de = words
    by_lang = {"es": es, "fr": fr, "it": it, "pt": pt, "de": de}
    return [by_lang[k] for k in LANG_ORDER]


def en_td(word: str, kind: str, en_class: str | None) -> str:
    if kind == "root":
        cls = "root"
        if en_class:
            cls += f" {en_class}"
        return f'<td class="{cls}">{word}</td>'
    if en_class:
        return f'<td class="{en_class}">{word}</td>'
    return f'<td>{word}</td>'


def other_td(word: str, kind: str) -> str:
    if kind == "root":
        return f'<td class="root">{word}</td>'
    return f'<td>{word}</td>'


lines: list[str] = []
sort = 0
for category, rows in groups:
    sort += 1
    rowspan = len(rows)
    lines.append(f'<tbody class="roots-group" data-sort="{sort}">')
    for i, (kind, words, en_class) in enumerate(rows):
        row_class = "roots-root-row" if kind == "root" else "roots-derived-row"
        lines.append(f'  <tr class="{row_class}">')
        if i == 0:
            lines.append(
                f'    <th scope="row" class="roots-category roots-sticky-col" rowspan="{rowspan}">{category}</th>'
            )
        en = words[0]
        lines.append(f'    {en_td(en, kind, en_class)}')
        for w in lang_cells(words):
            lines.append(f'    {other_td(w, kind)}')
        lines.append("  </tr>")
    lines.append("</tbody>")

body = "\n".join(lines)

ROOT = Path(__file__).resolve().parent.parent
head = """<!doctype html>
<html lang="en" class="h-100 roots-page" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Parallel word families across English, Spanish, Portuguese, Italian, French, and German — see how Romance languages keep Latin roots visible while English often breaks the pattern.">
    <link rel="canonical" href="https://edwardlthompson.com/word-connections.html">
    <title>Word Connections | Language Comparison</title>
    <meta property="og:title" content="Word Connections | Language Comparison">
    <meta property="og:description" content="Read English first, then Spanish, Portuguese, Italian, French, and German. Romance languages keep Latin connections clear; English often breaks them.">
    <meta property="og:image" content="https://edwardlthompson.com/img/word-connections.png">
    <meta property="og:url" content="https://edwardlthompson.com/word-connections.html">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <link rel="preload" as="style" href="vendor/bootstrap-5.3.3/css/bootstrap.min.css">
    <link href="vendor/bootstrap-5.3.3/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/modules/base.css" rel="stylesheet">
    <link href="css/modules/glass.css" rel="stylesheet">
    <link href="css/modules/identity.css" rel="stylesheet">
    <link href="css/modules/responsive.css" rel="stylesheet">
    <link href="css/modules/animations.css" rel="stylesheet">
    <link href="css/modules/language-roots.css" rel="stylesheet">
    <link rel="apple-touch-icon" href="img/icon-192.png">
    <link rel="icon" type="image/png" href="img/icon-192.png">
    <meta name="theme-color" content="#1a331a">
  </head>
  <body class="d-flex h-100 text-center text-bg-dark">

    <canvas id="matrix" aria-hidden="true"></canvas>

    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">

      <main class="px-3 mb-auto mt-auto justify-content-center">
        <a role="button" class="btn btn-sm btn-light download-btn matrix-cta roots-back" href="index.html">Back to Portal</a>

        <div class="section roots-panel glass-panel">
          <h1 class="matrix-identity">Language Comparison</h1>
          <p class="roots-intro"><strong>Read from <em>English</em>, then <em>German</em> — both often hide Latin on the first row.</strong> Scan right through Spanish, Portuguese, Italian, and French to see the word family stay visible. Latin may reappear in English and German borrowings on the rows below.</p>

          <div class="roots-table-wrapper" tabindex="0" role="region" aria-label="Word connections scrollable table">
            <table class="roots-table" aria-label="Word roots compared across English, Spanish, Portuguese, Italian, French, and German">
              <thead class="roots-sticky-head">
                <tr>
                  <th scope="col" class="roots-sticky-col">Category</th>
                  <th scope="col">English</th>
                  <th scope="col">German</th>
                  <th scope="col">Spanish</th>
                  <th scope="col">Portuguese</th>
                  <th scope="col">Italian</th>
                  <th scope="col">French</th>
                </tr>
              </thead>
"""

foot = """
            </table>
          </div>
        </div>
      </main>

      <footer class="mt-auto text-white-50">
        <p>© Copyright Edward Lee Thompson 2026. All Rights Reserved.</p>
      </footer>
    </div>
    <script src="vendor/bootstrap-5.3.3/js/bootstrap.bundle.min.js"></script>
    <script src="js/matrix.js"></script>
  </body>
</html>
"""

out_path = ROOT / "word-connections.html"
out_path.write_text(head + body + foot, encoding="utf-8")
print(f"Wrote {len(groups)} groups to {out_path}")
