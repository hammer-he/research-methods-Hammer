import streamlit as st

def show():
    st.markdown('<div class="main-header">📊 Chapter 2: Quantitative Research</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Systematic methods that use numerical data to answer research questions</div>', unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Chapter intro
    st.markdown("""
    <div class="highlight-box">
        <b>What is Quantitative Research?</b><br>
        Quantitative research uses <b>numbers, measurements, and statistical analysis</b> to investigate
        research questions. It aims to find patterns, test hypotheses, and establish relationships
        between variables in an objective and replicable way.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # Method selector
    method = st.radio(
        "Select a method to explore:",
        options=[
            "🧪 Method 1: Experimental Research",
            "📋 Method 2: Survey Research",
            "🔗 Method 3: Correlational Research",
            "📚 Method 4: Meta-Analysis",
        ],
        label_visibility="collapsed",
        horizontal=True,
    )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    if method == "🧪 Method 1: Experimental Research":
        show_experimental()
    elif method == "📋 Method 2: Survey Research":
        show_survey()
    elif method == "🔗 Method 3: Correlational Research":
        show_correlational()
    elif method == "📚 Method 4: Meta-Analysis":
        show_meta_analysis()


# ── Method 1: Experimental Research ────────────────────────────────────────
def show_experimental():
    st.markdown("## 🧪 Experimental Research")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📌 Research Topic",
        "📚 Learning Structure",
        "🔥 Warming Topic",
        "📖 Content Learning",
        "💬 Group Talking",
        "📝 Assignment"
    ])

    with tab1:
        st.markdown("### What kinds of questions does this method answer?")
        st.markdown("""
        Experimental research is designed to answer **causal questions** — it is the only method
        that can establish a cause-and-effect relationship between variables.

        **Typical research questions:**
        - Does sleep duration affect memory performance?
        - Does caffeine improve reaction time?
        - Does a high-fat diet lead to greater weight loss than a high-carb diet?

        **Best used when:**
        - You want to prove that X *causes* Y
        - You can actively manipulate the independent variable
        - You can randomly assign participants to conditions
        """)
        st.info("💡 **Key distinction**: Other methods can show that two things are *related*, but only experiments can show that one thing *causes* another.")

    with tab2:
        st.markdown("### Learning Structure")
        st.markdown("By the end of this section, you should be able to:")

        items = [
            "Define independent variable (IV), dependent variable (DV), and control variables",
            "Explain the difference between between-subjects and within-subjects design",
            "Describe the purpose of randomization and blinding",
            "Identify potential confounding variables in an experiment",
            "Explain what internal validity and external validity mean",
            "Choose an appropriate statistical test for a given experimental design",
        ]
        for i, item in enumerate(items, 1):
            st.markdown(f"**{i}.** {item}")

    with tab3:
        st.markdown("### 🔥 Warming Topic")
        st.markdown("""
        **Think about this before we begin:**

        > *You notice that students who drink coffee in the morning tend to score higher on exams.
        > Your friend concludes: "Coffee makes you smarter — I should drink more of it!"*

        **Discuss with a partner:**
        - Is your friend's conclusion valid? Why or why not?
        - What other explanations could there be?
        - How would you design a study to *properly* test whether coffee improves exam scores?
        """)
        st.markdown("""
        <div class="highlight-box">
            This is exactly the problem experimental research solves: moving from
            <b>observation → correlation → controlled experiment → causal conclusion</b>.
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 📖 Core Content")

        with st.expander("1. Key Components of an Experiment", expanded=True):
            data = {
                "Component": ["Independent Variable (IV)", "Dependent Variable (DV)", "Control Variables", "Confounding Variables", "Control Group", "Experimental Group"],
                "Definition": [
                    "The variable the researcher manipulates",
                    "The variable the researcher measures",
                    "Variables kept constant across conditions",
                    "Uncontrolled variables that may affect results",
                    "The group that does NOT receive the treatment",
                    "The group that receives the treatment"
                ],
                "Example (Diet Study)": [
                    "Type of diet (high-fat vs high-carb)",
                    "Weight loss after 3 months (kg)",
                    "Total calorie intake, exercise level, age",
                    "Stress levels, sleep quality",
                    "High-carb diet group",
                    "High-fat diet group"
                ]
            }
            st.table(data)

        with st.expander("2. Between-subjects vs Within-subjects Design"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                <div class="card">
                    <div class="card-title">Between-subjects</div>
                    <p style="color:#4a6580;font-size:0.92rem">
                    Each participant experiences <b>only one</b> condition.<br><br>
                    ✅ No carry-over effects<br>
                    ❌ Requires more participants<br><br>
                    <b>Stats</b>: Independent t-test / ANOVA
                    </p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="card">
                    <div class="card-title">Within-subjects</div>
                    <p style="color:#4a6580;font-size:0.92rem">
                    Each participant experiences <b>all</b> conditions.<br><br>
                    ✅ Fewer participants needed<br>
                    ❌ Risk of practice/fatigue effects<br><br>
                    <b>Stats</b>: Paired t-test / Repeated measures ANOVA
                    </p>
                </div>
                """, unsafe_allow_html=True)

        with st.expander("3. Randomization & Blinding"):
            st.markdown("""
            **Randomization** ensures participants are equally distributed across groups,
            eliminating systematic bias before the experiment begins.

            **Blinding** prevents expectations from influencing results:
            - **Single-blind**: Participants don't know which group they're in → reduces demand characteristics
            - **Double-blind**: Neither participants nor researchers know → also eliminates experimenter bias
            """)

        with st.expander("4. Validity"):
            col1, col2 = st.columns(2)
            with col1:
                st.success("**Internal Validity**\nDid the IV actually cause the change in DV?\n→ Controlled by randomization and controlling confounds")
            with col2:
                st.success("**External Validity**\nCan the results be generalized beyond the lab?\n→ Depends on sample representativeness and ecological validity")

    with tab5:
        st.markdown("### 💬 Group Discussion")
        st.markdown("""
        **Scenario:**
        > A researcher wants to test whether listening to classical music improves
        > mathematical performance in university students. They recruit 60 students
        > and split them into two groups: one solves math problems with classical music
        > playing, the other solves the same problems in silence. The music group scores
        > significantly higher.

        **Discuss the following questions in your group:**
        1. What is the IV? What is the DV?
        2. What confounding variables might threaten the results?
        3. Is this design between-subjects or within-subjects? What are the trade-offs?
        4. How would you improve this study?
        5. Can the researcher conclude that classical music *causes* better math performance?
        """)

    with tab6:
        st.markdown("### 📝 Assignment")
        st.markdown("""
        **Design Your Own Experiment**

        Choose **one** of the following research questions and design a complete experiment:

        1. Does exercise before studying improve memory retention?
        2. Does the color of a room affect creativity?
        3. Does positive feedback improve task performance compared to negative feedback?

        **Your design must include:**
        - [ ] A clear H₀ and H₁
        - [ ] Identification of IV, DV, and at least 3 control variables
        - [ ] Choice of between-subjects or within-subjects design with justification
        - [ ] Description of randomization procedure
        - [ ] Whether blinding is possible and how
        - [ ] How the DV will be specifically measured (operationalization)
        - [ ] At least 2 potential confounding variables and how you would address them
        - [ ] Appropriate statistical test

        **Format**: 400–600 words or a structured table
        """)


# ── Method 2: Survey Research ───────────────────────────────────────────────
def show_survey():
    st.markdown("## 📋 Survey Research")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📌 Research Topic",
        "📚 Learning Structure",
        "🔥 Warming Topic",
        "📖 Content Learning",
        "💬 Group Talking",
        "📝 Assignment"
    ])

    with tab1:
        st.markdown("### What kinds of questions does this method answer?")
        st.markdown("""
        Survey research collects **self-reported data** from a large number of participants
        to describe attitudes, opinions, behaviours, or characteristics of a population.

        **Typical research questions:**
        - How much time do university students spend on social media per day?
        - What percentage of adults report experiencing work-related stress?
        - Do people prefer online or in-person learning, and why?

        **Best used when:**
        - You want to describe a large population efficiently
        - Direct manipulation is not possible or ethical
        - You are interested in people's opinions, attitudes, or self-reported behaviours
        """)
        st.warning("⚠️ **Limitation**: Surveys show *what* people report, but cannot prove *why* or establish causation.")

    with tab2:
        st.markdown("### Learning Structure")
        st.markdown("By the end of this section, you should be able to:")
        items = [
            "Distinguish between different types of survey questions (Likert scale, open-ended, multiple choice)",
            "Explain the difference between a population and a sample",
            "Describe common sampling methods (random, stratified, convenience)",
            "Identify sources of bias in survey research (response bias, sampling bias)",
            "Assess the reliability and validity of a survey instrument",
            "Choose appropriate statistical methods for survey data analysis",
        ]
        for i, item in enumerate(items, 1):
            st.markdown(f"**{i}.** {item}")

    with tab3:
        st.markdown("### 🔥 Warming Topic")
        st.markdown("""
        **Think about this:**

        > *A news headline reads: "90% of people say they are above-average drivers."*

        **Discuss:**
        - Is this statistically possible? What does it tell us about self-reported data?
        - If you were designing a survey about driving ability, what problems might you encounter?
        - Have you ever answered a survey question dishonestly or differently depending on how it was worded?
        """)
        st.markdown("""
        <div class="highlight-box">
            This illustrates the core challenge of survey research: <b>people's reports about
            themselves are not always accurate</b> — and the way you ask questions matters enormously.
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 📖 Core Content")

        with st.expander("1. Types of Survey Questions", expanded=True):
            data = {
                "Type": ["Likert Scale", "Multiple Choice", "Open-ended", "Dichotomous"],
                "Example": [
                    '"I feel stressed at work" (1=Strongly Disagree → 5=Strongly Agree)',
                    '"How often do you exercise? (Daily / Weekly / Monthly / Never)"',
                    '"Describe your experience with online learning."',
                    '"Do you smoke? (Yes / No)"'
                ],
                "Best for": [
                    "Measuring attitudes and opinions",
                    "Categorical behaviours or preferences",
                    "Exploring experiences in depth",
                    "Simple factual questions"
                ]
            }
            st.table(data)

        with st.expander("2. Sampling Methods"):
            st.markdown("""
            | Method | Description | Strength | Weakness |
            |---|---|---|---|
            | **Random sampling** | Every member of population has equal chance | Most representative | Hard to achieve in practice |
            | **Stratified sampling** | Population divided into subgroups, then randomly sampled | Ensures representation of subgroups | More complex |
            | **Convenience sampling** | Whoever is easiest to reach | Fast and cheap | High risk of sampling bias |
            | **Snowball sampling** | Participants recruit other participants | Good for hard-to-reach groups | Non-representative |
            """)

        with st.expander("3. Common Sources of Bias"):
            st.markdown("""
            - **Response bias**: Participants answer in socially desirable ways rather than honestly
            - **Sampling bias**: Sample does not represent the target population
            - **Question wording bias**: Leading or loaded questions influence answers
            - **Non-response bias**: People who don't respond may differ from those who do
            """)

        with st.expander("4. Reliability & Validity of Surveys"):
            col1, col2 = st.columns(2)
            with col1:
                st.info("**Reliability**\nWould the survey give consistent results if repeated?\n→ Test-retest reliability, internal consistency (Cronbach's α)")
            with col2:
                st.info("**Validity**\nDoes the survey measure what it claims to measure?\n→ Content validity, construct validity")

    with tab5:
        st.markdown("### 💬 Group Discussion")
        st.markdown("""
        **Scenario:**
        > A university wants to understand student satisfaction with online learning.
        > They send an email survey to all 10,000 students. Only 300 respond.
        > Results show 85% are satisfied with online learning.

        **Discuss:**
        1. What sampling issues exist here? Who is likely to respond to such surveys?
        2. How might the question wording affect the results?
        3. Can the university conclude that "most students are satisfied"?
        4. How would you redesign this study to get more reliable data?
        5. What is one advantage and one disadvantage of using a survey here compared to an experiment?
        """)

    with tab6:
        st.markdown("### 📝 Assignment")
        st.markdown("""
        **Design a Survey Study**

        Choose one topic and design a complete survey study:
        1. Screen time habits among university students
        2. Attitudes toward mental health support on campus
        3. Student preferences for in-person vs online learning

        **Your submission must include:**
        - [ ] A clear research question and purpose
        - [ ] Target population and sampling method (with justification)
        - [ ] 8–10 survey questions using at least 3 different question types
        - [ ] Identification of at least 2 potential sources of bias and how to minimise them
        - [ ] How you would analyse the data (descriptive statistics, etc.)
        - [ ] One major limitation of your survey design

        **Format**: Survey draft + 200-word methodology explanation
        """)


# ── Method 3: Correlational Research ───────────────────────────────────────
def show_correlational():
    st.markdown("## 🔗 Correlational Research")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📌 Research Topic",
        "📚 Learning Structure",
        "🔥 Warming Topic",
        "📖 Content Learning",
        "💬 Group Talking",
        "📝 Assignment"
    ])

    with tab1:
        st.markdown("### What kinds of questions does this method answer?")
        st.markdown("""
        Correlational research examines the **relationship between two or more variables**
        without manipulating them. It tells you whether variables tend to move together —
        but not which one causes the other.

        **Typical research questions:**
        - Is there a relationship between social media use and anxiety levels?
        - Do students who sleep more tend to get higher grades?
        - Is income level associated with reported happiness?

        **Best used when:**
        - Manipulation of variables is impossible or unethical
        - You want to explore whether a relationship exists before designing an experiment
        - You are working with naturally occurring data
        """)
        st.error("⚠️ **Golden rule**: Correlation ≠ Causation. Always remember the third variable problem.")

    with tab2:
        st.markdown("### Learning Structure")
        st.markdown("By the end of this section, you should be able to:")
        items = [
            "Define positive correlation, negative correlation, and zero correlation",
            "Interpret a correlation coefficient (r value) and its strength",
            "Explain why correlation does not imply causation",
            "Identify the third variable problem with real examples",
            "Choose between Pearson and Spearman correlation and explain when to use each",
            "Describe the appropriate use of scatter plots for correlational data",
        ]
        for i, item in enumerate(items, 1):
            st.markdown(f"**{i}.** {item}")

    with tab3:
        st.markdown("### 🔥 Warming Topic")
        st.markdown("""
        **Consider these two "findings":**

        > 1. *Countries that eat more chocolate per capita win more Nobel Prizes.*
        > 2. *The more firefighters sent to a fire, the more damage the fire causes.*

        **Discuss:**
        - Do these correlations make sense? What is actually going on?
        - What "third variable" might explain each relationship?
        - Can you think of a correlation in everyday life that is clearly not causal?
        """)
        st.markdown("""
        <div class="highlight-box">
            These are real correlations found in data — and they perfectly illustrate why
            <b>correlation alone can never tell us what is causing what</b>.
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 📖 Core Content")

        with st.expander("1. Types of Correlation", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""
                <div class="card">
                    <div class="card-title">Positive Correlation</div>
                    <p style="color:#4a6580;font-size:0.92rem">
                    As X increases, Y increases.<br><br>
                    r = 0 to +1<br><br>
                    Example: More study hours → higher grades
                    </p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="card">
                    <div class="card-title">Negative Correlation</div>
                    <p style="color:#4a6580;font-size:0.92rem">
                    As X increases, Y decreases.<br><br>
                    r = -1 to 0<br><br>
                    Example: More stress → lower sleep quality
                    </p>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown("""
                <div class="card">
                    <div class="card-title">Zero Correlation</div>
                    <p style="color:#4a6580;font-size:0.92rem">
                    No relationship between X and Y.<br><br>
                    r ≈ 0<br><br>
                    Example: Shoe size and intelligence
                    </p>
                </div>
                """, unsafe_allow_html=True)

        with st.expander("2. Interpreting the Correlation Coefficient (r)"):
            data = {
                "r value": ["0.9 to 1.0", "0.7 to 0.9", "0.5 to 0.7", "0.3 to 0.5", "0.0 to 0.3"],
                "Strength": ["Very strong", "Strong", "Moderate", "Weak", "Negligible"],
                "Note": ["Rare in social science", "Practically significant", "Common and meaningful", "Exists but limited", "Likely not useful"]
            }
            st.table(data)
            st.markdown("*Note: The same scale applies to negative r values (e.g., r = -0.8 is a strong negative correlation)*")

        with st.expander("3. Correlation ≠ Causation: The Third Variable Problem"):
            st.markdown("""
            Even a strong correlation between X and Y does not mean X causes Y. There are three possibilities:
            1. **X causes Y** (possible, but not proven by correlation alone)
            2. **Y causes X** (reverse causation)
            3. **Z causes both X and Y** (third variable / confound)

            **Example**: Ice cream sales and drowning rates are positively correlated.
            → The third variable is **hot weather**, which increases both independently.
            """)

        with st.expander("4. Pearson vs Spearman Correlation"):
            col1, col2 = st.columns(2)
            with col1:
                st.info("**Pearson (r)**\nFor continuous, normally distributed data\nExample: Height and weight")
            with col2:
                st.info("**Spearman (ρ)**\nFor ranked/ordinal data or non-normal distributions\nExample: Ranking of satisfaction (1–5 scale)")

    with tab5:
        st.markdown("### 💬 Group Discussion")
        st.markdown("""
        **Scenario:**
        > A study finds a strong negative correlation (r = -0.72) between the number of
        > hours teenagers spend on social media and their self-reported well-being scores.
        > A journalist reports: *"Social media is destroying teenagers' mental health."*

        **Discuss:**
        1. Is the journalist's conclusion justified? What's the problem?
        2. What third variables might explain this correlation?
        3. Could the direction of causation be reversed? How?
        4. What kind of study would you need to actually establish causation?
        5. Is r = -0.72 a strong enough correlation to be practically meaningful?
        """)

    with tab6:
        st.markdown("### 📝 Assignment")
        st.markdown("""
        **Correlational Study Analysis**

        Find **one published correlational study** (from Google Scholar or a textbook)
        on a topic that interests you.

        **Your submission must include:**
        - [ ] Full citation of the study
        - [ ] The research question and the two (or more) variables being correlated
        - [ ] The reported r value and what it means in plain language
        - [ ] Whether the authors appropriately avoided claiming causation
        - [ ] At least 2 possible third variables the study did not account for
        - [ ] Your own evaluation: is this a well-conducted correlational study? Why or why not?

        **Format**: 300–500 words
        """)


# ── Method 4: Meta-Analysis ─────────────────────────────────────────────────
def show_meta_analysis():
    st.markdown("## 📚 Meta-Analysis")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📌 Research Topic",
        "📚 Learning Structure",
        "🔥 Warming Topic",
        "📖 Content Learning",
        "💬 Group Talking",
        "📝 Assignment"
    ])

    with tab1:
        st.markdown("### What kinds of questions does this method answer?")
        st.markdown("""
        Meta-analysis is a **study of studies** — it statistically combines the results of
        multiple independent studies to produce a single, more reliable conclusion.

        **Typical research questions:**
        - Overall, does cognitive behavioural therapy (CBT) work for depression?
        - What is the true effect size of exercise on anxiety across all published studies?
        - Do high-fat diets consistently outperform high-carb diets for weight loss?

        **Best used when:**
        - Many studies have been conducted on the same question with mixed results
        - You want the most statistically powerful estimate of an effect
        - You want to resolve contradictions in the existing literature
        """)
        st.success("✅ **Strength**: Meta-analysis sits at the top of the evidence hierarchy — it provides the most reliable conclusions in science.")

    with tab2:
        st.markdown("### Learning Structure")
        st.markdown("By the end of this section, you should be able to:")
        items = [
            "Explain what a meta-analysis is and why it is more powerful than a single study",
            "Describe the steps involved in conducting a meta-analysis",
            "Define effect size and explain why it is central to meta-analysis",
            "Explain what a forest plot shows and how to read one",
            "Identify the problem of publication bias and explain how it affects meta-analyses",
            "Critically evaluate the quality of a meta-analysis",
        ]
        for i, item in enumerate(items, 1):
            st.markdown(f"**{i}.** {item}")

    with tab3:
        st.markdown("### 🔥 Warming Topic")
        st.markdown("""
        **Imagine this situation:**

        > Study A (n=50): Exercise reduces depression. p = 0.04 ✅
        > Study B (n=45): Exercise has no effect on depression. p = 0.12 ❌
        > Study C (n=60): Exercise reduces depression. p = 0.03 ✅
        > Study D (n=30): Exercise has no effect on depression. p = 0.08 ❌

        **Discuss:**
        - The studies contradict each other. What should we conclude?
        - If you were a doctor, which result would you rely on?
        - Is there a way to combine all four studies to get a clearer answer?
        """)
        st.markdown("""
        <div class="highlight-box">
            This is exactly the problem meta-analysis solves: <b>combining all available evidence
            into one statistically rigorous conclusion</b> instead of cherry-picking individual studies.
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 📖 Core Content")

        with st.expander("1. Steps in a Meta-Analysis", expanded=True):
            steps = [
                ("Define the research question", "e.g., 'Does exercise reduce symptoms of depression in adults?'"),
                ("Set inclusion/exclusion criteria", "e.g., RCTs only, adults 18+, published in peer-reviewed journals"),
                ("Systematic literature search", "Search databases: PubMed, PsycINFO, Web of Science"),
                ("Screen and select studies", "Remove duplicates, assess titles/abstracts, read full texts"),
                ("Extract data", "Record sample size, effect size, methodology from each study"),
                ("Calculate a combined effect size", "Use weighted average — larger studies count more"),
                ("Assess heterogeneity", "Are the studies similar enough to be combined? (I² statistic)"),
                ("Check for publication bias", "Funnel plot, Egger's test"),
                ("Report findings", "Forest plot, overall effect size, confidence intervals"),
            ]
            for i, (step, detail) in enumerate(steps, 1):
                st.markdown(f"**Step {i}: {step}**")
                st.markdown(f"<small style='color:#4a6580'>→ {detail}</small>", unsafe_allow_html=True)
                st.markdown("")

        with st.expander("2. How to Read a Forest Plot"):
            st.markdown("""
            A forest plot displays the results of each individual study and the overall combined effect:

            - Each **horizontal line** = one study (width = confidence interval, box size = sample size)
            - The **diamond** at the bottom = overall combined effect size
            - If the confidence interval **does not cross zero** → the effect is statistically significant
            - Studies are listed with their effect sizes — you can see which ones agree and disagree
            """)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Forestplot01.jpg/600px-Forestplot01.jpg",
                     caption="Example of a forest plot", use_column_width=True)

        with st.expander("3. Publication Bias"):
            st.markdown("""
            **Publication bias** occurs because studies with *significant results* are more likely
            to be published than studies with *null results*. This means meta-analyses
            may overestimate the true effect size.

            **How to detect it:**
            - **Funnel plot**: If the plot is asymmetrical, publication bias may be present
            - **Fail-safe N**: How many unpublished null studies would it take to overturn the conclusion?

            **Why it matters**: If only positive studies get published, combining them gives a falsely
            optimistic picture of an intervention's effectiveness.
            """)

        with st.expander("4. Strengths and Limitations"):
            col1, col2 = st.columns(2)
            with col1:
                st.success("""
                **Strengths**
                - Largest possible sample size (combines many studies)
                - Most statistically powerful conclusions
                - Can resolve contradictions between studies
                - Top of the evidence hierarchy
                """)
            with col2:
                st.error("""
                **Limitations**
                - "Garbage in, garbage out" — quality depends on included studies
                - Publication bias can distort results
                - Combining very different studies may be misleading (heterogeneity)
                - Cannot be done if too few studies exist
                """)

    with tab5:
        st.markdown("### 💬 Group Discussion")
        st.markdown("""
        **Scenario:**
        > A meta-analysis of 23 studies concludes that mindfulness meditation
        > significantly reduces anxiety (overall effect size d = 0.58, p < 0.001).
        > However, 20 of the 23 studies were conducted in the United States,
        > and the funnel plot shows slight asymmetry.

        **Discuss:**
        1. What does d = 0.58 tell us about the practical significance of the finding?
        2. What concerns does the geographic concentration of studies raise?
        3. What does the asymmetrical funnel plot suggest, and how does it affect your confidence in the result?
        4. Would you recommend mindfulness programmes based on this meta-analysis? What caveats would you add?
        5. How is this conclusion stronger (or weaker) than a single well-designed RCT?
        """)

    with tab6:
        st.markdown("### 📝 Assignment")
        st.markdown("""
        **Critical Appraisal of a Meta-Analysis**

        Find **one published meta-analysis** on a health, psychological, or educational intervention
        (search Google Scholar for: *"meta-analysis" + your topic of interest*).

        **Your submission must include:**
        - [ ] Full citation of the meta-analysis
        - [ ] The research question it addresses
        - [ ] How many studies were included and the overall effect size reported
        - [ ] Whether the authors addressed publication bias (how?)
        - [ ] One strength and one limitation of this specific meta-analysis
        - [ ] Your overall verdict: how much should we trust this conclusion?

        **Format**: 400–600 words
        """)
