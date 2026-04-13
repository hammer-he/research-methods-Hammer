import streamlit as st
import random

TOPICS = [
    {
        "title": "睡眠时长是否影响记忆力？",
        "hints": ["考虑睡眠质量作为混淆变量", "记忆力如何操作化？", "伦理问题：能强制剥夺睡眠吗？"],
        "key_concepts": ["Between-subjects", "Pre-test post-test", "ANCOVA", "Manipulation check"],
    },
    {
        "title": "听音乐是否能提高学习效率？",
        "hints": ["有歌词 vs 无歌词的音乐效果一样吗？", "学习效率如何测量？", "不同类型的学习任务结果一样吗？"],
        "key_concepts": ["控制变量", "操作化定义", "Demand characteristics", "Effect size"],
    },
    {
        "title": "运动频率是否影响焦虑水平？",
        "hints": ["焦虑如何测量？（量表？生理指标？）", "是否需要长期追踪？", "因果 vs 相关的区别"],
        "key_concepts": ["Within-subjects", "Pearson correlation", "纵向研究", "Self-report bias"],
    },
    {
        "title": "社交媒体使用时间是否与自尊心负相关？",
        "hints": ["相关 ≠ 因果", "自尊心如何测量？", "第三变量问题"],
        "key_concepts": ["相关分析", "问卷信效度", "混淆变量", "WEIRD样本"],
    },
    {
        "title": "课堂座位位置是否影响学生参与度？",
        "hints": ["参与度如何量化？", "学生是主动选座还是随机分配？", "老师的行为也是变量？"],
        "key_concepts": ["自然实验", "观察法", "选择偏差", "生态效度"],
    },
]

CHECKLIST = [
    "H₀ 和 H₁ 是否清晰且可证伪？",
    "自变量是否被明确操控？",
    "因变量是否被具体操作化？",
    "是否有对照组？",
    "是否随机分配被试？",
    "是否考虑了盲法？",
    "样本量是否足够（power analysis）？",
    "是否列出并控制了混淆变量？",
    "统计方法是否合适？",
    "是否考虑了外部效度？",
]

def show():
    st.markdown('<div class="main-header">🧪 练习中心</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">获取题目，设计实验，对照清单自我评估</div>', unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("### 🎲 选择题目")
    col1, col2 = st.columns([3, 1])

    with col1:
        if "topic_index" not in st.session_state:
            st.session_state.topic_index = 0

    with col2:
        if st.button("🎲 随机题目", use_container_width=True):
            st.session_state.topic_index = random.randint(0, len(TOPICS) - 1)
            st.rerun()

    topic = TOPICS[st.session_state.topic_index]

    st.markdown(f"""
    <div class="card">
        <div class="card-title" style="font-size:1.3rem">❓ {topic['title']}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**💡 思考提示**")
        for h in topic["hints"]:
            st.markdown(f"- {h}")
    with col2:
        st.markdown("**🔑 涉及核心概念**")
        for c in topic["key_concepts"]:
            st.markdown(f'<span class="tag">{c}</span>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### ✍️ 你的实验设计")

    col1, col2 = st.columns(2)
    with col1:
        st.text_area("H₀（零假设）", placeholder="例：X与Y之间没有显著关系", key="h0", height=80)
        st.text_area("自变量（IV）", placeholder="例：睡眠时长（充足 vs 不足）", key="iv", height=80)
        st.text_area("控制变量及处理方式", placeholder="例：年龄（筛选），咖啡因（实验当天控制）", key="cv", height=80)
        st.selectbox("设计类型", ["Between-subjects", "Within-subjects", "Mixed design"])
    with col2:
        st.text_area("H₁（备择假设）", placeholder="例：X会导致Y显著增加", key="h1", height=80)
        st.text_area("因变量（DV）及测量方式", placeholder="例：词表回忆任务，正确回忆词数（0-20）", key="dv", height=80)
        st.text_area("潜在混淆变量及应对", placeholder="例：睡眠质量 → 加入PSQI量表作为协变量", key="confounds", height=80)
        st.selectbox("统计方法", ["Independent t-test", "Paired t-test", "ANOVA", "ANCOVA", "Repeated measures ANOVA", "Pearson correlation"])

    st.markdown("---")

    st.markdown("### ✅ 自我评估清单")
    st.markdown("完成设计后，对照以下清单检查你的方案：")

    score = 0
    for i, item in enumerate(CHECKLIST):
        if st.checkbox(item, key=f"practice_check_{i}"):
            score += 1

    pct = int(score / len(CHECKLIST) * 100)
    color = "#2ecc71" if pct >= 80 else "#f39c12" if pct >= 50 else "#e74c3c"
    label = "优秀 🎉" if pct >= 80 else "良好，继续完善 💪" if pct >= 50 else "还需加油 📚"

    st.markdown(f"""
    <div class="card" style="text-align:center;border-color:{color}">
        <div style="font-size:2.5rem;font-weight:700;color:{color}">{pct}%</div>
        <div style="color:#4a6580">{score} / {len(CHECKLIST)} 项 · {label}</div>
    </div>
    """, unsafe_allow_html=True)
