# Kitsu Event Listener

This project listens for new shots created in Kitsu, a management system, and sends email notifications using Gmail's SMTP server. It connects to Kitsu's event stream and reacts to events related to shot creation. 

### Features
- Listens for the `shot:new` event in Kitsu.
- Sends email notifications to predefined recipients with details about the newly created shot.
- Configurable environment variables for Kitsu server and Gmail credentials.

### Prerequisites
- A running Kitsu instance that exposes an API to which this listener can connect.
- A Gmail account with access to the Gmail App Key (for sending email notifications).

### User Details
You will need to authenticate as a regular user to connect to Kitsu's event stream. Please use the following credentials to authenticate:

- **Kitsu Username**: `admin@example.com`
- **Kitsu Password**: `mysecretpassword`

These details are required to log into Kitsu and listen for events. If these credentials need to be created on your local instance, please ensure they match the ones used here.

### Environment Variables
The following environment variables need to be set when running the Docker container:

- **KITSU_HOST**: The host for your Kitsu instance. Default is `127.0.0.1`.
- **KITSU_PORT**: The port for your Kitsu instance. Default is `538`.
- **GMAIL_APP_KEY**: The Gmail App Key used for authenticating the email account.

If these environment variables are not provided at runtime, the default values specified in `config/__init__.py` will be used.

### Project Structure
```
kitsu-event-listener
├── src/  
│   ├── configs/  
│   │   └── __init__.py       # Configuration settings  
│   ├── utils/  
│   │    ├── decorators.py   # Handles callback on different thread
│   │    └── email.py        # Handles email notifications  
│   ├── listener.py         # Listens for Kitsu events
├── tests/  
├── README.md              # Project documentation  
├── requirements.txt
└── Dockerfile             # Use to build image  
 
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rashish423/kitsu_event_listener.git
   cd kitsu_event_listener
   ```

2. Build the Docker image:

   ```bash
   docker build -t kitsu_event_listener .
   ```

4. Run the Docker container, passing environment variables for the Kitsu host, port, and Gmail App key:

   ```bash
   docker run --network="host" -e KITSU_HOST=127.0.0.1 -e KITSU_PORT=538 -e GMAIL_APP_KEY="your_gmail_app_key" kitsu_event_listener
   ```

   Or, if you do not want to pass environment variables at runtime, the default values specified in `config/__init__.py` will be used:

   ```bash
   docker run --network="host" kitsu_event_listener
   ```

### Running the Application

When you run the container, it will authenticate as a regular user with the credentials specified in `config/__init__.py`, connect to the Kitsu event stream, and listen for `shot:new` events. Whenever a new shot is created, it will send an email notification to the recipients defined in `config/__init__.py`.

### Docker Configuration
The Docker container is set up to use the default environment variables, and can be configured at runtime by passing the necessary environment variables via the `docker run` command.

### Troubleshooting
- Ensure that Kitsu is running and accessible at the specified host and port.
- Double-check that your Gmail App Key is correctly configured for email notifications.
- If you encounter connection issues, verify that Kitsu's API is properly exposed and that the user credentials are correct.

### Author
**Ashish Rana**
- 📫 How to reach me: [Twitter](https://twitter.com/Rashish423), [LinkedIn](https://www.linkedin.com/in/raashish)
- 😄 Pronouns: He/Him
- ⚡ Fun fact: I spend 10+ hours daily on the computer to learn and build







