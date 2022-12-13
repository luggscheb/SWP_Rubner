# pylint: disable=all

from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, Text
from sqlalchemy import create_engine,  or_
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

from dataclasses import dataclass

from flask_restful import Resource, Api

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine('sqlite:////workspaces/SWP_Rubner/HÜ_3/db.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein Millionaire) ein Attribut query für Abfragen
app = Flask(__name__)
api = Api(app)

with app.app_context():
    Base.metadata.create_all(bind=engine)
    
    
@dataclass
class Data(Base):
    __tablename__ = 'data'  # Abbildung auf diese Tabelle

    id: int
    player: int
    computer: int
    won: str
    

    id = Column(Integer, primary_key=True)
    player = Column(Integer)
    computer = Column(Integer)
    won = Column(Text)

    def serialize(self):
        return {'id' : self.id,
                'player':  self.player,
                'computer' : self.computer,
                'won' : self.won}
        
        
class Database(Resource):
    def get(self):
        jsonify(Data.query.all())
        #statistics berechnen
        
        #wie oft gespielt
        insgGespielt = Data.query.count()
        #wie oft Mensch gewonnen
        menschGewonnen = Data.query.filter(Data.won == 'S').count()
        #wie oft CP gewonnen
        computerGewonnen = Data.query.filter(Data.won == 'C').count()
        #wie oft unentschieden
        unentschiedenGewonnen = Data.query.filter(Data.won == 'U').count()
        #zu wie viel % gewinnt Mensch
        menschProz = (menschGewonnen/insgGespielt) * 100
        return jsonify({'insg': insgGespielt, 'mensch': menschGewonnen, 'comp': computerGewonnen, 'proz':menschProz})
    
    def put(self):
        d = request.get_json(force=True)
        info = Data(player=d['player'],computer=d['computer'],won=d['won'])
        db_session.add(info)
        db_session.flush()
        return jsonify(info)
    
api.add_resource(Database, '/db')


@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()


        
def save():
    info = Data(player = decision, computer = compNummer, won = hatGewonnen)
    db_session.add(info)
    db_session.flush()
    
def main():
    app.run(debug=True)
    
def stat():
    info = Data.query.all()
    print(jsonify(info))
    
if __name__ == '__main__':
    main()