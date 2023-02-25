import streamlit as st
import requests
from PIL import Image

import time
import numpy as np
import pandas as pd
import folium
import ast
import pydeck as pdk
import hydralit_components as hc
import json
import plotly.graph_objects as go

#--- Load Assets ----
img_crec_logo = Image.open("images/crec_logo.png")
img_data_home = Image.open("images/data_home_2.png")
img_seethru_green = Image.open("images/seethrugreen.png")
img_triangles = Image.open("images/triangles_home.png")
img_fuzz = Image.open("images/fuzz.jpg")
img_banner = Image.open("images/banner_grid.png")
img_buildings = Image.open("images/buildings.png")
img_crecddp = Image.open("images/CRECddp.png")
img_crecddp_2 = Image.open("images/CRECddp_2.png")
crecddp_3 = Image.open("images/CRECddp_3.png")

#--- page layout ----
st.set_page_config(page_title="Capstone Real Estate Consultants", page_icon=":house:", layout="wide", initial_sidebar_state="collapsed")

#st.image(img_crec_logo, width=100) 
st.image(img_crecddp, width=1000)

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User Not Known, or Password Incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():

    df = pd.read_csv("./data/join.csv", index_col=False)
    @st.experimental_singleton
    def get_data() -> pd.DataFrame:
        start = time.time()
        end = time.time()
        elapsed = end - start
        #st.write("Elapsed time loading data:", elapsed)
        return df

    addresses = df['address'].values#.tolist()

    input = st.selectbox("Enter Address or Select From Dropdown", addresses)

    @st.experimental_memo
    def search_data(search_term: str) -> pd.DataFrame:
        df = get_data()
        start = time.time()
        filtered = df[df["address"].astype("str").str.contains(search_term, na=False)]
        end = time.time()
        elapsed = end - start
        #st.write("search time:", elapsed)
        return filtered
        
    if st.button('Run Analysis', input):
        filtered = search_data(input)
        index = filtered['location'].keys()[0]
        #st.write("Loaded", len(filtered), "row(s), ", "Index", index)
        #index = latlon
        
        latlon = ast.literal_eval(filtered.location.get(index))
        #st.write(latlon)
        lat = latlon.get('lat')
        lon = latlon.get('lon')
        map_data = pd.DataFrame(data=[[lon, lat]], columns=['lon', 'lat'])


    ### Column 1 (Recommendations and PyDeck Viz) #####
        
        col_1, col_2 = st.columns((1,1))
        with col_1: 
        
        ### recommendation engine ###
            replace = st.empty()
            replace.text('Reading in packages...')
            time.sleep(0.8)
            replace.text("Defining Functions...")
            time.sleep(0.8)
            replace.text("Reading in tax records...")
            time.sleep(0.3)
            replace.text("Reading in investor records...")
            time.sleep(0.3)
            replace.text("Reading in property records...")
            time.sleep(0.3)
            replace.text("Reading in city data...")
            time.sleep(0.3)
            replace.text("Transforming data...")
            time.sleep(0.3)
            replace.text('Mapping property...')
            time.sleep(0.3)
            replace.text('Recommendations, Map, & Analysis ready...')
            time.sleep(0.5)
            replace.empty()
            
            def unpack(dict_str, key):
                try:
                    as_dict = ast.literal_eval(dict_str)
                except:
                    return np.nan
                if not key in as_dict.keys():
                    return np.nan
                return as_dict[key]


            def ShallowMatchEuclid(address):
                results_list = []
                #Get Data!
                transaction_id = prop_map[prop_map['address'] == address]['id'].values[0]
                buyer_id = prop_map[prop_map['id'] == transaction_id]["buyerId"].values[0]
                investor_name_real = investor_map[investor_map['buyerId'] == buyer_id]['name'].values[0]
                
                res = [json.loads(idx.replace("'", '"')) for idx in txn_sim[txn_sim['id'] == transaction_id]['recs']][0]
                
                ids_list = [x['id'] for x in res]
                scores_list = [x['euclidean_distance'] for x in res]
                
                for i,el in enumerate(ids_list):
                    bdf = prop_map[prop_map['id']== el]
                    #print(bdf)
                    bid = bdf['buyerId'].values[0]
                    inv_city = bdf['OwnerCity'].values[0]
                    inv_state = bdf['OwnerState'].values[0]
                    inv_name = investor_map[investor_map['buyerId'] == bid]['name'].values[0]
                    inv_email = "contact@" + inv_name.split(" ")[0] + inv_name.split(" ")[1] + ".co"
                    distance = scores_list[i]


                    results_list.append([inv_name,inv_city,inv_state,inv_email,distance])
                return results_list

            inv_loc = './data/investor_map.csv'
            join_location = './data/join.csv'
            txn_sim_loc = './data/transaction_euclidean_sim_result.csv'

            txn_sim = pd.read_csv('./data/transaction_euclidean_sim_result.csv')

            investor_map = pd.read_csv(inv_loc)

            prop_map = pd.read_csv(join_location)

            prop_map.columns = ['Unnamed: 0_x', 'Unnamed: 0.1_x', 'id', 'buyerId', 'importDate',
                'taxId', 'mailId', 'name', 'hasPhone', 'hasEmail', 'isEntity',
                'situs_x', 'mail', 'sqft', 'value', 'purchasePrice', 'purchaseDate',
                'investmentType', 'fundingSource', 'propertyType', 'zip_x', 'state_x',
                'med_pp', 'med_sqft', 'med_val', 'pricePerSqft', 'valuePerSqft',
                'txn_count', 'test', 'OwnerCity', 'OwnerState', 'Unnamed: 0_y',
                'Unnamed: 0.1_y', 'id_y', 'recs', 'situs_y', 'zip_y', 'state_y',
                'address', 'city', 'location']

            with hc.HyLoader('',hc.Loaders.standard_loaders,index=5):
                st.subheader('Investor Recommendations')
                time.sleep(1.5)
                city_addresses = prop_map['address'].values
                recommendations = ShallowMatchEuclid(city_addresses[index])
                recommendations = pd.DataFrame(recommendations)
                recommendations.columns = ['Investor Name', 'City', 'State', 'Contact', 'Euclidean Distance']
                st.dataframe(recommendations)

    #### PyDeck Viz Mapping ###

            with hc.HyLoader('',hc.Loaders.standard_loaders,index=5):
                time.sleep(1.5)
                view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=15, pitch=55)
                layer = pdk.Layer(
                    'ColumnLayer',
                    data=map_data,
                    get_position=['lon', 'lat'],
                    #get_radius=100,  
                    radius=5,
                    #wireframe=True,
                    opacity=0.25,
                    getFillColor = [119, 146, 227,],
                    getLineColor = [119, 146, 227,],
                    elevation_scale=3,
                    pickable=True,
                    filled=True
                )

                st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    layers=[layer],
                    initial_view_state=view_state,
                ))
    #### Market Features ###
        with col_2:
            #print("Transforming data...")
            #prop_map = prop_map[['taxId', 'id', 'situs', 'zip', 'state', 'address', 'city', 'location']]
            #properties = pd.merge(txn_sim,prop_map,how = 'left', on = 'id')
            #city_data = properties[properties["state"].isin(["DC","VA","MD"])]
            #city_data = pd.merge(city_data,txn_sim,how = 'inner',on = 'id')
            #city_data[["address","id"]]
            #df_total['pricePerSqft'] = df_total['purchasePrice']/df_total['sqft']
            #df_total['valuePerSqft'] = df_total['value']/df_total['sqft']
            #df_total['OwnerCity'] = df_total['mail'].apply(lambda x: unpack(x,'city'))
            #df_total["OwnerState"] = df_total['mail'].apply(lambda x: unpack(x,'state'))
            #df_txn = df_total[['id', 'sqft', 'value', 'purchasePrice', 'propertyType','zip', 'state']]#, 'pricePerSqft', 'valuePerSqft']]

            ###Results ####

            #ShallowMatchEuclid(city_addresses[seed])

                #st.write('##')
                #st.write('##')
            #st.write('- - -')
            with hc.HyLoader('',hc.Loaders.standard_loaders,index=5):
                st.subheader('Market Features')
                time.sleep(1.5)
                tab1, tab2, tab3 = st.tabs(["Market Scoring", "Median Home Values", "Recent Sales"])
                
                with tab1:
                    st.subheader(':blue[Buyer/Seller Market Indicator]')

                    fig = go.Figure(go.Indicator(
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        value = 31,
                        mode = "gauge+number+delta",
                        title = {'text': "Buyer's Market"},
                        delta = {'reference': 73},
                        gauge = {'axis': {'range': [None, 100]}}))
                    fig.update_layout(width=300, height=280)
                    st.plotly_chart(fig, use_container_width=False)
                    st.write('- - -')
                    st.subheader(':blue[Investor Health Indicator]')
                    fig_2 = go.Figure(go.Indicator(
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        value = 68,
                        mode = "gauge+number+delta",
                        title = {'text': "Competitive Market"},
                        delta = {'reference': 97},
                        gauge = {'axis': {'range': [None, 100]}}))
                    fig_2.update_layout(width=300, height=280)
                    st.plotly_chart(fig_2, use_container_width=False)

                with tab2:
                    st.write(':blue[Median Localized Home Values]')
                    median_values = pd.read_csv('./data/Median_Values.csv')
                    st.dataframe(median_values.style.set_precision(2))

                with tab3:
                    st.write(':blue[**Nearby Recent Sales**]')
                    recent_sales = pd.read_csv('./data/Recent_Sales.csv')
                    recent_sales = pd.DataFrame(recent_sales)
                    recent_sales.columns = ['MLS Transaction', 'Address', 'Owner', 'Sale Date', 'Sale Price']
                    st.dataframe(recent_sales.style.set_precision(2))


