from agents.billing import billing_agent
from agents.technical import technical_agent
from agents.product import product_agent
from agents.complaint import complaint_agent
from agents.faq import faq_agent


def route_query(question: str):

    question = question.lower()

    # Billing
    if any(word in question for word in [
        "bill",
        "billing",
        "payment",
        "invoice",
        "refund",
        "price"
    ]):
        return billing_agent(question)

    # Technical
    elif any(word in question for word in [
        "install",
        "installation",
        "error",
        "bug",
        "issue",
        "problem",
        "technical"
    ]):
        return technical_agent(question)

    # Product
    elif any(word in question for word in [
        "product",
        "laptop",
        "mouse",
        "keyboard",
        "monitor",
        "specification"
    ]):
        return product_agent(question)

    # Complaint
    elif any(word in question for word in [
        "complaint",
        "broken",
        "damage",
        "damaged",
        "return"
    ]):
        return complaint_agent(question)

    # Default
    else:
        return faq_agent(question)