# Auto Anime Bot
<div align="center">
  <img src="https://graph.org/file/8bb750efbe7f08176e2ae.png" alt="Auto Anime Bot">
</div>
Auto Anime Bot is a Telegram bot designed to automatically upload anime files to a Telegram channel and provide users with access to these files. It supports multiple file resolutions, including 480p, 720p, and 1080p. Additionally, the bot has the capability to encode 720p files.

You can see the channel which is used by main production bot. | [Upload Channel](https://t.me/ani_upload)


## Features

- Automatic upload of anime files to a Telegram channel.
- Support for multiple file resolutions: 480p, 720p, and 1080p.
- Encoding of 720p files.
- User-friendly interface for accessing uploaded files from Bot.

## Requirements

- Powerful VPS (Virtual Private Server)
- Anime files in the specified resolutions

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Dhruv-Tara/Auto-Anime-Bot && cd Auto-Anime-Bot
   ```

2. **Install Dependencies:**
   
   - Remeber to Run the setup in sudo environment.

    ```bash
   bash setup.sh
   ```

3. **Configure Bot:**
   - Create a Telegram bot and obtain the API token.
   - Before running the bot, ensure that you fill in the necessary configuration details in the `config.json` file. Here's an example configuration:

```json
{
    "Author" : "Yash-Kun",
    "Licensed_under" : "GNU GPL V-3.0",
    "owner" : ["Replace with ID of sudos."],
    "database_url" : "Your Mongo",
    "main_channel" : "Id or channel username",
    "thumbnail_url" : "AAB/utils/thumb.jpeg",
    "files_channel" : -100,
    "production_chat" : -100,
    "api_id" : 123456,
    "api_hash" : "Api Hash",
    "main_bot" : "Main Bot for file transfer",
    "client_bot" : "Client Bot for upload"
}
```
4. **Run the Bot:**
   ```bash
   python3.11 -m AAB
   ```
   or
   ```bash
   bash start.sh
   ```

5. **Accessing Files:**
   - Users can access the uploaded files directly from the Telegram bot.

## Notes

- Ensure that your VPS has sufficient resources to handle encoding and file uploads.
- Customize the bot behavior as needed by modifying the source code.
- Feel free to contribute to the project by submitting issues or pull requests.

## Contributors

| ![**Dhruv-Tara**](https://github.com/Dhruv-Tara.png?size=50) | [**_Dhruv-Tara_**](https://github.com/Dhruv-Tara) |
| --- | --- |
| ![**illuminati-Dev**](https://github.com/illuminati-Dev.png?size=50) | [**_illuminati-Dev_**](https://github.com/illuminati-Dev) |
| --- | --- |
| ![**Qewertyy**](https://github.com/Qewertyy.png?size=50) | [**_Qewertyy_**](https://github.com/Qewertyy) |


## Support and Contribution

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/Dhruv-Tara/Auto-Anime-Bot/issues). Contributions are welcome!

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/Dhruv-Tara/Auto-Anime-Bot/blob/main/LICENSE).
