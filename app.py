import streamlit as st
from ai_engine import analyze_ticket

st.title("AI Support Ticket Assistant")


if "ticket_history" not in st.session_state:

    st.session_state.ticket_history = []

issue = st.text_area("Enter support issue")


def get_severity_color(severity):

    severity = severity.upper()

    if severity == "CRITICAL":
        return "red"

    elif severity == "HIGH":
        return "orange"

    elif severity == "MEDIUM":
        return "gold"

    elif severity == "LOW":
        return "green"

    return "gray"



if st.button("Analyze Ticket"):
    if issue:

        with st.spinner("Analyzing issue..."):

            result = analyze_ticket(issue)
            if "error" in result:

                st.error(result["error"])

            else:
                severity = result["severity"]

                color = get_severity_color(severity)

                st.markdown(
                    f"""
                    ### Severity:
                    <span style='color:{color}; font-size:24px; font-weight:bold;'>
                    {severity}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

                st.subheader("Summary:")
                st.write(result["summary"])

                st.subheader("Possible Causes:")
                for cause in result["possible_causes"]:
                   st.markdown(f"- {cause}")

                st.subheader("Suggested Fixes:")
                for fix in result["suggested_fixes"]:
                    st.markdown(f"- {fix}")

                st.session_state.ticket_history.append(
                {
                    "issue": issue,
                    "severity": result["severity"],
                    "summary": result["summary"]
                }
)
    
    else:
        st.warning("Please enter a support issue.")

st.divider()

st.header("Ticket History")

if st.session_state.ticket_history:

    for ticket in reversed(st.session_state.ticket_history):

        color = get_severity_color(ticket["severity"])

        st.markdown(
            f"""
            <span style='color:{color}; font-size:20px; font-weight:bold;'>
            {ticket["severity"]}
            </span>
            """,
            unsafe_allow_html=True
        )

        st.write("Issue:")
        st.write(ticket["issue"])

        st.write("Summary:")
        st.write(ticket["summary"])

        st.divider()

else:

    st.write("No ticket history yet.")