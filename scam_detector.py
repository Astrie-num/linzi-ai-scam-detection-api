#Core logic

import re

# Simple predefined scam patterns (demo)
SCAM_KEYWORDS = [
    "urgent", "verify now", "blocked", "act now", "final warning", "last chance"
]

SCAM_TYPES = {
    "account takeover": ["account", "blocked", "verify now"],
    "lottery scam": ["congratulations", "prize", "won"],
    "payment scam": ["transfer", "pay", "money", "momo"]
}

def clean_text(text: str) -> str:
    """Lowercase and remove extra spaces"""
    return re.sub(r'\s+', ' ', text.lower()).strip()

def detect_scam(text: str):
    """Return scam score, type, reason"""
    text_clean = clean_text(text)
    score = 0
    reasons = []

    # Check keywords
    for kw in SCAM_KEYWORDS:
        if kw in text_clean:
            score += 20
            reasons.append(f"Contains suspicious keyword: '{kw}'")

    # Check links
    urls = re.findall(r'http[s]?://\S+', text_clean)
    if urls:
        score += 30
        reasons.append("Message contains a suspicious link")

    # Scam type classification
    scam_type = "Unknown"
    for t, patterns in SCAM_TYPES.items():
        for p in patterns:
            if p in text_clean:
                scam_type = t
                break

    # Risk verdict
    if score >= 60:
        verdict = "Scam"
        confidence = "High"
    elif score >= 30:
        verdict = "Suspicious"
        confidence = "Medium"
    else:
        verdict = "Safe"
        confidence = "Low"

    return {
        "verdict": verdict,
        "confidence": confidence,
        "scam_type": scam_type,
        "reason": reasons,
        "recommended_action": recommend_actions(verdict)
    }

def recommend_actions(verdict: str):
    if verdict == "Scam":
        return [
            "Do not click any links",
            "Block the sender",
            "Report the message"
        ]
    elif verdict == "Suspicious":
        return [
            "Check the sender carefully",
            "Do not provide personal info",
            "Verify before clicking links"
        ]
    else:
        return ["No action needed"]
