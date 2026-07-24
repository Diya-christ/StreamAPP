import streamlit as st

st.title("Online Food Ordering System")

name = st.text_input("Enter Customer Name")

restaurant = st.selectbox(
    "Select Restaurant",
    ["KFC", "Dominos", "Royal Foods", "Pizza Hut", "Burger King","Savoury"]
)

food = st.multiselect(
    "Choose Food Items",
    ["Chicken Biriyani", "Pizza", "French Fries", "Chicken Roll", "Veg Noooles"]
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
            "Customer Name": name,
            "Restaurant": restaurant,
            "Food Items": food,
            "Quantity": quantity,
            "Delivery Instructions": instructions,
            "Payment Method": payment
        }

        st.json(order)

    else:
        st.warning("Please confirm your order before placing it.")