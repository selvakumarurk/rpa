# Academic Demonstration Checklist

This checklist is designed for your final project viva or presentation. It ensures you demonstrate all necessary components of **RPA Process Monitoring using UiPath Orchestrator**.

## Preparation Before Demo
- [ ] Ensure UiPath Assistant is connected to your Orchestrator tenant.
- [ ] Ensure the `Data/Input/EmployeeRecords.xlsx` file exists and is closed.

## 1. Local Execution & Code Review
- [ ] **Open Excel Input**: Open `Data/Input/EmployeeRecords.xlsx`. Show the examiner the data. Point out the valid records and explicitly show the invalid ones (e.g., negative salary, missing ID, inactive status).
- [ ] **Open UiPath Studio**: Show the project structure. Point out `Main.xaml`.
- [ ] **Explain Logic**: Briefly explain the validation rules and exception handling (business vs system failures).
- [ ] **Run Locally**: Click "Run File" in Studio.
- [ ] **Show Output**: Open `Data/Output/ProcessedEmployeeRecords.xlsx`. Show how the `ProcessingStatus` and `ProcessingMessage` columns correctly reflect the validation logic.
- [ ] **Show Local Logs**: Open the Output panel in Studio to show the Info and Warn logs generated during execution.

## 2. Orchestrator Demonstration
- [ ] **Publish Package**: In Studio, click "Publish". Show the package being created and deployed to Orchestrator.
- [ ] **Open Orchestrator**: Navigate to your Orchestrator web interface.
- [ ] **Show Process**: Go to **Automations -> Processes**. Add or update the Process using the newly published package.
- [ ] **Start Job**: Go to **Jobs**. Manually start a Job for your Process.
- [ ] **Monitor Execution**: Show the Job status changing from "Pending" to "Running" and then "Successful".
- [ ] **Show Logs**: Open the Job logs in Orchestrator. Point out the different Log Levels:
    - **Info**: Used for successful transactions.
    - **Warn**: Used for business validation failures (e.g., "Employee is inactive").
- [ ] **Show Scheduling**: Go to **Automations -> Triggers**. Create a new Time Trigger (e.g., "Run every day at 10:00 AM"). Explain how this automates the process without human intervention.

## 3. System Failure Demonstration (Optional but Recommended)
- [ ] **Simulate Error**: Rename `Data/Input/EmployeeRecords.xlsx` to `Hidden_EmployeeRecords.xlsx`.
- [ ] **Run Job**: Start the Job again from Orchestrator.
- [ ] **Show Failure**: Show the Job status as "Faulted".
- [ ] **Show Error Log**: Open the logs and show the `Error` level log detailing that the file could not be found. Explain why this constitutes a system failure rather than a business failure.

## Required Manual Screenshots for Documentation
If you need to submit a report, take screenshots of the following during your demo:
1. [ ] UiPath Studio project panel.
2. [ ] `Main.xaml` workflow open in the designer.
3. [ ] Excel input data (showing both valid/invalid rows).
4. [ ] Excel output data (showing ProcessingStatus and ProcessingMessage).
5. [ ] The "Publish" success window in UiPath Studio.
6. [ ] Orchestrator "Processes" page showing the deployed process.
7. [ ] Orchestrator "Jobs" page showing a Successful job.
8. [ ] Orchestrator "Jobs" page showing a Faulted/Failed job.
9. [ ] Orchestrator "Logs" window showing Info, Warn, and Error logs.
10. [ ] Orchestrator "Triggers" page showing the created schedule.
11. [ ] Orchestrator Dashboard/Monitoring page showing job statistics.
