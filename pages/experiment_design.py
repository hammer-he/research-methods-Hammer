import streamlit as st

def show():
    st.markdown('<div class="main-header">📐 实验设计</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">如何设计一个严谨、有效的实验</div>', unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["假设与变量", "设计类型", "随机化与盲法", "样本量"])

    with tab1:
        st.markdown("### 🎯 假设的构成")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
                <div class="card-title">H₀ 零假设（Null Hypothesis）</div>
                <p style="color:#4a6580;font-size:0.92rem">
                变量之间没有关系或没有差异。<br><br>
                例：<em>睡眠时间与记忆力测试得分无关。</em>
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
                <div class="card-title">H₁ 备择假设（Alternative Hypothesis）</div>
                <p style="color:#4a6580;font-size:0.92rem">
                变量之间存在关系或差异。<br><br>
                例：<em>睡眠时间越长，记忆力测试得分越高。</em>
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 🔧 变量类型")
        data = {
            "变量类型": ["自变量 (IV)", "因变量 (DV)", "控制变量", "混淆变量"],
            "定义": ["研究者主动操控的变量", "研究者测量的结果变量", "保持不变以排除干扰", "未被控制、可能影响结果的变量"],
            "睡眠实验示例": ["睡眠时长（充足 vs 不足）", "记忆力测试分数（0-20）", "年龄、测试时间、房间环境", "咖啡因摄入、学习习惯"],
        }
        st.table(data)

        st.markdown("""
        <div class="highlight-box">
            <b>控制变量的三种处理方式</b><br>
            1. <b>招募时筛选</b>：只招18-25岁、无睡眠障碍的被试<br>
            2. <b>实验中控制</b>：所有人在同一时间、同一地点参加测试<br>
            3. <b>统计上控制</b>：将变量作为协变量（covariate）放入 ANCOVA
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("### 🔀 Between-subjects vs Within-subjects")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
                <div class="card-title">Between-subjects（组间设计）</div>
                <p style="color:#4a6580;font-size:0.92rem">
                每个被试只接受<b>一种</b>实验条件。<br><br>
                ✅ 避免 carry-over effect<br>
                ✅ 无顺序效应<br>
                ❌ 需要更多被试<br>
                ❌ 个体差异是噪音来源<br><br>
                <b>统计方法</b>：Independent t-test / ANOVA
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
                <div class="card-title">Within-subjects（组内设计）</div>
                <p style="color:#4a6580;font-size:0.92rem">
                同一被试接受<b>所有</b>实验条件。<br><br>
                ✅ 样本量需求小<br>
                ✅ 控制个体差异<br>
                ❌ 存在练习/疲劳效应<br>
                ❌ 可能有 carry-over effect<br><br>
                <b>统计方法</b>：Paired t-test / Repeated measures ANOVA
                </p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("### 🎲 随机化")
        st.markdown("""
        随机化的目的是消除**系统性偏差**，确保两组被试在实验前是等价的。

        - **随机分配（Random Assignment）**：将被试随机分到各组
        - **随机化刺激顺序**：避免呈现顺序本身影响结果
        - **随机化 ≠ 随便选**：必须使用随机数工具（如 Python `random` 库）
        """)

        st.markdown("### 🕶️ 盲法（Blinding）")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Single-blind**\n\n被试不知道自己属于哪组，但主试知道。\n\n→ 减少 demand characteristics")
        with col2:
            st.info("**Double-blind**\n\n被试和主试都不知道分组情况。\n\n→ 同时减少 experimenter bias")

    with tab4:
        st.markdown("### 📏 样本量计算")
        st.markdown("""
        样本量不是越多越好，而是**刚好够**检测到真实效应。
        使用 **Power Analysis** 来决定：
        """)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Effect Size (d)", "0.5", "medium")
        col2.metric("Power (1-β)", "0.80", "standard")
        col3.metric("α (significance)", "0.05", "standard")
        col4.metric("每组人数", "~52人", "t-test")

        st.markdown("""
        <div class="highlight-box">
            <b>推荐工具</b>：G*Power（免费桌面软件），可计算各类统计检验所需样本量
        </div>
        """, unsafe_allow_html=True)
              
