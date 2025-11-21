from app.database import SessionLocal
from app.models import Painting

paintings = [
    Painting(title="Mona Lisa", image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg"),
    Painting(title="La joven de la Perla", image_url="https://upload.wikimedia.org/wikipedia/commons/d/d7/Meisje_met_de_parel.jpg"),
    Painting(title="El Viejo Guitarrista", image_url="https://e01-elmundo.uecdn.es/elmundosalud/imagenes/2004/04/13/1081872818_0.jpg"),
    Painting(title="La Noche Estrellada", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1135px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"),
    Painting(title="El Ángel Herido", image_url="https://es.wikipedia.org/wiki/El_%C3%A1ngel_herido#/media/Archivo:The_Wounded_Angel_-_Hugo_Simberg.jpg"),
    Painting(title="Retrato de Ambroise Vollard", image_url="https://imgadcip.wikioo.org/ADC/Art-ImgScreen-2.nsf/O/A-5ZKDP9/$FILE/Paul_cezanne-portrait_of_ambroise_vollard.Jpg"),
    Painting(title="El Grito", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/The_Scream_by_Edvard_Munch%2C_1893_-_Nasjonalgalleriet.png/960px-The_Scream_by_Edvard_Munch%2C_1893_-_Nasjonalgalleriet.png"),
    Painting(title="La Sopa", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Pablo_Picasso%2C_1902-03%2C_La_soupe_%28The_soup%29%2C_oil_on_canvas%2C_38.5_x_46.0_cm%2C_Art_Gallery_of_Ontario%2C_Toronto%2C_Canada.jpg/1074px-Pablo_Picasso%2C_1902-03%2C_La_soupe_%28The_soup%29%2C_oil_on_canvas%2C_38.5_x_46.0_cm%2C_Art_Gallery_of_Ontario%2C_Toronto%2C_Canada.jpg?20170212141115"),
    Painting(title="Devil", image_url="https://magazineculturalytecnologico.com/wp-content/uploads/2025/02/Foto-1.jpg"),
    Painting(title="Midiero", image_url="https://www.artmajeur.com/rui-da-costa-artista-plastico-portugal/es/obras-de-arte/8415853/mineiro"),
    Painting(title="Escena del Campeon", image_url="https://objetos.estaticos-marca.com/assets/multimedia/imagenes/2017/03/30/14908940146517.jpg")
]

db = SessionLocal()
db.add_all(paintings)
db.commit()
db.close()