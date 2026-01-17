from dotenv import load_dotenv
from crew import stock_crew
import streamlit as st
import html

load_dotenv()

# Custom CSS for better styling
st.set_page_config(
    page_title="Stock Analysis Agent",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 1px;
    }
    .input-section {
        background: transparent;
        padding: 2rem 2rem 1rem 2rem;
        border-radius: 12px;
        margin: 0 auto 2rem auto;
        max-width: 600px;
        box-shadow: none;
        text-align: center;
        border: none;
    }
    .output-section {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #d1d5db;
        min-height: 300px;
        margin: 0 auto;
        max-width: 900px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.06);
        display: block;
    }
    .output-wrapper {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 0 auto;
    }
    .stTextInput>div>div>input {
        text-align: center;
        border: 1px solid #d1d5db;
        border-radius: 6px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #b8860b;
        box-shadow: 0 0 0 3px rgba(184, 134, 11, 0.1);
    }
    .stButton>button {
        width: 100%;
        max-width: 300px;
        margin: 0 auto;
        display: block;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #f5f5dc;
        font-weight: 600;
        padding: 0.875rem 2rem;
        border-radius: 8px;
        border: none;
        font-size: 1.1rem;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(26, 26, 46, 0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(26, 26, 46, 0.3);
        color: #ffd700;
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        background: linear-gradient(to bottom, #fafafa 0%, #ffffff 100%);
    }
    h3 {
        color: #1a1a2e;
        font-weight: 600;
    }
    h4 {
        color: #16213e;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

def run(stock: str):
    """Run the stock analysis crew"""
    with st.spinner("🤖 Analyzing stock with AI crew... This may take a moment."):
        result = stock_crew.kickoff(inputs={"stock": stock})
    return result

if __name__ == "__main__":
    # Main container for centering
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">Stock Analysis </h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #4a5568; font-size: 1.2rem; margin-bottom: 1rem; font-weight: 300; letter-spacing: 0.5px;">AI-Powered Multi-Agent Stock Analysis System</p>', unsafe_allow_html=True)
    
    # Input Section - Centered
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        st.markdown("### 📝 Enter Stock Symbol")
        stock = st.text_input(
            "Stock Symbol (e.g., AAPL, GOOGL, MSFT)",
            placeholder="Enter a stock ticker symbol...",
            label_visibility="collapsed"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Button to trigger analysis - Centered
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button("🚀 Analyze Stock", use_container_width=True)
    
    # Output Section - Centered
    st.markdown('<h3 style="text-align: center; margin-bottom: 1.5rem; color: #1a1a2e; font-weight: 600;">📊 Analysis Results</h3>', unsafe_allow_html=True)
    
    # Build output content
    output_content = ""
    if analyze_button:
        if stock and stock.strip():
            result = run(stock.strip().upper())
            # Get the result text
            result_text = str(result.raw) if hasattr(result, 'raw') else str(result)
            # Escape HTML special characters
            result_text = html.escape(result_text)
            # Build the output HTML
            output_content = f"""
            <div class="output-section">
                <hr style="border: 1px solid #d1d5db; margin: 1rem 0;">
                <h4 style="text-align: center; color: #16213e;">Analysis Output:</h4>
                <p style="text-align: center; color: #4a5568;"><strong style="color: #1a1a2e;">Stock Analyzed:</strong> <span style="color: #0f3460; font-weight: 600;">{stock.strip().upper()}</span></p>
                <hr style="border: 1px solid #d1d5db; margin: 1rem 0;">
                <div style="background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%); padding: 1.5rem; border-radius: 8px; white-space: pre-wrap; font-family: 'Segoe UI', monospace; line-height: 1.6; text-align: left; border: 1px solid #d1d5db; color: #2d3748;">
{result_text}
                </div>
            </div>
            """
        else:
            output_content = """
            <div class="output-section">
                <div style="padding: 2rem; text-align: center;">
                    <p style="color: #b8860b; font-size: 1.1rem; font-weight: 500;">⚠️ Please enter a stock symbol to analyze.</p>
                </div>
            </div>
            """
    else:
        output_content = """
        <div class="output-section">
            <div style="padding: 2rem; text-align: center; color: #4a5568;">
                <p style="font-size: 1.1rem; font-weight: 300;">👆 Enter a stock symbol above and click 'Analyze Stock' to see results here.</p>
            </div>
        </div>
        """
    
    # Display the output - Centered
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(output_content, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)



