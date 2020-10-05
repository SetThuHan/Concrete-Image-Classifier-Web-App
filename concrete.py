import streamlit as st 
from PIL import Image

from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import load_model
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Cracked Or Uncracked 🤔❓")
st.header("Please upload any concrete image 🖌️ (.jpg)")
uploaded_file = st.file_uploader(" ", type="jpg")


if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption='*Uploaded Image*', use_column_width=True)
    st.write("")
    st.subheader("Classifying Image  👨‍💻............................................")
    
    vgg16_model = load_model('classifier_vgg16_model.h5')
 
    image = img_to_array(image)
  
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    image = preprocess_input(image)

    vggmodel = vgg16_model.predict(image)
    def pred(x):
        for i in x:
            j = np.argmax(i)
            if(j==0):
                st.header("**Uncracked Concrete 🧱 **")
                
            else:
                st.header("**Cracked Concrete! 🚧 **")
                st.subheader("Why does Concrete crack ? For more information, Please GOOGLE it! 🤪 ")
    st.write(pred(vggmodel))
