import streamlit as st
from ai_engine import analyze_ticket
from database import (
    save_ticket,
    get_all_tickets,
    delete_ticket
)

st.title("AI Support Ticket Assistant")


with st.form("ticket_form", clear_on_submit=True):

    issue = st.text_area("Enter support issue")

    submitted = st.form_submit_button("Analyze Ticket")

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



if submitted:
    if issue:

        with st.spinner("Analyzing issue..."):

            result = analyze_ticket(issue)
            if "error" in result:

                st.error(result["error"])
                

            else:
                severity = result["severity"]
                save_ticket(
                    issue,
                    severity,
                    result["summary"]
                )

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
    
    else:
        st.warning("Please enter a support issue.")

st.divider()

st.header("Ticket History")
tickets = get_all_tickets()



if tickets:

    for ticket in tickets:

        ticket_id, issue, severity, summary = ticket

        color = get_severity_color(severity)

        st.markdown(
            f"""
            Severity:
            <span style='color:{color}; font-size:20px; font-weight:bold;'>
            {severity}
            </span>
            """,
            unsafe_allow_html=True
        )

        st.write("Issue:")
        st.write(issue)

        st.write("Summary:")
        st.write(summary)

        if st.button("Delete",key=f"delete_{ticket_id}"):
            delete_ticket(ticket_id)
            st.rerun()

        st.divider()

else:

    st.write("No ticket history yet.")