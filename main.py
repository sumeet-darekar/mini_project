import streamlit as st
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Restro Management", page_icon="🍽️", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
menu_options = st.sidebar.radio("Go to", ["Home", "Manage Menu", "Reservations"])

# Function to format image for better display
def display_image(image_path, caption=None):
    img = Image.open(image_path)
    st.image(img, caption=caption, use_column_width=True)

# Home Page
if menu_options == "Home":
    st.title("Welcome to Restro Management Dashboard!")
    st.subheader("Streamline your restaurant operations.")

# Manage Menu Page
elif menu_options == "Manage Menu":
    st.title("Manage Menu")

    # Form for adding menu items
    with st.form(key='menu_form', clear_on_submit=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            item_name = st.text_input("Dish Name")
            item_description = st.text_area("Description")
            item_price = st.number_input("Price (in $)", min_value=0.0, step=0.1)
            uploaded_image = st.file_uploader("Upload Dish Image", type=["jpg", "png"])

        with col2:
            if uploaded_image:
                display_image(uploaded_image, caption=item_name)
        
        submit_menu = st.form_submit_button("Add to Menu")

    # Show success message after form submission
    if submit_menu:
        st.success(f"{item_name} added to the menu!")

    # Example of displaying menu items with images
    st.subheader("Current Menu")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_image("pizza.jpeg", caption="Pizza - $10")
    with col2:
        display_image("pasta.jpeg", caption="Pasta - $8")
    with col3:
        display_image("maggi.jpeg", caption="Salad - $6")
    with col4:
        display_image("chicken.jpeg", caption="chicken - $60")


# Reservations Page
elif menu_options == "Reservations":
    st.title("Manage Reservations")
    st.subheader("Table Reservation")

    with st.form(key='reservation_form', clear_on_submit=True):
        guest_name = st.text_input("Guest Name")
        num_people = st.number_input("Number of People", min_value=1, step=1)
        reservation_date = st.date_input("Reservation Date")
        reservation_time = st.time_input("Reservation Time")

        submit_reservation = st.form_submit_button("Reserve Table")

    # Show success message after form submission
    if submit_reservation:
        st.success(f"Table reserved for {guest_name} on {reservation_date} at {reservation_time} for {num_people} people.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Created by dummies ")
