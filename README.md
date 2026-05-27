# QueryForge

QueryForge is a technical Q&A chatbot built with Gradio. It allows users to ask technical questions using text or audio input and receive AI-generated answers from different AI providers such as OpenAI, Google Gemini, and Claude.

The project also includes an analytics dashboard that tracks user interactions, provider usage, response time, success rate, model usage, and conversation history.

---

## Features

### Technical Q&A Chatbot

QueryForge provides a chatbot interface where users can ask technical questions and receive AI-generated responses.

The chatbot supports streamed responses, which means the answer appears gradually while the AI is generating it.

The assistant is designed to answer programming questions, explain technical concepts, help with debugging, and generate code examples.

---

### Multi-Provider AI Support

QueryForge supports multiple AI providers.

The current providers are:

- OpenAI
- Google Gemini
- Claude

The user can choose which provider they want to use before asking a question.

---

### Dynamic Model Selection

QueryForge uses dynamic model selection.

When the user selects a provider, the model dropdown automatically updates and only shows models related to that provider.

For example:

- If the user selects OpenAI, only OpenAI models are shown.
- If the user selects Google, only Gemini models are shown.
- If the user selects Claude, only Claude models are shown.

This prevents users from accidentally selecting a model that does not belong to the selected provider.

---

### Audio Input and Transcription

QueryForge supports audio input through microphone recording or audio file upload.

The user can speak their question or upload an audio file.

The audio is transcribed into text using OpenAI Whisper.

After transcription, the transcribed text is placed into the message box and sent to the chatbot as the user prompt.

This allows users to ask questions using either text or voice.

---

### Code-Based Answers

QueryForge is designed for technical Q&A, so the assistant is instructed to provide code when needed.

If the user asks for code, the assistant should:

- Provide complete working code
- Use Markdown code blocks
- Explain how the code works

This makes the assistant useful for programming, debugging, and software development questions.

---

### Analytics Dashboard

QueryForge includes an analytics dashboard that tracks usage and performance.

The analytics dashboard shows:

- Total interactions
- Successful requests
- Success rate
- Average response time
- Most used provider
- Most used model
- Provider usage chart
- Response time chart
- Interaction history table

The analytics data is stored locally in a JSON file.

---

## Project Structure

### Main Project Files

ai.py — Contains the main AI response logic.

app.py — Contains the Gradio user interface.

analytics.py — Handles analytics saving, loading, summaries, charts, and dataframes.

config.py — Handles API key loading and AI client configuration.

analytics.json — Stores saved interaction history.

.env — Stores API keys as environment variables.

pyproject.toml — Stores project dependencies.

uv.lock — Stores locked dependency versions.

README.md — Contains project documentation.

---

## Requirements

This project uses the following main libraries:

- gradio
- openai
- pandas
- matplotlib
- python-dotenv

Gradio is used to build the web interface.

OpenAI SDK is used to connect with OpenAI-compatible APIs.

pandas is used to manage analytics data.

matplotlib is used to generate analytics charts.

python-dotenv is used to load API keys from the environment file.

---

## Environment Variables

The project uses a `.env` file to store API keys.

The required environment variables are:

OPENAI_API_KEY

ANTHROPIC_API_KEY

GOOGLE_API_KEY

These keys are loaded in `config.py` using `python-dotenv`.

---

## API Client Configuration

The project uses the OpenAI SDK to connect to different AI providers.

OpenAI uses the default OpenAI client.

Google Gemini is connected using an OpenAI-compatible base URL.

Claude is also connected using an OpenAI-compatible client setup.

The configured clients are:

openai — Used for OpenAI models.

google — Used for Google Gemini models.

anthropic — Used for Claude models.

---

## Supported Providers and Models

### OpenAI Models

- gpt-5-mini
- gpt-4o-mini
- gpt-4o

### Google Models

- gemini-2.5-flash
- gemini-2.5-pro

### Claude Models

- claude-sonnet-4-5
- claude-haiku-4-5

---

## How the Application Works

The user opens the Gradio app.

The user selects an AI provider.

The model dropdown updates automatically based on the selected provider.

The user selects a model.

The user can either type a question or provide an audio input.

If audio is provided, QueryForge transcribes the audio into text.

The text is added as the user message in the chatbot.

The selected provider and model are used to generate a response.

The response is streamed into the chatbot.

After the response is complete, the interaction is saved into `analytics.json`.

The analytics dashboard reads the saved data and displays summaries, charts, and history.

---

## AI System Prompt

QueryForge uses a system prompt to guide the assistant’s behavior.

The assistant is instructed to act as a technical Q&A assistant.

The assistant is also instructed to provide complete working code when the user asks for code.

The system prompt helps keep the responses clear, technical, and useful for programming-related questions.

