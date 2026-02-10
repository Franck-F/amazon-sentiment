import pandas as pd
import numpy as np
import random
import os

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_reviews(num_samples=10000):
    products = [
        "Clavier Gamer RGB", "Ecouteurs Bluetooth", "Souris Sans Fil", 
        "Ecran 4K 27 pouces", "Cable USB-C Charge Rapide", "Tapis de Souris XXL",
        "Casque Audio Noise Cancelling", "Support PC Portable", "Enceinte Connectée",
        "Webcam HD 1080p"
    ]
    
    positive_phrases = [
        "C'est un excellent produit !", "Vraiment ravi de mon achat.", "La qualité est au rendez-vous.",
        "Fonctionne parfaitement bien.", "Je recommande vivement cet article.", "Expédition rapide et soignée.",
        "Excellent rapport qualité-prix.", "Design élégant et robuste.", "Très simple à installer.",
        "Les performances sont impressionnantes.", "Super produit, rien à dire."
    ]
    
    neutral_phrases = [
        "Produit correct pour le prix.", "Fait le job mais sans plus.", "Correct sans être exceptionnel.",
        "Un peu déçu par la finition mais ça fonctionne.", "Pas mal du tout, malgré quelques petits défauts.",
        "Moyen, j'attendais un peu mieux.", "Arrivé dans les temps, emballage sommaire.",
        "Conforme à la description, mais l'usage est limité."
    ]
    
    negative_phrases = [
        "Très déçu par cet achat.", "Ne fonctionne pas du tout.", "La qualité est médiocre.",
        "Plastique de mauvaise qualité.", "Je ne recommande pas ce produit.", "En panne après deux jours d'utilisation.",
        "Une perte de temps et d'argent.", "C'est une arnaque, passez votre chemin.", 
        "Le SAV est inexistant.", "Arrivé cassé, inadmissible."
    ]

    data = []
    
    for _ in range(num_samples):
        product = random.choice(products)
        # 60% positive, 20% neutral, 20% negative to mimic real Amazon skew
        rand_val = random.random()
        
        if rand_val < 0.6:
            rating = random.randint(4, 5)
            text = random.choice(positive_phrases)
            sentiment = "Positive"
        elif rand_val < 0.8:
            rating = 3
            text = random.choice(neutral_phrases)
            sentiment = "Neutral"
        else:
            rating = random.randint(1, 2)
            text = random.choice(negative_phrases)
            sentiment = "Negative"
            
        data.append({
            "product_name": product,
            "review_body": text,
            "stars": rating,
            "sentiment": sentiment
        })
        
    df = pd.DataFrame(data)
    
    # Save to csv
    output_path = os.path.join("data", "amazon_reviews.csv")
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Dataset generated with {num_samples} samples at {output_path}")

if __name__ == "__main__":
    generate_reviews()
