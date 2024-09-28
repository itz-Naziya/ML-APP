"""
import streamlit as st
import pandas as pd

st.title('🎈 Machine learning app')

st.info('This app builds a machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X_raw=df.drop('species',axis=1)
  X_raw

  st.write('**y**')
  y_raw=df.species
  y_raw

with st.expander('Data Visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data=df, x= 'bill_length_mm',y='body_mass_g',color='species')

#input featires
with st.sidebar:
  st.header('Input Features') 
  #"bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island=st.selectbox('Island',('Biscoe','Torgersen','Dream')) 
  bill_length_mm=st.slider('Bill length (mm)',32.1,59.6,43.9)
  bill_depth_mm=st.slider('Bill Depth (mm)' , 13.1,21.5,17.2)
  flipper_length_mm=st.slider('Flipper Length (mm) ', 172.0, 231.0, 201.0)
  body_mass_g=st.slider('Body mass (g)' , 2700.0 , 6300.0 , 4207.0 )
  gender=st.selectbox('Gender',('male','female'))

#create a dataframe for input features
  data={'island' : island , 'bill_length_mm' : bill_length_mm, ' bill_depth_mm ' : bill_depth_mm , 
        ' flipper_length_mm' : flipper_length_mm , ' body_mass_g ' : body_mass_g ,
        ' sex': gender }
  input_df= pd.DataFrame(data , index = [0])
  input_penguins = pd.concat([input_df , X_raw ],axis=0)

#Data preparation
#encode X
encode = ['island', 'sex']
df_penguins=pd.get_dummies(input_penguins,columns=encode)
input_row = df_penguins[:1]

#encode Y
target_mapper = { 'Adelie' :0, 
                 'Chinstrap': 1 , 
                 'Gentoo' :2 }
def target_encode(val):
  return target_mapper[val]
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium
import streamlit_folium as st_folium
import time

# Add a title
st.title("Streamlit Example Features")

# Add a slider
slider_value = st.slider("Select a value", 0, 100)

# Add a button
if st.button("Click me!"):
    st.write(f"Slider value is: {slider_value}")

# Generate a simple chart
chart_data = pd.DataFrame(
    [[10, 20, 30], [20, 30, 40], [30, 40, 50]],
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

# Show a matplotlib chart
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 15, 25])
st.pyplot(fig)

# Add a title to the app
st.title("Streamlit Comprehensive Features Demo")

# --- SLIDER ---
# Add a slider for user input and display the selected value
slider_value = st.slider("Select a value", 0, 100)
st.write(f"Slider value is: {slider_value}")

# --- BUTTON ---
# Add a button that reacts when clicked and shows the slider value
if st.button("Click me!"):
    st.write(f"Button clicked! Slider value is: {slider_value}")

# --- TEXT INPUT ---
# Capture user input through a text input widget
user_input = st.text_input("Enter some text")
st.write(f"You entered: {user_input}")

# --- SELECTBOX (DROPDOWN) ---
# Add a dropdown (selectbox) for user to choose from multiple options
option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {option}')

# --- RADIO BUTTONS ---
# Add radio buttons to allow selection of one option from several
genre = st.radio("Choose your favorite genre:", ('Comedy', 'Drama', 'Documentary'))
st.write(f'You selected {genre}')

# --- CHECKBOX ---
# Show or hide content based on a checkbox
if st.checkbox('Show/Hide Data'):
    st.write("Checkbox is checked and data is shown")

# --- MULTISELECT ---
# Allow multiple selections from a list using a multiselect widget
options = st.multiselect('Select multiple options:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {options}')

# --- DATE PICKER ---
# Allow the user to pick a date using a date picker
selected_date = st.date_input("Pick a date")
st.write(f'Date selected: {selected_date}')

# --- FILE UPLOADER ---
# Upload a CSV file and display its content
uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# --- PROGRESS BAR ---
# Display a progress bar that updates dynamically
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress_bar.progress(i + 1)

# --- COLOR PICKER ---
# Allow user to pick a color from a color picker widget
color = st.color_picker('Pick a color', '#00f900')
st.write(f'The selected color is {color}')

# --- LINE CHART (using Streamlit) ---
# Generate and display a simple line chart
chart_data = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [20, 30, 40],
    'C': [30, 40, 50]
})
st.line_chart(chart_data)

# --- MATPLOTLIB CHART ---
# Generate and display a simple matplotlib chart
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 15, 25])
st.pyplot(fig)

# --- PLOTLY CHART ---
# Generate and display an interactive Plotly chart
df = px.data.iris()  # Using the iris dataset
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
st.plotly_chart(fig)

# --- INTERACTIVE MAP (using Folium) ---
# Generate and display an interactive map with a marker
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.Marker([45.5236, -122.6750], popup="Location 1").add_to(m)
st_folium.folium_static(m)

# --- TABS ---
# Create two tabs to organize content
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("This is content for Tab 1.")
with tab2:
    st.write("This is content for Tab 2.")

# --- EXPANDER ---
# Use an expander to hide and show additional content
with st.expander("Click to expand"):
    st.write("Here is some expanded content!")

# --- METRIC COMPONENT ---
# Display a key metric value
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# --- AUDIO/VIDEO ---
# Allow user to play audio and video files
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")






