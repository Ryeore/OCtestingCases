# Testcases description

## Testcase 1 - Changing country in header dropdown and checking visibility of shops on the homepage
1. The script changes the location to the Germany.
2. By checking the name of the country location used on the page, the script verifies language change.
3. By checking the `<a>` tag in the shop cashback offers div the script verifies the shop offers visible on page.
4. If steps 2 and 3 the test is verified as PASSED.
5. At the end the country location is set back to Polish.

## Testcase 2 - Login Form
1. The script presses the "login" button.
2. Mail and password are entered.
3. The verification of successful login is performed on the profile page, where the username field is checked - the test is verified as PASSED.

## Testcase 3 - Going to the Shop page from search in the header
1. The shop name is entered into the search bar.
2. Enter pressed to go to the shop page.
3. If the name of the shop name matches the expected shop the test is verified as PASSED.

## Testcase 4 - Activating offer
1. The button "activate offer" is clicked
2. If the green checkmark appears on the screen the test is verified as PASSED.
