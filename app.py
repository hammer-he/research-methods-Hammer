import streamlit as st

st.set_page_config(
    page_title="Research Portfolio",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0f1923;
}
[data-testid="stSidebar"] * {
    color: #e8edf2 !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.95rem;
    padding: 6px 0;
    cursor: pointer;
}

/* ── Main area ── */
.main .block-container {
    padding-top: 2rem;
    max-width: 960px;
}

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #0f1923 0%, #1a2f45 60%, #0e3a5e 100%);
    border-radius: 16px;
    padding: 2.8rem 3rem;
    margin-bottom: 2rem;
    color: white;
}
.hero h1 {
    font-family: 'Lora', serif;
    font-size: 2.4rem;
    font-weight: 600;
    margin: 0 0 0.4rem 0;
    color: white;
}
.hero .subtitle {
    font-size: 1.05rem;
    color: #93b8d8;
    margin-bottom: 1rem;
}
.hero .tagline {
    font-size: 0.9rem;
    color: #b8cfe0;
    line-height: 1.7;
    max-width: 600px;
}
.hero .badges {
    margin-top: 1.4rem;
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.badge {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.82rem;
    color: #d4e8f8;
}

/* ── Section title ── */
.section-title {
    font-family: 'Lora', serif;
    font-size: 1.7rem;
    font-weight: 600;
    color: #0f1923;
    border-left: 4px solid #1a6fa8;
    padding-left: 14px;
    margin: 2rem 0 1.4rem 0;
}

/* ── Cards ── */
.card {
    background: #ffffff;
    border: 1px solid #e4eaf0;
    border-radius: 12px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: box-shadow 0.2s;
}
.card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
.card-tag {
    display: inline-block;
    background: #e8f2fb;
    color: #1a6fa8;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 2px 10px;
    margin-bottom: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.card-tag.green { background: #e6f6ee; color: #1a7a4a; }
.card-tag.orange { background: #fef3e2; color: #c47a15; }
.card-tag.purple { background: #f0ecfb; color: #6b3fb5; }
.card h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #0f1923;
    margin: 0 0 0.5rem 0;
}
.card p {
    font-size: 0.92rem;
    color: #4a5568;
    line-height: 1.65;
    margin: 0;
}
.card .meta {
    font-size: 0.82rem;
    color: #8a9ab0;
    margin-top: 0.7rem;
}

/* ── Stats bar ── */
.stats-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}
.stat-box {
    flex: 1;
    min-width: 120px;
    background: #f7fafd;
    border: 1px solid #dde8f0;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.stat-box .num {
    font-size: 2rem;
    font-weight: 700;
    color: #1a6fa8;
    line-height: 1;
}
.stat-box .label {
    font-size: 0.78rem;
    color: #6b7f94;
    margin-top: 4px;
}

/* ── Knowledge post ── */
.knowledge-card {
    background: #fff;
    border: 1px solid #e4eaf0;
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.4rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.knowledge-card h3 {
    font-family: 'Lora', serif;
    font-size: 1.2rem;
    color: #0f1923;
    margin: 0 0 0.8rem 0;
}
.knowledge-card .kbody {
    font-size: 0.92rem;
    color: #4a5568;
    line-height: 1.75;
}
.knowledge-card .kbody ul {
    margin: 0.6rem 0;
    padding-left: 1.4rem;
}
.knowledge-card .kbody li {
    margin-bottom: 0.4rem;
}
.divider { border: none; border-top: 1px solid #e8eef4; margin: 1.6rem 0; }

/* ── Contact ── */
.contact-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #f0f6fb;
    border: 1px solid #c8dff0;
    border-radius: 8px;
    padding: 6px 14px;
    font-size: 0.88rem;
    color: #1a4f75;
    margin: 4px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔬 Research Portfolio")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["🏠  Home", "📋  Research Experience", "📚  Knowledge Hub", "📬  Contact"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.8rem; color:#6b8aa0; line-height:1.6;'>
    <b>Research Interests</b><br>
    • Sports Performance Analysis<br>
    • Exercise & Behavioral Health<br>
    • Physical Education<br>
    • Systematic Review Methods
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# PAGE 1 — HOME
# ════════════════════════════════════════════════════════════
if "Home" in page:
    st.markdown("""
    <div class="hero">
        <h1>Jiayi Ma</h1>
        <div class="subtitle">Sport Science Researcher · Data Analyst · Educator</div>
        <div class="tagline">
            Passionate about bridging quantitative research methods and sports performance.
            My work spans biomechanics, behavioral health, and physical education,
            with a focus on evidence-based insights for athletes and coaches.
        </div>
        <div class="badges">
            <span class="badge">🥊 Sports Biomechanics</span>
            <span class="badge">📊 Meta-Analysis</span>
            <span class="badge">🎓 Physical Education</span>
            <span class="badge">🧠 Exercise & Behavior</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class="stats-row">
        <div class="stat-box">
            <div class="num">2</div>
            <div class="label">International<br>Conferences</div>
        </div>
        <div class="stat-box">
            <div class="num">1</div>
            <div class="label">Meta-Analysis<br>In Progress</div>
        </div>
        <div class="stat-box">
            <div class="num">1</div>
            <div class="label">Systematic Review<br>In Progress</div>
        </div>
        <div class="stat-box">
            <div class="num">2+</div>
            <div class="label">Years Research<br>Experience</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">What You\'ll Find Here</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-tag">Research Portfolio</div>
            <h3>📋 My Research Work</h3>
            <p>Conference presentations, ongoing meta-analysis, and systematic review projects — with context on methods, contributions, and key findings.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-tag green">Knowledge Sharing</div>
            <h3>📚 Research Methods Hub</h3>
            <p>Practical guides on systematic reviews, meta-analysis, sports data visualization, and research design — written from hands-on experience.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Current Focus</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-tag orange">Active Project</div>
        <h3>🔄 Meta-Analysis: Exercise Intervention & Digital/Electronic Addiction</h3>
        <p>
        Collaborating with a research team to systematically examine the effect of physical exercise interventions on
        electronic device addiction behaviors. This project involves comprehensive literature search across PubMed,
        Web of Science, and CNKI, PRISMA-guided screening, and effect size pooling using random-effects models.
        </p>
        <div class="meta">📍 Status: Data extraction phase &nbsp;|&nbsp; 👥 Team project</div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# PAGE 2 — RESEARCH EXPERIENCE
# ════════════════════════════════════════════════════════════
elif "Research Experience" in page:
    st.markdown('<div class="section-title">Research Experience</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="color:#4a5568; font-size:0.95rem; margin-bottom:1.6rem;">
    A record of my academic presentations, collaborative projects, and independent research work
    in sport science and physical education.
    </p>
    """, unsafe_allow_html=True)

    # ── Conference Presentations ─────────────────────────────
    st.markdown("#### 🎤 Conference Presentations")

    st.markdown("""
    <div class="card">
        <div class="card-tag purple">International Conference</div>
        <h3>Construction of Boxing Technical Movement Development Sequence</h3>
        <p>
        Presented at the <b>CSPAH (Chinese Society of Physical Activity and Health) Annual Conference</b>.
        This study investigated the progressive structure of technical movements in boxing,
        proposing a developmental sequence framework that can guide skill acquisition
        in youth and competitive athletes. The work draws on movement analysis and
        pedagogical sequencing principles.
        </p>
        <div class="meta">
            🏛 CSPAH Annual Conference &nbsp;|&nbsp; 📌 Sports Biomechanics & Coaching Science
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-tag purple">International Conference</div>
        <h3>Dilemmas Faced by Newly Employed Female Physical Education Teachers</h3>
        <p>
        Presented at the <b>Harvard International Education Forum</b>.
        This qualitative study examined the professional and personal challenges encountered
        by newly hired female PE teachers, including workplace identity, role conflict, and
        institutional barriers. Findings highlight the need for mentorship structures and
        gender-sensitive onboarding policies in physical education departments.
        </p>
        <div class="meta">
            🏛 Harvard International Education Forum &nbsp;|&nbsp; 📌 Physical Education · Gender Studies
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ── Ongoing Research ─────────────────────────────────────
    st.markdown("#### 🔄 Ongoing Research Projects")

    st.markdown("""
    <div class="card">
        <div class="card-tag orange">In Progress · Team Project</div>
        <h3>Meta-Analysis: The Effect of Exercise on Electronic Device Addiction</h3>
        <p>
        A collaborative systematic review and meta-analysis examining whether physical exercise interventions
        can reduce problematic use of electronic devices (smartphone addiction, internet addiction, gaming disorder).
        The review follows <b>PRISMA 2020 guidelines</b>, with searches across PubMed, Web of Science,
        Embase, and CNKI. Planned analyses include pooled effect sizes (Hedges' g),
        subgroup analyses by exercise type and intervention duration, and publication bias assessment.
        </p>
        <div class="meta">
            👥 Team collaboration &nbsp;|&nbsp; 🧰 Tools: R (meta), RevMan, Rayyan
            &nbsp;|&nbsp; 📍 Status: Data extraction & quality assessment
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-tag green">In Progress · Independent</div>
        <h3>Systematic Review: [Title In Development]</h3>
        <p>
        An independent systematic review project currently in the protocol development stage.
        The review will follow PRISMA guidelines and address a focused research question
        in sport science or physical education. Topic and scope are being finalized.
        Protocol registration via PROSPERO is planned.
        </p>
        <div class="meta">
            👤 Independent project &nbsp;|&nbsp; 📍 Status: Protocol design
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ── Skills ────────────────────────────────────────────────
    st.markdown("#### 🛠 Research Methods & Tools")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card" style="min-height:160px;">
            <div class="card-tag">Synthesis Methods</div>
            <p>Systematic Review · Meta-Analysis · PRISMA 2020 · Risk of Bias (RoB 2) · GRADE</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card" style="min-height:160px;">
            <div class="card-tag green">Data & Statistics</div>
            <p>R (meta, metafor) · Python · Streamlit · Effect Size Calculation · Forest Plots</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card" style="min-height:160px;">
            <div class="card-tag purple">Literature Tools</div>
            <p>PubMed · Web of Science · CNKI · Rayyan · Zotero · Covidence</p>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# PAGE 3 — KNOWLEDGE HUB
# ════════════════════════════════════════════════════════════
elif "Knowledge Hub" in page:
    st.markdown('<div class="section-title">Knowledge Hub</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="color:#4a5568; font-size:0.95rem; margin-bottom:0.5rem;">
    Practical notes and guides from my own research experience — covering systematic review workflow,
    meta-analysis methods, and sports performance data analysis.
    </p>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📋 Research Methodology", "📊 Data Analysis & Visualization"])

    # ── Tab 1: Research Methodology ──────────────────────────
    with tab1:
        st.markdown("""
        <div class="knowledge-card">
            <h3>🔍 How to Conduct a Systematic Review: A Step-by-Step Guide</h3>
            <div class="kbody">
            A systematic review is a rigorous synthesis of existing evidence on a focused research question.
            Here is the general workflow I follow, based on the <b>PRISMA 2020</b> framework:

            <ul>
                <li><b>Step 1 — Formulate your PICO question:</b> Define Population, Intervention, Comparator, and Outcome clearly before searching.</li>
                <li><b>Step 2 — Register your protocol:</b> Submit to PROSPERO to establish your review plan publicly and prevent duplication.</li>
                <li><b>Step 3 — Develop search strings:</b> Use Boolean operators (AND/OR) across at least 3 databases (e.g., PubMed, Web of Science, CNKI for Chinese literature).</li>
                <li><b>Step 4 — Screen with Rayyan or Covidence:</b> Title/abstract screening followed by full-text eligibility — always with two independent reviewers.</li>
                <li><b>Step 5 — Extract data systematically:</b> Use a standardized extraction form (study design, sample, intervention, outcome, effect size).</li>
                <li><b>Step 6 — Assess risk of bias:</b> For RCTs, use RoB 2; for observational studies, use NOS (Newcastle-Ottawa Scale).</li>
                <li><b>Step 7 — Synthesize:</b> Narrative synthesis for heterogeneous studies; meta-analysis when pooling is appropriate.</li>
            </ul>

            <b>Key tip:</b> Spend the most time on your search string. A poor search strategy cannot be fixed later — it undermines the entire review.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knowledge-card">
            <h3>📐 Meta-Analysis Fundamentals: Effect Sizes & Heterogeneity</h3>
            <div class="kbody">
            Meta-analysis pools quantitative results from multiple studies. Here are the concepts that matter most:

            <ul>
                <li><b>Effect size choices:</b> Use <i>Hedges' g</i> (preferred over Cohen's d for small samples), log odds ratio for binary outcomes, or correlation r for relationship studies.</li>
                <li><b>Fixed vs. Random effects:</b> Almost always use a <b>random-effects model</b> in sport science — studies differ in populations, interventions, and settings.</li>
                <li><b>Heterogeneity (I²):</b> I² > 75% signals high heterogeneity — run subgroup analyses or meta-regression to explore sources (e.g., by exercise type, age group, session duration).</li>
                <li><b>Publication bias:</b> Inspect funnel plot asymmetry; run Egger's test or trim-and-fill correction.</li>
                <li><b>Forest plot reading:</b> Each row is one study. The diamond at the bottom is the pooled estimate. Wider diamonds = more uncertainty.</li>
            </ul>

            <b>Tools I use:</b> R packages <code>meta</code> and <code>metafor</code> for analysis; RevMan 5 for reporting-ready forest plots.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knowledge-card">
            <h3>🗂 Literature Search Strategy: Getting It Right</h3>
            <div class="kbody">
            A reproducible, comprehensive search is the backbone of any evidence synthesis.

            <ul>
                <li><b>Build your term list in 3 categories:</b> Population terms, Intervention terms, Outcome terms — then combine with AND between categories, OR within.</li>
                <li><b>Use MeSH terms in PubMed</b> alongside free-text to capture indexed vocabulary (e.g., "Exercise Therapy"[MeSH] OR "physical activity").</li>
                <li><b>Don't forget grey literature:</b> WHO, government reports, and ProQuest Dissertations for unpublished work — reduces publication bias.</li>
                <li><b>CNKI is essential for Chinese-language sport science:</b> Many relevant exercise studies are only published in Chinese journals.</li>
                <li><b>Document everything:</b> Save your exact search strings with dates — this goes directly into your PRISMA flow diagram and methods section.</li>
            </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 2: Data Analysis ─────────────────────────────────
    with tab2:
        st.markdown("""
        <div class="knowledge-card">
            <h3>📈 Sports Performance Data Visualization: Where to Start</h3>
            <div class="kbody">
            Good visualization communicates performance trends that raw numbers hide. Here's my go-to toolkit:

            <ul>
                <li><b>Python + Plotly:</b> For interactive dashboards — ideal for showing match-by-match trends, load monitoring curves, or athlete comparisons. Plotly Express makes it fast.</li>
                <li><b>Streamlit:</b> Deploy your analysis as a shareable web app in hours. No web development experience needed. Great for coaching staff who aren't comfortable with R/Python.</li>
                <li><b>R + ggplot2:</b> For publication-quality static figures — clean, customizable, and reproducible with <code>theme_minimal()</code>.</li>
                <li><b>Key chart types for sport science:</b>
                    <ul>
                        <li>Line chart — training load over time, recovery trends</li>
                        <li>Radar/spider chart — multi-attribute athlete profiling</li>
                        <li>Scatter + regression — relationship between two performance variables</li>
                        <li>Box plot — group comparisons (experimental vs. control)</li>
                        <li>Heatmap — movement frequency zones (e.g., attack zones in combat sports)</li>
                    </ul>
                </li>
            </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knowledge-card">
            <h3>🥊 Analyzing Combat Sports Technique Data: My Approach</h3>
            <div class="kbody">
            From my work on boxing movement development sequences, here are practical notes on analyzing
            technical action data in combat sports:

            <ul>
                <li><b>Action coding:</b> Define a clear taxonomy of techniques first (e.g., jab, cross, hook, defense actions). Video-based manual coding or automated pose estimation (MediaPipe, OpenPose) can be used.</li>
                <li><b>Sequence analysis:</b> Use transition matrices or sequential analysis (SDIS-GSEQ software) to identify what actions tend to follow each other — useful for scouting and tactical pattern recognition.</li>
                <li><b>Development stage classification:</b> Cross-reference technique execution with skill level (novice → intermediate → expert). Look for qualitative shifts, not just frequency counts.</li>
                <li><b>Inter-rater reliability:</b> Always report Cohen's Kappa (≥ 0.80 = strong agreement) when two coders classify technique data independently.</li>
            </ul>

            <b>Key insight:</b> In combat sports research, <i>when</i> a technique is used matters as much as <i>how often</i>. Context-sensitive sequence data reveals tactical intelligence.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="knowledge-card">
            <h3>🧮 Essential Statistics for Sport Science Researchers</h3>
            <div class="kbody">
            You don't need to be a statistician — but you do need to know these:

            <ul>
                <li><b>Effect size over p-value:</b> A result can be statistically significant but practically meaningless. Always report Cohen's d, η², or r alongside your p-value.</li>
                <li><b>Minimal Detectable Change (MDC) and Minimal Clinically Important Difference (MCID):</b> Critical when evaluating whether a training intervention produces a meaningful performance change.</li>
                <li><b>ICC (Intraclass Correlation Coefficient):</b> Use for reliability studies — e.g., test-retest reliability of a performance measure. ICC > 0.90 = excellent.</li>
                <li><b>Non-parametric tests:</b> In small sport science samples (n < 30), normality is often not met. Know when to use Mann-Whitney U, Wilcoxon signed-rank, and Kruskal-Wallis.</li>
                <li><b>Mixed ANOVA:</b> The workhorse of intervention studies with repeated measures — handles time × group interactions cleanly.</li>
            </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# PAGE 4 — CONTACT
# ════════════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="color:#4a5568; font-size:0.95rem; margin-bottom:1.6rem;">
    I'm always open to research collaboration, academic discussion, or questions about the
    methods and projects described on this site.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>📬 Contact & Links</h3>
        <p style="margin-bottom:1rem;">Feel free to reach out through any of the following:</p>
        <a class="contact-chip" href="mailto:your.email@university.edu">✉️ your.email@university.edu</a>
        <a class="contact-chip" href="https://github.com/yourusername" target="_blank">🐙 GitHub</a>
        <a class="contact-chip" href="https://linkedin.com/in/yourprofile" target="_blank">💼 LinkedIn</a>
        <a class="contact-chip" href="#" target="_blank">🌐 Main CV / Resume Site</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-tag green">Open To</div>
        <h3>Collaboration Interests</h3>
        <p>
        • <b>Evidence synthesis projects</b> — systematic reviews and meta-analyses in sport science or physical education<br>
        • <b>Sports analytics projects</b> — performance data analysis for teams or individual athletes<br>
        • <b>Physical education research</b> — teacher development, curriculum design, gender & equity topics<br>
        • <b>Student discussions</b> — happy to chat about research methods, grad school applications, or sports science career paths
        </p>
    </div>
    """, unsafe_allow_html=True)
