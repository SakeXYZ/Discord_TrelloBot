 ## FasTask - Discord Bot for Simplified Trello Card Creation

FasTask is a Discord bot designed to streamline the process of recording and creating Trello cards for requests within your tech department. It not only simplifies the request submission but also provides monitoring capabilities for better task management.

### Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Languages](#languages)
- [Contributing](#contributing)
- [License](#license)

### Description

FasTask, your personal assistant in Discord, makes it effortless to create Trello cards for tech-related requests. By using predefined commands, FasTask allows you to quickly record your requests and monitors their status, enhancing collaboration and task management.

### Installation

To install FasTask on your operating system, follow these steps:

**Windows:**

1. Download the latest release from the [GitHub repository](https://github.com/your-repository-link).
2. Run the installer and follow the on-screen instructions.

**macOS:**

1. Use Homebrew to install FasTask:
   ```bash
   brew tap your-repository-link
   brew install fastask
   ```

**Linux:**

1. Clone the GitHub repository and navigate to the project directory:
   ```bash
   git clone your-repository-link
   cd FasTask
   ```
2. Run the installer script:
   ```bash
   ./install.sh
   ```

### Configuration

Before using FasTask, you need to configure it by setting up your environment variables and Discord token:

1. Create a `.env` file and add your environment variables, including Trello API credentials and Discord token.

   ```
   URL=your-trello-api-url
   API_KEY=your-trello-api-key
   TOKEN=your-trello-token
   ID=your-trello-list-id
   TOKEN_DISCORD=your-discord-bot-token
   ```

2. Save the `.env` file in the root directory of your FasTask installation.

### Usage

FasTask responds to the following commands:

- `!hello`: Bot responds with a friendly "Hello."
- `!tch <title> <description>`: Creates a Trello card with the specified title and description. The card will be added to the designated Trello list.

### Languages

FasTask supports two languages for user interaction:

**English:** The default language.

**Russian:** To switch to Russian language commands, use `!lang ru`. To switch back to English, use `!lang en`.

### Contributing

If you'd like to contribute to FasTask, please follow the guidelines in our [Contributing](CONTRIBUTING.md) document.

### License

FasTask is open-source software released under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.
