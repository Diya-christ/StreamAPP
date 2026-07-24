import streamlit as st
import pandas as pd

st.title("Online Food Ordering System")

name = st.text_input("Enter Customer Name")

restaurant = st.selectbox(
    "Select Restaurant",
    ["KFC", "Dominos", "McDonald's", "Pizza Hut", "Burger King"]
)

food = st.multiselect(
    "Choose Food Items",
    ["Burger", "Pizza", "French Fries", "Chicken", "Cold Drink"]
)

quantity = st.slider("Select Quantity", 1, 10)

instructions = st.text_area("Delivery Instructions")

payment = st.radio(
    "Select Payment Method",
    ["Cash on Delivery", "UPI", "Credit/Debit Card"]
)

confirm = st.checkbox("I Confirm My Order")

if st.button("Place Order"):

    if confirm:

        st.success("Order Placed Successfully!")

        order = {
            "Customer Name": [name],
            "Restaurant": [restaurant],
            "Food Items": [", ".join(food)],
            "Quantity": [quantity],
            "Delivery Instructions": [instructions],
            "Payment Method": [payment]
        }

        df = pd.DataFrame(order)

        st.write("### Order Details")
        st.table(df)

    else:
        st.warning("Please confirm your order.")
