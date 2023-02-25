import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Capstone Real Estate Consultants", page_icon=":house:", layout="wide", initial_sidebar_state="collapsed")

#--- Load Assets ----
img_crec_logo = Image.open("images/crec_logo.png")
img_seethru_green = Image.open("images/seethrugreen.png")
img_timetodeal = Image.open("images/time_to_deal.jpeg")
img_heatmap = Image.open("images/heatmap.jpg")
img_buyer = Image.open("images/buyer.jpeg")
img_houses = Image.open("images/houses_q.png")
img_people = Image.open("images/people_q.png")
img_crecddp = Image.open("images/CRECddp.png")
img_crec_logo = Image.open("images/crec_logo.png")
img_seethru_green = Image.open("images/seethrugreen.png")
img_timetodeal = Image.open("images/time_to_deal.jpeg")
img_heatmap = Image.open("images/heatmap.jpg")
img_buyer = Image.open("images/buyer.jpeg")
img_data_1 = Image.open("images/data_1.png")
img_data_2 = Image.open("images/data_2.png")
img_data_3 = Image.open("images/data_3.png")
img_data_stats = Image.open("images/data_stats.png")
crecddp_3 = Image.open("images/CRECddp_3.png")
platform = Image.open("images/platform_snip.png")

#---- Header Section -----
st.image(crecddp_3, width=200)
st.write("- - -")

#--- Top section ----
with st.container():
    st.title("The Use Case")
    st.write("Real estate continues to be the biggest asset class in the world. While investing in the real estate market can be a lucrative endeavor, making the right decisions at the right time with the right insights has historically been more **art than science**. Access to accurate data, trends, and ML-driven market recommendation engines can deeply enrich an investor's perspective, enabling faster decision-making, lowering risk, and improving long term profitability.")
    st.write("##")
    text_1, text_2 = st.columns((1,1))
    with text_1:
        st.image(img_houses, width=300)
        st.subheader("**Buyers are constrained by two primary factors:**")
        st.caption("> The ability to acquire sufficient, accurate, and current market information")
        st.caption("> The ability to source good deals, fast")
   # st.write("##")
    with text_2:
        st.image(img_people, width=300)
        st.subheader("**Sellers are also trying to solve for two challenges:**")
        st.caption("> How can I make my property attractive to buyers?")
        st.caption("> Who is most likely to be interested in my property?")
    st.write("##")
    st.title("The Solution")
    st.write("##")
    st.image(img_crecddp) #width=900)
    st.write("##")
    st.header("Business Value Creation")
    st.write("##")
    tab1, tab2, tab3 = st.tabs(["Time to Deal", "Competitive Insights", "Connecting Parties"])
    with tab1:
        st.subheader("Time to Deal")
        st.markdown("_What can we do to move faster?_")
        st.write("Clients are always in a balancing act between gathering information and making quick decisions. To maximize upside and deal velocity, they need access to data, predictions, and resources to augment their decisions.")
        st.write("**CREC's DealData platform enables investors to understand property trends and buyer/seller behavior in order to move fast towards a deal.**")
        st.image(img_timetodeal)
    with tab2:
        st.subheader("Competitive Insights")
        st.markdown("_Where should we be investing?_")
        st.write("Segment analysis, as provided by **CREC's DealData platform**, enables clients to better understand the players in local markets, what actions they are taking, and how to optimize outcomes in a competitive market, whether buying or selling.")
        st.image(img_heatmap)
    with tab3:
        st.subheader("Connecting Parties")
        st.markdown("_Who will buy this property?_")
        st.write("Wouldn't it be nice to know who would buy a property long before they have seen it?")
        st.write("CREC's DealData platform automates connections between buyers and property features, enabling sellers to pursue high probability interested parties fast.")
        st.write("This ML technique works in reverse, where buyers can identify best-fit properties, and get notified if and when an owner is ready to sell.")
        st.image(img_buyer, width=450)
    st.write("- - -")
    st.write("##")
    st.header("The Approach")
    tab4, tab5, tab6 = st.tabs(["The Data", "The Tech", "The Platform"])
    with tab4:
        st.subheader("The Data")
        st.write("Substantial data is necessary to execute a machine learning model for as complex an industry as real estate. Amalgamated from a variety of root sources, CREC's proprietary techniques leverage 170 million unique North American real estate records. This data can be described in 3 distinct dataset buckets, as outlined below:")
        st.caption("Data is supplemented by CREC's partner, RealProp RT, LLC")
        st.write("##")
        text_1, text_2, text_3 = st.columns((1,1,1))
        with text_1:
            st.subheader("Tax Records")
            st.write("The Tax record dataset contains all of the property level details, like building features, valuation information, and parcel specifics.")
            st.image(img_data_1, width=250)
        with text_2:
            st.subheader("Deed Records")
            st.write("The Deed record dataset contains information about historical transactions and any publicly reported mortgage information.")
            st.image(img_data_2, width=250)
        with text_3:
            st.subheader("Buyer Segmentation")
            st.write("Proprietary rules are applied to an aggregated composite of the Tax and Deeds records during a weekly ETL process, in order to identify unique investor types for every transaction")
            st.image(img_data_3, width=250)
        st.write("- - -")
        st.subheader("Descriptive Statistics")
        st.image(img_data_stats, width=800)
    with tab5:
        st.subheader("The Tech")
        st.write("Capstone Real Estate Consultants plans to utilize the following cutting edge technologies to execute the initial scope of work, and ultimately deliver the business values as stated in the project goals and deliverables.")
        st.write("##")
        st.subheader("**:blue[Infrastructure]**")
        st.write("> data store: Amazon Web services (AWS) S3")
        st.write("> data warehouse: AWS redshift")
        st.write("> code repository and management: Github")
        st.write("##")
        st.subheader("**:blue[Exploratory Data Analysis (EDA)]**")
        st.write("> Language: Python 3.11.x (most current at time of poc)")
        st.write("> data wrangling: Pandas ")
        st.write("> visualizations: matplotlib, seaborn")
        st.write("##")
        st.subheader("**:blue[Recommendation Engine]**")
        st.write("> Language: python 3.11.x")
        st.write("> algorithms: K-means, knn, dbscan")
        st.write("> frameworks: scikitlearn, keras, tensorflow, surprise, lightfm")
        st.write("##")
        st.subheader("**:blue[Front-End Dashboards]**")
        st.write("> microservice containerization: docker")
        st.write("> web app: streamlit")
    with tab6:
        st.subheader("The Platform")
        st.write("CREC's DealData Platform provides investor recommendations, mapping, and statistics for any property in the DC metro area")
        st.image(platform)
    ####### Data and EDA Page ###########

#--- Load Assets ----
#Capstone Real Estate Consultants plans to utilize the following cutting edge technologies to execute the initial scope of work, and ultimately deliver the business values as stated in the project goals and deliverables.



















#--- top section ----
    
    
#--- middle section ----
