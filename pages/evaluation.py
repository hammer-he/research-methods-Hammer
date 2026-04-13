import streamlit as st

def show():
    st.markdown('<div class="main-header">✅ 评估框架</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">用四维效度框架系统评估任意实验研究</div>', unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["四维效度框架", "快速评估清单"])

    with tab1:
        dimensions = [
            {
                "icon": "🔒",
                "title": "内部效度（Internal Validity）",
                "question": "实验结论是否真实反映了变量间的因果关系？",
                "threats": [
                    ("选择偏差 Selection Bias", "两组被试本来就不等价"),
                    ("历史效应 History", "实验期间发生了外部事件影响结果"),
                    ("成熟效应 Maturation", "被试随时间自然变化"),
                    ("混淆变量 Confounds", "未被控制的第三变量"),
                ],
                "tips": "是否有对照组？是否随机分配？是否有 manipulation check？"
            },
            {
                "icon": "🌍",
                "title": "外部效度（External Validity）",
                "question": "结论能否推广到其他人群、情境、时间？",
                "threats": [
                    ("WEIRD问题", "样本过于西方化、受教育、富裕"),
                    ("生态效度 Ecological Validity", "实验室设置过于人工化"),
                    ("霍桑效应 Hawthorne Effect", "被试因为被观察而改变行为"),
                ],
                "tips": "样本是否有代表性？任务是否贴近真实场景？"
            },
            {
                "icon": "📊",
                "title": "统计结论效度（Statistical Conclusion Validity）",
                "question": "统计分析是否正确且充分？",
                "threats": [
                    ("样本量不足 Low Power", "无法检测到真实效应"),
                    ("P-hacking", "多次分析直到 p < 0.05"),
                    ("多重比较 Multiple Comparisons", "比较越多，假阳性越多"),
                    ("未报告 Effect Size", "只有 p 值不够"),
                ],
                "tips": "是否报告了 effect size？样本量是否经过 power analysis？"
            },
            {
                "icon": "🧩",
                "title": "构念效度（Construct Validity）",
                "question": "测量工具是否真正测到了目标构念？",
                "threats": [
                    ("操作化不当", "因变量测量与理论构念不符"),
                    ("需求特征 Demand Characteristics", "被试猜到假设并改变行为"),
                    ("实验者偏差 Experimenter Bias", "主试无意影响结果"),
                ],
                "tips": "测量工具的信度和效度是否被验证过？"
            },
        ]

        for d in dimensions:
            with st.expander(f"{d['icon']} {d['title']}", expanded=False):
                st.markdown(f"**核心问题**：{d['question']}")
                st.markdown("**常见威胁**：")
                for threat, desc in d["threats"]:
                    st.markdown(f"- **{threat}**：{desc}")
                st.markdown(f"""
                <div class="highlight-box">
                    💡 <b>评估时问自己</b>：{d['tips']}
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        st.markdown("### 📋 快速评估清单")
        st.markdown("用这个清单快速扫描一篇实验论文：")

        checks = [
            ("假设", "研究假设是否清晰且可证伪？"),
            ("自变量", "自变量操控是否干净？是否有 manipulation check？"),
            ("因变量", "因变量测量是否有信度和效度支持？"),
            ("对照组", "是否有合适的对照组？"),
            ("随机化", "被试是否被随机分配到各组？"),
            ("样本量", "样本量是否经过 power analysis？"),
            ("统计方法", "统计方法选择是否正确？"),
            ("Effect Size", "是否报告了效应量？"),
            ("外部效度", "样本是否有代表性？结论是否过度推广？"),
            ("混淆变量", "是否讨论了潜在混淆变量？"),
        ]

        for i, (category, question) in enumerate(checks):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"**{category}**")
            with col2:
                st.checkbox(question, key=f"check_{i}")
