from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data - In a real application, this would come from a database
team_members = [
    {"name": "John Doe", "role": "Executive Director", "bio": "Leading our organization since 2020"},
    {"name": "Jane Smith", "role": "Program Manager", "bio": "Expert in community outreach"},
    {"name": "Mike Johnson", "role": "Volunteer Coordinator", "bio": "Organizing our amazing volunteers"}
]

contact_info = {
    "address": "123 Nonprofit Street, Charity City, ST 12345",
    "email": "contact@nonprofit.org",
    "phone": "(555) 123-4567"
}

donation_tiers = [
    {"name": "Friend", "amount": 25, "description": "Helps provide basic supplies"},
    {"name": "Supporter", "amount": 50, "description": "Supports our monthly programs"},
    {"name": "Champion", "amount": 100, "description": "Makes a significant impact"}
]

impact_stats = [
    {"number": "1,000+", "description": "People Helped"},
    {"number": "50+", "description": "Community Programs"},
    {"number": "100+", "description": "Volunteers"}
] #removed from the front end view 

@app.route('/')
def home():
    return render_template("home.html",
                         page_title="Home",
                         current_year=datetime.now().year)

@app.route('/about')
def about():
    return render_template("about.html",
                         page_title="About Us",
                         current_year=datetime.now().year,
                         founding_year=2020,
                         team_members=team_members)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you would typically process the form data
        # For now, we'll just redirect back to the contact page
        return redirect(url_for('contact'))
    
    return render_template("contact.html",
                         page_title="Contact Us",
                         current_year=datetime.now().year,
                         contact_info=contact_info)

@app.route('/donate')
def donate():
    return render_template("donate.html",
                         page_title="Donate",
                         current_year=datetime.now().year,
                         donation_tiers=donation_tiers,
                         impact_stats=impact_stats)

@app.route('/process_donation', methods=['POST'])
def process_donation():
    # Here you would typically process the donation
    # For now, we'll just redirect back to the donate page
    return redirect(url_for('donate'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
