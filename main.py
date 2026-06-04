
import re
from collections import defaultdict

# Risk scoring for different security events
RISK_POINTS = {
    "EMAIL_RECEIVED": 5,
    "LINK_CLICKED": 25,
    "LOGIN_FAILED": 10,
    "LOGIN_SUCCESS": 45,
    "PASSWORD_CHANGED": 30,
    "MAILBOX_FORWARDING_ENABLED": 50
}

# Store scores and events
user_scores = defaultdict(int)
user_events = defaultdict(list)

# Determine risk level
def get_risk_level(score):
    if score >= 150:
        return "HIGH"
    elif score >= 60:
        return "MEDIUM"
    else:
        return "LOW"

# AI-style recommendation engine
def get_recommendation(risk_level):
    if risk_level == "HIGH":
        return "Disable account, reset password, remove forwarding rules, and investigate immediately."
    elif risk_level == "MEDIUM":
        return "Review user activity, monitor login behavior, and verify user identity."
    else:
        return "Continue monitoring for suspicious activity."

# Parse security log file
def analyze_logs(file_path):
    with open(file_path, "r") as file:
        for line in file:

            # Extract user
            user_match = re.search(r'USER=(\w+)', line)
            event_match = re.search(r'EVENT=([A-Z_]+)', line)
            ip_match = re.search(r'IP=([\d\.]+)', line)
            location_match = re.search(r'LOCATION=([A-Za-z]+)', line)

            if user_match and event_match:

                user = user_match.group(1)
                event = event_match.group(1)

                ip = ip_match.group(1) if ip_match else "N/A"
                location = location_match.group(1) if location_match else "N/A"

                # Assign points
                risk_points = RISK_POINTS.get(event, 0)

                # Increase risk score
                user_scores[user] += risk_points

                # Store event details
                user_events[user].append({
                    "event": event,
                    "ip": ip,
                    "location": location,
                    "risk_points": risk_points
                })

# Print AI SOC report
def print_report():
    print("\n=== AI Threat Detection Risk Report ===\n")

    for user, score in sorted(user_scores.items(), key=lambda x: x[1], reverse=True):

        risk_level = get_risk_level(score)
        recommendation = get_recommendation(risk_level)

        print(f"User: {user}")
        print(f"Risk Score: {score}")
        print(f"Risk Level: {risk_level}")
        print("Events:")

        for event in user_events[user]:
            print(
                f" - {event['event']} | "
                f"IP: {event['ip']} | "
                f"Location: {event['location']} | "
                f"Points: {event['risk_points']}"
            )

        print(f"Recommendation: {recommendation}")
        print("-" * 70)

# Save report to file
def save_report(output_file="incident_report.txt"):

    with open(output_file, "w") as report:

        report.write("=== AI Threat Detection Risk Report ===\n\n")

        for user, score in sorted(user_scores.items(), key=lambda x: x[1], reverse=True):

            risk_level = get_risk_level(score)
            recommendation = get_recommendation(risk_level)

            report.write(f"User: {user}\n")
            report.write(f"Risk Score: {score}\n")
            report.write(f"Risk Level: {risk_level}\n")
            report.write("Events:\n")

            for event in user_events[user]:
                report.write(
                    f" - {event['event']} | "
                    f"IP: {event['ip']} | "
                    f"Location: {event['location']} | "
                    f"Points: {event['risk_points']}\n"
                )

            report.write(f"Recommendation: {recommendation}\n")
            report.write("-" * 70 + "\n")

# Main execution
if __name__ == "__main__":

    analyze_logs("security_logs.txt")

    print_report()

    save_report()

    print("\nReport saved to incident_report.txt")
  
