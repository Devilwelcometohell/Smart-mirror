def analyze(cloth, hair, posture):
    suggestions = []

# Clothing + Hairstyle matching logic
formal = ["shirt", "blazer", "suit"]
casual = ["tshirt", "hoodie"]
sports = ["jersey", "track"]

def analyze(cloth, hair, posture):
    suggestions = []

    cloth_type = cloth.get("type", "").lower()
    hair_suggestion = hair.get("suggestion", "").lower()
    posture_status = posture.get("posture", "")

    # 👔 Clothing type feedback
    if cloth_type in formal:
        suggestions.append("You are wearing a formal outfit")
    elif cloth_type in casual:
        suggestions.append("Casual look 👍")
    elif cloth_type in sports:
        suggestions.append("Sporty look 💪")

    # 👕 Clothing grooming
    if cloth_type == "shirt":
        suggestions.append("Make sure your shirt is properly ironed and tucked")

    if cloth_type == "tshirt":
        suggestions.append("Check for wrinkles on your t-shirt")

    # 💇 Hair suggestions
    if "comb" in hair_suggestion:
        suggestions.append("Fix hair: comb your hair properly")

    if "messy" in hair_suggestion:
        suggestions.append("Fix hair: your hairstyle looks messy")
    if "adjust camera" in hair_suggestion:
        suggestions.append("Ensure your full hairstyle is visible")
    if "head straight" in hair_suggestion:
        suggestions.append("Face the mirror properly")

    # 🔗 Clothing + Hairstyle matching
    if cloth_type in formal and ("messy" in hair_suggestion or "comb" in hair_suggestion):
        suggestions.append("Formal outfit needs a neat hairstyle")

    # 🧍 Posture suggestions
    if posture_status == "Bad posture":
        suggestions.append("Fix posture: stand straight")

    elif posture_status == "Good posture":
        suggestions.append("Good posture")

    # 🔥 General grooming
    suggestions.append("Check your overall appearance before going out")

    return suggestions