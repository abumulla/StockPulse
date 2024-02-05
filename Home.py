import streamlit as st
import streamlit as st


from PIL import Image
def app():

    st.title("Main Page")

    
    def main():
        # Set page title and icon
        st.set_page_config(
            page_title="StockPulse",
            page_icon="📈",
            layout="centered",
        )
    
        # Page layout with custom CSS
        page_bg_img = """
    <style>
        body {
            background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=chCOzZiD&id=ABE5C775C7CD6D2E8763A005EEF07E42175EE3F4&thid=OIP.chCOzZiDmL4uQux2XuOBxwHaE0&mediaurl=https%3a%2f%2fg.foolcdn.com%2feditorial%2fimages%2f542641%2fgettyimages-614223862.jpg&exph=1396&expw=2147&q=stockmarket+bg+&simid=608006179616338046&FORM=IRPRST&ck=6626E53AF0C2528B5820148CC2294656&selectedIndex=80&itb=0");
            background-size: cover;
        }
    </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
    
        # Header
        st.title("StockPulse")
        st.subheader("Elevate your investment with StockPulse")
    
        # Logo
        logo = Image.open("your_logo.png")  # Replace "your_logo.png" with the path to your logo image
        st.image(logo, use_column_width=True)
    
        # Welcome message
        st.write("Welcome to StockPulse! Analyze stock trends in real-time and make informed decisions.")
    
        # Features section
        st.markdown("### Features:")
        st.write(
            "- Real-time stock analysis of stocks.\n"
            "- Visualize future trends for selected stocks.\n"
            "- Stay updated with the latest stocks"
        )
    
        # Get Started section
        st.markdown("### Get Started:")
        stock_symbols = st.text_input("Enter stock symbols (e.g., AAPL, GOOGL, MSFT):")
        if st.button("Analyze"):
            st.success(f"Sentiment analysis for {stock_symbols} will be displayed here.")
    
        # About Us section
        st.markdown("### About Us:")
        st.write(
            "StockPulse is dedicated to providing you with valuable insights into the stock market. "
            "Our platform uses advanced ML model techniques to analyze data and generate future trends."
        )
    
        # Info section
        st.info("Note: This is a demo landing page. Actual functionality will be added in future updates.")
    
        # Stock Sentiment Trends section
        st.markdown("### Stock Trend Analyzer:")
        st.line_chart({"Positive": [0, 1, 1, 0, -1, -1, 0], "Neutral": [1, 2, 0, -1, 0, 1, 0], "Negative": [-1, -2, -1, 0, 1, 0, -1]})
    
        # Latest Stock Market Sentiments section
        st.markdown("### Latest Stock Market Sentiments:")
        st.table({"Stock": ["AAPL", "GOOGL", "MSFT"],
                "Sentiment": ["Positive", "Neutral", "Negative"],
                "Score": [0.8, 0.2, -0.5]})
    
    if __name__ == "__main__":
        main()
import streamlit as st

import yfinance as yf

import datetime
 
def app():
    st.title('StockPulse - Stock Market Analysis')

    st.markdown(

        "Welcome to StockPulse - Your Stock Market Analysis App! "

        "Enter a stock symbol in the sidebar to get started."

    )
    
    # Sidebar for user input

    symbol = st.sidebar.text_input('Enter Stock Symbol', value='AAPL')
    
    # Display stock information

    if st.sidebar.button('Get Stock Info'):

        if symbol:

            st.write(f"Displaying information for stock symbol: {symbol}")
    
            # Fetching stock data using yfinance

            stock_data = yf.Ticker(symbol)

            today = datetime.date.today()

            one_year_ago = today - datetime.timedelta(days=365)

            df = stock_data.history(start=one_year_ago, end=today)
    
            # Displaying historical stock data

            st.subheader(f"{symbol} Stock Data")

            st.write(df.head())
    
            # Line chart for stock prices

            st.subheader(f"{symbol} Stock Price Chart")

            st.line_chart(df['Close'])
    
            # More details about the company

            info = stock_data.info

            st.subheader(f"{symbol} Company Information")

            st.write(f"**Company Name:** {info['longName']}")

            st.write(f"**Market Cap:** {info['marketCap']}")

            st.write(f"**Website:** {info['website']}")

        else:

            st.warning('Please enter a stock symbol.')




# import streamlit as st

# def app():
#     st.title('Home Page')
#     st.write("Welcome to the Home Page! This is your starting point.")

# if __name__ == "__main__":
#     app()




