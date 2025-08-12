
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("ventes_ifri_fictives.csv")

st.title("Tableau de Bord - Ventes Ifri")
st.markdown("Analyse interactive des ventes d'eau minérale par région et produit.")

# Sélection de filtres
regions = st.multiselect("Sélectionner les régions :", df["Région"].unique(), default=df["Région"].unique())
produits = st.multiselect("Sélectionner les produits :", df["Produit"].unique(), default=df["Produit"].unique())

# Filtrer les données
df_filtre = df[(df["Région"].isin(regions)) & (df["Produit"].isin(produits))]

# Affichage tableau
st.subheader("Aperçu des données filtrées")
st.dataframe(df_filtre)

# Graphique des ventes
st.subheader("Évolution des ventes")
fig, ax = plt.subplots()
sns.lineplot(data=df_filtre, x="Mois", y="Ventes", hue="Région", marker="o", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Statistiques simples
st.subheader("Chiffres clés")
st.write("Ventes totales :", int(df_filtre["Ventes"].sum()))
st.write("Chiffre d'affaires total (DA) :", int(df_filtre["Chiffre d'Affaires (DA)"].sum()))
