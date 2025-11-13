import pickle
from typing import Literal

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, ConfigDict, Field
from sklearn.utils.validation import check_is_fitted

from utils.save_load_model import load_model


class Order(BaseModel):
    model_config = ConfigDict(extra="forbid")

    order_id: int = Field(..., ge=0)
    customer_id: int = Field(..., ge=0.0)
    restaurant_name: Literal[
        "Hangawi",
        "Blue Ribbon Sushi Izakaya",
        "Cafe Habana",
        "Blue Ribbon Fried Chicken",
        "Dirty Bird to Go",
        "Tamarind TriBeCa",
        "The Meatball Shop",
        "Barbounia",
        "Anjappar Chettinad",
        "Bukhara Grill",
        "Big Wong Restaurant \x8c_¤¾Ñ¼",
        "Empanada Mama (closed)",
        "Pylos",
        "Lucky's Famous Burgers",
        "Shake Shack",
        "Sushi of Gari",
        "RedFarm Hudson",
        "Blue Ribbon Sushi",
        "Five Guys Burgers and Fries",
        "Tortaria",
        "Cafe Mogador",
        "Otto Enoteca Pizzeria",
        "Vezzo Thin Crust Pizza",
        "Sushi of Gari 46",
        "The Kati Roll Company",
        "Klong",
        "5 Napkin Burger",
        "TAO",
        "Parm",
        "Sushi Samba",
        "Haru Gramercy Park",
        "Chipotle Mexican Grill $1.99 Delivery",
        "RedFarm Broadway",
        "Cafeteria",
        "DuMont Burger",
        "Sarabeth's East",
        "Hill Country Fried Chicken",
        "Bistango",
        "Jack's Wife Freda",
        "Mamoun's Falafel",
        "Prosperity Dumpling",
        "Blue Ribbon Sushi Bar & Grill",
        "Westville Hudson",
        "Blue Ribbon Brooklyn",
        "Nobu Next Door",
        "Osteria Morini",
        "Haandi",
        "Benihana",
        "Han Dynasty",
        "Chote Nawab",
        "Mission Cantina",
        "Xi'an Famous Foods",
        "Rubirosa",
        "Joe's Shanghai \x8e_À\x8eü£¾÷´",
        "Bareburger",
        "The Odeon",
        "Pongsri Thai",
        "Yama Japanese Restaurant",
        "Momoya",
        "Balthazar Boulangerie",
        "CafÌ© China",
        "Boqueria",
        "Song Thai Restaurant & Bar",
        "Five Leaves",
        "Pinto Nouveau Thai Bistro",
        "Amy Ruth's",
        "Pepe Giallo",
        "indikitch",
        "Yama 49",
        "Piccolo Angolo",
        "Pepe Rosso To Go",
        "L'Express",
        "Amma",
        "Delicatessen",
        "S'MAC",
        "Vanessa's Dumplings",
        "Bhatti Indian Grill",
        "Taro Sushi",
        "Donburi-ya",
        "Hatsuhana",
        "Samurai Mama",
        "Waverly Diner",
        "Tarallucci e Vino Restaurant",
        "P.J. Clarke's",
        "Lantern Thai Kitchen",
        "ilili Restaurant",
        "The Smile",
        "Vanessa's Dumpling House",
        "Bubby's ",
        "Woorijip",
        "Dirty Bird To Go (archived)",
        "Haveli Indian Restaurant",
        "Dos Caminos",
        "da Umberto",
        "Sushi of Gari Tribeca",
        "Burger Joint",
        "Room Service",
        "Sarabeth's Restaurant",
        "Xe May Sandwich Shop",
        "Hibino",
        "Mira Sushi",
        "Melt Shop",
        "J. G. Melon",
        "Hummus Place",
        "Saravanaa Bhavan",
        "Friend of a Farmer",
        "The Loop",
        "Balade",
        "Posto",
        "Terakawa Ramen",
        "Kambi Ramen House",
        "Wo Hop Restaurant",
        "Spice Thai",
        "Dickson's Farmstand Meats",
        "UVA Wine Bar & Restaurant",
        "Serafina Fabulous Pizza",
        "Gaia Italian Cafe",
        "Chola Eclectic Indian Cuisine",
        "Hot Kitchen",
        "Junoon",
        "Ravagh Persian Grill",
        "Rohm Thai",
        "Dig Inn Seasonal Market",
        "Olea",
        "Cho Dang Gol",
        "El Parador Cafe",
        "Socarrat Paella Bar",
        "Don's Bogam BBQ & Wine Bar",
        "Alidoro",
        "Tony's Di Napoli",
        "Cipriani Le Specialita",
        "Sushi Choshi",
        "Kanoyama",
        "V-Nam Cafe",
        "Zero Otto Nove",
        "Dos Caminos Soho",
        "Go! Go! Curry!",
        "La Follia",
        "Izakaya Ten",
        "12 Chairs",
        "Philippe Chow",
        "The MasalaWala",
        "brgr",
        "Carmine's",
        "Asuka Sushi",
        "Aurora",
        "Sarabeth's",
        "Crema Restaurante",
        "Big Daddy's",
        "Moonstruck on Second",
        "Cafe de La Esquina",
        "Olive Garden",
        "67 Burger",
        "Tres Carnes",
        "Schnipper's Quality Kitchen",
        "Nha Trang One",
        "Market Table",
        "Galli Restaurant",
        "Hampton Chutney Co.",
        "Byblos Restaurant",
        "Grand Sichuan International",
        "Le Grainne Cafe",
        "Il Bambino",
        "Kori Restaurant and Bar",
        "DespaÌ±a",
        "Lamarca Pasta",
        "Lucky Strike",
        "Paul & Jimmy's",
        "Hunan Manor",
        "Coppola's East",
        "Emporio",
        "Wa Jeal",
        "Le Zie 2000 Trattoria",
        "Rye House",
        "Hiroko's Place",
        "Frank Restaurant",
        "Sarabeth's West",
        "'wichcraft",
    ]
    cuisine_type: Literal[
        "Korean",
        "Japanese",
        "Mexican",
        "American",
        "Indian",
        "Italian",
        "Mediterranean",
        "Chinese",
        "Middle Eastern",
        "Thai",
        "Southern",
        "French",
        "Spanish",
        "Vietnamese",
    ]
    cost_of_the_order: float = Field(..., ge=0.0)
    day_of_the_week: Literal["Weekend", "Weekday"]


class PredictResponse(BaseModel):
    order_id: int
    customer_id: int
    prediction: float


app = FastAPI(title="food_preparation_time_prediction")

file_path = "model/model.pkl"
pipeline = load_model(file_path)

print(check_is_fitted(pipeline))


@app.get("/")
def root():
    # return {"status": "ok", "docs": "/docs"}
    return RedirectResponse(url="/docs")


@app.post("/predict")
def predict(order: Order) -> PredictResponse:
    X = pd.DataFrame([order.model_dump()])
    pred = pipeline.predict(X)
    # print(order)

    return PredictResponse(
        order_id=order.order_id, customer_id=order.customer_id, prediction=pred
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
