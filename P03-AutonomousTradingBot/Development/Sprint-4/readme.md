Project: Autonomous Trading Bot - P03
Team:
Ahmed Tahir Shekhani - 23100197
Syed Talal Hasan - 23100176
Suleman Mahmood - 23100011
Ali Asghar - 23100198

SPRINT-4 SUBMISSION GUIDELINES

1. Properly tested working system deployed on an online hosting platform.
2. Code with readable comments uploaded in “Development/Sprint-2” folder of your project’s Github repository.
3. 3-4 minutes video that explains the functionality of your system developed so far. This must be uploaded in “Sprint-2” folder of your project’s Github repository.
4. Updated architecture and data model must be uploaded in the respective folders on Github.
5. Test case execution report. Create the test cases document and update the same document with testing result.
6. Update project schedule on Github. The following two views must be available in Github (a) A table view where use cases are grouped according to Sprints (Sprints view) (c) A board view that reflects the status of development (completed, in progress, to be done).
7. This "Readme" file should be uploaded in Sprint-2 folder.
8. Bonus: automate testing of 1 use case using your selected testing tool. For instance, automate using Selenium or any other tool that you have selected.

---

LIST OF REQUIREMENTS COMPLETED IN THE SPRINT

<List down use cases completed in the current sprint>

1. Configure Model Parameters to make predictions (integration in sprint 2)
2. Define stoppiong parameters of the bot
3. User initiates the bot for execution
4. Forcefully terminate the execution of the bot
5. Assign bots to investor
6. As an investor, I want to be able to login to my dashboard with the credentials provided by my analyst.

---

LIST OF REQUIREMENTS COMPLETED SO FAR

<List down use cases completed so far including those in the previous sprints>

1. Login with credentials
2. Analyst gets credentials for a registered investor
3. Configure Model Parameters to make predictions (integration in sprint 2)
4. Define stoppiong parameters of the bot
5. User initiates the bot for execution
6. Forcefully terminate the execution of the bot
7. Assign bots to investor
8. As an investor, I want to be able to login to my dashboard with the credentials provided by my analyst.

---

HOW TO ACCESS THE SYSTEM

Frontend: https://autonomous-trading-bot.vercel.app/
Backend on GCP and will run on-demand (due to pricing constraints)

---

ADDITIONAL INFORMATION

<Any additional information that you would like me to know>

1. Implemented JWT (Json Web Token)
2. Single Login for Analyst and Investor Implemented that fetches the role from backend automatically. This was implemented after a suggestion made during the meeting with 10 pearls representatives.
3. We used an environment variable to manage the private credentials of databse connections
