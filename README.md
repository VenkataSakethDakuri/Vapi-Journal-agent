  # 🗣️ AI Voice Journaling Assistant

This project integrates journaling with AI-generated voice calls using the [VAPI](https://vapi.ai/) and [Trieve](https://trieve.ai/) APIs. It allows users to initiate a personalized, AI-powered voice call where conversations are recorded, summarized, and stored for future reference. 🧠📝

## ✨ Features

- 🧍 AI voice agent for journaling purposes  
- 🤖 Personalized conversations powered by OpenAI's GPT-4o  
- 🗨️ Voice transcription with Deepgram  
- 📚 Dynamic knowledge base using Trieve  
- 📄 Summarized call content added to a knowledge base  

## ⚙️ Prerequisites

Make sure you have the following:

- 🐍 Python 3.7+
- 🔐 VAPI API Key
- 🔐 Trieve API Key
- 🆔 Dataset ID from Trieve
- 🆔 Assistant ID, Phone Number ID, and Customer Number from VAPI

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone [https://github.com/your-username/ai-voice-journaling.gi](https://github.com/VenkataSakethDakuri/Vapi-Journal-agent)t
```

2. **Set up your `.env` file**

Create a `.env` file in the root directory and include the following:

```env
VAPI_API_KEY=your_vapi_api_key
ASSISTANT_ID=your_assistant_id
PHONE_NUMBER_ID=your_phone_number_id
CUSTOMER_NUMBER=your_customer_number
TRIEVE_API_KEY=your_trieve_api_key
DATASET_ID=your_dataset_id
```

## 🚀 Usage

Run the main script:

```bash
python main.py
```

This will:

- 🧠 Create a knowledge base
- 📞 Start a voice call using the assistant
- 📝 Record and summarize the conversation
- 📥 Add the summary to the Trieve knowledge base

## 🧰 Technologies Used

- [VAPI.ai](https://vapi.ai/)
- [Trieve.ai](https://trieve.ai/)
- [OpenAI GPT-4o](https://openai.com/)
- [Deepgram](https://deepgram.com/)
- Python `requests` and `dotenv`

## 📄 License

MIT License. See `LICENSE` file for more information.

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or issue. 🚧🔧
