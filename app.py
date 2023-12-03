import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

items_data = json.load(open("output_items.json", "r", encoding="utf-8"))
print(items_data)
items_df = pd.DataFrame({"Objetos": [x["description"] for x in items_data["items"]]})

people_df = pd.DataFrame({"Personas": items_data['entidades']['people']})
companies_df = pd.DataFrame({"Organizaciones/Companias":items_data['entidades']['companies/organizations']})

df = pd.read_json("items_market.json")

# Function to simulate processing and return results
def process_file(uploaded_file):
    # Simulate some processing
    df = pd.DataFrame({"name": []})
    return df

# Main page layout
st.title("Subir Archivo JSON del Contrato a Analizar")

# File uploader
uploaded_file = st.file_uploader("Elige el Archivo")

if uploaded_file is not None:
    # Button to upload file
    if st.button('Upload'):
        # Process the file
        result = process_file(uploaded_file)

        # Open a new window to show results
        with st.expander("Elementos de Interes"):
            st.subheader("Items")
            st.table(items_df)

            # Assuming the JSON contains 'companies' and 'names', display them
            st.subheader("Lista de Personas mencionadas en el archivo")
            st.write(people_df)
            
            st.subheader("Lista de Orgnizaciones/Empresas mencionadas en el archivo")
            st.write(companies_df)
            

        with st.expander("Analisis de las partes y sanciones"):
            st.write("No se encontraron resultados :(")
        
        with st.expander("Analisis de los elementos comprados o contratados"):
            for _, item in items_df.iterrows():
                st.header(f"Analisis de {item['Objetos']}")

                st.subheader("Resultados encontrados en Internet para Items similares")
                st.write(df)

                st.subheader("Distribucion de los costos de items similares")

                # Filter out rows where cost/unit is not a number
                df = df[df['success'] == "OK"]

                # Convert cost/unit to numeric
                df['cost/unit'] = pd.to_numeric(df['cost/unit'])

                # Plotting histogram
                fig, ax = plt.subplots(figsize=(10,6))
                ax.hist(df['cost/unit'], bins=10, edgecolor='black', color='blue')
                ax.axvline(x=15, color='red', linestyle='--')
                ax.set_title('Distribucion de los costos de los items encontrados (En Rojo, Costo en Contrato)')
                ax.set_xlabel('Costo por unidad')
                ax.set_ylabel('Frecuencia')
                ax.grid(axis='y', alpha=0.75)
                
                st.pyplot(fig)

                st.subheader("Diagnostico de Precio")
                st.write("No se encontraron anomalias de costos")
                    