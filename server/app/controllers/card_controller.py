from app.database.connection import connect_to_psql
from flask import Flask, jsonify

# Assuming `data` contains the list of lists you provided

from app.models.card import Card


def get_cards_exact(keyword):
    try:
        db = connect_to_psql()
        cursor = db.cursor()
        card_name = keyword
        query = "SELECT * FROM cards WHERE name = %s;"
        cursor.execute(query, (card_name,))
        result = cursor.fetchall()
        cursor.close()
        db.close()
        cards = [Card(*row).serialize() for row in result]
        return cards
    except Exception as error:
        print("Error while fetching data from PostgreSQL:", error)
        return "not found"


def get_cards_contain(keyword):
    return {"hello": "here"}
