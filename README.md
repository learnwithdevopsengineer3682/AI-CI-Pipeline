# AI-CI-Pipeline

CI with AI Failure Prediction
This workflow runs whenever there is a push or pull request to the main branch. It executes a test suite and, if tests fail, it uses Ollama with the Mistral AI model to analyze errors and suggest fixes.

Steps Explained
Trigger Conditions

Runs on every push and pull request to the main branch.

Checkout Code

Uses actions/checkout@v4 to fetch the latest code from the repository.

Install Dependencies

Updates the package list (sudo apt-get update).

Installs required tools like libxml2-utils (for XML processing) and jq (for JSON parsing).

Set Up Python

Uses actions/setup-python@v4 to install Python 3.11.

Install Pytest

Installs pytest for running tests.

Run Tests

Runs pytest and generates a JUnit-style test report (report.xml).

If tests fail, it sets an environment variable (TEST_FAILED=true).

Analyze Failures with Ollama (AI-powered Debugging)

Extracts error messages from the report.xml file using xmllint.

Sends the error message to Mistral AI via Ollama.

The AI model suggests potential fixes, which are stored in ai_suggestions.txt.

Upload AI Failure Suggestions

If tests failed, ai_suggestions.txt is uploaded as an artifact.

This allows developers to review AI-generated recommendations in the GitHub Actions UI.

This project uses GitHub Actions for Continuous Integration (CI) and AI-powered failure analysis.

How It Works
On each push or pull request to main, the workflow:

Checks out the latest code.

Installs dependencies (libxml2-utils, jq, pytest).

Runs tests using pytest.

If tests fail:

AI analysis is triggered using Ollama and Mistral AI.

The AI suggests potential fixes for the failure.

These suggestions are uploaded as an artifact (AI-Failure-Suggestions).

How to View AI Suggestions
Navigate to GitHub Actions.

Open the latest failed workflow run.

Download the artifact AI-Failure-Suggestions to view AI-generated recommendations.