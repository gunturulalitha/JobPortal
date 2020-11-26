Feature: Review Candidate details
Background : Home Page is opened and user browses to uploads resume and clicks upload button
    Given  Candidate details to enter
    When   submit button is clicked

  Scenario : Candidate Details validations
      Then   Check first name field is empty or given and characters "<FirstName>" are <= 50
      Then   Check last name field is empty or given and characters "<LastName>" are <= 50
      Then   Check phone number field is empty or given and format should be "<PhNum>" in 123-345-3456
      Then   Check Email Address field is empty or given and format "<EmailId>" is in abcd@domainname.com
      Then   Check Technical skill set field is empty or given and characters "<TechSkills>" are <= 200
      Then   Check Education field is empty or given and characters "<Education>" are <= 20
      Then   Check Employment Authorisation field is empty or given and characters "<EmpAuth>" are <= 20

