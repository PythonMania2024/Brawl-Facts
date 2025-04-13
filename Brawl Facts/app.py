from flask import Flask, render_template, request, send_from_directory, Response, url_for
import os

app = Flask(__name__)

MEDIA_FOLDER = 'static/media'
app.config['MEDIA_FOLDER'] = MEDIA_FOLDER

# Letras
# Diccionario con datos curiosos
curiosidades_dict = {
    "Tiempo y ranking de todas las familias de Brawl stars contra la caja de atraco": "El primer brawler creado fue Shelly, y siempre ha sido la brawler con la que empiezas el juego.",
    "Shelly antes del lanzamiento": "Shelly ya era jugable durante la versión beta de Brawl Stars. ¡Fue clave en las pruebas!",
    "Brawlers musicales": "Melodie y Poco tienen muchas skins relacionadas con la música. ¡Melodie fue diseñada como una estrella del pop!"
}

@app.route('/curiosidades')
def curiosidades():
    return render_template('curiosidades.html', curiosidades=curiosidades_dict)

lyrics_dict = {
    "Lumi-Musica.mp3": """One , Two , Three , Four
[Music]
Let's gooooooo
I can be ice cold to Draco
or warmer tham the sun.
I'm radical
But fire and ice are all I need , 
I said no new friends.
I will beat my drums and scream.
Madevil Manor look out for me
I am fire.
[Music]
Ho hoooo
Ha ha hua
[Music]
Fire and ice are all I need ,
I said no new friends.
I will beat my drums and scream.
MadEvil Manor look out of me.
I am fire.



""",
    "Melodie-Musica.mp3": """The world is my stage
Feel the lights
Feel the fear
The sticks
Through the star
Wich one
Do you hear
I'm not
Caught up 
At this
I'm too good
Stay in your lane
Like you now you should
This is
The show business
Not Not
Not Not
Not
Your Business
Think you're the one
But honey
Nah Nah
Nah Nah
Nah
I'm made for this
Built for this
My rhymes are my friends
You're just a...
Cant' keep it up
Turn it up
Amplify this
Melodie
[Music]
Faster than Max
Cuter than Kit
Karaoke
Baby
I'm your first pick
Remember my name
You can't get away
I'm the best star
Can't ever be tamed
This is
The show business
Not Not
Not Not
Not
Your Business
Think you're the one
But honey
Nah Nah
Nah Nah
Nah
I'm made for this
Built for this
My rhymes are my friends
You're just a...
Cant' keep it up
Turn it up
Amplify this
Melodie
You'll remember this
You'll remember this
Melodie forever
Pitch perfect
I'ma be your idol
I'ma be your idol
But you don't owe me
I don't want thath
Nah nah nah
Nah nah nah
Nah nah nah
Nah nah nah
Hey
Think you're the one
But honey
Nah Nah
Nah Nah
Nah
I'm made for this
Built for this
My rhymes are my friends
You're just a...
Cant' keep it up
Turn it up
Amplify this
Melodie
This is
The show business
Not Not
Not Not
Not
Your Business
Think you're the one
But honey
Nah Nah
Nah Nah
Nah
I'm made for this
Built for this
My rhymes are my friends
You're just a...
Cant' keep it up
Turn it up
Amplify this
Melodie
""",
    "A-Draco-Tale-Video.mp4": """Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And the story shall be told

So let me tell you a story
About a dragon I know
A mystical dragon
Here he comes to steal the show

So gather 'round and listen
Hear his mighty words
And with his axe of power
The strengths to lead one thousand herds

Dungeons!
Dragons!
Metal!

Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And the story shall be told
Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And a legend now is born

He was the saviour of dragons
He was a tamer of trolls
An everlasting alliance
Forged in fire in days of old

Now in the mad evil manor
The villains start to pray
Feel his power arising
Watch them run so far away

Fire!
Guitar!
Metal!

Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And the story shall be told
Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And a legend now is born

Draco!
Draco!
Draco!
Draco!
Draco!

Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And the story shall be told
Master of the Starr Park
Ruler of the world
Say Draco! Draco!
And a legend now is born
"""
}

# Títulos más bonitos
titles_dict = {
    "Lumi-Musica.mp3": "The Hottest Brawler Ever!",
    "Melodie-Musica.mp3": "Amplify This Melodie",
    "A-Draco-Tale-Video.mp4": "A Draco Tale"
}

# Opciones del selector
@app.route('/', methods=['GET', 'POST'])
def index():
    selected_file = None

    opciones = {
        "THE HOTTEST BRAWLER EVER!": "Lumi-Musica.mp3",
        "Amplify this Melodie": "Melodie-Musica.mp3",
        "A Draco Tale": "A-Draco-Tale-Video.mp4",
        "Amplify this Melodie (Video)": "Melodie.mp4",
        "THE HOTTEST BRAWLER EVER! (Video)": "Lumi.mp4"
    }

    if request.method == 'POST':
        selected_file = request.form.get('media')
        if selected_file not in opciones.values():
            selected_file = None

    return render_template("index.html", opciones=opciones, selected_file=selected_file)

# Descargar archivo multimedia
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename, as_attachment=True)

# Ver letra
@app.route('/lyrics/<filename>')
def show_lyrics(filename):
    lyrics = lyrics_dict.get(filename, "Letra no disponible")
    title = titles_dict.get(filename, "Letra de la canción")
    return render_template('lyrics.html', lyrics=lyrics, filename=filename, title=title)

# Descargar letra como .txt
@app.route('/download-lyrics/<filename>')
def download_lyrics(filename):
    lyrics = lyrics_dict.get(filename)
    if not lyrics:
        return "Letra no disponible", 404

    clean_name = titles_dict.get(filename, filename.split('-')[0])
    safe_name = clean_name.replace(" ", "_").lower()

    return Response(
        lyrics,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={safe_name}_letra.txt"}
    )
@app.route('/animaciones', methods=['GET', 'POST'])
def animaciones():
    videos = {
        "Lumi": "Lumi.mp4",
        "Melodie": "Melodie.mp4",
        "A Draco Tale": "A-Draco-Tale-Video.mp4"
    }

    selected_video = None

    if request.method == 'POST':
        selected_video = request.form.get('video')

    return render_template('animaciones.html', videos=videos, selected_video=selected_video)


@app.route('/curiosidades')
def curiosidades():
    return render_template('curiosidades.html')

if __name__ == "__main__":
    app.run(debug=True)
