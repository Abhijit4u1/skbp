import request

# Get the form data
form_data = request.form
name = form_data['name']
reg_no = form_data['reg-no']
college_name = form_data['college-name']

# Save the data to a file
with open('login_info.txt', 'w') as f:
  f.write(f"Name: {name}\nRegistration Number: {reg_no}\nCollege Name: {college_name}")

# Redirect to the quiz page
return redirect('https://abhijit4u1.github.io/skbp.github.io/quiz.html')
