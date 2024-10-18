import cv2
import numpy as np
import streamlit as st
import main
from pylatexenc.latex2text import LatexNodes2Text

#ui
st.title("IDOC Tools.")
st.header("Text Extraction from Image")


#for camera input
st.subheader("Camera Input")

pic = st.camera_input("Capture image")

if pic is not None:
    bytes_data = pic.read()

    np_array = np.frombuffer(bytes_data,np.uint8)

    image = cv2.imdecode(np_array,cv2.IMREAD_COLOR)

    cv2.imwrite("cap_img.jpg",image)

    one,two =st.columns(2)
    with one:
        st.image(pic, caption='Uploaded Image')
        st.write("Image saved successfully.")
    
    processed_image, text = main.extract_text("cap_img.jpg")
    with two:
        st.image(processed_image, caption='Processed Image')
        st.write("Image Processed.")
    
    st.subheader("Extracted Text:")
    st.code(text)
    st.download_button("Download Text File", main.get_docx(text), file_name="latexFile.txt", mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    st.download_button("Download docx File", main.get_docx(text), file_name="latexFile_doc.docx", mime="docx")  

st.divider()




#add to upload Text img from user
st.header("File Input - Text Image")

uploaded_file = st.file_uploader("Upload image:",type=["jpg","png","jpeg"]) 

if uploaded_file is None:
    st.write("NO image is Uploaded!!")

if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    # Convert bytes to a NumPy array
    np_array = np.frombuffer(bytes_data, np.uint8)

    # Decode the NumPy array as a OpenCV image (BGR color space)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Save the image to a specified location
    temp_image_path="captured_image.jpg"
    cv2.imwrite(temp_image_path,image)
    
    #creating columns
    one,two =st.columns(2)

    # Display the uploaded image
    with one:
        st.image(uploaded_file, caption='Uploaded Image')
        st.write("Image saved successfully.")
    
    processed_image, text = main.extract_text(temp_image_path)
    with two:
        st.image(processed_image, caption='Processed Image')
        st.write("Image Processed.")
    
    st.subheader("Extracted Text:")
    st.code(text)
    
    st.download_button("Download text File", text, file_name="newfile.txt", mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)   
    st.download_button("Download docx File", main.get_docx(text), file_name="newfile_doc.docx", mime="docx")
st.divider()







#add to upload math formula img from user
st.header("File Input - Math Formula Image")

uploaded_file = st.file_uploader("Upload_formula image:",type=["jpg","png","jpeg"]) 

if uploaded_file is None:
    st.write("NO image is Uploaded!!")

if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    # Convert bytes to a NumPy array
    np_array = np.frombuffer(bytes_data, np.uint8)

    # Decode the NumPy array as a OpenCV image (BGR color space)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Save the image to a specified location
    temp_image_path="captured_image.jpg"
    cv2.imwrite(temp_image_path,image)
    
    #creating columns
    one,two =st.columns(2)

    # Display the uploaded image
    with one:
        st.image(uploaded_file, caption='Uploaded Image')
        st.write("Image saved successfully.")
    
    processed_image, text = main.extract_text(temp_image_path)
    with two:
        st.image(uploaded_file, caption='Processed Image')
        st.write("Image Processed.")
    letx = main.image_formula_to_text(uploaded_file)
    st.subheader("Extracted Formula:")
    st.latex(letx)
    latex_content = f"""
        \\documentclass{{article}}
        \\usepackage{{amsmath}}

        \\title{{Maths Formula}}
        \\author{{Rajnish Singh}}

        \\begin{{document}}

        \\maketitle

        Editable Math Formula:

        \\[
        {letx}
        \\]

        \\end{{document}}
            """
    main.create_Latex_File(latex_content)
    main.latex_to_docx('sampleLatTexFile.tex','latexFile_doc.docx')
    doc_text = main.copy_docx()
    res = LatexNodes2Text().latex_to_text(latex_content)
    st.download_button("Download Text File", res, file_name="latexFile.txt", mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    st.download_button("Download Latex Code", main.get_docx(letx), file_name="latexFile.txt", mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    st.download_button("Download docx File", main.get_docx(res), file_name="latexFile_doc.docx", mime="docx")  

st.divider()



#add to upload Tabular Data img from user
st.header("File Input - Tabular Data Image")

uploaded_file = st.file_uploader("Upload_tabular image:",type=["jpg","png","jpeg"]) 

if uploaded_file is None:
    st.write("NO image is Uploaded!!")

if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    # Convert bytes to a NumPy array
    np_array = np.frombuffer(bytes_data, np.uint8)

    # Decode the NumPy array as a OpenCV image (BGR color space)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Save the image to a specified location
    temp_image_path="captured_image.jpg"
    cv2.imwrite(temp_image_path,image)
    
    #creating columns
    one,two =st.columns(2)

    # Display the uploaded image
    with one:
        st.image(uploaded_file, caption='Uploaded Image')
        st.write("Image saved successfully.")
    
    processed_image, text = main.extract_text(temp_image_path)
    with two:
        st.image(processed_image, caption='Processed Image')
        st.write("Image Processed.")
    
    st.subheader("Extracted Table:")
    # st.code(text)
    table_data = main.img_to_excel(processed_image)
    st.table(table_data)
    csv_data = table_data.to_csv(index=False).encode("utf-8")
    st.download_button("Download text File", csv_data, file_name="newfile.txt", mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)   
    st.download_button("Download Excel File", csv_data, file_name="newExcelFile_excel.csv", mime="text/csv")
st.divider()





st.write("Made with 🧠 and 🍯 by IDOC teams 🐝")
