#pip install streamlit

import streamlit as st

st.markdown(
    """
    <style>
    .stApp{
        background-image: url('https://img.freepik.com/premium-vector/dark-concrete-background-with-grunge-effect_278222-9845.jpg')
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config(
    page_title='House Design Profile',
    layout='wide'
)

col1, col2,= st.columns([1,3])

with col1:
    uploaded_image = st.file_uploader('Choose an image...', type=['jpg','png','jpeg'], )

if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image', width=150)


with col2:
    st.title("THE DUO ")
    st.write('Interior Design Studio')
    st.write('Interior Consultancy')
    st.success('Design Consulation | Interior Styling | Furniture')
    st.success('let,s embrace the beauty of individuality together')


st.divider()

tab1, tab2, tab3, tab4 = st.tabs(['🏠About', '🖼️ Gallery', 'Services', '📞 Contact us'])

with tab1:
    st.header('About Us')
    st.write("""
    we specialize in commercial and interior house designs.
    Our goal is to provide affordable, beautiful and
    industrial house layouts for our clients.
    """)

    st.info("5+ Year Experience in House Designing")


with tab2:
    st.header('House Design Gallery')
    uploaded_images = st.file_uploader('Choose images...', type=['jpg','png','jpeg'], accept_multiple_files=True)

if uploaded_images:
    for image in uploaded_images:
        st.image(image, caption=image.name) 

    
with tab3:
    st.header(' Our Services')
    st.write('We provide complete interior design and technical documentation support for residential and commercial projects')
    st.write('- Interior design & concept development')
    st.write('- Space planning and 2D layouts')
    st.write('- Execution-ready working drawings')
    st.write('- Furniture and joinery detailing')
    st.write(' - Ceiling, lighting & electrical layouts')
    st.write(' - 3D realistic visualizations')
    st.write('- Material and finish selection')
    st.write('- Design coordination & execution') 
    
with tab4:
      st.write('- +92 3474133474')
      st.write('- +92 3254027167')
      st.write('- theduopk@gmail.com')
    
    
st.divider()
st.caption('@ 2026 House Design Website | Built with Streamlit')

    













    