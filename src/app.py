import streamlit as st
from ocr.processor import extract_text_from_image
from ai.analyzer import analyze_text
import pandas as pd
import io
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Document Analyzer",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.image("https://your-logo-url.png", width=100)  # Add your logo
    st.title("Settings")
    
    # Language selection
    language = st.selectbox(
        "OCR Language",
        ["English", "Spanish", "French", "German"],
        index=0
    )
    
    # Document type filter
    doc_type = st.selectbox(
        "Document Type",
        ["All", "Invoice", "Receipt", "Letter"],
        index=0
    )
    
    # Confidence threshold
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        help="Minimum confidence score for extracted information"
    )

# Main content
st.title("📄 AI Document Analyzer")
st.markdown("---")

# File upload section
col1, col2 = st.columns([2, 1])
with col1:
    uploaded_file = st.file_uploader(
        "Upload your document",
        type=["jpg", "jpeg", "png", "pdf"],
        help="Supported formats: JPG, JPEG, PNG, PDF"
    )

with col2:
    st.info("📌 **Supported Features**\n"
            "- Text Extraction (OCR)\n"
            "- Document Classification\n"
            "- Data Structuring\n"
            "- Multi-language Support")

if uploaded_file is not None:
    # Processing section
    with st.spinner('Processing document...'):
        # Extract text
        extracted_text = extract_text_from_image(uploaded_file)
        
        # Analyze text
        analysis_results = analyze_text(extracted_text)
        
        # Display results in tabs
        tab1, tab2, tab3 = st.tabs(["📝 Extracted Text", "📊 Analysis Results", "📈 Summary"])
        
        with tab1:
            st.text_area("Raw Extracted Text", extracted_text, height=300)
            
        with tab2:
            # Display structured results in columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Document Information")
                st.write(f"**Type:** {analysis_results.get('document_type', 'Unknown')}")
                st.write(f"**Date:** {analysis_results.get('date', 'Not found')}")
                st.write(f"**Reference:** {analysis_results.get('reference', 'Not found')}")
                
            with col2:
                st.subheader("Financial Information")
                st.write(f"**Total Amount:** {analysis_results.get('total_amount', 'Not found')}")
                st.write(f"**Currency:** {analysis_results.get('currency', 'Not found')}")
                st.write(f"**Tax Amount:** {analysis_results.get('tax_amount', 'Not found')}")
        
        with tab3:
            st.subheader("Document Summary")
            # Add any additional analytics or summaries here
            st.write("Document processed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            # Add a simple visualization if needed
            if 'confidence_scores' in analysis_results:
                st.bar_chart(analysis_results['confidence_scores'])

        # Export options
        st.markdown("---")
        st.subheader("Export Options")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Download as CSV"):
                df = pd.DataFrame([analysis_results])
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Click to Download CSV",
                    data=csv,
                    file_name=f"document_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        with col2:
            if st.button("📊 Download as Excel"):
                df = pd.DataFrame([analysis_results])
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                st.download_button(
                    label="Click to Download Excel",
                    data=buffer.getvalue(),
                    file_name=f"document_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        with col3:
            if st.button("📋 Copy to Clipboard"):
                st.write("Results copied to clipboard!")
                # Add clipboard functionality here

else:
    # Display welcome message and instructions when no file is uploaded
    st.info("👋 Welcome! Please upload a document to begin analysis.")
    
    # Sample results or demo
    with st.expander("See Demo"):
        st.write("Here's how the analysis will look:")
        st.image("https://your-demo-image-url.png", caption="Sample Analysis")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Developed with ❤️ | <a href="https://github.com/yourusername">GitHub</a> | <a href="#">Documentation</a></p>
    </div>
    """,
    unsafe_allow_html=True
)