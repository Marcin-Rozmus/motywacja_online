from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Klucz do szyfrowania sesji

CARDS = [
    {"text": "Każdy dzień jest dobry, by się poddać.", "img_src": "pola.png"},
    {"text": "Nie ilość i nie jakość.", "img_src": "kurs_wzrostowy.png"},
    {"text": "Rób rzeczy od A do B.", "img_src": "samolot.png"},
    {"text": "Ignoruj swoje możliwości.", "img_src": "astronauta.png"},
    {
        "text": "Nie zatrzymuj się na dnie, zawsze jest coś niżej.",
        "img_src": "rybka.png",
    },
    {"text": "Później albo nigdy.", "img_src": "budzik.png"},
    {"text": "Nigdy nie nastawiaj się na sukces.", "img_src": "rakieta.png"},
    {"text": "Żyj tak, żeby inni nie chcieli być Tobą.", "img_src": "baloniki.png"},
    {"text": "Każdego dnia dawaj z siebie coraz mniej. ", "img_src": "wspinaczka.png"},
    {"text": "Bądź zawsze o krok do tyłu.", "img_src": "krok.png"},
    {"text": "Zacząłeś, nie kończ.", "img_src": "kilof.png"},
    {
        "text": "Niech symbolem Twojego życia będzie zero.",
        "img_src": "sztuczne_ognie.png",
    },
    {"text": "Zbuduj imperium demotywacji.", "img_src": "zamek.png"},
    {"text": "Dzień bez problemu to dzień stracony.", "img_src": "origami.png"},
    {"text": "Nie bierz odpowiedzialności za swoje błędy.", "img_src": "sztanga.png"},
    {"text": "Wyznaczaj nowe granice niekompetencji.", "img_src": "swiat.png"},
    {"text": "Zawężaj swoje horyzonty.", "img_src": "horyzont.png"},
    {"text": "Bądź pionierem w żadnej dziedzinie.", "img_src": "superbohater.png"},
    {"text": "Nie sięgaj nawet tam gdzie wzrok sięga.", "img_src": "okulary.png"},
    {
        "text": "Nadzieja pierwszym krokiem do rozczarowania.",
        "img_src": "kuglarstwo.png",
    },
    {
        "text": "Nie czekaj na innych sam rzucaj sobie kłody pod nogi.",
        "img_src": "przeszkody.png",
    },
    {"text": "Rozczarowuj każdego dnia.", "img_src": "gwiazdki.png"},
    {"text": "Bądź zorientowany na porażkę.", "img_src": "kompas.png"},
    {
        "text": "Nie liczy się to jak zaczynasz. Ani to jak kończysz.",
        "img_src": "start.png",
    },
    {"text": "Cokolwiek robisz – nie warto.", "img_src": "reanimacja.png"},
    {
        "text": "Niech Twoje działania mówią ciszej niż Twoje słowa.",
        "img_src": "megafon.png",
    },
    {
        "text": "Dopóki nie spróbujesz, nie dowiesz się, że się nie nadajesz.",
        "img_src": "lista.png",
    },
    {
        "text": "Najtrudniejsze jest zdecydowanie się na bezczynność.",
        "img_src": "medytacja.png",
    },
    {
        "text": "Jeśli masz marzenie możesz je zignorować lub porzucić.",
        "img_src": "drogowskaz.png",
    },
    {"text": "Zmarnuj swój potencjał.", "img_src": "sila.png"},
    {
        "text": "Jeśli przechodzisz przez piekło, zatrzymaj się i odpocznij.",
        "img_src": "ognisko.png",
    },
    {
        "text": "Sukces to wymówka ludzi, którzy nie mają motywacji, by doświadczać porażek.",
        "img_src": "sukces.png",
    },
    {"text": "Uwierz w siebie, a niczego nie osiągniesz.", "img_src": "puchar.png"},
    {"text": "Bądź inicjatorem każdej porażki.", "img_src": "idea.png"},
    {
        "text": "Kiedy spytają Cię jak się masz, odpowiedz, że wcale.",
        "img_src": "trumna.png",
    },
    {"text": "Wystarczy nie chcieć.", "img_src": "diament.png"},
    {"text": "Żyj tak, by nikt nie przyszedł na Twój pogrzeb.", "img_src": "grupa.png"},
    {"text": "Chlub się porażką.", "img_src": "podium.png"},
    {"text": "Droga do porażki usłana jest sukcesami.", "img_src": "labirynt.png"},
    {"text": "Upadaj zawsze plecami do mety.", "img_src": "wedrowiec.png"},
    {"text": "Umrzyj nie próbując.", "img_src": "miecz.png"},
    {"text": "Minimum to zbyt wiele.", "img_src": "obroty.png"},
    {"text": "Nie myśl o złocie. Zadowalaj się niczym.", "img_src": "medal.png"},
    {"text": "Przegap każdą okazję.", "img_src": "kometa.png"},
    {"text": "Aktywnie zaniżaj swój status.", "img_src": "krol.png"},
    {
        "text": "Gdy myślisz, że coś możesz lub czegoś nie możesz, to masz rację tylko w drugim przypadku.",
        "img_src": "zonglerz.png",
    },
    {"text": "Stosuj negatywną afirmację każdego dnia.", "img_src": "po_turecku.png"},
    {"text": "Graj, by przegrać.", "img_src": "karate.png"},
    {"text": "Wybierz wymówki, a nie wyniki.", "img_src": "kolowrotek.png"},
    {"text": "Niech Twoje ograniczenia nie mają granic.", "img_src": "kosmos.png"},
    {"text": "Najgorszym momentem na rozpoczęcie jest teraz.", "img_src": "palmy.png"},
    {"text": "Wypracuj nawyk przegrywania.", "img_src": "tygrys.png"},
    {"text": "Żyj jako ofiara okoliczności.", "img_src": "wstazka.png"},
    {"text": "Stań się najgorszą wersją siebie.", "img_src": "martini.png"},
    {"text": "Pielęgnuj swoje ograniczenia.", "img_src": "bonsai.png"},
    {"text": "Każde życie to wielki dar. Tylko nie Twoje.", "img_src": "prezent.png"},
    {
        "text": "Nie obawiaj się porażki. To już Twoje naturalne środowisko.",
        "img_src": "ryba_w_wodzie.png",
    },
    {
        "text": "Nie liczy się ile razy upadniesz. Ani to czy powstaniesz.",
        "img_src": "powtorz.png",
    },
    {"text": "Najlepszy na ból jest kolejny ból.", "img_src": "kierunki.png"},
    {"text": "Ból jest tymczasowy. Porażka jest wieczna.", "img_src": "drzewo.png"},
]

COLORS = [
    "aliceblue",
    "aquamarine",
    "dimgray",
    "darkolivegreen",
    "pink",
    "chocolate",
    "darkkhaki",
    "peachpuff",
    "salomon",
    "royalblue",
]

# Hasło dostępu do strony
PASSWORD = "biegunka"


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["password"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            error = "Nieprawidłowe hasło. Spróbuj ponownie."

    color_name = COLORS[get_random_index(COLORS)]
    return render_template("login.html", error=error, bgcolor=color_name)


@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    card_index = get_random_index(CARDS)
    color_name = COLORS[get_random_index(COLORS)]

    message = CARDS[card_index]["text"]
    adress = CARDS[card_index]["img_src"]

    return render_template(
        "index.html",
        message=message,
        img_src=f"{adress}",
        bgcolor=color_name,
        card_no=card_index + 1,
        total_no_cards=len(CARDS),
    )


def get_random_index(collection):
    index = random.randint(0, len(collection) - 1)
    return index


if __name__ == "__main__":
    app.run(debug=True, port=21082, host="0.0.0.0")
