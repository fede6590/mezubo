import streamlit as st
import requests

BASE_URL = "http://localhost:5000"


def main():
    st.title("Roulette API")

    if st.button("Create New Roulette"):
        response = requests.post(f"{BASE_URL}/roulette")
        st.write(response.json())
        if response.status_code == 200:
            roulette_id = response.json()["roulette_id"]
            st.success(f"Created new roulette with ID {roulette_id}")

    if st.button("Open Roulette"):
        response = requests.put(f"{BASE_URL}/roulette/{roulette_id}/open")
        st.write(response.json())
        if response.status_code == 200:
            st.success("Roulette opened successfully")

    bet = st.text_input("Your bet (black, red or a number between 0 and 36)", value="")
    amount = st.number_input("How much you bet?", value=0)
    if st.button("Place Bet"):
        response = requests.post(f"{BASE_URL}/roulette/{roulette_id}/{bet}-{amount}")
        st.write(response.json())
        if response.status_code == 200:
            st.success("Bet placed successfully")

    if st.button("Close Roulette"):
        response = requests.post(f"{BASE_URL}/roulette/{roulette_id}/close")
        st.write(response.json())
        if response.status_code == 200:
            st.success("Roulette closed successfully")

    if st.button("Show DB"):
        response = requests.get(f"{BASE_URL}/DB")
        st.write(response.json())


if __name__ == "__main__":
    main()
