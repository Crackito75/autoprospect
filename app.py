import streamlit as st
import openai

# Ajouter ta clé API OpenAI (on fera mieux après)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤖 AutoProspect – Trouve tes premiers leads avec l'IA")

user_icp = st.text_area("Décris ton client idéal (ex: CEO d’une startup legaltech en France)")

if st.button("Trouver des leads et générer des emails") and user_icp:
    st.write("📊 **Résultats générés (Mock Data)**")

    # Simuler des leads
    mock_leads = [
        {"name": "Sophie Martin", "company": "LegalBoost", "title": "CEO"},
        {"name": "Thomas Dupont", "company": "LexTech", "title": "Co-founder"},
    ]

    for lead in mock_leads:
        # Génération d'email avec OpenAI
        prompt = f"""
Tu es un SDR junior dans une startup B2B. Tu veux contacter {lead['name']}, {lead['title']} chez {lead['company']}.
Voici le type de client recherché : {user_icp}

Écris un email de prospection court, professionnel et personnalisé.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un expert en prospection B2B."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        email = response.choices[0].message.content

        # Afficher le résultat
        st.markdown(f"### 📩 Email pour {lead['name']} – {lead['company']}")
        st.code(email, language="markdown")