---

## Chatbot Logic

The chatbot uses message history to maintain conversation context.

Each message contains a role and content.

The user message is added to the chat history.

The full message history is sent to the selected AI provider.

The AI response is streamed back and displayed in the chatbot.

This allows the assistant to understand previous messages in the same conversation.

---

## Text Input Flow

The user types a question into the message box.

When the user submits the message, it is added to the chatbot history.

The chatbot sends the message history to the selected AI provider.

The assistant response is streamed back into the chatbot interface.

The interaction is saved for analytics.

---

## Audio Input Flow

The user records audio using the microphone or uploads an audio file.

The user clicks the Transcribe button.

The audio file is sent to OpenAI Whisper for transcription.

The transcribed text is placed into the message box.

The text is added to the chatbot as the user message.

The selected AI provider generates a response.

The interaction is saved for analytics.

---

## Analytics System

QueryForge saves every completed interaction into `analytics.json`.

Each saved interaction contains:

- timestamp
- provider
- model
- question
- answer
- response time
- success status
- error status

The analytics system uses this data to calculate useful metrics.

---

## Analytics Summary

The analytics summary shows:

- Total interactions
- Successful requests
- Success rate
- Average response time
- Most used provider
- Most used model

If no data is available, the dashboard displays a message saying that there is no analytics data yet.

---

## Provider Usage Chart

The provider usage chart shows how many times each provider was used.

The chart is generated using matplotlib.

If no analytics data exists, the chart displays a “No data yet” message.

---

## Response Time Chart

The response time chart shows how response time changes across requests.

Each request is shown using its index number.

The chart helps show whether responses are becoming faster or slower over time.

If no analytics data exists, the chart displays a “No data yet” message.

---

## Interaction History Table

The analytics dashboard also includes an interaction history table.

The table displays saved records from `analytics.json`.

This allows the user to review previous questions, answers, providers, models, response times, and success status.

---

## Main Files

### app.py

This file contains the main Gradio interface.

It includes:

- QueryForge title
- Technical Q&A tab
- Chatbot component
- Provider dropdown
- Model dropdown
- Audio input component
- Transcribe button
- Message textbox
- Analytics tab
- Refresh Analytics button
- Analytics summary
- Provider usage chart
- Response time chart
- Interaction history table

---

### ai.py

This file contains the AI response logic.

It imports the configured AI clients from `config.py`.

It receives the selected provider, selected model, and chatbot history.

It sends the conversation to the correct AI provider.

It streams the assistant response back to the chatbot.

It calculates the response time.

It saves the interaction using the analytics system.

---

### config.py

This file handles environment configuration.

It loads API keys from the `.env` file.

It checks whether API keys are available.

It creates OpenAI-compatible clients for OpenAI, Google Gemini, and Claude.

---

### analytics.py

This file handles all analytics logic.

It loads analytics data from `analytics.json`.

It saves new interactions.

It converts analytics data into a pandas DataFrame.

It creates the analytics summary.

It generates the provider usage chart.

It generates the response time chart.

---

## Data Storage

QueryForge stores analytics data in `analytics.json`.

If the file does not exist, the app treats the analytics data as empty.

If the file exists but is empty, the app also treats it as empty.

This prevents the app from crashing when no analytics data has been saved yet.

---

## Error Handling

The AI response function uses error handling to catch provider or API errors.

If an error occurs, QueryForge saves the failed interaction in analytics.

The error is also returned to the chatbot so the user can see what went wrong.

---

## Current Status

The current implementation supports:

- Technical Q&A chatbot
- Multi-provider AI support
- Dynamic provider and model selection
- Text input
- Audio input
- Audio transcription
- Streaming AI responses
- Analytics tracking
- Analytics dashboard
- Provider usage chart
- Response time chart
- Interaction history table
- JSON-based local data storage

---

## Example Use Cases

QueryForge can be used for:

- Programming questions
- Debugging help
- Code generation
- Algorithm explanations
- AI and machine learning concepts
- Database questions
- DevOps questions
- Cloud computing questions
- Technical interview preparation
- General software development support

---

## Future Improvements

Possible future improvements include:

- Conversation reset button
- Export analytics as CSV
- Downloadable chat history
- Better UI styling
- Dark mode interface
- Local Ollama model support
- User authentication
- Separate analytics for each provider
- More chart types
- Better audio transcription error handling
- File upload support for documents and code files

---

## Notes

The analytics file should be named `analytics.json`.

If the file is manually created and left empty, the app will still work because the analytics loader checks for empty files.

The `.env` file should not be shared publicly because it contains API keys.

The app uses OpenAI-compatible API clients for all providers.

The selected provider and model must match the available model names in the provider model dictionary.

---