Feature: Resume File Upload Validation

  Background : Set up for validating file uploaded
    Given  Home Page opened
    When   User browses and uploads the resume and clicks Upload button

  Scenario Outline: Check the type and size of file uploaded
    Then  Uploaded file should be of type .doc/.docx "<path>"
    Then  Maximum uploaded file size should be less than 20KB "<path>" , "<size>"

    Examples:
      | path                           | size |
      | C:/bdd.txt                     | 6    |
      | C:/BDD_Word.docx               | 25   |
      | C:/BDD_Word_lessthan20kb.docx  | 18   |

