import streamlit as st

st.set_page_config(
    page_title="科研主页 | Research Portfolio",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ══════════════════════════════════════════════════════════════
#  BILINGUAL CONTENT DICTIONARY
#  规则：中文版是主版本，英文版针对国际读者重新撰写（非直译）
# ══════════════════════════════════════════════════════════════
TEXTS = {
    "zh": {
        # ── Sidebar ──
        "nav_home":       "🏠  首页",
        "nav_research":   "📋  科研经历",
        "nav_knowledge":  "📚  知识分享",
        "nav_contact":    "📬  联系我",
        "sidebar_interests_title": "研究方向",
        "sidebar_interests": [
            "运动表现分析",
            "体育教育",
        ],
        # ── Home ──
        "hero_name":     "何晨苗",
        "hero_subtitle": "体育科学研究者 · 运动表现分析 · 体育教育",
        "hero_tagline":  (
            "专注于运动表现的量化分析与循证研究。"
            "研究方向横跨运动生物力学、健康行为干预与体育教育，"
            "致力于将严谨的科研方法应用于体育实践。"
        ),
        "badges": ["🥊 格斗运动技术分析", "📊 Meta分析", "🎓 体育教师教育", "🧠 运动与健康行为"],
        "stat_conf_label":    "国际会议\n学术报告",
        "stat_meta_label":    "Meta分析\n（进行中）",
        "stat_review_label":  "系统综述\n（进行中）",
        "stat_years_label":   "年科研\n经历",
        "home_what_title":   "本页内容",
        "home_card1_tag":    "科研经历",
        "home_card1_title":  "📋 我的研究工作",
        "home_card1_body":   "包括国际会议报告、正在推进的Meta分析与系统综述项目——呈现研究背景、方法选择与核心贡献。",
        "home_card2_tag":    "知识分享",
        "home_card2_title":  "📚 研究方法笔记",
        "home_card2_body":   "基于亲身实践的系统综述流程、Meta分析方法、运动数据可视化等内容，供同学和同行参考。",
        "home_focus_title":  "当前项目",
        "home_focus_tag":    "进行中 · 团队项目",
        "home_focus_title2": "🔄 Meta分析：运动锻炼对电子产品成瘾的干预效果",
        "home_focus_body":   (
            "与研究团队合作，系统考察身体锻炼干预对电子产品成瘾行为（手机成瘾、网络成瘾、游戏障碍）的影响效果。"
            "研究严格遵循 PRISMA 2020 指南，检索数据库包括 PubMed、Web of Science、Embase 及中国知网（CNKI）。"
            "计划采用随机效应模型合并效应量（Hedges' g），并进行亚组分析与发表偏倚评估。"
        ),
        "home_focus_meta":  "📍 当前阶段：数据提取与质量评估 &nbsp;|&nbsp; 👥 团队协作项目",
        # ── Research ──
        "research_title":   "科研经历",
        "research_intro":   "记录我在体育科学与体育教育领域的学术报告、合作项目与独立研究经历。",
        "conf_section":     "🎤 国际会议报告",
        "conf1_tag":   "国际学术会议",
        "conf1_title": "拳击技术动作发展序列构建",
        "conf1_body":  (
            "在 <b>中国体育与运动健康学会（CSPAH）年会</b> 进行学术报告。"
            "本研究探讨拳击技术动作的进阶结构，提出面向青少年与竞技运动员的动作发展序列框架，"
            "融合动作分析与教学序列化理论，为拳击技能习得提供理论依据。"
        ),
        "conf1_meta":  "🏛 CSPAH 年会 &nbsp;|&nbsp; 📌 运动生物力学 · 训练科学",
        "conf2_tag":   "国际学术会议",
        "conf2_title": "新入职女性体育教师的职业困境",
        "conf2_body":  (
            "在 <b>哈佛国际教育论坛</b> 进行报告。"
            "本研究采用质性研究方法，考察新入职女性体育教师在职业认同、角色冲突与制度性障碍等方面面临的挑战，"
            "研究发现为建立性别敏感的入职支持机制与导师制提供了依据。"
        ),
        "conf2_meta":  "🏛 哈佛国际教育论坛 &nbsp;|&nbsp; 📌 体育教育 · 性别与教育",
        "ongoing_section": "🔄 进行中的研究项目",
        "proj1_tag":   "进行中 · 团队项目",
        "proj1_title": "Meta分析：运动锻炼对电子产品成瘾的干预效果",
        "proj1_body":  (
            "系统回顾并量化分析身体锻炼干预对电子产品成瘾的影响，遵循 <b>PRISMA 2020</b> 规范。"
            "检索范围覆盖 PubMed、Web of Science、Embase、CNKI 等数据库，"
            "计划通过随机效应模型合并效应量，并按运动类型、干预时长等变量进行亚组分析，同时评估发表偏倚。"
        ),
        "proj1_meta":  "👥 团队协作 &nbsp;|&nbsp; 🧰 R（meta包）、RevMan、Rayyan &nbsp;|&nbsp; 📍 数据提取与质量评估阶段",
        "proj2_tag":   "进行中 · 独立项目",
        "proj2_title": "系统综述：题目待定",
        "proj2_body":  (
            "独立开展的系统综述项目，目前处于研究方案设计阶段。"
            "研究将遵循 PRISMA 规范，聚焦体育科学或体育教育领域的特定问题，"
            "方案确定后计划在 PROSPERO 进行预注册。"
        ),
        "proj2_meta":  "👤 独立项目 &nbsp;|&nbsp; 📍 方案设计阶段",
        "skills_section": "🛠 研究方法与工具",
        "skill1_tag":  "综述方法",
        "skill1_body": "系统综述 · Meta分析 · PRISMA 2020 · 偏倚风险评估（RoB 2）· GRADE",
        "skill2_tag":  "数据与统计",
        "skill2_body": "R（meta、metafor）· Python · Streamlit · 效应量计算 · 森林图绘制",
        "skill3_tag":  "文献管理",
        "skill3_body": "PubMed · Web of Science · 中国知网 · Rayyan · Zotero · Covidence",
        # ── Knowledge Hub ──
        "knowledge_title": "知识分享",
        "knowledge_intro": "基于自身科研实践整理的方法笔记，涵盖系统综述流程、Meta分析核心概念与运动数据分析方法，供同行与同学参考。",
        "tab_methods": "📋 研究方法论",
        "tab_data":    "📊 数据分析与可视化",
        "k1_title": "📖 如何做一篇系统综述：从零到提交的完整流程",
        "k1_body": """
系统综述是对特定研究问题现有证据的严格综合，以下是我基于 <b>PRISMA 2020</b> 框架整理的操作流程：
<ul>
    <li><b>第一步 — 构建 PICO 问题：</b>在检索前明确定义 Population（人群）、Intervention（干预）、Comparator（对照）、Outcome（结局），这是整篇综述的锚点。</li>
    <li><b>第二步 — 在 PROSPERO 预注册：</b>公开提交你的综述方案，避免重复劳动，也体现研究透明度——投稿时编辑会看这个。</li>
    <li><b>第三步 — 制定检索策略：</b>用布尔逻辑（AND/OR）组合检索词，至少覆盖 3 个数据库；涉及中文文献务必纳入中国知网（CNKI）。</li>
    <li><b>第四步 — 使用 Rayyan 或 Covidence 筛文献：</b>先进行题目/摘要筛选，再全文筛选；须有两名独立评审，计算一致性（Cohen's κ）。</li>
    <li><b>第五步 — 标准化提取数据：</b>使用统一的提取表（研究设计、样本量、干预措施、结局指标、效应量），宁可提取多，不要漏。</li>
    <li><b>第六步 — 偏倚风险评估：</b>RCT 用 RoB 2，观察性研究用 Newcastle-Ottawa 量表（NOS）。</li>
    <li><b>第七步 — 结果综合：</b>研究异质性高时做叙述性综合；条件允许时进行 Meta 分析合并效应量。</li>
</ul>
<b>实践经验：</b>把最多时间花在检索策略上。检索词漏了就是漏了，后期无法弥补——这是整篇综述的地基。
        """,
        "k2_title": "📐 Meta分析核心概念：效应量与异质性",
        "k2_body": """
Meta 分析通过统计方法合并多项研究结果，以下是最需要理解的几个概念：
<ul>
    <li><b>效应量选择：</b>小样本优先用 <i>Hedges' g</i>（比 Cohen's d 更稳健）；二分类结局用对数比值比（log OR）；关系研究用相关系数 r。</li>
    <li><b>固定效应 vs. 随机效应模型：</b>体育科学研究几乎都应选 <b>随机效应模型</b>——不同研究的人群、干预方案和环境各不相同。</li>
    <li><b>异质性（I²）：</b>I² &gt; 75% 表示高异质性——此时应进行亚组分析或 Meta 回归，探索异质性来源（如运动类型、年龄、干预时长）。</li>
    <li><b>发表偏倚：</b>检查漏斗图不对称性；进行 Egger 检验或剪补法（trim-and-fill）校正。</li>
    <li><b>森林图怎么看：</b>每行代表一项研究，最底部菱形是合并估计值，菱形越宽表示不确定性越大。</li>
</ul>
<b>常用工具：</b>R 的 <code>meta</code> 和 <code>metafor</code> 包用于分析；RevMan 5 用于生成符合发表要求的森林图。
        """,
        "k3_title": "🗂 文献检索策略：怎么搜才不漏",
        "k3_body": """
可重复、全面的检索策略是证据综合的基石，以下是实操要点：
<ul>
    <li><b>按三类拆分检索词：</b>人群词 AND 干预词 AND 结局词——类别之间用 AND，类别内部用 OR。</li>
    <li><b>PubMed 要同时用 MeSH 词和自由词：</b>例如同时检索 "Exercise Therapy"[MeSH] OR "physical activity"，避免漏掉不同标引方式的文献。</li>
    <li><b>不要忽视灰色文献：</b>世卫组织报告、政府文件、ProQuest 学位论文库——有助于降低发表偏倚。</li>
    <li><b>体育科学研究必检 CNKI：</b>大量相关研究只发表在中文期刊，忽略中文文献会严重影响综述完整性。</li>
    <li><b>记录每一步：</b>保存带日期的完整检索式——这直接对应 PRISMA 流程图和方法部分的撰写。</li>
</ul>
        """,
        "k4_title": "📈 运动表现数据可视化：从哪里开始",
        "k4_body": """
好的可视化能揭示原始数字掩盖的规律，以下是我的常用工具组合：
<ul>
    <li><b>Python + Plotly：</b>交互式图表首选，适合展示逐场比赛趋势、训练负荷曲线或运动员横向比较。Plotly Express 上手很快。</li>
    <li><b>Streamlit：</b>几小时内把分析成果部署为可分享的网页应用，不需要前端开发经验，教练组直接在浏览器里看数据。</li>
    <li><b>R + ggplot2：</b>发表级静态图表，主题可高度定制，用 <code>theme_minimal()</code> 可以直接出图。</li>
    <li><b>体育科学常用图表类型：</b>
        <ul>
            <li>折线图 — 训练负荷、恢复趋势</li>
            <li>雷达图 — 运动员多维能力画像</li>
            <li>散点图 + 回归线 — 两个表现变量的关系</li>
            <li>箱线图 — 实验组 vs. 对照组比较</li>
            <li>热力图 — 格斗运动攻击区域频率分布</li>
        </ul>
    </li>
</ul>
        """,
        "k5_title": "🥊 格斗运动技术数据分析：我的实践经验",
        "k5_body": """
基于拳击动作发展序列研究，整理出以下格斗运动技术数据分析的实践要点：
<ul>
    <li><b>技术动作编码：</b>先建立清晰的技术分类体系（如：刺拳、直拳、勾拳、防守动作），再开始编码。可用人工录像编码或自动姿态估计（MediaPipe、OpenPose）。</li>
    <li><b>序列分析：</b>用转移矩阵或序列分析（SDIS-GSEQ 软件）识别动作间的衔接规律——对战术侦察和比赛准备有直接价值。</li>
    <li><b>技术发展阶段划分：</b>结合技术执行质量与运动员水平（初学者→中级→高水平）交叉分析，关注质变，而非只统计频率。</li>
    <li><b>评分者间信度：</b>双人独立编码时务必报告 Cohen's Kappa（≥ 0.80 = 强一致性）。</li>
</ul>
<b>核心洞察：</b>在格斗运动研究中，技术动作<i>在什么时机使用</i>往往比<i>使用了多少次</i>更重要，情境化的序列数据才能揭示真正的战术智慧。
        """,
        "k6_title": "🧮 体育科研人必知的统计学要点",
        "k6_body": """
你不需要成为统计学家，但这些概念必须掌握：
<ul>
    <li><b>效应量比 p 值更重要：</b>一个结果可以在统计上显著，但在实践中毫无意义。永远在 p 值旁边报告 Cohen's d、η² 或 r。</li>
    <li><b>MDC 与 MCID：</b>最小可检测变化（MDC）与最小临床重要差异（MCID）——评估训练干预是否产生有意义变化时至关重要。</li>
    <li><b>组内相关系数（ICC）：</b>用于信度研究。ICC &gt; 0.90 = 优秀。</li>
    <li><b>非参数检验：</b>体育科学小样本（n &lt; 30）中正态性常不满足，要知道何时用 Mann-Whitney U、Wilcoxon 符号秩检验或 Kruskal-Wallis。</li>
    <li><b>混合设计 ANOVA：</b>干预研究的主力方法，可以清晰处理时间 × 组别的交互效应。</li>
</ul>
        """,
        # ── Contact ──
        "contact_title": "联系我",
        "contact_intro": "欢迎就科研合作、研究方法问题或学术讨论与我联系。",
        "contact_card_title": "📬 联系方式",
        "contact_card_body": "可通过以下方式找到我：",
        "cv_link_label": "简历主页",
        "collab_tag":   "开放合作",
        "collab_title": "合作方向",
        "collab_body":  (
            "• <b>证据综合项目</b>——体育科学或体育教育领域的系统综述与 Meta 分析<br>"
            "• <b>运动数据分析</b>——面向球队或个人运动员的表现数据分析项目<br>"
            "• <b>体育教育研究</b>——教师发展、课程设计、性别与公平议题<br>"
            "• <b>学生交流</b>——很乐意探讨研究方法、研究生申请或体育科学职业发展"
        ),
    },

    "en": {
        # ── Sidebar ──
        "nav_home":       "🏠  Home",
        "nav_research":   "📋  Research",
        "nav_knowledge":  "📚  Knowledge Hub",
        "nav_contact":    "📬  Contact",
        "sidebar_interests_title": "Research Interests",
        "sidebar_interests": [
            "Sports Performance Analysis",
            "Physical Education",
        ],
        # ── Home ──
        "hero_name":     "He Chenmiao",
        "hero_subtitle": "Sport Science Researcher · Sports Performance Analysis · Physical Education",
        "hero_tagline":  (
            "My work bridges quantitative research methods and applied sport science, "
            "with a focus on combat sports biomechanics, exercise-behavioral health intervention, "
            "and physical education policy. I am committed to evidence-based practice "
            "and rigorous synthesis methodology."
        ),
        "badges": ["🥊 Combat Sports Biomechanics", "📊 Meta-Analysis", "🎓 PE Teacher Education", "🧠 Exercise & Health Behavior"],
        "stat_conf_label":   "International\nConferences",
        "stat_meta_label":   "Meta-Analysis\nIn Progress",
        "stat_review_label": "Systematic Review\nIn Progress",
        "stat_years_label":  "Years Research\nExperience",
        "home_what_title":   "What You'll Find Here",
        "home_card1_tag":    "Research Portfolio",
        "home_card1_title":  "📋 My Research Work",
        "home_card1_body":   "Conference presentations, collaborative meta-analysis, and independent systematic review — with context on methods, contributions, and key findings.",
        "home_card2_tag":    "Knowledge Sharing",
        "home_card2_title":  "📚 Research Methods Hub",
        "home_card2_body":   "Practical notes on systematic review workflow, meta-analysis methodology, and sports performance data visualization — written from hands-on experience.",
        "home_focus_title":  "Current Focus",
        "home_focus_tag":    "Active · Team Project",
        "home_focus_title2": "🔄 Meta-Analysis: Exercise Intervention & Electronic Device Addiction",
        "home_focus_body":   (
            "Collaborating with a research team to systematically examine the effect of physical exercise "
            "interventions on problematic electronic device use (smartphone addiction, internet addiction, gaming disorder). "
            "The review follows PRISMA 2020 guidelines with searches across PubMed, Web of Science, Embase, and CNKI. "
            "Planned analyses include pooled effect sizes (Hedges' g), subgroup analyses, and publication bias assessment."
        ),
        "home_focus_meta":  "📍 Status: Data extraction & quality assessment &nbsp;|&nbsp; 👥 Team project",
        # ── Research ──
        "research_title":   "Research Experience",
        "research_intro":   "A record of my academic presentations, collaborative projects, and independent research in sport science and physical education.",
        "conf_section":     "🎤 Conference Presentations",
        "conf1_tag":   "International Conference",
        "conf1_title": "Construction of Boxing Technical Movement Development Sequence",
        "conf1_body":  (
            "Presented at the <b>CSPAH (Chinese Society of Physical Activity and Health) Annual Conference</b>. "
            "This study proposed a developmental progression framework for boxing technical movements, "
            "drawing on movement analysis and pedagogical sequencing to guide skill acquisition in youth and competitive athletes."
        ),
        "conf1_meta":  "🏛 CSPAH Annual Conference &nbsp;|&nbsp; 📌 Sports Biomechanics · Coaching Science",
        "conf2_tag":   "International Conference",
        "conf2_title": "Professional Dilemmas of Newly Employed Female Physical Education Teachers",
        "conf2_body":  (
            "Presented at the <b>Harvard International Education Forum</b>. "
            "This qualitative study examined challenges faced by newly hired female PE teachers — including "
            "professional identity, role conflict, and institutional barriers — to inform gender-sensitive mentorship frameworks."
        ),
        "conf2_meta":  "🏛 Harvard International Education Forum &nbsp;|&nbsp; 📌 Physical Education · Gender Studies",
        "ongoing_section": "🔄 Ongoing Research Projects",
        "proj1_tag":   "In Progress · Team Project",
        "proj1_title": "Meta-Analysis: Exercise Intervention & Electronic Device Addiction",
        "proj1_body":  (
            "A collaborative systematic review and meta-analysis following <b>PRISMA 2020</b>, examining whether "
            "exercise interventions reduce problematic electronic device use. Searches span PubMed, Web of Science, "
            "Embase, and CNKI. Analyses include pooled effect sizes, subgroup analyses by exercise type and duration, "
            "and publication bias correction."
        ),
        "proj1_meta":  "👥 Team collaboration &nbsp;|&nbsp; 🧰 R (meta), RevMan, Rayyan &nbsp;|&nbsp; 📍 Data extraction & quality assessment",
        "proj2_tag":   "In Progress · Independent",
        "proj2_title": "Systematic Review: Title in Development",
        "proj2_body":  (
            "An independent systematic review in the protocol development stage, targeting a focused research "
            "question in sport science or physical education. Will follow PRISMA guidelines with planned PROSPERO registration."
        ),
        "proj2_meta":  "👤 Independent project &nbsp;|&nbsp; 📍 Protocol design stage",
        "skills_section": "🛠 Research Methods & Tools",
        "skill1_tag":  "Synthesis Methods",
        "skill1_body": "Systematic Review · Meta-Analysis · PRISMA 2020 · Risk of Bias (RoB 2) · GRADE",
        "skill2_tag":  "Data & Statistics",
        "skill2_body": "R (meta, metafor) · Python · Streamlit · Effect Size Calculation · Forest Plots",
        "skill3_tag":  "Literature Tools",
        "skill3_body": "PubMed · Web of Science · CNKI · Rayyan · Zotero · Covidence",
        # ── Knowledge Hub ──
        "knowledge_title": "Knowledge Hub",
        "knowledge_intro": "Practical methodology notes from hands-on research experience — covering systematic review workflow, meta-analysis concepts, and sports performance data analysis.",
        "tab_methods": "📋 Research Methodology",
        "tab_data":    "📊 Data Analysis & Visualization",
        "k1_title": "📖 How to Conduct a Systematic Review: A Step-by-Step Guide",
        "k1_body": """
A systematic review rigorously synthesises evidence on a focused research question. Here is the workflow I follow based on <b>PRISMA 2020</b>:
<ul>
    <li><b>Step 1 — Formulate your PICO question:</b> Define Population, Intervention, Comparator, and Outcome before searching. This anchors all subsequent decisions.</li>
    <li><b>Step 2 — Register on PROSPERO:</b> Public registration establishes your plan, prevents duplication, and signals methodological transparency to reviewers.</li>
    <li><b>Step 3 — Build search strings:</b> Boolean operators (AND/OR) across ≥3 databases. For sport science with Chinese literature, always include CNKI.</li>
    <li><b>Step 4 — Screen with Rayyan or Covidence:</b> Two independent reviewers for title/abstract and full-text screening. Report inter-rater agreement (Cohen's κ).</li>
    <li><b>Step 5 — Extract data systematically:</b> Standardised forms covering study design, sample, intervention, outcomes, and effect size.</li>
    <li><b>Step 6 — Assess risk of bias:</b> RoB 2 for RCTs; Newcastle-Ottawa Scale for observational studies.</li>
    <li><b>Step 7 — Synthesise:</b> Narrative synthesis for high heterogeneity; meta-analysis when statistical pooling is appropriate.</li>
</ul>
<b>Key lesson:</b> Invest the most time in your search strategy. A poor search cannot be fixed later — it is the foundation of the entire review.
        """,
        "k2_title": "📐 Meta-Analysis Fundamentals: Effect Sizes & Heterogeneity",
        "k2_body": """
Meta-analysis pools quantitative results across studies. These are the concepts that matter most:
<ul>
    <li><b>Effect size selection:</b> <i>Hedges' g</i> for small samples; log odds ratio for binary outcomes; correlation r for relationship studies.</li>
    <li><b>Fixed vs. random effects:</b> Use a <b>random-effects model</b> in sport science — populations, interventions, and settings differ across studies.</li>
    <li><b>Heterogeneity (I²):</b> I² &gt; 75% = substantial heterogeneity. Run subgroup analyses or meta-regression to explore sources (exercise type, age, duration).</li>
    <li><b>Publication bias:</b> Inspect funnel plot asymmetry; run Egger's test or trim-and-fill correction.</li>
    <li><b>Reading a forest plot:</b> Each row = one study; the bottom diamond = pooled estimate; wider diamond = greater uncertainty.</li>
</ul>
<b>Tools:</b> R packages <code>meta</code> and <code>metafor</code>; RevMan 5 for publication-ready forest plots.
        """,
        "k3_title": "🗂 Literature Search Strategy: Comprehensive and Reproducible",
        "k3_body": """
<ul>
    <li><b>Three-category structure:</b> Population AND Intervention AND Outcome terms — OR within each category.</li>
    <li><b>Combine MeSH and free-text in PubMed:</b> e.g., "Exercise Therapy"[MeSH] OR "physical activity" captures both indexed and non-indexed records.</li>
    <li><b>Include grey literature:</b> WHO reports, government documents, ProQuest dissertations — reduces publication bias.</li>
    <li><b>CNKI is essential:</b> Many relevant sport science studies are only published in Chinese-language journals.</li>
    <li><b>Document everything:</b> Save exact search strings with dates — these go directly into your PRISMA flow diagram and methods section.</li>
</ul>
        """,
        "k4_title": "📈 Sports Performance Data Visualization: Where to Start",
        "k4_body": """
<ul>
    <li><b>Python + Plotly:</b> Interactive dashboards for match trends, training load curves, and athlete comparisons. Plotly Express is fast to learn.</li>
    <li><b>Streamlit:</b> Deploy analyses as shareable web apps in hours — ideal for coaching staff needing browser-accessible dashboards.</li>
    <li><b>R + ggplot2:</b> Publication-quality static figures with <code>theme_minimal()</code>.</li>
    <li><b>Key chart types:</b>
        <ul>
            <li>Line chart — training load, recovery trends</li>
            <li>Radar/spider chart — multi-attribute athlete profiling</li>
            <li>Scatter + regression — performance variable relationships</li>
            <li>Box plot — experimental vs. control group comparisons</li>
            <li>Heatmap — movement frequency zones in combat sports</li>
        </ul>
    </li>
</ul>
        """,
        "k5_title": "🥊 Analysing Combat Sports Technique Data: Practical Notes",
        "k5_body": """
From my boxing movement development sequence research:
<ul>
    <li><b>Action coding:</b> Define a clear taxonomy first (jab, cross, hook, defensive actions), then code. Options include manual video coding or automated pose estimation (MediaPipe, OpenPose).</li>
    <li><b>Sequential analysis:</b> Use transition matrices or SDIS-GSEQ software to identify action-to-action patterns — directly useful for scouting and tactical preparation.</li>
    <li><b>Developmental stage classification:</b> Cross-reference technique quality with athlete level. Look for qualitative shifts, not just frequency counts.</li>
    <li><b>Inter-rater reliability:</b> Always report Cohen's Kappa (≥ 0.80 = strong agreement) for dual independent coding.</li>
</ul>
<b>Key insight:</b> <i>When</i> a technique is used often matters more than <i>how often</i>. Context-sensitive sequential data reveals tactical intelligence.
        """,
        "k6_title": "🧮 Essential Statistics for Sport Science Researchers",
        "k6_body": """
<ul>
    <li><b>Effect size over p-value:</b> Statistical significance ≠ practical importance. Always report Cohen's d, η², or r alongside p-values.</li>
    <li><b>MDC and MCID:</b> Minimal Detectable Change and Minimal Clinically Important Difference — critical for evaluating whether interventions produce meaningful change.</li>
    <li><b>ICC:</b> Intraclass Correlation Coefficient for reliability studies. ICC &gt; 0.90 = excellent.</li>
    <li><b>Non-parametric tests:</b> With small samples (n &lt; 30), use Mann-Whitney U, Wilcoxon signed-rank, or Kruskal-Wallis as appropriate.</li>
    <li><b>Mixed ANOVA:</b> The workhorse of intervention studies — cleanly handles time × group interactions.</li>
</ul>
        """,
        # ── Contact ──
        "contact_title": "Contact",
        "contact_intro": "I'm open to research collaboration, methodology discussions, and academic exchange.",
        "contact_card_title": "📬 Get In Touch",
        "contact_card_body": "Reach me through any of the following:",
        "cv_link_label": "Main CV Site",
        "collab_tag":   "Open To",
        "collab_title": "Collaboration Interests",
        "collab_body":  (
            "• <b>Evidence synthesis</b> — systematic reviews and meta-analyses in sport science or physical education<br>"
            "• <b>Sports analytics</b> — performance data analysis for teams or individual athletes<br>"
            "• <b>PE research</b> — teacher development, curriculum design, gender & equity topics<br>"
            "• <b>Student exchange</b> — happy to discuss research methods, grad school applications, or sport science careers"
        ),
    }
}

# ══════════════════════════════════════════════════════════════
#  GLOBAL CSS
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ── Sidebar: deep wine red ── */
[data-testid="stSidebar"] { background: #1c0508; }
[data-testid="stSidebar"] * { color: #f5e8ea !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 0.92rem; padding: 5px 0; }
[data-testid="stSidebar"] hr { border-color: #4a1520 !important; }

.main .block-container { padding-top: 2rem; max-width: 960px; }

/* ── Hero: PMS 202 red gradient ── */
.hero { background: linear-gradient(135deg, #3d0d12 0%, #6a1e28 55%, #862633 100%); border-radius: 16px; padding: 2.8rem 3rem; margin-bottom: 2rem; color: white; }
.hero h1 { font-family: 'Lora', serif; font-size: 2.4rem; font-weight: 600; margin: 0 0 0.4rem 0; color: white; }
.hero .subtitle { font-size: 1.05rem; color: #f0c0c6; margin-bottom: 1rem; }
.hero .tagline { font-size: 0.9rem; color: #f5d8db; line-height: 1.7; max-width: 620px; }
.hero .badges { margin-top: 1.4rem; display: flex; gap: 10px; flex-wrap: wrap; }
.badge { background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.25); border-radius: 20px; padding: 4px 14px; font-size: 0.82rem; color: #fde8ea; }

/* ── Section title: red left border ── */
.section-title { font-family: 'Lora', serif; font-size: 1.7rem; font-weight: 600; color: #1a0508; border-left: 4px solid #862633; padding-left: 14px; margin: 2rem 0 1.4rem 0; }

/* ── Cards ── */
.card { background: #fff; border: 1px solid #e8d8da; border-radius: 12px; padding: 1.6rem 1.8rem; margin-bottom: 1.2rem; box-shadow: 0 2px 8px rgba(134,38,51,0.06); transition: box-shadow 0.2s; }
.card:hover { box-shadow: 0 4px 16px rgba(134,38,51,0.13); }
.card-tag { display: inline-block; background: #fdf0f1; color: #862633; border-radius: 6px; font-size: 0.75rem; font-weight: 600; padding: 2px 10px; margin-bottom: 0.7rem; text-transform: uppercase; letter-spacing: 0.04em; }
.card-tag.green  { background: #e6f6ee; color: #1a7a4a; }
.card-tag.orange { background: #fef3e2; color: #c47a15; }
.card-tag.purple { background: #f0ecfb; color: #6b3fb5; }
.card h3 { font-size: 1.1rem; font-weight: 600; color: #1a0508; margin: 0 0 0.5rem 0; }
.card p  { font-size: 0.92rem; color: #4a5568; line-height: 1.65; margin: 0; }
.card .meta { font-size: 0.82rem; color: #8a9ab0; margin-top: 0.7rem; }

/* ── Stats ── */
.stats-row { display: flex; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap; }
.stat-box { flex: 1; min-width: 120px; background: #fdf8f8; border: 1px solid #f0d5d7; border-radius: 10px; padding: 1rem 1.2rem; text-align: center; }
.stat-box .num   { font-size: 2rem; font-weight: 700; color: #862633; line-height: 1; }
.stat-box .label { font-size: 0.78rem; color: #6b7f94; margin-top: 4px; white-space: pre-line; }

/* ── Knowledge cards ── */
.knowledge-card { background: #fff; border: 1px solid #e8d8da; border-radius: 12px; padding: 1.8rem; margin-bottom: 1.4rem; box-shadow: 0 2px 8px rgba(134,38,51,0.05); }
.knowledge-card h3 { font-family: 'Lora', serif; font-size: 1.2rem; color: #1a0508; margin: 0 0 0.8rem 0; }
.knowledge-card .kbody { font-size: 0.92rem; color: #4a5568; line-height: 1.75; }
.knowledge-card .kbody ul { margin: 0.6rem 0; padding-left: 1.4rem; }
.knowledge-card .kbody li { margin-bottom: 0.4rem; }
.divider { border: none; border-top: 1px solid #f0d8da; margin: 1.6rem 0; }

/* ── Contact chips ── */
.contact-chip { display: inline-flex; align-items: center; gap: 6px; background: #fdf5f6; border: 1px solid #e8c5c8; border-radius: 8px; padding: 6px 14px; font-size: 0.88rem; color: #6a1e27; margin: 4px; text-decoration: none; }
.contact-chip:hover { background: #fde8ea; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  LANGUAGE + NAVIGATION  (session_state 保持切换不丢失)
# ══════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "zh"

with st.sidebar:
    st.markdown("### 🔬 科研主页 | Portfolio")
    st.markdown("---")

    # ── Language toggle ──────────────────────────────────────
    lang_choice = st.radio(
        "语言 / Language",
        ["中文", "English"],
        index=0 if st.session_state.lang == "zh" else 1
    )
    st.session_state.lang = "zh" if lang_choice == "中文" else "en"
    lang = st.session_state.lang
    T = TEXTS[lang]

    st.markdown("---")

    # ── Page navigation ──────────────────────────────────────
    page = st.radio(
        "页面导航",
        [T["nav_home"], T["nav_research"], T["nav_knowledge"], T["nav_contact"]],
        label_visibility="collapsed"
    )

    st.markdown("---")
    interests_html = "".join(f"• {i}<br>" for i in T["sidebar_interests"])
    st.markdown(f"""
    <div style='font-size:0.8rem; color:#6b8aa0; line-height:1.8;'>
    <b>{T["sidebar_interests_title"]}</b><br>{interests_html}
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════
def render_card(tag, tag_color, title, body, meta=None):
    meta_html = f'<div class="meta">{meta}</div>' if meta else ""
    title_html = f"<h3>{title}</h3>" if title else ""
    st.markdown(f"""
    <div class="card">
        <div class="card-tag {tag_color}">{tag}</div>
        {title_html}
        <p>{body}</p>
        {meta_html}
    </div>
    """, unsafe_allow_html=True)

def render_knowledge(title, body):
    st.markdown(f"""
    <div class="knowledge-card">
        <h3>{title}</h3>
        <div class="kbody">{body}</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  PAGE: HOME / 首页
# ══════════════════════════════════════════════════════════════
if T["nav_home"] in page:
    badges_html = "".join(f'<span class="badge">{b}</span>' for b in T["badges"])
    st.markdown(f"""
    <div class="hero">
        <h1>{T["hero_name"]}</h1>
        <div class="subtitle">{T["hero_subtitle"]}</div>
        <div class="tagline">{T["hero_tagline"]}</div>
        <div class="badges">{badges_html}</div>
    </div>
    """, unsafe_allow_html=True)

    boxes_html = "".join(f"""
    <div class="stat-box">
        <div class="num">{n}</div>
        <div class="label">{l}</div>
    </div>""" for n, l in [
        ("2", T["stat_conf_label"]),
        ("1", T["stat_meta_label"]),
        ("1", T["stat_review_label"]),
    ])
    st.markdown(f'<div class="stats-row">{boxes_html}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="section-title">{T["home_what_title"]}</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        render_card(T["home_card1_tag"], "",      T["home_card1_title"], T["home_card1_body"])
    with c2:
        render_card(T["home_card2_tag"], "green", T["home_card2_title"], T["home_card2_body"])

    st.markdown(f'<div class="section-title">{T["home_focus_title"]}</div>', unsafe_allow_html=True)
    render_card(T["home_focus_tag"], "orange", T["home_focus_title2"], T["home_focus_body"], T["home_focus_meta"])


# ══════════════════════════════════════════════════════════════
#  PAGE: RESEARCH / 科研经历
# ══════════════════════════════════════════════════════════════
elif T["nav_research"] in page:
    st.markdown(f'<div class="section-title">{T["research_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#4a5568;font-size:0.95rem;margin-bottom:1.6rem;">{T["research_intro"]}</p>', unsafe_allow_html=True)

    st.markdown(f"#### {T['conf_section']}")
    render_card(T["conf1_tag"], "purple", T["conf1_title"], T["conf1_body"], T["conf1_meta"])
    render_card(T["conf2_tag"], "purple", T["conf2_title"], T["conf2_body"], T["conf2_meta"])

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown(f"#### {T['ongoing_section']}")
    render_card(T["proj1_tag"], "orange", T["proj1_title"], T["proj1_body"], T["proj1_meta"])
    render_card(T["proj2_tag"], "green",  T["proj2_title"], T["proj2_body"], T["proj2_meta"])

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown(f"#### {T['skills_section']}")
    c1, c2, c3 = st.columns(3)
    with c1: render_card(T["skill1_tag"], "",       "", T["skill1_body"])
    with c2: render_card(T["skill2_tag"], "green",  "", T["skill2_body"])
    with c3: render_card(T["skill3_tag"], "purple", "", T["skill3_body"])


# ══════════════════════════════════════════════════════════════
#  PAGE: KNOWLEDGE HUB / 知识分享
# ══════════════════════════════════════════════════════════════
elif T["nav_knowledge"] in page:
    st.markdown(f'<div class="section-title">{T["knowledge_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#4a5568;font-size:0.95rem;margin-bottom:0.5rem;">{T["knowledge_intro"]}</p>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs([T["tab_methods"], T["tab_data"]])
    with tab1:
        render_knowledge(T["k1_title"], T["k1_body"])
        render_knowledge(T["k2_title"], T["k2_body"])
        render_knowledge(T["k3_title"], T["k3_body"])
    with tab2:
        render_knowledge(T["k4_title"], T["k4_body"])
        render_knowledge(T["k5_title"], T["k5_body"])
        render_knowledge(T["k6_title"], T["k6_body"])


# ══════════════════════════════════════════════════════════════
#  PAGE: CONTACT / 联系我
# ══════════════════════════════════════════════════════════════
elif T["nav_contact"] in page:
    st.markdown(f'<div class="section-title">{T["contact_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#4a5568;font-size:0.95rem;margin-bottom:1.6rem;">{T["contact_intro"]}</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <h3>{T["contact_card_title"]}</h3>
        <p style="margin-bottom:1rem;">{T["contact_card_body"]}</p>
        <a class="contact-chip" href="mailto:chenmiaohe7@gmail.com">✉️ chenmiaohe7@gmail.com</a>
        <a class="contact-chip" href="mailto:602471974@qq.com">✉️ 602471974@qq.com</a>
        <a class="contact-chip" href="https://github.com/yourusername" target="_blank">🐙 GitHub</a>
        <a class="contact-chip" href="#" target="_blank">🌐 {T["cv_link_label"]}</a>
    </div>
    """, unsafe_allow_html=True)

    render_card(T["collab_tag"], "green", T["collab_title"], T["collab_body"])
