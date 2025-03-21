import streamlit as st

st.title("🤖 AutoProspect – Trouve tes premiers leads avec l'IA")

user_icp = st.text_area("Décris ton client idéal (ex: CEO d’une startup legaltech en France)")

if st.button("Trouver des leads et générer des emails") and user_icp:
    st.write("📊 **Résultats générés (Mock Data)**")
    mock_leads = [
        {"name": "Sophie Martin", "company": "LegalBoost", "title": "CEO"},
        {"name": "Thomas Dupont", "company": "LexTech", "title": "Co-founder"},
    ]

    for lead in mock_leads:
        st.write(f"**{lead['name']}** – {lead['company']} ({lead['title']})")
        st.write("📩 Email généré : *Bonjour, voici pourquoi je vous contacte…*")
        st.markdown("---")
