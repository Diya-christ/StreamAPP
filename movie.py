import streamlit as st
import pandas as pd

st.title("Movie Ticket Booking System")

name = st.text_input("Enter Customer Name")

movie = st.selectbox(
    "Select Movie",
    ["Leo", "Jailer", "Avengers", "Kalki", "Pushpa 2"]
)

show = st.radio(
    "Select Show Timing",
    ["10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM"]
)

tickets = st.number_input("Number of Tickets", 1, 10)

seat = st.select_slider(
    "Select Seat Type",
    options=["Silver", "Gold", "Platinum"]
)

snacks = st.multiselect(
    "Choose Snacks",
    ["Popcorn", "Burger", "Cold Drink", "Nachos"]
)

agree = st.checkbox("I Agree to the Terms and Conditions")

if st.button("Book Ticket"):

    if agree:

        st.balloons()
        st.success("Movie Ticket Booked Successfully!")

        booking = {
            "Customer Name": [name],
            "Movie": [movie],
            "Show Timing": [show],
            "Tickets": [tickets],
            "Seat Type": [seat],
            "Snacks": [", ".join(snacks)]
        }

        df = pd.DataFrame(booking)

        st.markdown("### Booking Details")
        st.table(df)

    else:
        st.warning("Please agree to the Terms and Conditions.")