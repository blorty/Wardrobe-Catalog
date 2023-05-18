from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class Wardrobe(Base):
    __tablename__ = 'wardrobes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    clothing_items = relationship('ClothingItem', order_by='ClothingItem.id', back_populates='wardrobe')
    outfits = relationship('Outfit', order_by='Outfit.id', back_populates='wardrobe')
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"<Wardrobe(name='{self.name}')>"

class Outfit(Base):
    __tablename__ = 'outfits'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    top_id = Column(Integer, ForeignKey('clothing_items.id'))
    bottom_id = Column(Integer, ForeignKey('clothing_items.id'))
    shoes_id = Column(Integer, ForeignKey('clothing_items.id'))
    top = relationship('ClothingItem', foreign_keys=[top_id])
    bottom = relationship('ClothingItem', foreign_keys=[bottom_id])
    shoes = relationship('ClothingItem', foreign_keys=[shoes_id])
    wardrobe_id = Column(Integer, ForeignKey('wardrobes.id'))
    wardrobe = relationship('Wardrobe', back_populates='outfits')
    
    def __init__(self, name, top, bottom, shoes):
        self.name = name
        self.top = top
        self.bottom = bottom
        self.shoes = shoes
        
    def __repr__(self):
        return f"<Outfit(name='{self.name}')>"
        
class ClothingItem(Base):
    __tablename__ = 'clothing_items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    wardrobe_id = Column(Integer, ForeignKey('wardrobes.id'))
    wardrobe = relationship('Wardrobe', back_populates='clothing_items')
    
    def __init__(self, name, category, wardrobe):
        self.name = name
        self.category = category
        self.wardrobe = wardrobe
        
    def __repr__(self):
        return f"<ClothingItem(name='{self.name}', category='{self.category}')>"

Wardrobe.clothing_items = relationship('ClothingItem', order_by=ClothingItem.id, back_populates='wardrobe')
Wardrobe.outfits = relationship('Outfit', order_by=Outfit.id, back_populates='wardrobe')

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a wardrobe
wardrobe = Wardrobe('Wardrobe')
session.add(wardrobe)
session.commit()

# Create tops
plain_shirt = ClothingItem('Plain Shirt', 'Top', wardrobe)
graphic_tee = ClothingItem('Graphic Tee', 'Top', wardrobe)
button_up = ClothingItem('Button Up', 'Top', wardrobe)
hoodie = ClothingItem('Hoodie', 'Top', wardrobe)
jacket = ClothingItem('Jacket', 'Top', wardrobe)

# Create different variations of plain shirts and set their parent to the plain shirt
plain_shirt_white = ClothingItem('Plain White T)', 'Top', wardrobe)
plain_shirt_white.parent = plain_shirt
plain_shirt_black = ClothingItem('Plain Black T)', 'Top', wardrobe)
plain_shirt_black.parent = plain_shirt
plain_shirt_gray = ClothingItem('Plain Gray T)', 'Top', wardrobe)
plain_shirt_gray.parent = plain_shirt
plain_shirt_tan = ClothingItem('Plain Tan T)', 'Top', wardrobe)
plain_shirt_tan.parent = plain_shirt
plain_shirt_blue = ClothingItem('Plain Blue T)', 'Top', wardrobe)
plain_shirt_blue.parent = plain_shirt

# Create different variations of graphic shirts and set their parent to the graphic shirt
graphic_tee_kw = ClothingItem('Kanye West T)', 'Top', wardrobe)
graphic_tee_kw.parent = graphic_tee
graphic_tee_ow = ClothingItem('Off-White T)', 'Top', wardrobe)
graphic_tee_ow.parent = graphic_tee
graphic_tee_supreme = ClothingItem('Supreme T)', 'Top', wardrobe)
graphic_tee_supreme.parent = graphic_tee
graphic_tee_emoji = ClothingItem('Emoji T)', 'Top', wardrobe)
graphic_tee_emoji.parent = graphic_tee
graphic_tee_nike = ClothingItem('Nike Swoosh T)', 'Top', wardrobe)

# Create different variations of button ups and set their parent to the button up
button_up_white = ClothingItem('White Button Up', 'Top', wardrobe)
button_up_white.parent = button_up
button_up_black = ClothingItem('Black Button Up', 'Top', wardrobe)
button_up_black.parent = button_up
button_up_gray = ClothingItem('Gray Button Up', 'Top', wardrobe)
button_up_gray.parent = button_up
button_up_striped = ClothingItem('Striped Button Up', 'Top', wardrobe)
button_up_striped.parent = button_up
button_up_plaid = ClothingItem('Plaid Button Up', 'Top', wardrobe)
button_up_plaid.parent = button_up

