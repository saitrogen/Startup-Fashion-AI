def get_recommendations(occasion, dominant_color, body_type):
    # Example recommendation logic
    recommendations = []

    # Occasion-based suggestions
    if occasion == "Casual":
        recommendations.append("T-shirt and jeans")
    elif occasion == "Formal":
        recommendations.append("Blazer and trousers")
    elif occasion == "Party":
        recommendations.append("Cocktail dress or sharp suit")
    elif occasion == "Wedding":
        recommendations.append("Traditional attire or formal gown")
    elif occasion == "Sports":
        recommendations.append("Activewear and sneakers")

    # Color-based suggestions
    color_suggestion = f"Choose outfits with accents of RGB: {dominant_color}"
    recommendations.append(color_suggestion)

    # Body-type-based suggestions
    if body_type == "Inverted Triangle":
        recommendations.append("Opt for A-line dresses to balance proportions.")
    elif body_type == "Pear":
        recommendations.append("Wear tops with broad shoulders or puffed sleeves.")
    elif body_type == "Rectangle":
        recommendations.append("Add a belt to create a defined waist.")

    return recommendations
