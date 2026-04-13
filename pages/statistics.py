import streamlit as st

def show():
    st.markdown('<div class="main-header">📊 统计方法</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">常用统计检验的选择与使用指南</div>', unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### 🗺️ 统计方法选择路径")

    st.markdown("""
    <div class="highlight-box">
        选择统计方法前，先问三个问题：<br>
        1. 你有几组？（2组 vs 3组以上）<br>
        2. 同一批人还是不同人？（within vs between）<br>
        3. 有没有需要控制的协变量？（加 ANCOVA）
    </div>
    """, unsafe_allow_html=True)

    data = {
        "情境": [
            "比较2组，不同人",
            "比较2组，同一批人",
            "比较3组以上，不同人",
            "比较3组以上，同一批人",
            "有协变量需要控制",
            "两个连续变量的关系",
        ],
        "使用方法": [
            "Independent samples t-test",
            "Paired samples t-test",
            "One-way ANOVA",
            "Repeated measures ANOVA",
            "ANCOVA",
            "Pearson / Spearman 相关分析",
        ],
        "睡眠实验示例": [
            "充足组 vs 不足组的后测分数",
            "同一批人不同睡眠条件下的表现",
            "4小时、6小时、8小时三组比较",
            "同一批人经历3种睡眠条件",
            "控制前测分数，比较各组后测",
            "睡眠时长与记忆分数的线性关系",
        ],
    }
    st.table(data)

    st.markdown("---")
    st.markdown("### 🔍 ANOVA vs ANCOVA 详解")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">ANOVA</div>
            <p style="color:#4a6580;font-size:0.92rem">
            将总变异分解为：<br>
            <code>总变异 = 组间变异 + 组内误差</code><br><br>
            问题：组内误差包含个体差异噪音，
            可能掩盖真实效应。
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">ANCOVA</div>
            <p style="color:#4a6580;font-size:0.92rem">
            将总变异分解为：<br>
            <code>总变异 = 组间变异 + 协变量 + 残差误差</code><br><br>
            优势：从误差中"切掉"协变量的影响，
            检验更精准，统计功效更高。
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📐 重要概念")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">p值</div>
            <p style="color:#4a6580;font-size:0.92rem">
            "如果H₀是真的，观察到这个结果的概率"<br><br>
            p < 0.05 → 拒绝H₀（显著）
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Effect Size</div>
            <p style="color:#4a6580;font-size:0.92rem">
            效应的实际大小，不受样本量影响<br><br>
            Cohen's d：0.2小 / 0.5中 / 0.8大
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">Statistical Power</div>
            <p style="color:#4a6580;font-size:0.92rem">
            "如果效应真实存在，被检测到的概率"<br><br>
            标准要求 ≥ 0.80
            </p>
        </div>
        """, unsafe_allow_html=True)