# Create different variations of hoodies and set their parent to the hoodie
hoodie_white = ClothingItem('White Hoodie', 'Top', wardrobe)
hoodie_white.parent = hoodie
hoodie_black = ClothingItem('Black Hoodie', 'Top', wardrobe)
hoodie_black.parent = hoodie
hoodie_hp = ClothingItem('Heron Preston Heron Hoodie', 'Top', wardrobe)
hoodie_hp.parent = hoodie
hoodie_undercover = ClothingItem('Undercover UFO Hoodie', 'Top', wardrobe)
hoodie_undercover.parent = hoodie
hoodie_cavempt = ClothingItem('Cav Empt Logo Hoodie', 'Top', wardrobe)
hoodie_cavempt.parent = hoodie

# Create different variations of jackets and set their parent to the jacket
jacket_vtm = ClothingItem('Vetements Bomber Jacket', 'Top', wardrobe)
jacket_vtm.parent = jacket
jacket_moncler = ClothingItem('Moncler Puffer Jacket', 'Top', wardrobe)
jacket_moncler.parent = jacket
jacket_supreme = ClothingItem('Supreme x TNF Jacket', 'Top', wardrobe)
jacket_supreme.parent = jacket
jacket_bape = ClothingItem('Bape Shark Hoodie', 'Top', wardrobe)
jacket_bape.parent = jacket
jacket_burberry = ClothingItem('Burberry Trench Coat', 'Top', wardrobe)


# Create bottoms
dress_pants = ClothingItem('Dress Pants', 'Bottom', wardrobe)
linen_pants = ClothingItem('Linen Pants', 'Bottom', wardrobe)
cargo_pants = ClothingItem('Cargo Pants', 'Bottom', wardrobe)
jeans = ClothingItem('Jeans', 'Bottom', wardrobe)
shorts = ClothingItem('Shorts', 'Bottom', wardrobe)

# Create different variations of dress pants and set their parent to the dress pants
dress_pants_black = ClothingItem('Dior Black Dress Pants', 'Bottom', wardrobe)
dress_pants_black.parent = dress_pants
dress_pants_gray = ClothingItem('Burberry Gray Plaid Dress Pants', 'Bottom', wardrobe)
dress_pants_gray.parent = dress_pants
dress_pants_tan = ClothingItem('Thom Browne Tan Dress Pants', 'Bottom', wardrobe)
dress_pants_tan.parent = dress_pants
dress_pants_blue = ClothingItem('Prada Blue Dress Pants', 'Bottom', wardrobe)
dress_pants_blue.parent = dress_pants
dress_pants_brown = ClothingItem('Hermes Brown Dress Pants', 'Bottom', wardrobe)

# Create different variations of linen pants and set their parent to the linen pants
linen_pants_black = ClothingItem('Black Linen Pants', 'Bottom', wardrobe)
linen_pants_black.parent = linen_pants
linen_pants_gray = ClothingItem('Gray Linen Pants', 'Bottom', wardrobe)
linen_pants_gray.parent = linen_pants
linen_pants_tan = ClothingItem('Tan Linen Pants', 'Bottom', wardrobe)
linen_pants_tan.parent = linen_pants
linen_pants_blue = ClothingItem('Blue Linen Pants', 'Bottom', wardrobe)
linen_pants_blue.parent = linen_pants
linen_pants_brown = ClothingItem('Brown Linen Pants', 'Bottom', wardrobe)
linen_pants_brown.parent = linen_pants

# Create different variations of cargo pants and set their parent to the cargo pants
cargo_pants_rhude = ClothingItem('Rhude Black Cargo Pants', 'Bottom', wardrobe)
cargo_pants_rhude.parent = cargo_pants
cargo_pants_rickowens = ClothingItem('Rick Owens Cargo Pants', 'Bottom', wardrobe)
cargo_pants_rickowens.parent = cargo_pants
cargo_pants_supreme = ClothingItem('Supreme Cargo Pants', 'Bottom', wardrobe)
cargo_pants_supreme.parent = cargo_pants
cargo_pants_undercover = ClothingItem('Undercover Cargo Pants', 'Bottom', wardrobe)
cargo_pants_undercover.parent = cargo_pants
cargo_pants_essentials = ClothingItem('Essentials Cargo Pants', 'Bottom', wardrobe)
cargo_pants_essentials.parent = cargo_pants

# Create different variations of jeans and set their parent to the jeans
jeans_ow = ClothingItem('Off-White White Paint Splatter Jeans', 'Bottom', wardrobe)
jeans_ow.parent = jeans
jeans_rickowens = ClothingItem('Rick Owens Black Ripped Jeans', 'Bottom', wardrobe)
jeans_rickowens.parent = jeans
jeans_represent = ClothingItem('Represent Acid Washed Jeans', 'Bottom', wardrobe)
jeans_represent.parent = jeans
jeans_amiri = ClothingItem('Amiri Black Snake Head Jeans', 'Bottom', wardrobe)
jeans_amiri.parent = jeans
jeans_fearofgod = ClothingItem('Fear of God Ripped Blue Jeans', 'Bottom', wardrobe)
jeans_fearofgod.parent = jeans

