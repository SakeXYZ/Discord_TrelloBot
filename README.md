## FasTask - Discord Bot for Simplified Trello Card Creation

### Description

FasTask is a Discord bot designed to streamline the process of recording and creating Trello cards for requests within your tech department. It not only simplifies the request submission but also provides monitoring capabilities for better task management.

### Installation

To install FasTask on your operating system, follow these steps:

**Windows:**

1. Download the latest release from the [GitHub repository]([https://github.com/your-repository-link](https://github.com/SakeXYZ/Discord_TrelloBot/archive/refs/heads/master.zip)).
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

---

## FasTask - Discord Бот для Упрощенного Создания Карточек в Trello

### Описание

FasTask - это бот для Discord, разработанный для упрощения процесса записи и создания карточек в Trello для запросов в техническом отделе. Он не только упрощает подачу запросов, но также предоставляет функциональность мониторинга для более эффективного управления задачами.

### Установка

Для установки FasTask на вашу операционную систему выполните следующие шаги:

**Windows:**

1. Загрузите последнюю версию из [репозитория GitHub]([https://github.com/your-repository-link](https://github.com/SakeXYZ/Discord_TrelloBot/archive/refs/heads/master.zip)).
2. Запустите установщик и следуйте инструкциям на экране.

**macOS:**

1. Используйте Homebrew для установки FasTask:
   ```bash
   brew tap your-repository-link
   brew install fastask
   ```

**Linux:**

1. Клонируйте репозиторий GitHub и перейдите в директорию проекта:
   ```bash
   git clone your-repository-link
   cd FasTask
   ```
2. Запустите скрипт установки:
   ```bash
   ./install.sh
   ```

### Настройка

Перед использованием FasTask необходимо настроить его, установив переменные окружения и токен Discord:

1. Создайте файл `.env` и добавьте в него переменные окружения, включая учетные данные Trello API и токен Discord.

   ```
   URL=your-trello-api-url
   API_KEY=your-trello-api-key
   TOKEN=your-trello-token
   ID=your-trello-list-id
   TOKEN_DISCORD=your-discord-bot-token
   ```

2. Сохраните файл `.env` в корневой директории установки FasTask.

### Использование

FasTask реагирует на следующие команды:

- `!hello`: Бот отвечает дружелюбным "Hello."
- `!tch <title> <description>`: Создает карточку Trello с указанным заголовком и описанием. Карточка будет добавлена в соответствующий список Trello.
