import streamlit as st

st.set_page_config(
    page_title="科研方法指南",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans SC', sans-serif; }
section[data-testid="stSidebar"] { background: #0f1923; border-right: 1px solid #1e3a5f; }
section[data-testid="stSidebar"] * { color: #e8f4f8 !important; }
.main-header { font-family: 'Noto Serif SC', serif; font-size: 2.6rem; font-weight: 700; color: #0f1923; letter-spacing: -0.5px; line-height: 1.2; }
.sub-header { font-size: 1.1rem; color: #4a6580; margin-top: 0.4rem; font-weight: 300; }
.tag { display: inline-block; background: #e8f4f8; color: #1e5f8a; border-radius: 4px; padding: 3px 10px; font-size: 0.78rem; font-weight: 500; margin: 2px; }
.card { background: white; border: 1px solid #e4edf5; border-radius: 12px; padding: 1.4rem 1.6rem; margin-bottom: 1rem; transition: box-shadow 0.2s; }
.card:hover { box-shadow: 0 4px 20px rgba(30, 95, 138, 0.1); }
.card-title { font-family: 'Noto Serif SC', serif; font-size: 1.15rem; font-weight: 600; color: #0f1923; margin-bottom: 0.4rem; }
.divider { border: none; border-top: 2px solid #e4edf5; margin: 1.5rem 0; }
.highlight-box { background: linear-gradient(135deg, #e8f4f8 0%, #f0f7ff 100%); border-left: 4px solid #1e5f8a; border-radius: 0 8px 8px 0; padding: 1rem 1.4rem; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔬 科研方法指南")
    st.markdown("---")
    page = st.radio(
        "导航",
        options=[
            "🏠 首页",
            "📐 实验设计",
            "📊 统计方法",
            "✅ 评估框架",
            "🧪 练习中心",
        ],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown(
        "<small style='color:#6b8fa8'>适合本科生 / 研究生<br>Laboratory Experimentation</small>",
        unsafe_allow_html=True
    )

if page == "🏠 首页":
    from pages.home import show
    show()
elif page == "📐 实验设计":
    from pages.experiment_design import show
    show()
elif page == "📊 统计方法":
    from pages.statistics import show
    show()
elif page == "✅ 评估框架":
    from pages.evaluation import show
    show()
elif page == "🧪 练习中心":
    from pages.practice import show
    show()