# Create different variations of shorts and set their parent to the shorts
shorts_nike = ClothingItem('Nike Black Basketball Shorts', 'Bottom', wardrobe)
shorts_nike.parent = shorts
shorts_jorts = ClothingItem('Jorts... really?', 'Bottom', wardrobe)
shorts_jorts.parent = shorts
shorts_booty = ClothingItem('Super Classy Booty Shorts', 'Bottom', wardrobe)
shorts_booty.parent = shorts
shorts_cargo = ClothingItem('Tan Cargo Shorts (ONLY FOR DADS GRILLING OUTSIDE)', 'Bottom', wardrobe)
shorts_cargo.parent = shorts
shorts_spandex = ClothingItem('Black Spandex Workout Shorts', 'Bottom', wardrobe)
shorts_spandex.parent = shorts

# Create shoes
dress_shoes = ClothingItem('Dress Shoes', 'Shoes', wardrobe)
boots = ClothingItem('Boots', 'Shoes', wardrobe)
loafers = ClothingItem('Loafers', 'Shoes', wardrobe)
slippers = ClothingItem('Slippers', 'Shoes', wardrobe)
sneakers = ClothingItem('Sneakers', 'Shoes', wardrobe)

# Create different variations of dress shoes and set their parent to the shoes
dress_shoes_prada = ClothingItem('Prada Black Alligator Skin Dress Shoes', 'Bottom', wardrobe)
dress_shoes_prada.parent = dress_shoes
dress_shoes_hermes = ClothingItem('White Hermes King Snake Skin Dress Shoes', 'Bottom', wardrobe)
dress_shoes_hermes.parent = dress_shoes
dress_shoes_lb = ClothingItem('Louboutin Red Bottom Boots', 'Bottom', wardrobe)
dress_shoes_lb.parent = dress_shoes
dress_shoes_gucci = ClothingItem('Gucci Black Leather Dress Shoes', 'Bottom', wardrobe)
dress_shoes_gucci.parent = dress_shoes
dress_shoes_versace = ClothingItem('Versace Blue Leather Dress Shoes', 'Bottom', wardrobe)
dress_shoes_versace.parent = dress_shoes

# Create different variations of boots and set their parent to the boots
boots_rickowens = ClothingItem('Rick Owens Black Combat Boots', 'Bottom', wardrobe)
boots_rickowens.parent = boots
boots_dr = ClothingItem('Dr. Martens Black Combat Boots', 'Bottom', wardrobe)
boots_dr.parent = boots
boots_timberland = ClothingItem('Timberland Wheat Boots', 'Bottom', wardrobe)
boots_timberland.parent = boots
boots_yeezy = ClothingItem('Yeezy Season 3 Combat Boots', 'Bottom', wardrobe)
boots_yeezy.parent = boots
boots_burberry = ClothingItem('Burberry Black Combat Boots', 'Bottom', wardrobe)
boots_burberry.parent = boots

# Create different variations of loafers and set their parent to the loafers
loafers_gucci = ClothingItem('Gucci Black Leather Loafers', 'Bottom', wardrobe)
loafers_gucci.parent = loafers
loafers_versace = ClothingItem('Versace Blue Leather Loafers', 'Bottom', wardrobe)
loafers_versace.parent = loafers
loafers_prada = ClothingItem('Prada Black Leather Loafers', 'Bottom', wardrobe)
loafers_prada.parent = loafers
loafers_ferragamo = ClothingItem('Ferragamo Black Leather Loafers', 'Bottom', wardrobe)
loafers_ferragamo.parent = loafers
loafers_burberry = ClothingItem('Burberry Black Leather Loafers', 'Bottom', wardrobe)
loafers_burberry.parent = loafers

# Create different variations of slippers and set their parent to the slippers
slippers_marbolo = ClothingItem('Marbolo Red Slippers', 'Bottom', wardrobe)
slippers_marbolo.parent = slippers
slippers_budlight = ClothingItem('Bud Light Slippers', 'Bottom', wardrobe)
slippers_budlight.parent = slippers
slippers_superman = ClothingItem('Superman Slippers', 'Bottom', wardrobe)
slippers_superman.parent = slippers
slippers_batman = ClothingItem('Batman Slippers', 'Bottom', wardrobe)
slippers_batman.parent = slippers
slippers_spongebob = ClothingItem('Spongebob Slippers', 'Bottom', wardrobe) 
slippers_spongebob.parent = slippers

# Create different variations of sneakers and set their parent to the sneakers
sneakers_yeezy = ClothingItem('Yeezy 350 V2 Black Static', 'Bottom', wardrobe)
sneakers_yeezy.parent = sneakers
sneakers_jordan = ClothingItem('Jordan 1 Retro High OG Chicago', 'Bottom', wardrobe)
sneakers_jordan.parent = sneakers
sneakers_nike = ClothingItem('Nike Air Max 97 Silver Bullet', 'Bottom', wardrobe)
sneakers_nike.parent = sneakers
sneakers_adidas = ClothingItem('Adidas NMD R1 Triple White', 'Bottom', wardrobe)
sneakers_adidas.parent = sneakers
sneakers_vans = ClothingItem('Vans Old Skool Black', 'Bottom', wardrobe)
sneakers_vans.parent = sneakers