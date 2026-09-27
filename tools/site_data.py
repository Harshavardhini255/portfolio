PROJECTS = [
    {
        "slug": "hr-analytics-dashboard",
        "n": "01",
        "title": "HR Analytics Dashboard",
        "category": "People Analytics",
        "kind": "dashboard",
        "year": "2026",
        "stack": ["Python", "SQL", "Power BI", "Streamlit"],
        "tags": ["ETL", "Power BI", "Streamlit"],
        "href": "https://github.com/Harshavardhini255/hr-analytics-dashboard",
        "overview": (
            "An end-to-end HR analytics application that performs ETL and data cleaning on "
            "employee datasets, then surfaces attrition, performance and compensation KPIs "
            "through interactive Power BI dashboards and a Streamlit interface."
        ),
        "built": [
            "Ran end-to-end ETL and data cleaning over employee record sets so the downstream numbers could be trusted.",
            "Modelled attrition, performance and compensation KPIs as the core measures of the application.",
            "Built interactive Power BI dashboards to explore those KPIs across dimensions.",
            "Added a Streamlit interface so the analysis could be reached without opening the desktop BI tool.",
        ],
        "results": [],
        "result_note": "",
    },
    {
        "slug": "customer-churn-analysis",
        "n": "02",
        "title": "Customer Churn Analysis",
        "category": "Predictive Analytics",
        "kind": "analysis",
        "year": "2026",
        "stack": ["SQL", "Python", "Random Forest", "Power BI"],
        "tags": ["Random Forest", "Segmentation", "Power BI"],
        "href": "https://github.com/Harshavardhini255/churn-analysis",
        "overview": (
            "A churn study that starts with SQL and Pandas to find the drivers behind customer "
            "loss, segments the customer base by risk, and then builds a Random Forest model "
            "to put a number on that risk, with Power BI visualisations to support retention strategy."
        ),
        "built": [
            "Analysed customer data with SQL and Pandas to identify which churn drivers actually mattered.",
            "Segmented customers by churn risk so retention effort could be aimed rather than spread evenly.",
            "Built a Random Forest predictive model to score churn likelihood per customer.",
            "Visualised the findings in Power BI to support retention strategy.",
        ],
        "results": [],
        "result_note": "",
    },
    {
        "slug": "vois-aicte-major-project",
        "n": "03",
        "title": "VOIS AICTE Major Project",
        "category": "Conversational AI",
        "kind": "ai",
        "year": "2025",
        "stack": ["LLM", "NLP", "Prompt Engineering"],
        "tags": ["LLM", "NLP", "Prompt Engineering"],
        "href": "https://github.com/Harshavardhini255/VOIS_AICTE_Oct2025_MajorProject_Harshavardini_S",
        "overview": (
            "A conversational analytics solution that lets a user ask questions of a structured "
            "dataset in natural language. NLP techniques process and interpret the data, and the "
            "model returns automated business insights instead of a query the user has to write."
        ),
        "built": [
            "Designed the conversational layer so questions could be asked in plain language against a structured dataset.",
            "Applied NLP techniques to process and interpret the dataset before generating an answer.",
            "Used prompt engineering to keep responses grounded in the actual data.",
            "Delivered the output as analytical reports aimed at stakeholders rather than raw model text.",
        ],
        "results": [
            ("15+", "analytical reports delivered"),
            ("50,000+", "records in the pipeline"),
            ("25%", "improvement in data accuracy"),
        ],
        "result_note": "Delivered during the VOIS AICTE data analyst internship.",
    },
    {
        "slug": "blinkit-grocery-sales-dashboard",
        "n": "04",
        "title": "Blinkit Grocery Sales Dashboard",
        "category": "Retail Intelligence",
        "kind": "dashboard",
        "year": "2025",
        "stack": ["Power BI", "DAX", "Data Modeling"],
        "tags": ["DAX", "Slicers", "KPI"],
        "href": None,
        "overview": (
            "An interactive retail sales dashboard built to replace manual reporting. It models "
            "the sales data, defines the measures in DAX, and exposes the result through KPI cards "
            "and slicers that let a stakeholder cut the numbers by outlet and category."
        ),
        "built": [
            "Modelled the sales dataset for fast, consistent reporting in Power BI.",
            "Defined the headline measures in DAX rather than hard-coding values into visuals.",
            "Built KPI cards for the figures leadership checked most often.",
            "Added slicers for outlet type, outlet size and item category so the view could be self-served.",
        ],
        "results": [
            ("$1.20M", "in sales analysed"),
            ("8,500+", "SKUs covered"),
            ("40%", "less manual reporting time"),
        ],
        "result_note": "",
    },
    {
        "slug": "netflix-content-data-analysis",
        "n": "05",
        "title": "Netflix Content Data Analysis",
        "category": "Exploratory Analysis",
        "kind": "analysis",
        "year": "2025",
        "stack": ["Python", "Pandas", "Seaborn"],
        "tags": ["EDA", "Statistical Modelling", "Viz"],
        "href": None,
        "overview": (
            "Exploratory data analysis and statistical modelling over a real-world catalogue of "
            "titles, aimed at identifying content trends, genre distribution and release patterns. "
            "The transformations in the pipeline were the point as much as the conclusions."
        ),
        "built": [
            "Profiled and cleaned the catalogue dataset before drawing any conclusions from it.",
            "Applied statistical modelling to test which relationships in the data actually held.",
            "Wrote more than ten pipeline transformations to reshape the raw catalogue into analysable form.",
            "Visualised genre distribution, content trends and release patterns with Matplotlib and Seaborn.",
        ],
        "results": [
            ("8,800+", "titles analysed"),
            ("10+", "pipeline transformations"),
        ],
        "result_note": "",
    },
    {
        "slug": "flipkart-market-analysis",
        "n": "06",
        "title": "Flipkart Web Scraping & Market Analysis",
        "category": "Data Engineering",
        "kind": "analysis",
        "year": "2025",
        "stack": ["Python", "Web Scraping", "ETL"],
        "tags": ["Scraping", "ETL", "Pricing"],
        "href": None,
        "overview": (
            "A data engineering project that starts with the collection problem: product and pricing "
            "data pulled from Flipkart through Python-based scraping, then run through ETL and "
            "cleaning before pricing and category performance are analysed in Power BI."
        ),
        "built": [
            "Extracted product and pricing data from Flipkart with Python-based scraping.",
            "Built the ETL and data cleaning steps needed to make the scraped data usable.",
            "Analysed pricing behaviour and category performance trends in Power BI.",
        ],
        "results": [],
        "result_note": "",
    },
    {
        "slug": "library-management-system",
        "n": "07",
        "title": "Library Management System",
        "category": "Relational Design",
        "kind": "database",
        "year": "2025",
        "stack": ["SQL", "MySQL"],
        "tags": ["Normalisation", "Joins", "Tuning"],
        "href": None,
        "overview": (
            "A normalised relational schema for library operations, built with DDL and DML "
            "operations and enforced key constraints. The interesting part is the tuning: the "
            "queries were profiled and rewritten until retrieval was measurably faster."
        ),
        "built": [
            "Designed a normalised relational schema for the library domain.",
            "Implemented the schema with DDL and DML operations and enforced key constraints.",
            "Profiled the queries and optimised them to cut execution time.",
        ],
        "results": [
            ("5,000+", "records managed"),
            ("30%", "faster execution time"),
            ("35%", "better retrieval efficiency"),
        ],
        "result_note": "",
    },
]
