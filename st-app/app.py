import streamlit as st
import requests

BASE_URL = "http://flask-api:5000"


def main():
    st.title("Roulette API")
    global roulette_id
    roulette_id = None

    if st.button("Create New Roulette"):
        response = requests.post(f"{BASE_URL}/roulette")
        st.write(response.json())
        if response.status_code == 200:
            roulette_id = response.json()["roulette_id"]
            st.success(f"Created new roulette with ID {roulette_id}")

    roulette_id = st.number_input("Indicate roulette_id:", value=roulette_id, key=0)
    if st.button("Open Roulette"):
        response = requests.put(f"{BASE_URL}/roulette/{roulette_id}/open")
        st.write(response.json())
        if response.status_code == 200:
            st.success("Roulette opened successfully")

    bet = st.text_input("Your bet (black, red or a number between 0 and 36)")
    amount = int(st.number_input("How much do you bet?", value="min", min_value=0, max_value=10000, step=1))
    if st.button("Place Bet"):
        response = requests.post(f"{BASE_URL}/roulette/{roulette_id}/{bet}-{amount}")
        st.write(response.json())
        if response.status_code == 200:
            st.success("Bet placed successfully")

    roulette_id = st.number_input("Indicate roulette_id:", value=roulette_id, key=1)
    if st.button("Close Roulette"):
        response = requests.post(f"{BASE_URL}/roulette/{roulette_id}/close")
        st.write(response.json())
        if response.status_code == 200:
            st.success("Roulette closed successfully")

    if st.button("Show DB"):
        response = requests.get(f"{BASE_URL}/roulette/DB")
        st.write(response.json())

    st.write('You have 10.000 initial credit')


if __name__ == "__main__":
    main()
