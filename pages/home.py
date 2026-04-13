import streamlit as st

def show():
    # Hero
    st.markdown('<div class="main-header">科研方法指南</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Laboratory Experimentation · 从设计到评估的完整学习路径</div>', unsafe_allow_html=True)

    st.markdown("")

    # Quick tags
    tags = ["实验设计", "变量控制", "假设检验", "ANOVA", "ANCOVA", "效度与信度", "统计功效", "样本量"]
    st.markdown(" ".join([f'<span class="tag">{t}</span>' for t in tags]), unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Feature cards
    st.markdown("### 📚 模块概览")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">📐 实验设计</div>
            <p style="color:#4a6580;font-size:0.92rem;margin:0">
                学习如何提出清晰假设、识别变量类型、
                选择 between/within-subjects 设计，以及控制混淆变量。
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">✅ 评估框架</div>
            <p style="color:#4a6580;font-size:0.92rem;margin:0">
                使用内部效度、外部效度、统计结论效度、构念效度四维框架，
                系统评估任意一篇实验研究。
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">📊 统计方法</div>
            <p style="color:#4a6580;font-size:0.92rem;margin:0">
                覆盖 t-test、ANOVA、ANCOVA、相关分析等常用方法，
                附带使用场景对比与选择指南。
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">🧪 练习中心</div>
            <p style="color:#4a6580;font-size:0.92rem;margin:0">
                获取随机练习题目，自主设计实验方案，
                并对照评分标准进行自我评估。
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Highlight tip
    st.markdown("""
    <div class="highlight-box">
        <strong>💡 如何使用本网站</strong><br>
        建议按照 <b>实验设计 → 统计方法 → 评估框架 → 练习中心</b> 的顺序学习，
        或直接跳转到你需要复习的模块。
    </div>
    """, unsafe_allow_html=True)
