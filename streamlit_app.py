import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ("Page 1", "Page 2"), index=0)  # Page 1 is set as the default page

# --- PAGE 1 ---
if page == "Page 1":
    st.title("Streamlit Comprehensive Features Demo")

    # --- SLIDER ---
    slider_value = st.slider("Select a value", 0, 100)
    st.write(f"Slider value is: {slider_value}")

    # --- BUTTON ---
    if st.button("Click me!"):
        st.write(f"Button clicked! Slider value is: {slider_value}")

    # --- TEXT INPUT ---
    user_input = st.text_input("Enter some text")
    st.write(f"You entered: {user_input}")

    # --- SELECTBOX (DROPDOWN) ---
    option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
    st.write(f'You selected: {option}')

    # --- RADIO BUTTONS ---
    genre = st.radio("Choose your favorite genre:", ('Comedy', 'Drama', 'Documentary'))
    st.write(f'You selected {genre}')

    # --- CHECKBOX ---
    if st.checkbox('Show/Hide Data'):
        st.write("Checkbox is checked and data is shown")

    # --- MULTISELECT ---
    options = st.multiselect('Select multiple options:', ['Option 1', 'Option 2', 'Option 3'])
    st.write(f'You selected: {options}')

    # --- DATE PICKER ---
    selected_date = st.date_input("Pick a date")
    st.write(f'Date selected: {selected_date}')

    # --- FILE UPLOADER ---
    uploaded_file = st.file_uploader("Upload a CSV file")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

    # --- PROGRESS BAR ---
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)

    # --- COLOR PICKER ---
    color = st.color_picker('Pick a color', '#00f900')
    st.write(f'The selected color is {color}')

    # --- LINE CHART (using Streamlit) ---
    chart_data = pd.DataFrame({
        'A': [10, 20, 30],
        'B': [20, 30, 40],
        'C': [30, 40, 50]
    })
    st.line_chart(chart_data)

    # --- MATPLOTLIB CHART ---
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 15, 25])
    st.pyplot(fig)

    # --- PLOTLY CHART ---
    df = px.data.iris()  # Using the iris dataset
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    st.plotly_chart(fig)

    # --- TABS ---
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("This is content for Tab 1.")
    with tab2:
        st.write("This is content for Tab 2.")

    # --- EXPANDER ---
    with st.expander("Click to expand"):
        st.write("Here is some expanded content!")

    # --- METRIC COMPONENT ---
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    # --- AUDIO/VIDEO ---
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# --- PAGE 2 ---
elif page == "Page 2":
    st.title('🎈 Machine Learning App')
    st.info('This app builds a machine learning model')

    with st.expander('Data'):
        st.write('**Raw Data**')
        df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
        st.write(df)

        st.write('**X**')
        X_raw = df.drop('species', axis=1)
        st.write(X_raw)

        st.write('**y**')
        y_raw = df.species
        st.write(y_raw)

    with st.expander('Data Visualization'):
        st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

    # Input features
    with st.sidebar:
        st.header('Input Features') 
        island = st.selectbox('Island', ('Biscoe', 'Torgersen', 'Dream')) 
        bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
        bill_depth_mm = st.slider('Bill Depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.slider('Flipper Length (mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
        gender = st.selectbox('Gender', ('male', 'female'))

    # Create a DataFrame for input features
    data = {
        'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'sex': gender
        }
    input_df = pd.DataFrame(data, index=[0])
    input_penguins = pd.concat([input_df, X_raw], axis=0)

    # Data preparation: encode X
    encode = ['island', 'sex']
    df_penguins = pd.get_dummies(input_penguins, columns=encode)
    input_row = df_penguins[:1]

    # Encode Y
    target_mapper = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
    def target_encode(val):
        return target_mapper[val]

