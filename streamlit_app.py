import streamlit as st
from cog_client import client

from datetime import datetime
import time
#from cognite.client import CogniteClient
st.title("BALLER TIL BALLEÅBNER")
#client = CogniteClient()

st.markdown("""
    <style>
        button {
            background-color: grey !important;
            width: 250px !important;
            height: 70px !important;
            color: white !important;
            font-size: 15px !important;
        }

        button:focus {
            background-color: green !important;
            color: white !important;
        }

        .big-font2 {
            font-size:30px !important;
            color: grey !important;
        }

        .big-font {
            font-size:30px !important;
            color: white !important;
            background-color: green !important;

        
        .small-font {
            font-size:8px !important;
            font-family: "Lucida Console", "Courier New", monospace;
            color: grey !important;
        }    
        }
        
    </style>
    
""", unsafe_allow_html=True)

cust_list = ["AFLD", "DKK_Lager", "DKK_Norfors", "DKK_SamAqua",
                        "DKK_Vejle", "Horsens", "L&T", "Marius_Pedersen",
                        "Marius_Pedersen_Industriaffald","MP_Nomi", "Renovest"]

customer_array = []

for i in cust_list:
    customer_array.append(client.time_series.data.retrieve_latest(external_id="esbjerg_" + i + "_infeed_status").to_pandas().iloc[0, 0])
active_customer = cust_list[customer_array.index(1)]


row0 = st.columns([1,1])
row1 = st.columns([1,1,1])
row4 = st.columns([1,1,1])


with row1[0]:
    option = st.selectbox("Vælg kunde", ("AFLD", "DKK_Lager", "DKK_Norfors", "DKK_SamAqua",
                        "DKK_Vejle", "Horsens", "L&T", "Marius_Pedersen",
                        "Marius_Pedersen_Industriaffald","MP_Nomi", "Renovest"), 
    index=None,
    placeholder="Kunde")

with row4[1]:
    if st.button(f'Bytt til {option}'):
        if option != active_customer:
            xid = "esbjerg_" + option + "_infeed_status"
            ts_name = "Esbjerg " + option + " infeed status"
            
            client.time_series.data.insert([(datetime.now(), 1)], external_id=xid)
            cust_list = ["AFLD", "DKK_Lager", "DKK_Norfors", "DKK_SamAqua",
                        "DKK_Vejle", "Horsens", "L&T", "Marius_Pedersen",
                        "Marius_Pedersen_Industriaffald","MP_Nomi", "Renovest"]
            cust_list.pop(cust_list.index(option))

            for i in cust_list:
                client.time_series.data.insert([(datetime.now(), 0)], external_id="esbjerg_" + i + "_infeed_status")
            st.write(f"Kunde {option} valgt")    
        else:
            st.write("Kunde er allerede valgt")

cust_list = ["AFLD", "DKK_Lager", "DKK_Norfors", "DKK_SamAqua",
            "DKK_Vejle", "Horsens", "L&T", "Marius_Pedersen",
            "Marius_Pedersen_Industriaffald","MP_Nomi", "Renovest"]
customer_array = []
for i in cust_list:
    customer_array.append(client.time_series.data.retrieve_latest(external_id="esbjerg_" + i + "_infeed_status").to_pandas().iloc[0, 0])
active_customer = cust_list[customer_array.index(1)]            

with row0[0]:
    st.markdown(f'<p class="big-font2">VALGT KUNDE: </p>', unsafe_allow_html=True)
with row0[1]:
    st.markdown(f'<p class="big-font">{active_customer.upper()}</p>', unsafe_allow_html=True)
