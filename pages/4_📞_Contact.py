import streamlit as st

# Set up Streamlit page configuration for Contact page
st.set_page_config(
    page_title="Contact Us",
    page_icon="📞",
    layout="wide",
)

# Contact Page Header
st.title("✉️Contact Us")
st.subheader("We'd love to hear from you!")

# Contact Form Section
contact_form = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .form-container {
            padding: 20px;
            border-radius: 8px;
            width: 100%;
            border: 1px solid gray;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 7px;
            box-sizing: border-box;
            background-color: rgb(38 39 48);
            outline: none;
            border: none;
            font-size: 16px;
        }
        textarea {
            height: 150px;
            resize: vertical;
        }
        .contact-btn {
            background-color: rgb(19 23 32);
            color: #fff;
            border: 1px solid gray;
            padding: 4px;
            border-radius: 7px;
            cursor: pointer;
            font-size: 16px;
            width: 5rem;
        }
        .contact-btn:hover {
            color: #ef4040;
            border: 1px solid #ef4040;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <form action="https://formsubmit.co/shivaaaaaa07@gmail.com" method="POST">
        <label>Enter your Name:</label>
            <input type="text" name="name" placeholder="Enter your Name" required>
                    <label>Enter your Email:</label>
            <input type="email" name="email" placeholder="Enter your Email" required>
                    <label>Enter Message:</label>
            <textarea name="message" placeholder="Enter your message"></textarea>
            <button class="contact-btn" type="submit">Send</button>
        </form>
    </div>
</body>
</html>

"""

st.markdown(contact_form, unsafe_allow_html=True)

# Contact Information Section
# st.write(
#     """
#     ### Reach Out to Us
#     If you have any questions or require further assistance, you can contact us through the following channels:

#     **Email:** support@personalizedfarmingplans.com  
#     **Phone:** +123-456-7890  
#     **Address:**  
#     Personalized Farming Plans  
#     123 Farm Lane  
#     Agriculture City, AG 12345  
#     Country

#     **Follow Us:**  
#     - [Facebook](https://facebook.com/yourpage)
#     - [Twitter](https://twitter.com/yourhandle)
#     - [LinkedIn](https://linkedin.com/company/yourcompany)

#     We look forward to connecting with you!
#     """
# )

